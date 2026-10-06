"""FastAPI application for the calculator backend."""

from __future__ import annotations

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from app.calculator import CalculatorError, calculate_expression
from app.database import clear_history, create_history, delete_history, init_db, list_history


app = FastAPI(title="Calculator Backend", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class CalculateRequest(BaseModel):
    expression: str = Field(..., min_length=1, max_length=200)


@app.on_event("startup")
def on_startup() -> None:
    init_db()


@app.get("/api/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
def api_root() -> str:
    return """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Calculator Backend</title>
        <style>
          body {
            margin: 0;
            min-height: 100vh;
            display: grid;
            place-items: center;
            background: #f4f6f8;
            color: #17202a;
            font-family: "Segoe UI", Arial, sans-serif;
          }

          main {
            width: min(760px, calc(100% - 32px));
            padding: 28px;
            border: 1px solid #d8e0e8;
            border-radius: 8px;
            background: #ffffff;
            box-shadow: 0 18px 55px rgba(17, 24, 39, 0.12);
          }

          h1 {
            margin: 0 0 8px;
          }

          p {
            color: #64748b;
          }

          code {
            padding: 2px 6px;
            border-radius: 6px;
            background: #edf1f5;
          }

          li {
            margin: 10px 0;
          }
        </style>
      </head>
      <body>
        <main>
          <h1>Calculator Backend Is Running</h1>
          <p>
            Open the frontend page and submit an expression. The frontend sends
            the request to this backend, and the backend calculates, saves, and
            returns the result.
          </p>
          <ul>
            <li><code>GET /api/health</code> health check</li>
            <li><code>POST /api/calculate</code> calculate an expression</li>
            <li><code>GET /api/history</code> query history records</li>
            <li><code>DELETE /api/history/{history_id}</code> delete one record</li>
            <li><code>DELETE /api/history</code> clear all records</li>
            <li><code>GET /docs</code> interactive API documentation</li>
          </ul>
        </main>
      </body>
    </html>
    """


@app.post("/api/calculate")
def calculate(request: CalculateRequest) -> dict[str, object]:
    try:
        result = calculate_expression(request.expression)
    except CalculatorError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    history = create_history(request.expression, result)
    return history


@app.get("/api/history")
def get_history() -> list[dict[str, object]]:
    return list_history()


@app.delete("/api/history/{history_id}")
def remove_history(history_id: int) -> dict[str, object]:
    deleted = delete_history(history_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="History record not found.")

    return {"deleted": True, "id": history_id}


@app.delete("/api/history")
def remove_all_history() -> dict[str, object]:
    deleted_count = clear_history()
    return {"deleted": True, "count": deleted_count}
