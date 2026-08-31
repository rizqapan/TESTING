# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: TaskBazaar
TEMPLATE_REGISTRY = {}

def register_template(name, factory):
    TEMPLATE_REGISTRY[name] = factory

def create_task_from_template(template_name, **overrides):
    factory = TEMPLATE_REGISTRY.get(template_name)
    if not factory:
        raise KeyError(f"Template {template_name!r} not registered")
    return factory(**overrides)

register_template(
    "quick_task",
    lambda title="New Task", description="No description", priority=3,
    budget=100, deadline_days=7, category="general", **kw: {
        "title": title, "description": description, "priority": priority,
        "budget": budget, "deadline_days": deadline_days,
        "category": category, **kw
    },
)
