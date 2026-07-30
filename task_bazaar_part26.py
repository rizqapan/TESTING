# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: TaskBazaar
def demo():
    print("=" * 50)
    print("TaskBazaar Demo")
    print("=" * 50)
    for task in tasks.values():
        if task["priority"] == "high":
            print(f"🔴 {task['title']} (High)")
        elif task["priority"] == "medium":
            print(f"🟡 {task['title']} (Medium)")
        else:
            print(f"🟢 {task['title']} (Low)")

demo()
