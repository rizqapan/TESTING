# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: TaskBazaar
import json, os

DATA_FILE = "data.json"

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"tasks": [], "users": []}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {"tasks": [], "users": []}

def get_data():
    data = load_data()
    if not isinstance(data.get("tasks"), list):
        data["tasks"] = []
    if not isinstance(data.get("users"), list):
        data["users"] = []
    save_data(data)
    return data
