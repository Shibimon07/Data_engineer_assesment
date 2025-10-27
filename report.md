# Project Report – Data Engineering Assessment

## What I Built

- A **Flask REST API** with CRUD endpoints for:
  - `users`
  - `employment_info`
  - `user_bank_info`
- **PostgreSQL database** with a well-defined schema and initial seed data.
- An **ETL script (`etl/group_users.py`)** that:
  - Connects to the PostgreSQL database.
  - Groups users by **bank**, **company**, and **pincode**.
  - Saves the grouped data as separate **CSV files**.
- **Docker + docker-compose** setup to easily run the database and API together.

---

## Implementation Overview

1. **Developed Flask application** with endpoints for creating, updating, listing, and deleting users.
2. **Linked models** (`User`, `EmploymentInfo`, `UserBankInfo`) using **SQLAlchemy ORM**.
3. **ETL script** was built using **Pandas** and **SQLAlchemy** to read from the DB and write group-based CSV outputs.
4. **Dockerized** the entire project for smooth setup and portability.

---

## Improvements & Future Work

- Add **input validation** and **error handling**.
- Implement **authentication and authorization** for the API.
- Add **pagination and filtering** for large datasets.
- Write **unit tests** for API and ETL components.
- Add **CI/CD integration** for automatic testing and deployment.
