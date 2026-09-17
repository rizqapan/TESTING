# === Stage 45: Добавь восстановление из резервной копии ===
# Project: TaskBazaar
import json, os

BACKUP_DIR = "backups"
def save_backup():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    with open("taskbazaar.json", "r") as f:
        data = json.load(f)
    with open(f"{BACKUP_DIR}/latest.json", "w") as f:
        json.dump(data, f, indent=2)
    print("Backup saved.")

def restore_backup(version="latest"):
    path = f"{BACKUP_DIR}/{version}.json"
    if not os.path.exists(path):
        print(f"Backup {path} not found.")
        return False
    with open(path, "r") as f:
        data = json.load(f)
    with open("taskbazaar.json", "w") as f:
        json.dump(data, f, indent=2)
    print(f"Restored from {path}.")
    return True
