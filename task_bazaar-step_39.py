# === Stage 39: Добавь документационную строку с описанием сценариев использования ===
# Project: TaskBazaar
def run_scenarios():
    """
    Продемонстрирует основные сценарии использования TaskBazaar:
    1. Создание задачи и назначение исполнителя.
    2. Поднятие ставки на задачу.
    3. Выполнение задачи и начисление вознаграждения.
    4. Просмотр истории выполнения задач.
    5. Управление приоритетами задач.
    """
    bazaar = TaskBazaar()

    # Сценарий 1: Создание задачи
    task = Task(
        title="Написать тесты для API",
        description="Разработать unit-тесты для основных эндпоинтов API.",
        priority=Priority.HIGH,
        budget=500,
        deadline="2024-12-31"
    )
    bazaar.add_task(task)

    # Сценарий 2: Регистрация исполнителя и выполнение
    worker = Worker(name="PythonPro", skills=["python", "testing"], rate=25)
    bazaar.add_worker(worker)

    # Сценарий 3: Назначение задачи исполнителю
    task.assign_to(worker)
    print(f"Задача '{task.title}' назначена исполнителю {worker.name}.")

    # Сценарий 4: Поднятие ставки
    task.raise_bid(200, worker)
    print(f"Исполнитель {worker.name} поднял ставку до {task.current_bid} руб.")

    # Сценарий 5: Выполнение задачи
    task.complete()
    print(f"Задача '{task.title}' выполнена. Исполнитель получил {task.budget} руб.")

    # Сценарий 6: Просмотр истории
    history = bazaar.get_history()
    print(f"\nИстория выполнения задач:")
    for entry in history:
        print(f"  - {entry}")

    # Сценарий 7: Управление приоритетами
    task2 = Task(title="Оптимизация БД", description="Ускорить запросы к базе данных.", priority=Priority.MEDIUM)
    bazaar.add_task(task2)
    task2.change_priority(Priority.URGENT)
    print(f"Задача '{task2.title}' изменена на приоритет {task2.priority}.")

    # Сценарий 8: Просмотр задач по приоритету
    urgent_tasks = bazaar.get_tasks_by_priority(Priority.URGENT)
    print(f"\nЗадачи с приоритетом {Priority.URGENT.name}:")
    for t in urgent_tasks:
        print(f"  - {t.title}")

    print("\nВсе сценарии использования TaskBazaar успешно выполнены.")
