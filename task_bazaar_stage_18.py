# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: TaskBazaar
def add_tag(task, tag):
    if not isinstance(tag, str) or len(tag.strip()) == 0:
        raise ValueError("Tag must be a non-empty string")
    tags = task.get('tags', [])
    if tag in tags:
        return task
    tags.append(tag)
    task['tags'] = tags
    return task

def remove_tag(task, tag):
    tags = task.get('tags', [])
    if tag not in tags:
        raise ValueError(f"Tag '{tag}' not found on task")
    new_tags = [t for t in tags if t != tag]
    task['tags'] = new_tags
    return task
