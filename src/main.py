import os
import uvicorn
from src.constants import DATA_DIR


class App:
    def __init__(self):
        self._init_notes_folder()

    def run(self):
        uvicorn.run("main:fastapi_app", host="127.0.0.1",
                    port=8000, reload=True)

    def _init_notes_folder(self):
        os.makedirs(DATA_DIR, exist_ok=True)


app = App()
