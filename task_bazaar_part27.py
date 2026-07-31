# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: TaskBazaar
def reset_demo_data():
    """Сбрасывает все данные в исходное демо-состояние."""
    global tasks, freelancers, bids, history, notifications
    tasks = [
        {"id": "T001", "title": "Написать README", "description": "Описание проекта", "status": "pending", "priority": 3, "budget": 500},
        {"id": "T002", "title": "Разработать API", "description": "RESTful API с валидацией", "status": "in_progress", "priority": 5, "budget": 1500},
        {"id": "T003", "title": "Тестирование UI", "description": "Написать тесты для интерфейса", "status": "pending", "priority": 2, "budget": 800},
    ]
    freelancers = [
        {"id": "F001", "name": "Алекс", "skills": ["python", "django"], "hourly_rate": 50, "rating": 4.9},
        {"id": "F002", "name": "Мария", "skills": ["java", "spring"], "hourly_rate": 60, "rating": 4.8},
    ]
    bids = [
        {"task_id": "T001", "freelancer_id": "F001", "amount": 500, "status": "accepted"},
        {"task_id": "T002", "freelancer_id": "F002", "amount": 1500, "status": "pending"},
    ]
    history = []
    notifications = []


def clear_all_data():
    """Полностью очищает все данные в системе."""
    global tasks, freelancers, bids, history, notifications
    tasks = []
    freelancers = []
    bids = []
    history = []
    notifications = []
