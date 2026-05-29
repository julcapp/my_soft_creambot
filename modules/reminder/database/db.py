import json
import os

DB_PATH = "database.json"


def load_db():
    if not os.path.exists(DB_PATH):
        return {}
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_db(data):
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def get_lessons():
    return load_db()


def get_lesson(lesson_id):
    db = load_db()
    return db.get(str(lesson_id))


def set_lesson(lesson_id, link):
    db = load_db()
    db[str(lesson_id)] = {"link": link}
    save_db(db)


def delete_lesson(lesson_id):
    db = load_db()
    db.pop(str(lesson_id), None)
    save_db(db)


def reset_db():
    save_db({})
