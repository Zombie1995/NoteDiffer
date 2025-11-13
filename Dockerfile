FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["sh", "-c", "sleep 10 && alembic upgrade head && uvicorn src.main:fastapi_app --host ${APP_HOST:-0.0.0.0} --port ${APP_PORT:-8000}"]
