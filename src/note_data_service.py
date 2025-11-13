# NOTE: the following allows us use definition of _instance without quotes
from __future__ import annotations

import difflib
from sqlalchemy.orm import Session
from sqlalchemy import desc

from src.db.database import SessionLocal
from src.db.models import Note, NoteVersion


class NoteDataService:
    """Singleton service for managing note data using database."""
    _instance: NoteDataService | None = None

    def __init__(self):
        if getattr(self, "_initialized", False):
            return

        self._initialized = True

    def __new__(cls, *args, **kwargs):  # noqa: D401 - simple singleton override
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def instance(cls) -> NoteDataService:
        """Return the singleton instance (preferred explicit accessor)."""
        return cls()

    def _get_db(self) -> Session:
        """Get a new database session."""
        return SessionLocal()

    def create_note(self, title: str, content: str) -> dict:
        """Create a new note with version 1.

        Args:
            title: Title of the note
            content: Content of the note

        Returns:
            dict with note information including title and version
        """
        db = self._get_db()
        try:
            # Check if note already exists
            existing_note = db.query(Note).filter(Note.title == title).first()
            if existing_note:
                raise ValueError(f"Note with title '{title}' already exists")

            # Create new note
            note = Note(title=title)
            db.add(note)
            db.flush()  # Get the note ID

            # Create version 1
            version = NoteVersion(note_id=note.id, version=1, content=content)
            db.add(version)
            db.commit()

            return {
                "title": title,
                "version": 1,
            }
        except Exception as e:
            db.rollback()
            raise
        finally:
            db.close()

    def update_note(self, title: str, content: str) -> dict:
        """Update an existing note by creating a new version.

        Args:
            title: Title of the note
            content: New content for the note

        Returns:
            dict with note information including title and version

        Raises:
            ValueError: If note with given title doesn't exist
        """
        db = self._get_db()
        try:
            # Find the note
            note = db.query(Note).filter(Note.title == title).first()
            if not note:
                raise ValueError(f"Note with title '{title}' not found")

            # Get the latest version number
            latest_version = db.query(NoteVersion)\
                .filter(NoteVersion.note_id == note.id)\
                .order_by(desc(NoteVersion.version))\
                .first()

            next_version = (latest_version.version +
                            1) if latest_version else 1

            # Create new version
            new_version = NoteVersion(
                note_id=note.id,
                version=next_version,
                content=content
            )
            db.add(new_version)
            db.commit()

            return {
                "title": title,
                "version": next_version,
            }
        except Exception as e:
            db.rollback()
            raise
        finally:
            db.close()

    def get_latest_note(self, title: str) -> dict:
        """Get the latest version of a note.

        Args:
            title: Title of the note

        Returns:
            dict with title, version number, and content

        Raises:
            ValueError: If note with given title doesn't exist
        """
        db = self._get_db()
        try:
            # Find the note
            note = db.query(Note).filter(Note.title == title).first()
            if not note:
                raise ValueError(f"Note with title '{title}' not found")

            # Get the latest version
            latest_version = db.query(NoteVersion)\
                .filter(NoteVersion.note_id == note.id)\
                .order_by(desc(NoteVersion.version))\
                .first()

            if not latest_version:
                raise ValueError(f"No version found for note '{title}'")

            return {
                "title": title,
                "version": latest_version.version,
                "content": latest_version.content,
            }
        finally:
            db.close()

    def list_versions(self, title: str) -> dict:
        """List all versions of a note.

        Args:
            title: Title of the note

        Returns:
            dict with title and list of version numbers

        Raises:
            ValueError: If note with given title doesn't exist
        """
        db = self._get_db()
        try:
            # Find the note
            note = db.query(Note).filter(Note.title == title).first()
            if not note:
                raise ValueError(f"Note with title '{title}' not found")

            # Get all versions
            versions = db.query(NoteVersion.version)\
                .filter(NoteVersion.note_id == note.id)\
                .order_by(NoteVersion.version)\
                .all()

            version_numbers = [v[0] for v in versions]

            return {
                "title": title,
                "versions": version_numbers,
            }
        finally:
            db.close()

    def get_diff(self, title: str, ver1: int, ver2: int) -> dict:
        """Get the difference between two versions of a note.

        Args:
            title: Title of the note
            ver1: First version number
            ver2: Second version number

        Returns:
            dict with title, version numbers, and line-by-line diff

        Raises:
            ValueError: If note or versions don't exist
        """
        db = self._get_db()
        try:
            # Find the note
            note = db.query(Note).filter(Note.title == title).first()
            if not note:
                raise ValueError(f"Note with title '{title}' not found")

            # Get both versions
            version1 = db.query(NoteVersion)\
                .filter(NoteVersion.note_id == note.id, NoteVersion.version == ver1)\
                .first()

            if not version1:
                raise ValueError(
                    f"Version {ver1} not found for note '{title}'")

            version2 = db.query(NoteVersion)\
                .filter(NoteVersion.note_id == note.id, NoteVersion.version == ver2)\
                .first()

            if not version2:
                raise ValueError(
                    f"Version {ver2} not found for note '{title}'")

            # Get content and split into lines
            content1 = version1.content.splitlines()
            content2 = version2.content.splitlines()

            # Generate diff
            diff = list(difflib.unified_diff(
                content1,
                content2,
                fromfile=f"v{ver1}",
                tofile=f"v{ver2}",
                lineterm=""
            ))

            return {
                "title": title,
                "version1": ver1,
                "version2": ver2,
                "diff": diff,
            }
        finally:
            db.close()
