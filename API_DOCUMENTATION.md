# TaskSphere API Documentation

## Base URL
```
http://localhost:8000/api/
```

## Authentication
All endpoints except `/register` and `/login` require JWT authentication.
Include the token in the Authorization header:
```
Authorization: Bearer <access_token>
```

---

## Authentication Endpoints

### 1. User Registration ✅
**URL:** `POST /api/register/`

**Request Body:**
```json
{
    "username": "testuser",
    "email": "test@example.com",
    "password": "password123",
    "password_confirm": "password123"
}
```

**Response (201 Created):**
```json
{
    "user": {
        "id": 1,
        "username": "testuser",
        "email": "test@example.com",
        "date_joined": "2026-03-15T06:38:00Z"
    },
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

---

### 2. User Login ✅
**URL:** `POST /api/login/`

**Request Body:**
```json
{
    "username": "testuser",
    "password": "password123"
}
```

**Response (200 OK):**
```json
{
    "user": {
        "id": 1,
        "username": "testuser",
        "email": "test@example.com",
        "date_joined": "2026-03-15T06:38:00Z"
    },
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

---

### 3. User Profile ✅
**URL:** `GET /api/profile/`
**Authentication:** Required

**Response (200 OK):**
```json
{
    "id": 1,
    "username": "testuser",
    "email": "test@example.com",
    "date_joined": "2026-03-15T06:38:00Z"
}
```

---

### 4. Token Refresh ✅
**URL:** `POST /api/token/refresh/`

**Request Body:**
```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

**Response (200 OK):**
```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

---

## Task Management Endpoints

### 5. List Tasks ✅
**URL:** `GET /api/tasks/`
**Authentication:** Required

**Response (200 OK):**
```json
[
    {
        "id": 1,
        "title": "Complete project setup",
        "description": "Set up Django project with authentication",
        "status": "todo",
        "created_at": "2026-03-15T06:38:00Z",
        "updated_at": "2026-03-15T06:38:00Z"
    }
]
```

---

### 6. Create Task ✅
**URL:** `POST /api/tasks/`
**Authentication:** Required

**Request Body:**
```json
{
    "title": "New task",
    "description": "Task description",
    "status": "todo"
}
```

**Response (201 Created):**
```json
{
    "id": 2,
    "title": "New task",
    "description": "Task description",
    "status": "todo",
    "created_at": "2026-03-15T06:38:00Z",
    "updated_at": "2026-03-15T06:38:00Z"
}
```

---

### 7. Get Task Detail ✅
**URL:** `GET /api/tasks/<id>/`
**Authentication:** Required

**Response (200 OK):**
```json
{
    "id": 1,
    "title": "Complete project setup",
    "description": "Set up Django project with authentication",
    "status": "todo",
    "created_at": "2026-03-15T06:38:00Z",
    "updated_at": "2026-03-15T06:38:00Z"
}
```

---

### 7. Update Task Status ✅
**URL:** `PATCH /api/tasks/<id>/status/`
**Authentication:** Required

**Request Body:**
```json
{
    "status": "in_progress"
}
```

**Response (200 OK):**
```json
{
    "id": 1,
    "title": "Complete project setup",
    "description": "Set up Django project with authentication",
    "status": "in_progress",
    "created_at": "2026-03-15T06:38:00Z",
    "updated_at": "2026-03-15T06:38:00Z"
}
```

**Response (400 Bad Request):**
```json
{
    "error": "Invalid status 'invalid_status'. Must be one of: ['todo', 'in_progress', 'completed']"
}
```

---

### 8. Update Task ✅
**URL:** `PUT /api/tasks/<id>/` or `PATCH /api/tasks/<id>/`
**Authentication:** Required

**Request Body (PUT):**
```json
{
    "title": "Updated task title",
    "description": "Updated description",
    "status": "in_progress"
}
```

**Request Body (PATCH):**
```json
{
    "title": "Updated title only"
}
```

**Response (200 OK):**
```json
{
    "id": 1,
    "title": "Updated task title",
    "description": "Updated description",
    "status": "in_progress",
    "created_at": "2026-03-15T06:38:00Z",
    "updated_at": "2026-03-15T06:38:00Z"
}
```

**Response (400 Bad Request):**
```json
{
    "title": ["Title cannot be empty"]
}
```

---

### 9. Delete Task ✅
**URL:** `PUT /api/tasks/<id>/` or `PATCH /api/tasks/<id>/`
**Authentication:** Required

**Request Body (PUT):**
```json
{
    "title": "Updated task title",
    "description": "Updated description",
    "status": "in_progress"
}
```

**Request Body (PATCH):**
```json
{
    "status": "completed"
}
```

**Response (200 OK):**
```json
{
    "id": 1,
    "title": "Updated task title",
    "description": "Updated description",
    "status": "completed",
    "created_at": "2026-03-15T06:38:00Z",
    "updated_at": "2026-03-15T06:38:00Z"
}
```

---

### 9. Delete Task ✅
**URL:** `DELETE /api/tasks/<id>/`
**Authentication:** Required

**Response (204 No Content)**

---

## Status Options
- `todo` - Task not started
- `in_progress` - Task currently being worked on
- `completed` - Task finished

---

## Error Responses

### 401 Unauthorized
```json
{
    "detail": "Authentication credentials were not provided."
}
```

### 403 Forbidden
```json
{
    "detail": "You do not have permission to perform this action."
}
```

### 404 Not Found
```json
{
    "detail": "Not found."
}
```

---

## Testing Results ✅
All endpoints have been tested and are working correctly:
- ✅ User Registration (201)
- ✅ User Login (200)
- ✅ User Profile (200)
- ✅ Task Creation (201)
- ✅ Task List (200)
- ✅ Task Detail (200)
- ✅ Task Update (200)
- ✅ Task Delete (204)

---

## User Story 7 Implementation ✅

### Changes Made:
- ✅ Enhanced TaskSerializer with comprehensive field validation
- ✅ Added title validation (empty check, max length)
- ✅ Existing TaskDetailView supports PUT/PATCH operations
- ✅ Full task updates (title, description, status)
- ✅ Partial updates (individual fields)
- ✅ Proper error handling for invalid data
- ✅ User permission enforcement (only task owner can edit)

### Features:
- **PUT Endpoint**: `PUT /api/tasks/<id>/` for full updates
- **PATCH Endpoint**: `PATCH /api/tasks/<id>/` for partial updates
- **Field Validation**: Title (required, max 200 chars), Status (choices)
- **Error Handling**: Clear validation error messages
- **Authentication**: Required for all editing operations

### Validation Rules:
- Title: Required, max 200 characters, cannot be empty
- Status: Must be one of ['todo', 'in_progress', 'completed']
- Description: Optional, can be blank
- User Isolation: Users can only edit their own tasks

---

## User Story 6 Implementation ✅

### Changes Made:
- ✅ Added status validation in TaskSerializer
- ✅ Created dedicated status update endpoint: `PATCH /api/tasks/<id>/status/`
- ✅ Enhanced existing PATCH endpoint for status updates
- ✅ Proper error handling for invalid statuses
- ✅ Status choices: 'todo', 'in_progress', 'completed'

### Features:
- **Dedicated Status Endpoint**: `PATCH /api/tasks/<id>/status/`
- **General Update Support**: Status can also be updated via `PATCH /api/tasks/<id>/`
- **Validation**: Only valid statuses accepted
- **Error Handling**: Clear error messages for invalid status values
- **Authentication**: Required for all status updates

### Status Options:
- `todo` - Task not started
- `in_progress` - Task currently being worked on
- `completed` - Task finished

---

## Testing Notes
- Use `http://localhost:8000/api/` for local testing
- All timestamps are in ISO 8601 format
- Tasks are filtered by the authenticated user
- Passwords must be at least 8 characters long
- JWT tokens: Access (60 min), Refresh (7 days)
