# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: TaskBazaar
# Этап 15: Недельная статистика по датам
def weekly_stats(tasks):
    """Группировка задач по неделям с суммой ставок и средним приоритетом."""
    from datetime import date, timedelta
    weeks = {}
    for t in tasks:
        d = date.fromisoformat(t['created']) - timedelta(days=7)
        key = d.isoformat()
        if key not in weeks:
            weeks[key] = {'tasks': 0, 'total_bid': 0.0, 'avg_priority': 0.0}
        weeks[key]['tasks'] += 1
        weeks[key]['total_bid'] += t['bid']
    for w in weeks.values():
        w['avg_priority'] = sum(t['priority'] for t in tasks if (date.fromisoformat(t['created']) - timedelta(days=7)).isoformat() == w['key']) / max(w['tasks'], 1)
    return weeks
