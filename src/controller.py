from fastapi import FastAPI


fastapi_app = FastAPI(title="Versioned Notes API")

# @fastapi_app.post("/notes/{note_id}")
# def create_note(note_id: str, data: NoteCreateUpdate):
#     return {}

# @fastapi_app.put("/notes/{note_id}")
# def update_note(note_id: str, data: NoteCreateUpdate):
#     return {}

# @fastapi_app.get("/notes/{note_id}")
# def get_latest_note(note_id: str):
#     return {}


# @fastapi_app.get("/notes/{note_id}/versions")
# def list_versions(note_id: str):
#     return {}


# @fastapi_app.get("/notes/{note_id}/diff/{ver1}/{ver2}")
# def get_diff(note_id: str, ver1: int, ver2: int):
#     return {}
