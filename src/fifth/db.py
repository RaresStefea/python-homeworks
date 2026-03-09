from __future__ import annotations
import os, json
from .schema import db_validator, user_validator, book_validator

# maps each table to its entry-level validator
entry_validators = {
    "users": user_validator,
    "books": book_validator,
}


def init_db(filepath: str) -> None:
    if os.path.exists(filepath):
        print("Error: Database already exists!")
    else:
        data = {"users": [], "books": [], "user_books": []}
        file = open(filepath, "w")
        json.dump(data, file)
        file.close()


def follow_id(filepath: str, table: str) -> int:
    file = open(filepath, "r")
    data = json.load(file)
    file.close()
    db_validator.validate(data)

    entries = data[table]
    start = 1

    if entries:
        start = max(int(element["id"]) for element in entries) + 1

    return start


def add_record(filepath: str, table: str, entry: dict) -> None:
    file = open(filepath, "r")
    data = json.load(file)
    file.close()
    db_validator.validate(data)

    entry["id"] = follow_id(filepath, table)
    entry_validators[table].validate(entry)

    data[table].append(entry)
    db_validator.validate(data)

    json_file = open(filepath, "w")
    json.dump(data, json_file)
    json_file.close()


def view_records(filepath: str, table: str) -> None:
    json_file = open(filepath, "r")
    data = json.load(json_file)
    db_validator.validate(data)

    for entry in data[table]:
        print(entry)

    json_file.close()


def get_record(filepath: str, table: str, id: int) -> dict | None:
    json_file = open(filepath, "r")
    data = json.load(json_file)
    json_file.close()
    db_validator.validate(data)

    for entry in data[table]:
        if entry["id"] == id:
            return entry
    return None


def delete_record(filepath: str, table: str, id: int) -> None:
    json_file = open(filepath, "r")
    data = json.load(json_file)
    json_file.close()
    db_validator.validate(data)

    data[table] = [entry for entry in data[table] if entry["id"] != id]
    db_validator.validate(data)

    new_json = open(filepath, "w")
    json.dump(data, new_json)
    new_json.close()
