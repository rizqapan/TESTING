# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: TaskBazaar
CONFIG = {
    "app_name": "TaskBazaar",
    "version": "0.3.29",
    "max_tasks_per_user": 5,
    "default_priority_levels": ["low", "medium", "high", "critical"],
    "currency_symbol": "$",
    "min_bet_amount": 1,
    "max_bet_amount": 10000,
    "bet_step": 5,
    "history_retention_days": 90,
    "log_level": "INFO",
}

def get_config(key=None):
    if key is None:
        return CONFIG
    return CONFIG.get(key)
