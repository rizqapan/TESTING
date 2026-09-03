# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: TaskBazaar
def check_and_repair_integrity(data):
    """Проверяет и 'ремонтирует' простые проблемы в данных маркетплейса задач.
    Returns: dict with keys: 'ok' (bool), 'issues' (list), 'repairs' (list)."""
    issues = []
    repairs = []
    
    # 1. Проверка уникальности задач по ID
    task_ids = [t['id'] for t in data.get('tasks', [])]
    if len(task_ids) != len(set(task_ids)):
        issues.append("Duplicate task IDs detected")
        # Ремонт: перезаписываем ID на порядковые числа
        repaired_tasks = {}
        for i, t in enumerate(data['tasks']):
            repaired_tasks[i] = {**t, 'id': i}
        repairs.append(f"Fixed {len(task_ids) - len(set(task_ids))} duplicate task IDs")
        data['tasks'] = list(repaired_tasks.values())
    
    # 2. Проверка корректности статусов задач
    valid_statuses = {'pending', 'in_progress', 'completed', 'cancelled'}
    for i, t in enumerate(data['tasks']):
        if t.get('status') not in valid_statuses:
            issues.append(f"Task {i} has invalid status: {t.get('status')}")
            t['status'] = 'pending'
            repairs.append(f"Reset task {i} status to 'pending'")
    
    # 3. Проверка ставок: сумма ставок >= 0
    for i, t in enumerate(data['tasks']):
        if t.get('bets', 0) < 0:
            issues.append(f"Task {i} has negative total bets")
            t['bets'] = 0
            repairs.append(f"Clamped task {i} bets to 0")
    
    # 4. Проверка исполнителей: наличие в списке
    workers = {w['name']: w for w in data.get('workers', [])}
    for i, t in enumerate(data['tasks']):
        if t.get('assigned_to') and t['assigned_to'] not in workers:
            issues.append(f"Task {i} assigned to unknown worker: {t['assigned_to']}")
            # Ремонт: назначаем на первого доступного рабочего
            first_worker = list(workers.values())[0]['name'] if workers else None
            if first_worker:
                t['assigned_to'] = first_worker
                repairs.append(f"Reassigned task {i} to worker '{first_worker}'")
    
    return {'ok': len(issues) == 0, 'issues': issues, 'repairs': repairs}
