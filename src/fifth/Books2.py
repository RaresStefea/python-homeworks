from __future__ import annotations
from . import db


class Books:
    title: str | None= None
    author: str | None= None
    year: int | None= None
    
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    def add(self, title: str, author: str, year: int) -> None:
        db.add_record(self.filepath, "books", {"title": title, "author": author, "year": year})

    def list(self) -> None:
        db.view_records(self.filepath, "books")

    def get(self, id: int) -> dict | None:
        return db.get_record(self.filepath, "books", id)

    def delete(self, id: int) -> None:
        db.delete_record(self.filepath, "books", id)
