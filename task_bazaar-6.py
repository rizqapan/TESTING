# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: TaskBazaar
def filter_tasks(tasks, status=None, category=None, tags=None):
    filtered = tasks.copy()
    if status:
        filtered = [t for t in filtered if t.get('status') == status]
    if category:
        filtered = [t for t in filtered if t.get('category') == category]
    if tags:
        task_tags = lambda t: set(t.get('tags', [])).issuperset(set(tags))
        filtered = [t for t in filtered if task_tags(t)]
    return filtered
