# 832402119 Calculator Backend

This repository contains the backend service for the Software Engineering Practice first assignment.

Student ID: `832402119`

Student Name: `Jingling Wang`

GitHub username: `AtoposPioneer`

## Features

- Calculate arithmetic expressions on the server side.
- Support addition, subtraction, multiplication, division, parentheses, decimals, and unary signs.
- Reject invalid expressions and division by zero.
- Store successful calculation history in SQLite.
- Query calculation history.
- Delete a single history record.
- Clear all history records.

## Frontend Repository

```text
https://github.com/AtoposPioneer/832402119_calculator_frontend
```

## Tech Stack

- Python 3.12
- FastAPI
- SQLite
- Pydantic

## Project Structure

```text
832402119_calculator_backend/
|-- app/
|   |-- __init__.py
|   |-- calculator.py
|   |-- database.py
|   |-- main.py
|-- tests/
|   |-- test_calculator.py
|-- codestyle.md
|-- README.md
|-- requirements.txt
```

## Run Locally

Enter this project directory:

```bash
cd 832402119_calculator_backend
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```bash
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the backend:

```bash
uvicorn app.main:app --reload
```

The backend will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## Run Tests

```bash
python -m unittest discover -s tests
```

## API

### Health Check

```http
GET /api/health
```

### Calculate

```http
POST /api/calculate
Content-Type: application/json

{
  "expression": "(1 + 2) * 3"
}
```

### Get History

```http
GET /api/history
```

### Delete One History Record

```http
DELETE /api/history/{id}
```

### Clear History

```http
DELETE /api/history
```

## Example Response

Request:

```json
{
  "expression": "(1 + 2) * 3"
}
```

Response:

```json
{
  "id": 1,
  "expression": "(1 + 2) * 3",
  "result": "9",
  "created_at": "2026-10-05 22:00:00"
}
```

## Error Handling

The backend returns `400 Bad Request` for invalid expressions, unsupported syntax, empty input, and division by zero.

Example:

```json
{
  "detail": "Division by zero is not allowed."
}
```

## Implementation Notes

The backend does not use `eval` or `exec` to execute user input. It parses the expression with Python's `ast` module and evaluates only a small allowlist of safe arithmetic nodes.

Successful calculation records are stored in the local SQLite database file `calculator.db`. This file is ignored by Git because it is runtime data.
