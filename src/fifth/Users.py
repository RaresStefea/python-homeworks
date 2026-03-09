from __future__ import annotations
from . import db


class Users:
    name: str | None= None
    id: int | None = None
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    def add(self, name: str) -> None:
        db.add_record(self.filepath, "users", {"name": name})

    def list(self) -> None:
        db.view_records(self.filepath, "users")

    def get(self, id: int) -> dict | None:
        return db.get_record(self.filepath, "users", id)

    def delete(self, id: int) -> None:
        db.delete_record(self.filepath, "users", id)
