from __future__ import annotations
import os, csv, json


def init_db(filepath: str) -> None:
    if os.path.exists(filepath):
        print("Error: Database already exists!")
    else:
        records = {"entries": []}
        file = open(filepath, "w")
        json.dump(records, file)  # dump to a file
        file.close()


def add_record(filepath: str, id: int, name: str, age: str, city: str) -> None:

    file = open(filepath, "r")
    data = json.load(file)

    new_entry = {"id": id, "name": name, "age": age, "city": city}
    data["entries"].append(new_entry)
    file.close()

    json_file = open(filepath, "w")
    json.dump(data, json_file)

    print("Record added!")
    json_file.close()


def view_records(filepath: str) -> None:
    json_file = open(filepath, "r")
    data = json.load(json_file)

    for entry in data["entries"]:
        print(
            f"Entry: ID: {entry['id']}, Name: {entry['name']}, Age: {entry['age']}, City: {entry['city']}"
        )

    json_file.close()


def search_record(filepath: str, search_term: str) -> None:
    json_file = open(filepath, "r")
    data = json.load(json_file)
    for entry in data["entries"]:
        if (
            str(entry.get("id")) == search_term
            or entry.get("name") == search_term
            or entry.get("age") == search_term
            or entry.get("city") == search_term
        ):
            print(entry)
    json_file.close()


def delete_record(filepath: str, delete_term: str) -> None:
    json_file = open(filepath, "r")
    data = json.load(json_file)

    new_entries = [
        entry
        for entry in data["entries"]
        if not any(
            delete_term in str(entry[field]) for field in ("id", "name", "age", "city")
        )
    ]
    data["entries"] = new_entries
    json_file.close()

    new_json = open(filepath, "w")
    json.dump(data, new_json)
    new_json.close()


def update_record(filepath: str, id: int, key: str, new_value: str) -> None:
    json_file = open(filepath, "r")
    data = json.load(json_file)
    json_file.close()

    key = key.lower()
    if key not in ("id", "name", "age", "city"):
        print("Error: Invalid key(id, name, age, city).")

    for entry in data["entries"]:
        if entry["id"] == id:
            entry[key] = new_value

    new_json = open(filepath, "w")
    json.dump(data, new_json)
    new_json.close()


# /Users/2473261/database.json
