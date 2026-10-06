# Backend Code Style

## Python

This project follows the main ideas of [PEP 8](https://peps.python.org/pep-0008/):

- Use 4 spaces for indentation.
- Use clear function and variable names.
- Keep functions focused on one responsibility.
- Use constants for repeated configuration values.
- Keep lines readable and avoid unnecessary complexity.
- Add comments only when they explain non-obvious logic.
- Use type hints for important function parameters and return values.
- Keep error messages controlled and user-friendly.

## File Organization

- `app/main.py` contains FastAPI routes and request/response handling.
- `app/calculator.py` contains expression parsing and safe calculation logic.
- `app/database.py` contains SQLite access functions.
- `tests/` contains unit tests for the calculation module.

## API Design

- Use RESTful routes.
- Use JSON request and response bodies.
- Return clear error messages for invalid input.
- Keep API paths under the `/api` prefix.
- Use meaningful HTTP status codes, such as `400` for invalid calculation requests and `404` for missing history records.

## Database

- Use parameterized SQL statements.
- Keep table names and column names lowercase with underscores.
- Store timestamps in a consistent string format.
- Do not commit runtime database files.

## Security

- Do not use `eval` or `exec` for user-provided expressions.
- Validate expression length and supported syntax on the backend.
- Return controlled error messages instead of raw exceptions.
- Allow only arithmetic AST nodes required by the assignment.

## Testing

- Add tests for normal expressions, compound expressions, invalid input, and division by zero.
- Run tests before submitting or deploying the backend:

```bash
python -m unittest discover -s tests
```
