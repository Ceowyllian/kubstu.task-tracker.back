# Project management & issue tracker system (backend)

A backend for a project management and issue tracking system, built with Django and REST Framework. This system provides functionality for managing projects, sprints, issues, and teams with real-time updates.

## Tech stack

- Backend Framework: Django 4.2+, Django REST Framework
- Database: PostgreSQL
- Real-time: Django Channels, Redis (Channel Layer)
- Task Queue: Celery, RabbitMQ (Broker)
- Storage: MinIO (S3-compatible)
- Logging: Graylog
- Containerization: Docker, Docker Compose
- API Documentation: Swagger/OpenAPI

## Local development setup

### Prerequisites
- Python 3.12+
- Pipenv
- Make

### Quick start

1. Create a root folder for parts of the project
    ```bash
    mkdir kubstu.task-tracker/back
    cd kubstu.task-tracker/back
    ```
2. Clone the repository
    ```bash
    git clone https://github.com/Ceowyllian/kubstu.task-tracker.back.git
    ```
3. Install dependencies
    ```bash
    pipenv install --dev
    ```
4. Set up environment variables
    ```bash
    cp .env.template src/.env
    # Edit src/.env with your configuration
    ```
5. Set up database
    ```bash
    make migrate
    python src/manage.py createsuperuser
    ```
6. Run development server
    ```bash
    python src/manage.py runserver
    ```
7. Access the application
   - API: http://localhost:8000/api/
   - Admin panel: http://localhost:8000/admin/
   - API docs: http://localhost:8000/oas3/schema/swagger-ui/

## API documentation

API documentation is available at `oas3/schema/swagger-ui/` when running the development server.

### Authentication example

```bash
# Obtain authentication token
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"email": "your@email.com", "password": "your_password"}'

# Use token in requests
curl -H "Authorization: Token your_token_here" \
  http://localhost:8000/api/projects/
```

## Testing

Run the test suite:
```bash
pytest
```

## Related projects
- [Docker repository](https://github.com/Ceowyllian/kubstu.task-tracker.docker)
- [Frontend repository](https://github.com/Ceowyllian/kubstu.task-tracker.front)
