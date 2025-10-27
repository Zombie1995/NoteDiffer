from fastapi import FastAPI, HTTPException
from src.dto import NoteCreate, NoteUpdate
from src.note_data_service import NoteDataService


fastapi_app = FastAPI(title="Versioned Notes API")
note_service = NoteDataService.instance()


@fastapi_app.post("/notes/create")
def create_note(data: NoteCreate):
    """Create a new note."""
    try:
        result = note_service.create_note(data.title, data.content)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@fastapi_app.put("/notes/{title}")
def update_note(title: str, data: NoteUpdate):
    """Update an existing note by creating a new version."""
    try:
        result = note_service.update_note(title, data.content)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@fastapi_app.get("/notes/{note_id}")
def get_latest_note(note_id: str):
    return {}


@fastapi_app.get("/notes/{note_id}/versions")
def list_versions(note_id: str):
    return {}


@fastapi_app.get("/notes/{note_id}/diff/{ver1}/{ver2}")
def get_diff(note_id: str, ver1: int, ver2: int):
    return {}
