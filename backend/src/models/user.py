from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, validates
from sqlalchemy.sql import func
from backend.src.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    wishlists = relationship("Wishlist", back_populates="owner")
    shared_permissions = relationship("SharePermission", back_populates="viewer")

    @validates('username')
    def validate_username(self, key, username):
        if not username or len(username) < 3 or len(username) > 50:
            raise ValueError('Username must be 3-50 characters')
        if not username.replace('_', '').replace('-', '').isalnum():
            raise ValueError('Username can only contain letters, numbers, underscores, and hyphens')
        return username

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"