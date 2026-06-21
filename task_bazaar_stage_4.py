# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: TaskBazaar
def edit_task(task_id, updates):
    if task_id not in tasks:
        raise ValueError(f"Task {task_id} not found")
    for key, value in updates.items():
        if key == 'status' and value not in ['pending', 'in_progress', 'completed']:
            raise ValueError("Invalid status")
        if key == 'priority' and value not in [1, 2, 3]:
            raise ValueError("Priority must be 1-3")
    tasks[task_id].update(updates)
