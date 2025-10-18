import os
import uvicorn
from src.constants import NOTES_DIR
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import difflib


class App:
    def __init__(self):
        self._init_notes_folder()

    def run(self):
        uvicorn.run("main:fastapi_app", host="127.0.0.1",
                    port=8000, reload=True)

    def _init_notes_folder(self):
        os.makedirs(NOTES_DIR, exist_ok=True)


app = App()
