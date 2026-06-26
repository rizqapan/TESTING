# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: TaskBazaar
class TaskSorter:
    def __init__(self, tasks):
        self.tasks = tasks

    def sort_by_date(self, reverse=True):
        return sorted(self.tasks, key=lambda t: t.get('created_at', ''), reverse=reverse)

    def sort_by_priority(self, priority_map=None):
        if not priority_map:
            priority_map = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
        return sorted(self.tasks, key=lambda t: priority_map.get(t.get('priority', 'low'), 99))

    def sort_by_name(self):
        return sorted(self.tasks, key=lambda t: t.get('title', ''))
