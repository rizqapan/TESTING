# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: TaskBazaar
def migrate_structure(current_version, target_version):
    """Миграция структуры данных при изменении версий.
    Версия структуры хранится в _VERSION. При обновлении проверяется
    совместимость и применяется соответствующий блок миграции."""
    if current_version < target_version:
        if target_version == 2:
            _VERSION = target_version
            # Добавляем поле _history в каждую задачу:
            for task in tasks:
                if not hasattr(task, '_history'):
                    task._history = []
        elif target_version == 3:
            _VERSION = target_version
            # Добавляем поле _priority в каждую задачу:
            for task in tasks:
                if not hasattr(task, '_priority'):
                    task._priority = 'medium'
        else:
            raise ValueError(f"Неизвестная миграция для версии {target_version}")
    else:
        _VERSION = target_version
