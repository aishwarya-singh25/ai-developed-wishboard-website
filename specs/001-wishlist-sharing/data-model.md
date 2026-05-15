# Data Model: Wishlist Sharing Website

## Entities

### User
Represents a registered user account.

**Fields**:
- `id`: Integer, Primary Key, Auto-increment
- `username`: String(50), Unique, Not Null
- `password_hash`: String(128), Not Null
- `created_at`: DateTime, Default CURRENT_TIMESTAMP

**Relationships**:
- One-to-Many: Wishlists (owned)
- One-to-Many: SharePermissions (as viewer)

**Validation Rules**:
- Username: 3-50 characters, alphanumeric + underscore
- Password: Minimum 8 characters (hashed)

### Wishlist
Represents a collection of wishlist items owned by a user.

**Fields**:
- `id`: Integer, Primary Key, Auto-increment
- `owner_id`: Integer, Foreign Key to User.id, Not Null
- `name`: String(100), Not Null
- `created_at`: DateTime, Default CURRENT_TIMESTAMP

**Relationships**:
- Many-to-One: User (owner)
- One-to-Many: WishlistItems
- One-to-Many: SharePermissions

**Validation Rules**:
- Name: 1-100 characters

### WishlistItem
Represents an individual item in a wishlist.

**Fields**:
- `id`: Integer, Primary Key, Auto-increment
- `wishlist_id`: Integer, Foreign Key to Wishlist.id, Not Null
- `name`: String(200), Not Null
- `note`: Text, Nullable
- `url`: String(500), Nullable
- `created_at`: DateTime, Default CURRENT_TIMESTAMP

**Relationships**:
- Many-to-One: Wishlist

**Validation Rules**:
- Name: 1-200 characters
- URL: Valid URL format if provided

### SharePermission
Represents permission for a user to view another user's wishlist.

**Fields**:
- `id`: Integer, Primary Key, Auto-increment
- `wishlist_id`: Integer, Foreign Key to Wishlist.id, Not Null
- `viewer_id`: Integer, Foreign Key to User.id, Not Null
- `granted_at`: DateTime, Default CURRENT_TIMESTAMP

**Relationships**:
- Many-to-One: Wishlist
- Many-to-One: User (viewer)

**Validation Rules**:
- Unique constraint: (wishlist_id, viewer_id) - prevent duplicate shares
- Cannot share with self: viewer_id != wishlist.owner_id

## State Transitions

### User States
- `active`: Normal user account
- `inactive`: Account disabled (future feature)

### Wishlist States
- `active`: Normal wishlist
- `archived`: Soft-deleted (future feature)

### SharePermission States
- `active`: Permission granted
- `revoked`: Permission removed (future feature)

## Data Integrity Rules

- Foreign key constraints enforce referential integrity
- Unique constraints prevent duplicate usernames and share permissions
- Check constraints validate field lengths and formats
- Cascade deletes: Deleting a user deletes their wishlists and items; deleting a wishlist deletes items and shares</content>
<parameter name="filePath">/Users/aishwaryasingh/Github stuff/GitHub/ai-developed-wishboard-website/specs/001-wishlist-sharing/data-model.md