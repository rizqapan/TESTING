# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: TaskBazaar
def monthly_stats(tasks, executors):
    """Возвращает словарь: {'YYYY-MM': [количество задач, среднее время выполнения (сек), количество исполнителей]}.
       Время считается как разница между завершением и созданием задачи. Если задача не завершена — пропускается."""
    
    stats = {}
    
    for task in tasks:
        if not hasattr(task, 'created_at') or not hasattr(task, 'completed_at'):
            continue
        
        created_str = str(getattr(task, 'created_at', ''))
        completed_str = str(getattr(task, 'completed_at', ''))
        
        month_key = created_str[:7]  # "YYYY-MM"
        
        if stats.get(month_key) is None:
            stats[month_key] = {'count': 0, 'total_time': 0, 'executors': set()}
        
        stats[month_key]['count'] += 1
        
        try:
            created_dt = datetime.fromisoformat(created_str.replace(' ', 'T'))
            completed_dt = datetime.fromisoformat(completed_str.replace(' ', 'T'))
            total_time = (completed_dt - created_dt).total_seconds()
            stats[month_key]['total_time'] += total_time
            
            if hasattr(task, 'executor_id'):
                stats[month_key]['executors'].add(getattr(task, 'executor_id', ''))
        except Exception:
            pass
    
    result = {}
    
    for month_key in sorted(stats.keys()):
        data = stats[month_key]
        
        avg_time = data['total_time'] / data['count'] if data['count'] > 0 else 0
        
        result[month_key] = {
            'tasks_completed': data['count'],
            'avg_completion_time_seconds': round(avg_time, 2),
            'unique_executors_count': len(data['executors']) if isinstance(data['executors'], set) else 0
        }
    
    return result
