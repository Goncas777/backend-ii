cd django_project
uv run python manage.py runserver
uv run uvicorn fastapi_app.main:app --host 127.0.0.1 --port 8001