from fastapi import APIRouter, Depends, HTTPException, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from backend.src.database import get_db
from backend.src.services.auth import create_user, authenticate_user

router = APIRouter()
templates = Jinja2Templates(directory="frontend/templates")

@router.post("/signup")
async def signup(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    """Create a new user account."""
    try:
        create_user(db, username, password)
        # Auto-login after signup
        user = authenticate_user(db, username, password)
        if user:
            request.session["user_id"] = user.id
            request.session["username"] = user.username
        return templates.TemplateResponse("dashboard.html", {"request": request})
    except ValueError as e:
        return templates.TemplateResponse(
            "auth.html",
            {"request": request, "error": str(e)}
        )

@router.post("/login")
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    """Authenticate a user and set session."""
    authenticated_user = authenticate_user(db, username, password)
    if not authenticated_user:
        return templates.TemplateResponse(
            "auth.html",
            {"request": request, "error": "Invalid username or password"}
        )

    # Set session
    request.session["user_id"] = authenticated_user.id
    request.session["username"] = authenticated_user.username

    return templates.TemplateResponse("dashboard.html", {"request": request})

@router.api_route("/logout", methods=["GET", "POST"])
async def logout(request: Request):
    """Logout the current user by clearing session."""
    request.session.clear()
    return RedirectResponse(url="/auth", status_code=302)

@router.get("/me")
async def get_current_user(request: Request, db: Session = Depends(get_db)):
    """Get current user info from session."""
    user_id = request.session.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Not authenticated")

    # In a real app, you'd fetch the user, but for now just return session info
    return {
        "user_id": user_id,
        "username": request.session.get("username")
    }