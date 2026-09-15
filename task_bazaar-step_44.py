# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: TaskBazaar
import shutil, os, datetime

def backup_data_file(data_file_path, backup_dir=None):
    """Создаёт резервную копию файла данных в archive/ с именем по дате."""
    if backup_dir is None:
        backup_dir = os.path.join(os.path.dirname(data_file_path), "archive")
    os.makedirs(backup_dir, exist_ok=True)
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"{os.path.basename(data_file_path)}.{ts}.bak")
    shutil.copy2(data_file_path, backup_path)
    return backup_path
