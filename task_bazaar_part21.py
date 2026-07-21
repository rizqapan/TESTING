# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: TaskBazaar
import datetime
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Reminder:
    task_id: int
    deadline: datetime.date
    message: str = ""
    notified: bool = False
    created_at: datetime.datetime = field(default_factory=datetime.datetime.now)

    def check_and_notify(self):
        if self.deadline <= datetime.date.today() and not self.notified:
            print(f"[Reminder] {self.message} — задача #{self.task_id} подошла к дедлайну")
            self.notified = True

    @classmethod
    def create(cls, task_id, deadline_str, message=""):
        try:
            deadline = datetime.date.fromisoformat(deadline_str)
        except ValueError as e:
            raise ValueError(f"Неверный формат даты: {deadline_str}") from e
        return cls(task_id=task_id, deadline=deadline, message=message)


class ReminderManager:
    def __init__(self):
        self._reminders = []

    @property
    def reminders(self):
        return list(self._reminders)

    def add_reminder(self, task_id, deadline_str, message=""):
        r = Reminder.create(task_id=task_id, deadline_str=deadline_str, message=message)
        self._reminders.append(r)
        print(f"[Reminder] Добавлено напоминание для задачи #{task_id}: {r.deadline.isoformat()}")

    def check_all(self):
        for r in self._reminders:
            if not r.notified:
                r.check_and_notify()


# Интеграция с TaskBazaar (пример использования)
if __name__ == "__main__":
    mgr = ReminderManager()
    mgr.add_reminder(1, "2025-12-31", "Завершить проект")
    mgr.check_all()
