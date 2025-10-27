# Project: User Management REST API with Flask, PostgreSQL, and Docker

## Overview

This project is a **User Management REST API** built using **Flask**, **SQLAlchemy**, and **PostgreSQL**, containerized with **Docker Compose**.  
It allows you to create, read, update, and delete users, along with their **employment** and **bank details**.

---

## Tech Stack

- **Backend Framework:** Flask (Python)
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Containerization:** Docker & Docker Compose
- **Language:** Python 3.10

---

## Project Structure

```
Data_eng_pro/
│
├── service/
│   ├── app.py
│   ├── models.py
│   ├── __init__.py
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
└── etl/
    ├── group_users.py
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Data_eng_pro.git
cd Data_eng_pro
```

### 2. Build and start containers

Make sure Docker is running, then execute:

```bash
docker-compose up --build
```

This command:

- Builds the Flask app image
- Spins up both **web** (Flask) and **db** (PostgreSQL) containers
- Automatically creates tables in the database

### 3. Verify setup

Once containers are running:

- Flask API: http://localhost:5000
- PostgreSQL: localhost:5432
  - Username: `postgres`
  - Password: `*********`
  - Database: `postgres`

---

## API Endpoints

### Users

| Method     | Endpoint           | Description                                              |
| ---------- | ------------------ | -------------------------------------------------------- |
| **POST**   | `/users`           | Create a new user (with optional employment & bank info) |
| **GET**    | `/users`           | List all users                                           |
| **GET**    | `/users/<user_id>` | Retrieve specific user and details                       |
| **PUT**    | `/users/<user_id>` | Update user details                                      |
| **DELETE** | `/users/<user_id>` | Delete user and related info                             |

**Example Request:**

```json
POST /users
{
  "first_name": "mallesh",
  "last_name": "kannan",
  "email": "mallesh.kannan@example.com",
  "city": "New York",
  "pincode": "123456",
  "employment": [
    {"company_name": "TechCorp", "designation": "Engineer", "start_date": "2022-01-01"}
  ],
  "banks": [
    {"bank_name": "Axis Bank", "account_number": "987654321", "ifsc": "AXIS0001234"}
  ]
}
```

---

### Employment

| Method   | Endpoint                      | Description                           |
| -------- | ----------------------------- | ------------------------------------- |
| **POST** | `/users/<user_id>/employment` | Add employment info for a user        |
| **GET**  | `/users/<user_id>/employment` | Get all employment details for a user |

---

### Bank Info

| Method   | Endpoint                | Description                      |
| -------- | ----------------------- | -------------------------------- |
| **POST** | `/users/<user_id>/bank` | Add bank info for a user         |
| **GET**  | `/users/<user_id>/bank` | Get all bank accounts for a user |

---

## Running ETL

The project includes a data transformation script (`etl/group_users.py`) that connects to the same database and performs grouping operations.

To run inside the container:

```bash
docker exec -it data_eng_pro-web-1 python etl/group_users.py --db-uri postgresql://postgres:postgres@db:5432/postgres
```

---

## Testing the API

You can use **Postman**, **curl**, or any REST client.

Example:

```bash
curl -X GET http://localhost:5000/users
```

---

## Cleanup

To stop and remove containers:

```bash
docker-compose down
```

To remove everything (including volumes/data):

```bash
docker-compose down -v
```

---

## Environment Variables

You can override defaults in your environment or in `docker-compose.yml`:

```
DATABASE_URL=postgresql://postgres:postgres@db:5432/postgres

```

---

## Future Improvements

- Add pagination and filtering
- Implement JWT authentication
- Add Alembic for migrations
- Build frontend dashboard for user management

---
