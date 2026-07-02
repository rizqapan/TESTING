# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: TaskBazaar
def export_state():
    import json
    from datetime import datetime
    state = {
        "timestamp": datetime.utcnow().isoformat(),
        "tasks": tasks,
        "users": users,
        "stats": stats
    }
    return json.dumps(state, ensure_ascii=False, indent=2)
