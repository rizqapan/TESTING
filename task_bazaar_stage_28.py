# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: TaskBazaar
def print_project_metrics(tasks, freelancers):
    total = len(tasks)
    completed = sum(1 for t in tasks if t['status'] == 'completed')
    active = sum(1 for t in tasks if t['status'] == 'active')
    avg_payout = sum(t.get('payout', 0) for t in tasks) / max(total, 1)
    top = sorted(freelancers, key=lambda f: len([t for t in tasks if t.get('freelancer_id') == f['id']]), reverse=True)
    print(f"Всего задач: {total}, Активных: {active}, Завершённых: {completed}")
    print(f"Средняя выплата: {avg_payout:.2f} юаней")
    if top:
        print(f"Топ-исполнитель: {top[0]['name']} ({len([t for t in tasks if t.get('freelancer_id') == top[0]['id']])} задач)")
