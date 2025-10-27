from pydantic import BaseModel


class NoteCreate(BaseModel):
    """Schema for creating or updating a note.

    FastAPI requires request bodies to be Pydantic models (or compatible types).
    The previous implementation was a plain Python class, which FastAPI could
    not introspect to build a request body schema, causing the FastAPIError.
    """
    title: str
    content: str


class NoteUpdate(BaseModel):
    """Schema for updating a note."""
    content: str
