
# FastAPI Blog

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)
![AWS S3](https://img.shields.io/badge/AWS-S3-orange)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-Async-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

A production-oriented full-stack blogging platform built with **FastAPI**, **PostgreSQL**, **SQLAlchemy (Async)**, **AWS S3**, and **Jinja2**. It provides JWT authentication, password reset via email, cloud-based profile image storage, blog management, and both REST APIs and server-rendered web pages.

> 🚧 **Status:** Active development. Current focus includes Alembic migrations, automated testing, Docker, CI/CD and production deployment.

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
- View posts by author
- User permissions

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

## Cloud
- AWS S3
- Boto3

## Frontend
- HTML5
- CSS3
- JavaScript
- Jinja2

## Planned
- Alembic
- Docker
- GitHub Actions
- Nginx
- VPS Deployment

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
├── routers/
├── templates/
├── static/
├── auth.py
├── config.py
├── database.py
├── email_utils.py
├── image_utils.py
├── models.py
├── schemas.py
├── main.py
├── pyproject.toml
├── .env
└── README.md
```

---

# 🚀 Getting Started

```bash
git clone https://github.com/Pratikshk16/fastapi_blog.git
cd fastapi_blog
uv sync
```

Run:

```bash
uv run fastapi dev main.py
```

Open:

- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc

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

---

# ☁ AWS S3 Image Pipeline

```
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

---

# 📚 API

## Authentication
| Method | Endpoint |
|--------|----------|
| POST | /api/users/register |
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
| DELETE | /api/posts/{id} |

---

# 🔒 Authentication

1. Register
2. Login via `/api/users/token`
3. Copy JWT
4. Authorize in Swagger
5. Access protected endpoints

---

# 🧪 Roadmap

- [ ] Alembic migrations
- [ ] Docker support
- [ ] Pytest suite
- [ ] GitHub Actions CI/CD
- [ ] Email verification
- [ ] Search
- [ ] Comments
- [ ] Rich text editor
- [ ] Likes & bookmarks

---

# 👨‍💻 Author

**Pratik Suchak**

- GitHub: https://github.com/Pratikshk16

---

# 📄 License

MIT License.
