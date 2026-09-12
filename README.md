# FastAPI Blog

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)
![AWS S3](https://img.shields.io/badge/AWS-S3-orange)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-Async-orange)
![Pytest](https://img.shields.io/badge/Tests-Pytest-orange)
![Moto](https://img.shields.io/badge/AWS%20Mocking-Moto-orange)
![Alembic](https://img.shields.io/badge/Migrations-Alembic-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

A production-oriented full-stack blogging platform built with **FastAPI**, **PostgreSQL**, **SQLAlchemy (Async)**, **AWS S3**, and **Jinja2**. It provides JWT authentication, password reset via email, cloud-based profile image storage, blog management, pagination, and both REST APIs and server-rendered web pages.

> 🚧 **Status:** Active development. The project now includes **Alembic migrations** and an automated **pytest** test suite with isolated PostgreSQL testing and mocked AWS S3 services.

---

# ✨ Features

## Authentication
- User registration & login
- OAuth2 + JWT authentication
- Password hashing
- Protected endpoints
- Password reset via email
- Secure reset tokens with expiration

## Blog Management
- Create, edit and delete posts
- View all posts
- View individual posts
- View posts by author
- User ownership and permission checks
- Partial post updates with `PATCH`
- Paginated post listing with `skip`, `limit`, `total` and `has_more`

## User Profiles
- Update username & email
- Upload profile pictures
- Automatic image resizing (300×300)
- JPEG optimisation
- Automatic replacement/deletion of previous images
- AWS S3 cloud storage

## Frontend
- Jinja2 templates
- Responsive UI
- Flash messages
- Custom error pages

## API
- RESTful APIs
- Swagger UI
- ReDoc
- Request validation with Pydantic
- Pagination support

## Testing
- Automated API tests with **pytest**
- Async endpoint testing with **HTTPX + AnyIO**
- Isolated PostgreSQL test database
- Transaction-based test isolation
- Mocked AWS S3 with **Moto**
- Tests for authentication, users, posts, permissions, pagination, uploads and password-reset email behaviour

---

# 🛠 Tech Stack

## Backend
- FastAPI
- Python 3.11
- SQLAlchemy (Async)
- Pydantic
- OAuth2
- JWT

## Database
- PostgreSQL
- Alembic

## Cloud
- AWS S3
- Boto3
- Moto (testing)

## Testing
- Pytest
- HTTPX
- AnyIO

## Frontend
- HTML5
- CSS3
- JavaScript
- Jinja2

## Planned
- Docker
- GitHub Actions
- Nginx
- VPS Deployment
- Email verification
- Search
- Comments
- Rich text editor
- Likes & bookmarks

---

# 📸 Screenshots

## 📸 Profile Picture Upload + AWS S3

After a profile picture is uploaded, the application automatically:

- ✅ Validates the image
- ✅ Resizes it to **300×300**
- ✅ Converts it to JPEG
- ✅ Uploads it to **AWS S3**
- ✅ Updates the user's profile
- ✅ Deletes the previous profile picture from S3

![Profile Picture Upload + AWS S3](assets/images/s3-profile-upload.png)

---

# 📁 Project Structure

```text
fastapi_blog/
├── alembic/
│   └── versions/
├── assets/
│   └── images/
├── routers/
├── static/
├── templates/
├── tests/
│   ├── conftest.py
│   ├── test_posts.py
│   ├── test_users.py
│   └── test_image.jpg
├── auth.py
├── config.py
├── database.py
├── email_utils.py
├── image_utils.py
├── main.py
├── models.py
├── schemas.py
├── alembic.ini
├── pyproject.toml
└── README.md
```

---

# 🚀 Getting Started

```bash
git clone https://github.com/Pratikshk16/fastapi_blog.git
cd fastapi_blog
uv sync
```

Configure your PostgreSQL database and environment variables, then apply migrations:

```bash
uv run alembic upgrade head
```

Run the application:

```bash
uv run fastapi dev main.py
```

Open:

- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc

---

# 🧪 Running Tests

The project uses **pytest**, **AnyIO**, and **Moto** for automated testing. Tests use a separate PostgreSQL database and mock AWS S3 so that cloud resources are not required during the test suite.

Create the test database configured in `tests/conftest.py`, then run:

```bash
uv run pytest
```

For detailed output:

```bash
uv run pytest -vv
```

The current test suite covers:

- Empty and missing post responses
- Post creation and authentication
- Successful post updates
- Unauthorized post updates
- Pagination behaviour
- User validation and duplicate email handling
- Profile picture uploads to mocked S3
- Password-reset email dispatch

---

# ⚙ Environment Variables

```env
SECRET_KEY=your_secret_key

DATABASE_URL=postgresql+psycopg://user:password@localhost/blog

S3_BUCKET_NAME=your_bucket
S3_REGION=eu-north-1
S3_ACCESS_KEY_ID=your_access_key
S3_SECRET_ACCESS_KEY=your_secret_key

MAIL_SERVER=
MAIL_PORT=
MAIL_USERNAME=
MAIL_PASSWORD=
MAIL_FROM=
MAIL_USE_TLS=true

FRONTEND_URL=http://localhost:8000
```

For tests, `tests/conftest.py` overrides the database, S3 bucket and AWS credentials with test values and runs against a mocked AWS environment.

---

# 🗄 Database Migrations

Database schema changes are managed with **Alembic**.

Create a new migration after model changes:

```bash
uv run alembic revision --autogenerate -m "describe change"
```

Apply migrations:

```bash
uv run alembic upgrade head
```

Rollback the latest migration:

```bash
uv run alembic downgrade -1
```

---

# ☁ AWS S3 Image Pipeline

```text
Browser
   │
Upload Image
   │
FastAPI
   │
Image Validation
   │
Resize (300x300)
   │
JPEG Optimisation
   │
AWS S3
   │
Store filename in PostgreSQL
   │
Render profile image
```

During testing, the same S3 flow is executed against **Moto's mocked AWS environment**, allowing the upload logic to be tested without making real AWS requests.

---

# 📚 API

## Authentication
| Method | Endpoint |
|--------|----------|
| POST | /api/users |
| POST | /api/users/token |
| POST | /api/users/forgot-password |
| POST | /api/users/reset-password |

## Users
| Method | Endpoint |
|--------|----------|
| GET | /api/users/{id} |
| PATCH | /api/users/{id} |
| PATCH | /api/users/{id}/picture |
| DELETE | /api/users/{id}/picture |

## Posts
| Method | Endpoint |
|--------|----------|
| GET | /api/posts |
| POST | /api/posts |
| GET | /api/posts/{id} |
| PUT | /api/posts/{id} |
| PATCH | /api/posts/{id} |
| DELETE | /api/posts/{id} |

### Post Pagination

`GET /api/posts` supports pagination using query parameters:

```text
/api/posts?skip=0&limit=10
```

The response includes:

```json
{
  "posts": [],
  "total": 0,
  "skip": 0,
  "limit": 10,
  "has_more": false
}
```

---

# 🔒 Authentication

1. Register a user via `/api/users`.
2. Login via `/api/users/token`.
3. Copy the returned JWT access token.
4. Click **Authorize** in Swagger UI.
5. Access protected endpoints.

Post update and delete operations also verify that the authenticated user owns the target post.

---

# 🔄 Current Development Progress

- ✅ Alembic migrations added
- ✅ Automated pytest suite added
- ✅ Async API testing with HTTPX + AnyIO
- ✅ PostgreSQL test database setup
- ✅ Transaction-based test isolation
- ✅ Mocked AWS S3 testing with Moto
- ✅ User validation tests
- ✅ Post CRUD and authorization tests
- ✅ Post pagination
- ✅ Profile image upload tests
- ✅ Password reset email test coverage
- ⬜ Docker support
- ⬜ GitHub Actions CI/CD
- ⬜ Nginx
- ⬜ VPS deployment
- ⬜ Email verification
- ⬜ Search
- ⬜ Comments
- ⬜ Rich text editor
- ⬜ Likes & bookmarks

---

# 👨‍💻 Author

**Pratik Suchak**

- GitHub: https://github.com/Pratikshk16

---

# 📄 License

MIT License.
