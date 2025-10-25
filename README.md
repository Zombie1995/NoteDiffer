Python 3.12.0

я выбрал вариант 9 - versioned notes

Создание виртуального окружения и установка зависимостей

```bash
python -m venv venv
source venv/bin/activate  # for Linux/MacOS
venv\Scripts\activate     # for Windows

pip freeze > requirements.txt

pip install -r requirements.txt
```

Запуск программы

```python
python main.py
```