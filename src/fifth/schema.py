from __future__ import annotations
from jsonschema.validators import validator_for

USER_SCHEMA: dict[str, object] = {
    "schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://homework.com/user.schema.json",
    "title": "User",
    "descritpion": "A user entry in the database.",
    "type": "object",
    "additionalProperties": False,
    "required": ["id", "name"],
    "properties": {
        "id": {"type": "integer", "minimum": 1},
        "name": {"type": "string", "minLength": 1, "maxLength": 200},
    },
}

BOOK_SCHEMA: dict[str, object] = {
    "schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://homework.com/book.schema.json",
    "title": "Book",
    "descritpion": "A book entry in the database.",
    "type": "object",
    "additionalProperties": False,
    "required": ["id", "title", "author", "year"],
    "properties": {
        "id": {"type": "integer", "minimum": 1},
        "title": {"type": "string", "minLength": 1, "maxLength": 300},
        "author": {"type": "string", "minLength": 1, "maxLength": 200},
        "year": {"type": "integer", "minimum": 0},
    },
}

USER_BOOK_SCHEMA: dict[str, object] = {
    "schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://homework.com/user_book.schema.json",
    "title": "UserBook",
    "descritpion": "A user-book relationship entry in the database.",
    "type": "object",
    "additionalProperties": False,
    "required": ["user_id", "book_id"],
    "properties": {
        "user_id": {"type": "integer", "minimum": 1},
        "book_id": {"type": "integer", "minimum": 1},
    },
}

DB_SCHEMA: dict[str, object] = {
    "schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://homework.com/database.schema.json",
    "title": "Database",
    "descritpion": "The schema of the database object.",
    "type": "object",
    "additionalProperties": False,
    "required": ["users", "books", "user_books"],
    "properties": {
        "users": {"type": "array", "items": USER_SCHEMA, "uniqueItems": False},
        "books": {"type": "array", "items": BOOK_SCHEMA, "uniqueItems": False},
        "user_books": {"type": "array", "items": USER_BOOK_SCHEMA, "uniqueItems": False},
    },
}

UserValidatorClass = validator_for(USER_SCHEMA)
BookValidatorClass = validator_for(BOOK_SCHEMA)
UserBookValidatorClass = validator_for(USER_BOOK_SCHEMA)
DBValidatorClass = validator_for(DB_SCHEMA)

user_validator = UserValidatorClass(USER_SCHEMA)
book_validator = BookValidatorClass(BOOK_SCHEMA)
user_book_validator = UserBookValidatorClass(USER_BOOK_SCHEMA)
db_validator = DBValidatorClass(DB_SCHEMA)
