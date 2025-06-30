# fastapi_database_redis
# 🚀 FastAPI + PostgreSQL + Redis Project

This is a minimal FastAPI project that demonstrates:

- Async PostgreSQL database access using SQLAlchemy + asyncpg
- Redis caching with `aioredis` for GET requests
- Pydantic for data validation

---

## 📂 Project Structure

fastapi_postgres_redis/
├── app/
│ ├── main.py # FastAPI application entrypoint
│ ├── database.py # Async DB session and engine setup
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic schemas
│ ├── crud.py # CRUD operations
│ └── redis_cache.py # Redis caching functions
├── .env # Environment variables
├── requirements.txt # Python dependencies

---

## 🧪 Features

- Add a new item: `POST /items/`
- List items (cached): `GET /items/`
- Caching via Redis with key: `items_{skip}_{limit}`

---

## ⚙️ Requirements

- Python 3.10+
- PostgreSQL installed and running
- Redis installed and running

---

## 🚀 Quick Start

### 1. Clone the project

```bash
unzip fastapi_postgres_redis.zip
cd fastapi_postgres_redis

Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies
pip install -r requirements.txt

### 2. Set up environment variables

Create a `.env` file in the root directory with the following variables:

```bash
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/dbname
REDIS_URL=redis://localhost:6379
```

### 3. Run the application

```bash
uvicorn app.main:app --reload
```

### 4. Test the application

```bash
http POST http://localhost:8000/items name="Test Item"
http GET http://localhost:8000/items
```

### 5. Access the API documentation

```bash
http GET http://localhost:8000/docs
```

---

## 📝 License

MIT License
