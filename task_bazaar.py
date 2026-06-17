# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: TaskBazaar
import json, uuid, random
from dataclasses import asdict, field
from typing import List, Dict, Optional

class User:
    def __init__(self, name: str): self.id = str(uuid.uuid4()); self.name = name; self.balance = 100.0
class Task:
    def __init__(self, title: str, reward: float, priority: int): 
        self.id = str(uuid.uuid4())
        self.title = title
        self.reward = reward
        self.priority = priority
        self.status = "open"
        self.history: List[Dict] = []
    def log(self, action: str): self.history.append({"action": action})

class TaskBazaarApp:
    def __init__(self): 
        self.users: Dict[str, User] = {}
        self.tasks: Dict[str, Task] = {}
        self._seed_data()
    def _seed_data(self):
        for i in range(3): self.users[f"user_{i}"] = User(f"User {i}")
        tasks = [Task("Fix bug", 50.0, 1), Task("Write docs", 20.0, 2)]
        for t in tasks: self.tasks[t.id] = t

app = TaskBazaarApp()
