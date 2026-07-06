# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: TaskBazaar
def search_tasks(query, fields=None):
    """Поиск задач по нескольким полям без учёта регистра."""
    if query is None:
        return tasks
    if fields is None:
        fields = ['title', 'description', 'category']
    lower_query = query.lower()
    results = []
    for task in tasks:
        for field in fields:
            value = getattr(task, field, '') or ''
            if lower_query in str(value).lower():
                results.append(task)
                break
    return results
