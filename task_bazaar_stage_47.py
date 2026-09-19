# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: TaskBazaar
def demo():
    print("=" * 60)
    print("  TaskBazaar Demo — главный сценарий использования")
    print("=" * 60)

    # --- 1. Регистрация исполнителя ---
    performer = Performer("Алексей")
    performer.set_skill("Python", 8)
    performer.set_skill("JavaScript", 6)
    performer.set_skill("SQL", 4)
    performer.set_hourly_rate(500)
    performer.set_location("Москва")
    performer.set_phone("+7-900-123-4567")
    performer.set_email("alex@example.com")
    performer.set_status("available")
    performer.set_description("Опытный Python-разработчик, люблю чистый код и тесты.")

    # --- 2. Регистрация заказчика ---
    client = Client("ООО 'СтартТех'")
    client.set_phone("+7-900-765-4321")
    client.set_email("orders@starttech.ru")
    client.set_address("г. Казань, ул. Ленина, 10")
    client.set_status("active")
    client.set_description("IT-стартап, разрабатывающий веб-приложения.")

    # --- 3. Создание задачи ---
    task = Task(
        title="Разработка REST API для мобильного приложения",
        description="Необходимо реализовать REST API с endpoints: "
                     "/users, /orders, /products. API должно поддерживать "
                     "pagination, фильтрацию и сортировку.",
        category="Backend",
        priority="high",
        budget=15000,
        duration_hours=80,
        deadline="2025-03-30",
        status="open",
        created_by=client,
        created_at=datetime(2025, 1, 15, 10, 0),
    )
    task.add_tag("REST")
    task.add_tag("API")
    task.add_tag("Python")

    # --- 4. Исполнитель присоединяется к задаче ---
    performer.offer_for_task(task)

    # --- 5. Заказчик просматривает предложения ---
    print("\n--- Просмотр предложений от исполнителей ---")
    for bid in task.get_bids():
        print(f"  Исполнитель: {bid.performer.name}")
        print(f"  Ставка: {bid.budget} руб.")
        print(f"  Сроки: {bid.duration_hours} часов")
        print(f"  Описание: {bid.description}")
        print()

    # --- 6. Заказчик принимает предложение ---
    task.accept_bid(bid=task.get_bids()[0])
    print("--- Задача принята! ---")

    # --- 7. Исполнитель выполняет задачу ---
    task.update_status("in_progress")
    performer.work_on_task(task)
    print("\n--- Исполнитель работает над задачей ---")
    task.update_status("completed")
    print("\n--- Задача завершена! ---")

    # --- 8. История выполнения ---
    print("\n--- История выполнения задачи ---")
    for log in task.get_history():
        print(f"  [{log.timestamp}] {log.action}")

    # --- 9. Статистика исполнителя ---
    print("\n--- Статистика исполнителя ---")
    print(f"  Имя: {performer.name}")
    print(f"  Навыки: {performer.get_skills_summary()}")
    print(f"  Профиль: {performer.get_profile_summary()}")
    completed_count = performer.get_completed_count()
    print(f"  Завершённых задач: {completed_count}")
    print(f"  Общая выручка: {performer.get_total_earnings()} руб.")

    # --- 10. Поиск задач ---
    print("\n--- Поиск задач ---")
    found_tasks = Task.search(tasks, query="Python")
    if found_tasks:
        for t in found_tasks:
            print(f"  Задача: {t.title}")
            print(f"  Категория: {t.category}, Приоритет: {t.priority}")
            print(f"  Бюджет: {t.budget} руб.")
            print()
    else:
        print("  Задачи не найдены.")

    print("\n" + "=" * 60)
    print("  Demo завершён. Спасибо за использование TaskBazaar!")
    print("=" * 60)
