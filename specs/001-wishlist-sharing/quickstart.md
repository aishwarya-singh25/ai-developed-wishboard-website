# Quickstart: Wishlist Sharing Website

## Prerequisites

- Python 3.11+
- `uv` package manager (for dependency management)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ai-developed-wishboard-website
   ```

2. Install dependencies:
   ```bash
   uv pip install -r backend/requirements.txt
   ```

## Running the Application

1. Start the FastAPI server:
   ```bash
   python run.py
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:8000
   ```

3. The application will create the SQLite database (`wishlist.db`) automatically on first run.

## Usage

1. **Sign Up**: Create a new account with username and password
2. **Login**: Use your credentials to access the dashboard
3. **Create Wishlist**: Add a new wishlist from your dashboard
4. **Add Items**: Add items to your wishlists with name, note, and optional URL
5. **Share Wishlists**: Share your wishlists with other registered users by username
6. **View Shared**: Access wishlists shared with you in the "Shared" section

## API Documentation

When running, visit `http://localhost:8000/docs` for interactive API documentation.

## Development

- Backend code is in `backend/src/`
- Frontend templates are in `frontend/templates/`
- Static files (CSS/JS) are in `frontend/static/`
- Tests are in `backend/tests/` and `frontend/tests/`

## Troubleshooting

- Ensure Python 3.11+ is installed
- Check that port 8000 is not in use
- Database file `wishlist.db` will be created in the project root