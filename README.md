# Python Timesheets API

A FastAPI-based backend service for handling timesheet-related operations.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

The server will start at `http://localhost:3000`

## API Endpoints

- `GET /`: Welcome message
- `POST /api/process-prompt`: Process prompt requests
  - Request body:
    ```json
    {
        "prompt": "string",
        "decision": "string" (optional)
    }
    ```

## Project Structure

```
python-timesheets/
├── main.py              # Main application entry point
├── requirements.txt     # Project dependencies
└── src/
    ├── controllers/     # Request handlers
    ├── models/         # Pydantic models
    ├── routes/         # API routes
    └── services/       # Business logic
```
