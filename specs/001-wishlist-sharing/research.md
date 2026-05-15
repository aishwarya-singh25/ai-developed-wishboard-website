# Research: Wishlist Sharing Website

## Decisions

### Backend Framework
**Decision**: Use FastAPI for the Python backend.

**Rationale**: FastAPI provides modern async API capabilities, automatic OpenAPI documentation, and strong typing with Pydantic. It's lightweight yet powerful for web applications, aligning with the simplicity principle.

**Alternatives Considered**:
- Flask: Simpler but lacks built-in async support and OpenAPI generation.
- Django: More feature-rich but heavier, better for complex apps.

### Database and ORM
**Decision**: Use SQLAlchemy with SQLite for data persistence.

**Rationale**: SQLAlchemy provides robust ORM capabilities with SQLite's simplicity for local development. Supports relationships and migrations if needed.

**Alternatives Considered**:
- Direct SQLite: Too low-level, increases boilerplate.
- PostgreSQL: Overkill for simple local app.

### Authentication
**Decision**: Implement basic username/password authentication with bcrypt hashing.

**Rationale**: Simple and secure for the scope. Uses session-based auth with FastAPI's session middleware.

**Alternatives Considered**:
- JWT tokens: More complex for simple web app.
- OAuth: Unnecessary without external providers.

### Frontend Approach
**Decision**: Use vanilla HTML/CSS/JS with FastAPI template rendering.

**Rationale**: Keeps code minimal and simple, no build tools needed. FastAPI can serve HTML directly.

**Alternatives Considered**:
- React/Vue: Adds complexity and build steps.
- Static HTML: Would require separate server.

### Testing Strategy
**Decision**: Use pytest for unit and integration tests.

**Rationale**: Standard Python testing framework, integrates well with FastAPI's TestClient.

**Alternatives Considered**:
- unittest: Built-in but less convenient.

### Security Considerations
**Decision**: Basic security: hashed passwords, CSRF protection, input validation.

**Rationale**: Essential for user accounts without overcomplicating.

**Alternatives Considered**:
- Advanced security: Not needed for simple app.

### Deployment
**Decision**: Local development with SQLite, production-ready structure.

**Rationale**: Simple deployment, can run with `uvicorn` or similar.

**Alternatives Considered**:
- Docker: Could be added later if needed.</content>
<parameter name="filePath">/Users/aishwaryasingh/Github stuff/GitHub/ai-developed-wishboard-website/specs/001-wishlist-sharing/research.md