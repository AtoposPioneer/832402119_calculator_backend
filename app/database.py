"""SQLite database access for calculation history."""

from __future__ import annotations

import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "calculator.db"


def get_connection() -> sqlite3.Connection:
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db() -> None:
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS calculation_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                expression TEXT NOT NULL,
                result TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )


def create_history(expression: str, result: str) -> dict[str, Any]:
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with get_connection() as connection:
        cursor = connection.execute(
            """
            INSERT INTO calculation_history (expression, result, created_at)
            VALUES (?, ?, ?)
            """,
            (expression, result, created_at),
        )
        history_id = cursor.lastrowid

    return {
        "id": history_id,
        "expression": expression,
        "result": result,
        "created_at": created_at,
    }


def list_history() -> list[dict[str, Any]]:
    with get_connection() as connection:
        rows = connection.execute(
            """
            SELECT id, expression, result, created_at
            FROM calculation_history
            ORDER BY id DESC
            """
        ).fetchall()

    return [dict(row) for row in rows]


def delete_history(history_id: int) -> bool:
    with get_connection() as connection:
        cursor = connection.execute(
            "DELETE FROM calculation_history WHERE id = ?",
            (history_id,),
        )

    return cursor.rowcount > 0


def clear_history() -> int:
    with get_connection() as connection:
        cursor = connection.execute("DELETE FROM calculation_history")

    return cursor.rowcount
