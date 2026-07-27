# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: TaskBazaar
def print_task_record(task):
    """Компактный вывод одной задачи."""
    status = task["status"]
    deadline_str = task.get("deadline", "нет")
    
    if isinstance(deadline_str, datetime):
        deadline_str = deadline_str.strftime("%d.%m %H:%M")
    
    history_summary = ""
    for h in task.get("history", [])[:3]:
        action = h.get("action", "")
        time_ago = h.get("time_ago", "")
        if action and time_ago:
            history_summary += f" {action} ({time_ago})"
    
    print(f"[{status.upper()}] #{task['id']} | "
          f"Автор: {task['author']} | "
          f"Статус: {status} | "
          f"Дедлайн: {deadline_str} | "
          f"История:{history_summary}")

if __name__ == "__main__":
    print_task_record(tasks[0])
