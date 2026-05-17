# Wishlist Sharing Website

A simple web application built with Python FastAPI, SQLite, and plain HTML/CSS/JavaScript.

Users can:
- create an account with a username and password
- log in and manage a personal wishlist
- add, edit, and delete wishlist items
- share wishlists with other registered users
- view wishlists shared by others

## Project structure

- `backend/` - Python backend code, API routes, services, and database models
- `frontend/` - HTML templates, CSS, and frontend JavaScript
- `run.py` - Application entry point for local development
- `specs/001-wishlist-sharing/` - feature spec, plan, tasks, and contract documentation

## Requirements

- Python 3.11+
- SQLite (built into Python)
- `pip` or compatible package manager

## Setup

1. Create and activate a Python virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```

## Run the app

Start the server from the repository root:

```bash
python run.py
```

Then open the app in your browser:

```text
http://127.0.0.1:8000
```

## Usage

1. Open the homepage.
2. Sign up with a username and password.
3. Log in to access your dashboard.
4. Add wishlist items and manage them from your dashboard.
5. Share a wishlist with another registered user.
6. View wishlists that have been shared with you.

## Testing

Run backend tests using:

```bash
pytest backend/tests
```

## Notes

- The project uses SQLite for local storage and stores data in a local database file.
- The frontend is implemented with server-rendered HTML templates and static assets.
- Documentation and feature details are available in `specs/001-wishlist-sharing/`.

