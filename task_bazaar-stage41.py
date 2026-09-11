# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: TaskBazaar
def dry_run(operation, data, *, enabled=True):
    """Dry-run wrapper: returns the original data unchanged when enabled."""
    if enabled:
        return data
    return operation(data)
