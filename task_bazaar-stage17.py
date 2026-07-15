# === Stage 17: Добавь группировку записей по категориям ===
# Project: TaskBazaar
def group_by_category(records):
    grouped = {}
    for r in records:
        cat = r.get("category") or "Uncategorized"
        if cat not in grouped:
            grouped[cat] = []
        grouped[cat].append(r)
    return grouped

for category, items in sorted(group_by_category(tasks).items()):
    print(f"\n[{category}] ({len(items)} tasks)")
    for i, task in enumerate(items, 1):
        status = "✓" if task.get("completed") else "○"
        print(f"  {i}. {status} {task['title']} — ${task.get('price', 0)} (priority: {task.get('priority', 'low')})")
