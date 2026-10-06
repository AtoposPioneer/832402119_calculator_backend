# 832402119 Calculator Frontend

This repository contains the frontend page for the Software Engineering Practice first assignment.

Student ID: `832402119`

GitHub username: `AtoposPioneer`

## Features

- Enter arithmetic expressions with buttons or keyboard.
- Send expressions to the backend for calculation.
- Display calculation results and error messages.
- Load calculation history from the backend database.
- Delete a single history record.
- Clear all history records.
- Toggle light and dark themes.

## Tech Stack

- HTML
- CSS
- JavaScript

## Backend Repository

```text
https://github.com/AtoposPioneer/832402119_calculator_backend
```

## Project Structure

```text
832402119_calculator_frontend/
|-- app.js
|-- codestyle.md
|-- index.html
|-- README.md
|-- styles.css
```

## Run Locally

Start the backend service first, then open `index.html` in a browser.

Default backend API address:

```text
http://127.0.0.1:8000
```

If the backend is deployed to another address, update `API_BASE_URL` in `app.js`.

## Main Workflow

1. The user enters an expression on the frontend.
2. The frontend sends the expression to `POST /api/calculate`.
3. The backend validates and calculates the expression.
4. The backend stores successful calculation records in SQLite.
5. The frontend reloads history from `GET /api/history`.

## API Usage

The frontend calls these backend endpoints:

```text
POST   /api/calculate
GET    /api/history
DELETE /api/history/{history_id}
DELETE /api/history
```

The frontend does not calculate the final result by itself. It only sends user input to the backend and renders the backend response.

## Browser Support

This page uses standard HTML, CSS, and JavaScript features. It can be opened directly in a modern browser after the backend is running.
