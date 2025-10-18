import os
import uvicorn
from src.constants import NOTES_DIR
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path
import difflib

print(NOTES_DIR)


def init_notes_folder(path):
    os.makedirs(path, exist_ok=True)


def init():
    init_notes_folder(NOTES_DIR)


app = FastAPI(title="Versioned Notes API")


# @app.post("/notes/{note_id}")
# def create_note(note_id: str, data: NoteCreateUpdate):
#     return {}

# @app.put("/notes/{note_id}")
# def update_note(note_id: str, data: NoteCreateUpdate):
#     return {}

# @app.get("/notes/{note_id}")
# def get_latest_note(note_id: str):
#     return {}


# @app.get("/notes/{note_id}/versions")
# def list_versions(note_id: str):
#     return {}


# @app.get("/notes/{note_id}/diff/{ver1}/{ver2}")
# def get_diff(note_id: str, ver1: int, ver2: int):
#     return {}

init()


def run():
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
