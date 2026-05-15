# API Contracts: Wishlist Management

## GET /dashboard
Get user's dashboard with their wishlists.

**Auth Required**: Yes

**Response 200**:
```json
{
  "user": {
    "id": 123,
    "username": "user123"
  },
  "wishlists": [
    {
      "id": 456,
      "name": "Birthday Wishes",
      "item_count": 5,
      "created_at": "2026-05-14T10:00:00Z"
    }
  ]
}
```

## POST /wishlists
Create a new wishlist.

**Auth Required**: Yes

**Request Body**:
```json
{
  "name": "string (1-100 chars, required)"
}
```

**Response 201**:
```json
{
  "id": 456,
  "name": "Birthday Wishes",
  "created_at": "2026-05-14T10:00:00Z"
}
```

## GET /wishlists/{id}
Get wishlist details and items.

**Auth Required**: Yes (owner or shared viewer)

**Response 200**:
```json
{
  "id": 456,
  "name": "Birthday Wishes",
  "owner": {
    "id": 123,
    "username": "user123"
  },
  "is_owner": true,
  "items": [
    {
      "id": 789,
      "name": "New Laptop",
      "note": "16GB RAM preferred",
      "url": "https://example.com/laptop",
      "created_at": "2026-05-14T10:05:00Z"
    }
  ]
}
```

## POST /wishlists/{id}/items
Add item to wishlist.

**Auth Required**: Yes (owner only)

**Request Body**:
```json
{
  "name": "string (1-200 chars, required)",
  "note": "string (optional)",
  "url": "string (optional, valid URL)"
}
```

**Response 201**:
```json
{
  "id": 789,
  "name": "New Laptop",
  "note": "16GB RAM preferred",
  "url": "https://example.com/laptop",
  "created_at": "2026-05-14T10:05:00Z"
}
```

## PUT /wishlists/{id}/items/{item_id}
Update wishlist item.

**Auth Required**: Yes (owner only)

**Request Body**:
```json
{
  "name": "string (optional)",
  "note": "string (optional)",
  "url": "string (optional)"
}
```

**Response 200**:
```json
{
  "id": 789,
  "name": "Updated Laptop",
  "note": "32GB RAM now",
  "url": "https://example.com/laptop",
  "updated_at": "2026-05-14T10:10:00Z"
}
```

## DELETE /wishlists/{id}/items/{item_id}
Delete wishlist item.

**Auth Required**: Yes (owner only)

**Response 204**: No Content