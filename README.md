# Versioned Notes API

**Variant 9 - Versioned Notes**

Python 3.12.0

# Быстрый запуск!!!

Создается db-шка postgres, указываются креды в .env (приведен .env.example), запускаете make up.

Важно!!! Обращается к внешней db-шке postgres.

## Запуск через Docker

```bash
# Запуск приложения и базы данных
make up

# Или вручную
docker-compose up --build
```

API доступен по адресу: http://localhost:8000/docs

## Локальная разработка

### Создание виртуального окружения

```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
```

### Установка зависимостей

```bash
pip install -r requirements.txt
```

### Запуск программы

```bash
python -m src.main
```

## Работа с миграциями базы данных

### Применить миграции

```bash
alembic upgrade head
```

### Создать новую миграцию (автоматически)

```bash
# После изменения моделей в src/db/models.py
alembic revision --autogenerate -m "описание изменений"
```

### Создать миграцию вручную

```bash
alembic revision -m "описание изменений"
```

### Откатить миграцию

```bash
# Откатить последнюю миграцию
alembic downgrade -1

# Откатить все миграции
alembic downgrade base
```

### Посмотреть историю миграций

```bash
alembic history
```

### Посмотреть текущую версию БД

```bash
alembic current
```