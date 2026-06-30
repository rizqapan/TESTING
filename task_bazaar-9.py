# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: TaskBazaar
import json, os, random
from datetime import datetime, timedelta

INITIAL_DATA = '''
{
  "tasks": [
    {"id": 101, "title": "Исправить баг в логике", "description": "Пользователь жалуется на зависание.", "status": "open", "priority": "high", "bid": 500.0},
    {"id": 102, "title": "Написать документацию", "description": "Оформить API для новых модулей.", "status": "in_progress", "priority": "medium", "bid": 300.0}
  ],
  "users": [
    {"id": 501, "name": "Алексей", "skills": ["python", "django"], "completed_tasks": []},
    {"id": 502, "name": "Мария", "skills": ["js", "react"], "completed_tasks": [{"task_id": 99}]}
  ],
  "history": [
    {"date": "2023-10-01", "event": "Система запущена"}
  ]
}'''

def load_initial_data():
    try:
        data = json.loads(INITIAL_DATA)
        if not isinstance(data, dict): raise ValueError("Некорректный формат JSON")
        
        # Валидация и нормализация дат в истории
        for entry in data.get("history", []):
            if "date" in entry:
                try: datetime.strptime(entry["date"], "%Y-%m-%d")
                except ValueError: del entry["date"]
            
        return data
    except json.JSONDecodeError as e:
        print(f"[ESCALATE] Ошибка парсинга JSON-строки: {e}")
        return {"tasks": [], "users": [], "history": []}

def seed_database(db):
    """Инициализация БД тестовыми данными из строки."""
    if not db.get("initialized"):
        data = load_initial_data()
        
        # Загрузка задач с генерацией уникальных ID, если они не заданы
        for task in data.get("tasks", []):
            if "id" not in task:
                task["id"] = random.randint(1000, 9999)
            
        # Загрузка пользователей
        for user in data.get("users", []):
            if "id" not in user:
                user["id"] = random.randint(2000, 9999)
        
        # Сохранение в структуру БД (имитация)
        db["tasks"].extend(data.get("tasks", []))
        db["users"].extend(data.get("users", []))
        db["history"].extend(data.get("history", []))
        
        db["initialized"] = True
        print(f"[INFO] Загружено {len(db['tasks'])} задач и {len(db['users'])} пользователей.")

# Пример вызова при старте приложения (раскомментируйте в main)
# if __name__ == "__main__":
