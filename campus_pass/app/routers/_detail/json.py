import json
from pathlib import Path
from threading import Lock


BASE_DIRECTORY = Path(__file__).resolve().parents[2]
DATABASE_FILE_DIRECTORY = BASE_DIRECTORY / "data" / "db.json"
database_lock = Lock()


def read_json():
    with DATABASE_FILE_DIRECTORY.open(encoding="utf-8") as file:
        return json.load(file)


def write_json(data):
    with DATABASE_FILE_DIRECTORY.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
