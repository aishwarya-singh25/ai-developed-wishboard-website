from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from sqlalchemy.orm import Session
from backend.src.database import engine, get_db, Base
from backend.src.api import auth, dashboard, wishlist, sharing

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(title="Wishlist Sharing Website")

# Add session middleware
app.add_middleware(SessionMiddleware, secret_key="your-secret-key-change-in-production")

# Mount static files
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="frontend/templates")

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])
app.include_router(wishlist.router, prefix="/wishlist", tags=["wishlist"])
app.include_router(sharing.router, prefix="/sharing", tags=["sharing"])

# Error handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    if request.headers.get("accept", "").startswith("application/json"):
        return {"detail": exc.detail}
    return templates.TemplateResponse(
        "error.html",
        {"request": request, "error": exc.detail, "status_code": exc.status_code}
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    if request.headers.get("accept", "").startswith("application/json"):
        return {"detail": "Internal server error"}
    return templates.TemplateResponse(
        "error.html",
        {"request": request, "error": "Internal server error", "status_code": 500}
    )

@app.get("/")
async def root(request: Request):
    user_id = request.session.get("user_id")
    if user_id:
        return templates.TemplateResponse("dashboard.html", {"request": request})
    else:
        return templates.TemplateResponse("auth.html", {"request": request})

@app.get("/auth")
async def auth_page(request: Request):
    return templates.TemplateResponse("auth.html", {"request": request})

@app.get("/dashboard")
async def dashboard_page(request: Request):
    user_id = request.session.get("user_id")
    if not user_id:
        return templates.TemplateResponse("auth.html", {"request": request})
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/wishlist/{wishlist_id}")
async def wishlist_page(request: Request, wishlist_id: int):
    user_id = request.session.get("user_id")
    if not user_id:
        return templates.TemplateResponse("auth.html", {"request": request})
    return templates.TemplateResponse("wishlist.html", {"request": request})

@app.get("/health")
async def health():
    return {"status": "healthy"}