from __future__ import annotations
from jsonschema.validators import validator_for

ENTRY_SCHEMA: dict[str, object] = {
    "schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://homework.com/entry.schema.json",
    "title": "Entry",
    "descritpion": "A person entry in the database.",
    "type": "object",
    "additionalProperties": False,
    "required": ["id", "name", "age", "city"],
    "properties": {
        "id": {"type": "integer", "minimum": 1},
        "name": {"type": "string", "minLength": 1, "maxLength": 200},
        "age": {"type": "integer", "minimum": 0, "maximum": 150},
        "city": {"type": "string", "minLength": 1, "maxLength": 120},
    },
}

DB_SCHEMA: dict[str, object] = {
    "schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://homework.com/database.schema.json",
    "title": "Database",
    "descritpion": "The schema of the database object.",
    "type": "object",
    "additionalProperties": False,
    "required": ["entries"],
    "properties": {
        "entries": {
            "type": "array",
            "items": ENTRY_SCHEMA,
            "uniqueItems": False,
        }
    },
}

EntryValidatorClass = validator_for(ENTRY_SCHEMA)
DBValidatorClass = validator_for(DB_SCHEMA)

entry_validator = EntryValidatorClass(ENTRY_SCHEMA)
db_validator = DBValidatorClass(DB_SCHEMA)
