# === Stage 43: Добавь пагинацию длинных списков ===
# Project: TaskBazaar
def paginate(tasks, page_size=20, page=1):
    """Compact pagination helper for task lists."""
    total_pages = max(1, (len(tasks) + page_size - 1) // page_size)
    page = max(1, min(page, total_pages))
    start = (page - 1) * page_size
    end = start + page_size
    return {
        "tasks": tasks[start:end],
        "page": page,
        "page_size": page_size,
        "total_pages": total_pages,
        "total": len(tasks),
    }
