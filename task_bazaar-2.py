# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: TaskBazaar
class TaskBazaarModels:
    def __init__(self):
        self.tasks = []
        self.users = {}
    
    def validate_task_input(self, title: str, description: str, priority: int, bid: float) -> tuple[bool, list[str]]:
        errors = []
        if not title.strip():
            errors.append("Заголовок задачи не может быть пустым.")
        elif len(title) > 100:
            errors.append("Заголовок задачи не должен превышать 100 символов.")
        
        if not description.strip():
            errors.append("Описание задачи не может быть пустым.")
        
        priority_levels = [1, 2, 3]
        if priority not in priority_levels:
            errors.append(f"Приоритет должен быть одним из {priority_levels}.")
        
        if bid < 0.0 or not isinstance(bid, (int, float)):
            errors.append("Ставка должна быть положительным числом.")
        
        return len(errors) == 0, errors

    def create_task(self, title: str, description: str, priority: int, bidder_id: str, bid: float):
        is_valid, errors = self.validate_task_input(title, description, priority, bid)
        if not is_valid:
            print(f"Ошибка валидации задачи: {', '.join(errors)}")
            return None
        
        task_id = len(self.tasks) + 1
        new_task = {
            "id": task_id,
            "title": title.strip(),
            "description": description.strip(),
            "priority": priority,
            "bidder_id": bidder_id,
            "bid": bid,
            "status": "pending",
            "created_at": datetime.now().isoformat() if 'datetime' in globals() else None
        }
        
        self.tasks.append(new_task)
        return new_task

    def get_tasks_by_priority(self, priority: int):
        return [task for task in self.tasks if task["priority"] == priority]
