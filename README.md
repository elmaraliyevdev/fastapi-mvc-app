# FastAPI MVC App

This is a FastAPI-based web application following the **MVC design pattern**. It provides **user authentication, post management, and caching** while using **SQLAlchemy ORM**.

## Features
- **User Authentication** (Signup, Login with JWT tokens)
- **Post Management** (Create, Retrieve, Delete Posts)
- **Payload Size Validation** (1MB limit for posts)
- **Caching** (Optimized with TTL cache for 5 minutes)
- **Dependency Injection** for authentication and database access
- **SQLAlchemy ORM**
- **Secure Password Hashing** with bcrypt
- **Token-Based Authentication** with JWT
- **Structured Project Following MVC Pattern**

## Project Structure
```
fastapi_mvc_app/
│── app/
│   ├── api/
│   │   ├── dependencies/
│   │   │   ├── auth.py
│   │   ├── routes/
│   │   │   ├── auth.py
│   │   │   ├── posts.py
│   ├── core/
│   │   ├── config.py
│   │   ├── database.py
│   ├── models/
│   │   ├── user.py
│   │   ├── post.py
│   ├── schemas/
│   │   ├── user.py
│   │   ├── post.py
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── post_service.py
│── main.py
│── requirements.txt
│── .env
│── README.md
```

## Setup & Installation
### 1. Clone the Repository
```bash
git clone https://github.com/elmaraliyevdev/fastapi-mvc-app
cd fastapi-mvc-app
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory and add:
```ini
DATABASE_URL=postgresql+psycopg2://user:password@localhost/db_name
SECRET_KEY=your_super_secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Apply Migrations
```bash
alembic revision --autogenerate -m "Initial migration"
```
```bash
alembic upgrade head  # If Alembic is set up
```

### 6. Run the Application
```bash
uvicorn main:app --reload
```

## API Endpoints

### Authentication
| Method | Endpoint      | Description       |
|--------|--------------|-------------------|
| POST   | `/auth/signup` | Register a user |
| POST   | `/auth/login`  | Login and get a token |

### Post Management
| Method | Endpoint      | Description       |
|--------|--------------|-------------------|
| POST   | `/posts/add`  | Create a post (1MB limit) |
| GET    | `/posts/get`  | Retrieve user's posts (cached for 5 min) |
| DELETE | `/posts/delete` | Delete a post |