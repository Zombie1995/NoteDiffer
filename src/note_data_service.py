# NOTE: the following allows us use definition of _instance without quotes
from __future__ import annotations

import os
import glob
import re

from src.constants import NOTES_DIR


class NoteDataService:
    """Singleton service for managing note data."""
    _instance: NoteDataService | None = None

    def __init__(self):
        if getattr(self, "_initialized", False):
            return

        os.makedirs(NOTES_DIR, exist_ok=True)

        self._initialized = True

    def __new__(cls, *args, **kwargs):  # noqa: D401 - simple singleton override
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def instance(cls) -> NoteDataService:
        """Return the singleton instance (preferred explicit accessor)."""
        return cls()

    def create_note(self, title: str, content: str) -> dict:
        """Create a new note with version 1.

        Args:
            title: Title of the note (used as folder name)
            content: Content of the note

        Returns:
            dict with note information including title, version, and content
        """
        # Create note directory
        note_dir = os.path.join(NOTES_DIR, title)
        os.makedirs(note_dir, exist_ok=True)

        # Create version 1 file
        version_file = os.path.join(note_dir, "v1.txt")

        with open(version_file, "w", encoding="utf-8") as f:
            f.write(content)

        return {
            "title": title,
            "version": 1,
        }

    def update_note(self, title: str, content: str) -> dict:
        """Update an existing note by creating a new version.

        Args:
            title: Title of the note (folder name)
            content: New content for the note

        Returns:
            dict with note information including title, version, and content

        Raises:
            ValueError: If note with given title doesn't exist
        """
        note_dir = os.path.join(NOTES_DIR, title)

        if not os.path.exists(note_dir):
            raise ValueError(f"Note with title '{title}' not found")

        # Find the latest version
        version_files = glob.glob(os.path.join(note_dir, "v*.txt"))

        if not version_files:
            raise ValueError(f"No version file found for title '{title}'")

        # Extract version numbers and find the maximum
        versions = []
        for file_path in version_files:
            filename = os.path.basename(file_path)
            match = re.match(r'v(\d+)\.txt', filename)
            if match:
                versions.append(int(match.group(1)))

        next_version = max(versions) + 1 if versions else 1

        # Create new version file
        version_file = os.path.join(note_dir, f"v{next_version}.txt")

        with open(version_file, "w", encoding="utf-8") as f:
            f.write(content)

        return {
            "title": title,
            "version": next_version,
        }
