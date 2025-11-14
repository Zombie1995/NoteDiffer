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


@fastapi_app.get("/notes/{title}")
def get_latest_note(title: str):
    """Get the latest version of a note."""
    try:
        result = note_service.get_latest_note(title)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@fastapi_app.get("/notes/{title}/versions")
def list_versions(title: str):
    """List all versions of a note."""
    try:
        result = note_service.list_versions(title)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@fastapi_app.get("/notes/{note_id}/diff/{ver1}/{ver2}")
def get_diff(note_id: str, ver1: int, ver2: int):
    """Get the difference between two versions of a note."""
    try:
        result = note_service.get_diff(note_id, ver1, ver2)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
