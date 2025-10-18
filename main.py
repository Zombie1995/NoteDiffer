from fastapi import FastAPI
from src.main import app
# Don't delete following otherwise not working
from src.controller import fastapi_app

if __name__ == "__main__":
    app.run()
