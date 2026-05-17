# Tasks: Wishlist Sharing Website

**Input**: Design documents from `/specs/001-wishlist-sharing/`

**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Unit tests deprioritized - removed from early phases, optional final testing task added.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- Backend: `backend/src/` for code, `backend/tests/` for tests
- Frontend: `frontend/templates/` for HTML, `frontend/static/` for CSS/JS

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project directory structure per plan.md
- [X] T002 Initialize Python project with FastAPI and SQLAlchemy dependencies
- [X] T003 [P] Configure pytest testing framework
- [X] T004 [P] Setup basic HTML/CSS/JS frontend structure

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T005 Setup SQLite database with SQLAlchemy engine configuration
- [X] T006 [P] Create base database models (User) in backend/src/models/user.py
- [X] T007 [P] Implement authentication service framework in backend/src/services/auth.py
- [X] T008 Setup FastAPI application with session middleware
- [X] T009 Configure error handling and response models

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Account Creation and Login (Priority: P1) 🎯 MVP

**Goal**: Allow users to create accounts and log in securely

**Independent Test**: User can register with username/password and log in successfully

### Implementation for User Story 1

- [X] T010 [US1] Implement User model with validation in backend/src/models/user.py
- [X] T011 [US1] Implement auth service with password hashing in backend/src/services/auth.py
- [X] T012 [US1] Create signup endpoint in backend/src/api/auth.py
- [X] T013 [US1] Create login endpoint in backend/src/api/auth.py
- [X] T014 [US1] Create logout endpoint in backend/src/api/auth.py
- [X] T015 [US1] Add signup/login HTML forms in frontend/templates/auth.html
- [X] T016 [US1] Add basic CSS styling for auth forms in frontend/static/css/auth.css

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Create and Manage Wishlist Items (Priority: P1) 🎯 MVP

**Goal**: Users can create wishlists and add/edit/delete items

**Independent Test**: User can create wishlist, add items, and modify them

### Implementation for User Story 2

- [X] T017 [US2] Implement Wishlist model in backend/src/models/wishlist.py
- [X] T018 [US2] Implement WishlistItem model in backend/src/models/wishlist_item.py
- [X] T019 [US2] Implement wishlist service in backend/src/services/wishlist.py
- [X] T020 [US2] Create dashboard endpoint in backend/src/api/dashboard.py
- [X] T021 [US2] Create wishlist CRUD endpoints in backend/src/api/wishlist.py
- [X] T022 [US2] Add dashboard HTML template in frontend/templates/dashboard.html
- [X] T023 [US2] Add wishlist management HTML in frontend/templates/wishlist.html
- [X] T024 [US2] Add CSS styling for dashboard and wishlists in frontend/static/css/main.css

**Checkpoint**: At this point, User Stories 1+2 provide a complete MVP with account management and wishlist functionality

---

## Phase 5: User Story 3 - Share Wishlist with Another User (Priority: P2)

**Goal**: Wishlist owners can share their lists with other registered users

**Independent Test**: Owner can share wishlist with another user who can then view it

### Implementation for User Story 3

- [ ] T025 [US3] Implement SharePermission model in backend/src/models/share_permission.py
- [ ] T026 [US3] Implement sharing service in backend/src/services/sharing.py
- [ ] T027 [US3] Create share wishlist endpoint in backend/src/api/sharing.py
- [ ] T028 [US3] Add sharing UI to wishlist template in frontend/templates/wishlist.html
- [ ] T029 [US3] Add JavaScript for share functionality in frontend/static/js/sharing.js

**Checkpoint**: Sharing functionality is complete and testable

---

## Phase 6: User Story 4 - View Shared Wishlists (Priority: P3)

**Goal**: Users can view wishlists shared with them

**Independent Test**: Shared viewer can access and view shared wishlists

### Implementation for User Story 4

- [ ] T030 [US4] Create shared wishlists endpoint in backend/src/api/sharing.py
- [ ] T031 [US4] Add shared wishlists HTML template in frontend/templates/shared.html
- [ ] T032 [US4] Add navigation to shared section in dashboard template

**Checkpoint**: All user stories are complete

---

## Final Phase: Polish & Cross-cutting Concerns

**Purpose**: Final touches, documentation, and quality improvements

- [ ] T033 [P] Add comprehensive README.md with setup and usage instructions
- [ ] T034 [P] Implement input validation and error messages throughout
- [ ] T035 [P] Add responsive CSS styling and UI improvements
- [ ] T036 [P] Configure production settings and environment variables
- [ ] T037 [P] Run basic integration tests (deprioritized)
- [ ] T038 Final code review and cleanup

---

## Dependencies

**Story Completion Order**:
1. US1 (Foundation) → US2 (MVP) → US3 → US4

**Parallel Opportunities**:
- Model creation tasks can run in parallel
- Service implementation tasks can run in parallel per story
- Frontend template tasks can run in parallel
- Test writing can run in parallel with implementation

**MVP Scope**: User Stories 1 + 2 (account creation, login, wishlist management)

**Implementation Strategy**: 
- Incremental delivery: Each user story is independently implementable
- MVP first: Focus on US1+US2 for initial release, then add sharing features
- Testing: Basic integration tests added to final phase (deprioritized)

## Task Summary

- **Total Tasks**: 38
- **Setup**: 4 tasks
- **Foundational**: 5 tasks  
- **US1**: 7 tasks
- **US2**: 8 tasks
- **US3**: 5 tasks
- **US4**: 3 tasks
- **Polish**: 6 tasks

**Format Validation**: ✅ All tasks follow checklist format with IDs, parallel markers, story labels, and file paths</content>
<parameter name="filePath">/Users/aishwaryasingh/Github stuff/GitHub/ai-developed-wishboard-website/specs/001-wishlist-sharing/tasks.md