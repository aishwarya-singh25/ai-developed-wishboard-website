from sqlalchemy.orm import Session
from typing import List, Optional
from backend.src.models.wishlist import Wishlist
from backend.src.models.wishlist_item import WishlistItem
from backend.src.models.user import User

def create_wishlist(db: Session, owner_id: int, name: str) -> Wishlist:
    """Create a new wishlist for a user."""
    if len(name) < 1 or len(name) > 100:
        raise ValueError("Wishlist name must be 1-100 characters")

    wishlist = Wishlist(owner_id=owner_id, name=name)
    db.add(wishlist)
    db.commit()
    db.refresh(wishlist)
    return wishlist

def get_wishlists_for_user(db: Session, user_id: int) -> List[Wishlist]:
    """Get all wishlists for a user."""
    return db.query(Wishlist).filter(Wishlist.owner_id == user_id).all()

def get_wishlist_by_id(db: Session, wishlist_id: int, user_id: int) -> Optional[Wishlist]:
    """Get a specific wishlist by ID, ensuring it belongs to the user."""
    return db.query(Wishlist).filter(
        Wishlist.id == wishlist_id,
        Wishlist.owner_id == user_id
    ).first()

def update_wishlist(db: Session, wishlist_id: int, user_id: int, name: str) -> Optional[Wishlist]:
    """Update a wishlist name."""
    wishlist = get_wishlist_by_id(db, wishlist_id, user_id)
    if not wishlist:
        return None

    if len(name) < 1 or len(name) > 100:
        raise ValueError("Wishlist name must be 1-100 characters")

    wishlist.name = name
    db.commit()
    db.refresh(wishlist)
    return wishlist

def delete_wishlist(db: Session, wishlist_id: int, user_id: int) -> bool:
    """Delete a wishlist."""
    wishlist = get_wishlist_by_id(db, wishlist_id, user_id)
    if not wishlist:
        return False

    db.delete(wishlist)
    db.commit()
    return True

def add_item_to_wishlist(db: Session, wishlist_id: int, user_id: int, name: str, note: Optional[str] = None, url: Optional[str] = None) -> Optional[WishlistItem]:
    """Add an item to a wishlist."""
    wishlist = get_wishlist_by_id(db, wishlist_id, user_id)
    if not wishlist:
        return None

    if len(name) < 1 or len(name) > 200:
        raise ValueError("Item name must be 1-200 characters")

    item = WishlistItem(wishlist_id=wishlist_id, name=name, note=note, url=url)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def get_items_for_wishlist(db: Session, wishlist_id: int, user_id: int) -> List[WishlistItem]:
    """Get all items for a wishlist."""
    wishlist = get_wishlist_by_id(db, wishlist_id, user_id)
    if not wishlist:
        return []

    return db.query(WishlistItem).filter(WishlistItem.wishlist_id == wishlist_id).all()

def update_wishlist_item(db: Session, item_id: int, wishlist_id: int, user_id: int, name: str, note: Optional[str] = None, url: Optional[str] = None) -> Optional[WishlistItem]:
    """Update a wishlist item."""
    wishlist = get_wishlist_by_id(db, wishlist_id, user_id)
    if not wishlist:
        return None

    item = db.query(WishlistItem).filter(
        WishlistItem.id == item_id,
        WishlistItem.wishlist_id == wishlist_id
    ).first()

    if not item:
        return None

    if len(name) < 1 or len(name) > 200:
        raise ValueError("Item name must be 1-200 characters")

    item.name = name
    item.note = note
    item.url = url
    db.commit()
    db.refresh(item)
    return item

def delete_wishlist_item(db: Session, item_id: int, wishlist_id: int, user_id: int) -> bool:
    """Delete a wishlist item."""
    wishlist = get_wishlist_by_id(db, wishlist_id, user_id)
    if not wishlist:
        return False

    item = db.query(WishlistItem).filter(
        WishlistItem.id == item_id,
        WishlistItem.wishlist_id == wishlist_id
    ).first()

    if not item:
        return False

    db.delete(item)
    db.commit()
    return True