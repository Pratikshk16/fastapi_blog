# FastAPI Blog

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-Async-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

A modern full-stack blogging platform built with **FastAPI**, **SQLAlchemy**, and **Jinja2**. The application provides JWT-based authentication, blog management, user profile customization, and profile picture uploads through both REST APIs and server-rendered web pages.

> 🚧 This project is currently under active development and is being extended with cloud storage, database migrations, testing, containerization, and production deployment.

---

## ✨ Features

### Authentication & Authorization

- User registration and login
- OAuth2 authentication with JWT tokens
- Password hashing and verification
- Protected API endpoints
- User-specific permissions

### Blog Management

- Create blog posts
- View all posts
- View individual posts
- View posts by a specific user
- Update and delete posts

### User Profiles

- User account page
- Upload profile pictures
- Profile image processing and validation
- Secure profile updates

### Frontend

- Server-side rendering with Jinja2 templates
- Responsive HTML pages
- Custom error pages
- Static asset support

### API

- RESTful API endpoints
- Interactive Swagger UI documentation
- Automatic request validation with Pydantic
- Custom exception handling

---

## 🛠️ Tech Stack

### Backend

- FastAPI
- Python 3.11
- SQLAlchemy (Async ORM)
- Pydantic
- OAuth2
- JWT Authentication

### Database

- SQLite (current)
- PostgreSQL (planned)

### Frontend

- HTML5
- CSS3
- JavaScript
- Jinja2 Templates

### DevOps (Planned)

- Docker
- AWS S3
- Boto3
- Alembic
- VPS Deployment
- CI/CD

---

## 📁 Project Structure

```text
fastapi_blog/
│
├── routers/
│   ├── posts.py
│   ├── users.py
│   └── __init__.py
│
├── templates/
│   ├── account.html
│   ├── error.html
│   ├── home.html
│   ├── login.html
│   ├── post.html
│   ├── register.html
│   └── user_posts.html
│
├── static/
│   ├── css/
│   ├── icons/
│   ├── js/
│   └── profile_pics/
│
├── media/
│   └── profile_pics/
│
├── auth.py
├── config.py
├── database.py
├── image_utils.py
├── main.py
├── models.py
├── schemas.py
├── pyproject.toml
├── .env
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/Pratikshk16/fastapi_blog.git

cd fastapi_blog
```

### Create and activate a virtual environment

```bash
python -m venv .venv
```

#### macOS / Linux

```bash
source .venv/bin/activate
```

#### Windows

```powershell
.venv\Scripts\activate
```

### Install dependencies

```bash
uv sync
```

### Create a `.env` file

Create a `.env` file in the project root:

```env
SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30

DATABASE_URL=sqlite+aiosqlite:///./blog.db

PROFILE_PICTURES_DIR=media/profile_pics

MAX_UPLOAD_SIZE_BYTES=5242880
```

### Run the application

```bash
uv run fastapi dev main.py
```

The application will be available at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

ReDoc documentation:

```text
http://127.0.0.1:8000/redoc
```

---

## ⚙️ Automatic Setup

On startup, the application automatically:

- Creates the profile pictures directory if it does not exist.
- Initializes the database tables.
- Mounts static and media files.

> **Note:** Uploaded images (`media/`) and the local SQLite database (`blog.db`) are excluded from version control via `.gitignore`.

---

## 📚 API Endpoints

### Authentication

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| POST | `/api/users/register` | Register a new user |
| POST | `/api/users/token` | Login and obtain a JWT token |

### Users

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| GET | `/api/users/{id}` | Get user details |
| PATCH | `/api/users/{id}/picture` | Upload profile picture |
| PUT | `/api/users/{id}` | Update user profile |

### Posts

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| GET | `/api/posts` | Get all posts |
| POST | `/api/posts` | Create a post |
| GET | `/api/posts/{id}` | Get a post |
| PUT | `/api/posts/{id}` | Update a post |
| DELETE | `/api/posts/{id}` | Delete a post |

---

## 🔒 Authentication

The API uses OAuth2 with JWT Bearer tokens.

1. Register a user.
2. Login using:

```text
POST /api/users/token
```

3. Copy the access token.
4. Open Swagger UI.
5. Click **Authorize**.
6. Paste the token.
7. Access protected endpoints.

---

## 🖼️ Profile Pictures

Users can upload profile pictures via:

```text
PATCH /api/users/{user_id}/picture
```

Features:

- File validation
- Maximum upload size restriction
- Automatic image processing
- Secure file storage
- Replacement of old profile pictures

---

## ⚡ Database

### Current

- SQLite
- SQLAlchemy Async ORM

### Planned

- PostgreSQL
- Alembic migrations

---

## 🧪 Planned Features

- [ ] Pagination
- [ ] Password reset via email
- [ ] PostgreSQL migration
- [ ] Alembic database migrations
- [ ] AWS S3 integration
- [ ] Boto3 file storage
- [ ] API testing with Pytest
- [ ] Docker support
- [ ] VPS deployment
- [ ] CI/CD pipeline

---

## 📌 Project Status

🚧 Active development.

This project is being developed as a production-ready blogging platform and backend learning project. Upcoming features include database migrations, cloud storage, automated testing, containerization, and deployment.

---

## 👨‍💻 Author

**Pratik Suchak**

- GitHub: https://github.com/Pratikshk16

---

## 📄 License

This project is licensed under the MIT License.
