# API Contracts: Wishlist Sharing

## POST /wishlists/{id}/share
Share wishlist with another user.

**Auth Required**: Yes (owner only)

**Request Body**:
```json
{
  "username": "string (required, existing user)"
}
```

**Response 201**:
```json
{
  "message": "Wishlist shared successfully",
  "viewer": {
    "id": 124,
    "username": "friend123"
  }
}
```

**Response 400**:
```json
{
  "error": "User not found" | "Already shared" | "Cannot share with yourself"
}
```

## GET /shared
Get wishlists shared with current user.

**Auth Required**: Yes

**Response 200**:
```json
{
  "shared_wishlists": [
    {
      "id": 456,
      "name": "Birthday Wishes",
      "owner": {
        "id": 123,
        "username": "user123"
      },
      "shared_at": "2026-05-14T10:15:00Z",
      "item_count": 5
    }
  ]
}
```

## DELETE /wishlists/{id}/share/{viewer_id}
Revoke sharing permission.

**Auth Required**: Yes (owner only)

**Response 204**: No Content

**Response 404**:
```json
{
  "error": "Share permission not found"
}
```