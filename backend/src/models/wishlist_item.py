from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from backend.src.database import Base

class WishlistItem(Base):
    __tablename__ = "wishlist_items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    wishlist_id = Column(Integer, ForeignKey("wishlists.id"), nullable=False)
    name = Column(String(200), nullable=False)
    note = Column(Text, nullable=True)
    url = Column(String(500), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    wishlist = relationship("Wishlist", back_populates="items")

    def __repr__(self):
        return f"<WishlistItem(id={self.id}, name='{self.name}', wishlist_id={self.wishlist_id})>"