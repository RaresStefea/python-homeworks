from __future__ import annotations
import json
from .schema import db_validator, user_book_validator


class UserBooks:
    filepath: str = None

    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    def add_book(self, id_user: int, id_book: int) -> None:

        if self.has_read(id_user, id_book):
            print("Error: User already has this book.")
            return

        json_file = open(self.filepath, "r")
        data = json.load(json_file)
        json_file.close()
        db_validator.validate(data)

        new_entry = {"user_id": id_user, "book_id": id_book}
        user_book_validator.validate(new_entry)

        data["user_books"].append(new_entry)
        db_validator.validate(data)

        new_json = open(self.filepath, "w")
        json.dump(data, new_json)
        new_json.close()

    def get_books(self, id_user: int) -> list:
        json_file = open(self.filepath, "r")
        data = json.load(json_file)
        json_file.close()
        db_validator.validate(data)

        book_ids = [
            ub["book_id"] for ub in data["user_books"] if ub["user_id"] == id_user
        ]
        books = [book for book in data["books"] if book["id"] in book_ids]
        return books

    def has_read(self, id_user: int, id_book: int) -> bool:
        json_file = open(self.filepath, "r")
        data = json.load(json_file)
        json_file.close()
        db_validator.validate(data)

        for ub in data["user_books"]:
            if ub["user_id"] == id_user and ub["book_id"] == id_book:
                return True
        return False

    def remove_book(self, user_id: int, book_id: int) -> None:
        json_file = open(self.filepath, "r")
        data = json.load(json_file)
        json_file.close()
        db_validator.validate(data)

        data["user_books"] = [
            ub
            for ub in data["user_books"]
            if not (ub["user_id"] == user_id and ub["book_id"] == book_id)
        ]
        db_validator.validate(data)

        new_json = open(self.filepath, "w")
        json.dump(data, new_json)
        new_json.close()
