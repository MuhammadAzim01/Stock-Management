# Stock-Management

## Overview

This project is a stock trading API built with Django and Django REST Framework. It allows users to perform transactions, manage stocks, and view transaction histories.

## Setup Guide

### Prerequisites

- Docker
- Docker Compose

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/MuhammadAzim01/Stock-Management.git
   cd stock-management
   ```

2. **Set Up Environment Variables**

   Create a `.env` file in the root directory and add the following:

   ```env
   DJANGO_SECRET_KEY=your_secure_secret_key
   DEBUG=True
   REDIS_HOST=redis
   REDIS_PORT=6379
   DB_HOST=db
   DB_PORT=5432
   DB_NAME=stock_trading
   DB_USER=postgres
   DB_PASSWORD=postgres
   ```

### Running the Application with Docker

1. **Build and Start the Docker Containers**

   Use Docker Compose to build and start the application:

   ```bash
   docker-compose up --build
   ```

   This command will build the Docker images and start all the services defined in the `docker-compose.yml` file, including the Django application, PostgreSQL, Redis, Celery, and Flower.

2. **Access the Application**

   - **Django Application**: Open your browser and go to `http://localhost:8000`.
   - **Flower Monitoring**: Open your browser and go to `http://localhost:5555` to monitor Celery tasks.

### Testing the API

To run all tests for the application, use the following command inside the Docker container:

```bash
docker-compose exec web python manage.py test
```

This command will execute all the test cases for transactions, users, and stocks.

## API Endpoints

- **Transactions**
  - `POST /api/transactions/`: Create a new transaction
  - `GET /api/transactions/{user_id}/`: List transactions for a user
  - `GET /api/transactions/{user_id}/{start_timestamp}/{end_timestamp}/`: List transactions within a time range

- **Users**
  - `POST /api/users/`: Create a new user
  - `GET /api/users/{username}/`: Retrieve user details

- **Stocks**
  - `POST /api/stocks/`: Create a new stock
  - `GET /api/stocks/{ticker}/`: Retrieve stock details

## Additional Information

- **Celery**: Used for asynchronous task processing.
- **Redis**: Used as the message broker for Celery.
- **Flower**: Used for monitoring Celery tasks.

For more detailed information, refer to the code and comments within the project.
