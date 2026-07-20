# === Stage 20: Добавь восстановление записей из архива ===
# Project: TaskBazaar
def restore_from_archive():
    import json, os
    archive = "task_bazaar_archive.json"
    if not os.path.exists(archive):
        print("Архив не найден.")
        return
    with open(archive, 'r', encoding='utf-8') as f:
        archived = json.load(f)
    restored = []
    for task in archived:
        if "id" not in task and "task_id" in task:
            task["id"] = task.pop("task_id")
        restored.append(task)
    print(f"Восстановлено {len(restored)} записей из архива.")
    return restored
