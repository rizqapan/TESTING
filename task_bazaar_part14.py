# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: TaskBazaar
def generate_bazaar_summary():
    """Генерирует краткую сводку по текущим данным маркетплейса задач."""
    import json, datetime
    summary = {"timestamp": datetime.datetime.now().isoformat(),
               "tasks_count": len(tasks),
               "total_value": sum(t['price'] for t in tasks if 'price' in t),
               "active_tasks": [t for t in tasks if t.get('status') == 'open'],
               "completed_tasks": [t for t in tasks if t.get('status') == 'done']}
    return json.dumps(summary, ensure_ascii=False)
