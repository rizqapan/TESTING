# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: TaskBazaar
class TaskBazaarState:
    def __init__(self):
        self.tasks = []
        self.users = {}
        self.history = []

    def add_task(self, title, description, priority, stake, executor_id=None):
        task_id = len(self.tasks) + 1
        task = {
            "id": task_id,
            "title": title,
            "description": description,
            "priority": priority,
            "stake": float(stake),
            "executor_id": executor_id,
            "status": "open" if not executor_id else "in_progress",
            "created_at": time.time()
        }
        self.tasks.append(task)
        return task

    def assign_task(self, task_id, executor_id):
        for task in self.tasks:
            if task["id"] == task_id and task["status"] == "open":
                task["executor_id"] = executor_id
                task["status"] = "in_progress"
                return True
        return False

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id and task["status"] == "in_progress":
                task["status"] = "completed"
                executor = self.users.get(task["executor_id"], {})
                history_entry = {
                    "task_id": task_id,
                    "action": "completed",
                    "timestamp": time.time(),
                    "stake_earned": task["stake"] if executor else 0
                }
                self.history.append(history_entry)
                return True
        return False

    def add_user(self, user_id, name):
        if user_id not in self.users:
            self.users[user_id] = {"name": name, "completed_tasks": 0}
            return True
        return False
