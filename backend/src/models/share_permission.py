from sqlalchemy import Column, Integer, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from backend.src.database import Base


class SharePermission(Base):
    __tablename__ = "share_permissions"
    __table_args__ = (
        UniqueConstraint("wishlist_id", "viewer_id", name="uq_share_permissions_wishlist_viewer"),
    )

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    wishlist_id = Column(Integer, ForeignKey("wishlists.id", ondelete="CASCADE"), nullable=False)
    viewer_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    granted_at = Column(DateTime(timezone=True), server_default=func.now())

    wishlist = relationship("Wishlist", back_populates="shares")
    viewer = relationship("User", back_populates="shared_permissions")

    def __repr__(self):
        return (
            f"<SharePermission(id={self.id}, wishlist_id={self.wishlist_id}, "
            f"viewer_id={self.viewer_id})>"
        )
