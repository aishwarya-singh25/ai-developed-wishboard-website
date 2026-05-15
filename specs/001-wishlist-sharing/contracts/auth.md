# API Contracts: Authentication

## POST /auth/signup
Create a new user account.

**Request Body**:
```json
{
  "username": "string (3-50 chars, required)",
  "password": "string (min 8 chars, required)"
}
```

**Response 201**:
```json
{
  "message": "Account created successfully",
  "user_id": 123
}
```

**Response 400**:
```json
{
  "error": "Username already exists" | "Invalid username format" | "Password too short"
}
```

## POST /auth/login
Authenticate user and start session.

**Request Body**:
```json
{
  "username": "string (required)",
  "password": "string (required)"
}
```

**Response 200**:
```json
{
  "message": "Login successful",
  "redirect": "/dashboard"
}
```

**Response 401**:
```json
{
  "error": "Invalid credentials"
}
```

## POST /auth/logout
End user session.

**Response 200**:
```json
{
  "message": "Logged out successfully",
  "redirect": "/"
}
```