FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["sh", "-c", "sleep 15 && alembic upgrade head && uvicorn src.main:fastapi_app --host 0.0.0.0 --port 8000 --reload"]
