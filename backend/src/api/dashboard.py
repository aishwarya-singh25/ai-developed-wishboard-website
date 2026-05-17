from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List
from backend.src.database import get_db
from backend.src.services.wishlist import get_wishlists_for_user
from backend.src.schemas import WishlistResponse

router = APIRouter()

@router.get("/dashboard", response_model=List[WishlistResponse])
async def get_dashboard(request: Request, db: Session = Depends(get_db)):
    """Get the current user's dashboard with their wishlists."""
    user_id = request.session.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Not authenticated")

    wishlists = get_wishlists_for_user(db, user_id)
    return wishlists