# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: TaskBazaar
def archive_old_tasks(db, cutoff_days=365):
    """Archive tasks that are completed or older than cutoff_days."""
    import datetime
    cutoff = datetime.datetime.now() - datetime.timedelta(days=cutoff_days)
    archived_count = 0
    for task_id in db:
        if not isinstance(task_id, int):
            continue
        task = db[task_id]
        status = task.get("status", "pending")
        if status != "completed":
            last_upd = datetime.datetime.fromtimestamp(task["updated"] or 0)
            if last_upd < cutoff:
                task["status"] = "archived"
                task["archived_at"] = datetime.datetime.now().isoformat()
                archived_count += 1
    return archived_count
