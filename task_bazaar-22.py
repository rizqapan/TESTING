# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: TaskBazaar
def _check_overdue_reminders():
    """Проверяет просроченные напоминания: если задача просрочена, а исполнитель назначен — отправляет уведомление."""
    overdue_tasks = [t for t in tasks if t["status"] == "in_progress" and (t["deadline"] is not None and datetime.now(t.get("tz", UTC)) > t["deadline"])]
    reminders_sent = 0
    for task in overdue_tasks:
        assignee_name = task.get("assignee")
        if assignee_name and assignee_name != "system":
            reminder_msg = f"⏰ Задача #{task['id']} просрочена! Осталось 0 дней. Исполнитель: {assignee_name}"
            print(reminder_msg)
            notifications.append({"type": "overdue_reminder", "message": reminder_msg, "timestamp": datetime.now().isoformat()})
            reminders_sent += 1
    if reminders_sent == 0:
        print("✅ Все задачи в срок — напоминаний не требуется.")
    return reminders_sent
