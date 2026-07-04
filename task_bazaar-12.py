# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: TaskBazaar
import json, os, sys
from pathlib import Path

def load_tasks_from_file(file_path: str) -> list[dict]:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, list):
            print("Ошибка: JSON файл должен содержать массив задач.")
            return []
        valid_tasks = [task for task in data if all(k in task for k in ['id', 'title', 'status'])]
        print(f"Загружено {len(valid_tasks)} валидных задач из '{file_path}'.")
        return valid_tasks
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON в файле '{file_path}': {e}")
        sys.exit(1)

if __name__ == "__main__":
    data_file = Path(__file__).parent / "tasks.json"
    if data_file.exists():
        tasks = load_tasks_from_file(str(data_file))
        for t in tasks:
            print(f"- {t['title']} [{t.get('status', 'unknown')}]")
    else:
        print("Файл задач не найден. Запуск без загрузки.")
