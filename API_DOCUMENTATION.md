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

## Testing Notes
- Use `http://localhost:8000/api/` for local testing
- All timestamps are in ISO 8601 format
- Tasks are filtered by the authenticated user
- Passwords must be at least 8 characters long
- JWT tokens: Access (60 min), Refresh (7 days)
