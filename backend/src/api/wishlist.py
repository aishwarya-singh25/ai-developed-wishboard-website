from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List
from backend.src.database import get_db
from backend.src.services.wishlist import (
    create_wishlist, get_wishlists_for_user, get_wishlist_by_id,
    update_wishlist, delete_wishlist, add_item_to_wishlist,
    get_items_for_wishlist, update_wishlist_item, delete_wishlist_item
)
from backend.src.schemas import (
    WishlistCreate, WishlistResponse, WishlistItemCreate,
    WishlistItemResponse, MessageResponse
)

router = APIRouter()

@router.post("/wishlists", response_model=WishlistResponse)
async def create_new_wishlist(
    wishlist: WishlistCreate,
    request: Request,
    db: Session = Depends(get_db)
):
    """Create a new wishlist."""
    user_id = request.session.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Not authenticated")

    try:
        new_wishlist = create_wishlist(db, user_id, wishlist.name)
        return new_wishlist
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/wishlists", response_model=List[WishlistResponse])
async def get_user_wishlists(request: Request, db: Session = Depends(get_db)):
    """Get all wishlists for the current user."""
    user_id = request.session.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Not authenticated")

    return get_wishlists_for_user(db, user_id)

@router.get("/wishlists/{wishlist_id}", response_model=WishlistResponse)
async def get_wishlist(wishlist_id: int, request: Request, db: Session = Depends(get_db)):
    """Get a specific wishlist."""
    user_id = request.session.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Not authenticated")

    wishlist = get_wishlist_by_id(db, wishlist_id, user_id)
    if not wishlist:
        raise HTTPException(status_code=404, detail="Wishlist not found")

    return wishlist

@router.put("/wishlists/{wishlist_id}", response_model=WishlistResponse)
async def update_existing_wishlist(
    wishlist_id: int,
    wishlist: WishlistCreate,
    request: Request,
    db: Session = Depends(get_db)
):
    """Update a wishlist."""
    user_id = request.session.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Not authenticated")

    try:
        updated = update_wishlist(db, wishlist_id, user_id, wishlist.name)
        if not updated:
            raise HTTPException(status_code=404, detail="Wishlist not found")
        return updated
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/wishlists/{wishlist_id}", response_model=MessageResponse)
async def delete_existing_wishlist(wishlist_id: int, request: Request, db: Session = Depends(get_db)):
    """Delete a wishlist."""
    user_id = request.session.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Not authenticated")

    if delete_wishlist(db, wishlist_id, user_id):
        return {"message": "Wishlist deleted"}
    else:
        raise HTTPException(status_code=404, detail="Wishlist not found")

@router.post("/wishlists/{wishlist_id}/items", response_model=WishlistItemResponse)
async def create_wishlist_item(
    wishlist_id: int,
    item: WishlistItemCreate,
    request: Request,
    db: Session = Depends(get_db)
):
    """Add an item to a wishlist."""
    user_id = request.session.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Not authenticated")

    try:
        new_item = add_item_to_wishlist(db, wishlist_id, user_id, item.name, item.note, item.url)
        if not new_item:
            raise HTTPException(status_code=404, detail="Wishlist not found")
        return new_item
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/wishlists/{wishlist_id}/items", response_model=List[WishlistItemResponse])
async def get_wishlist_items(wishlist_id: int, request: Request, db: Session = Depends(get_db)):
    """Get all items in a wishlist."""
    user_id = request.session.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Not authenticated")

    return get_items_for_wishlist(db, wishlist_id, user_id)

@router.put("/wishlists/{wishlist_id}/items/{item_id}", response_model=WishlistItemResponse)
async def update_wishlist_item_endpoint(
    wishlist_id: int,
    item_id: int,
    item: WishlistItemCreate,
    request: Request,
    db: Session = Depends(get_db)
):
    """Update a wishlist item."""
    user_id = request.session.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Not authenticated")

    try:
        updated = update_wishlist_item(db, item_id, wishlist_id, user_id, item.name, item.note, item.url)
        if not updated:
            raise HTTPException(status_code=404, detail="Item not found")
        return updated
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/wishlists/{wishlist_id}/items/{item_id}", response_model=MessageResponse)
async def delete_wishlist_item_endpoint(
    wishlist_id: int,
    item_id: int,
    request: Request,
    db: Session = Depends(get_db)
):
    """Delete a wishlist item."""
    user_id = request.session.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Not authenticated")

    if delete_wishlist_item(db, item_id, wishlist_id, user_id):
        return {"message": "Item deleted"}
    else:
        raise HTTPException(status_code=404, detail="Item not found")