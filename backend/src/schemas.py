from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# User schemas
class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="Username for the account")

class UserCreate(UserBase):
    password: str = Field(..., min_length=8, description="Password for the account")

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Wishlist schemas
class WishlistBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="Name of the wishlist")

class WishlistCreate(WishlistBase):
    pass

class WishlistResponse(WishlistBase):
    id: int
    owner_id: int
    created_at: datetime

    class Config:
        from_attributes = True

# WishlistItem schemas
class WishlistItemBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=200, description="Name of the item")
    note: Optional[str] = Field(None, description="Optional note about the item")
    url: Optional[str] = Field(None, description="Optional URL for the item")

class WishlistItemCreate(WishlistItemBase):
    pass

class WishlistItemResponse(WishlistItemBase):
    id: int
    wishlist_id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Share schemas
class ShareCreate(BaseModel):
    wishlist_id: int
    viewer_username: str

class ShareResponse(BaseModel):
    id: int
    wishlist_id: int
    viewer_id: int
    granted_at: datetime

    class Config:
        from_attributes = True

# Generic response
class MessageResponse(BaseModel):
    message: str