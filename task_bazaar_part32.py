# === Stage 32: Добавь журнал действий пользователя ===
# Project: TaskBazaar
from datetime import datetime

class ActionLog:
    def __init__(self):
        self.entries = []
    
    def log(self, action, user, details=""):
        self.entries.append({
            'timestamp': datetime.now().isoformat(),
            'action': action,
            'user': user,
            'details': details
        })
    
    def get_history(self, user=None):
        if user:
            return [e for e in self.entries if e['user'] == user]
        return self.entries
