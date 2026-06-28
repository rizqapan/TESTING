# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: TaskBazaar
def main_menu():
    print("\n=== TaskBazaar: Маркет задач ===")
    print("1. Список всех задач")
    print("2. Создать новую задачу")
    print("3. Найти исполнителя по навыкам")
    print("4. История выполненных задач")
    print("5. Выход из программы")
    choice = input("Выберите действие (1-5): ")
    
    if choice == "1":
        tasks = get_tasks()  # Предположим, что эта функция уже существует в проекте
        for t in tasks:
            print(f"ID: {t['id']}, Задача: {t['title']}, Статус: {t['status']}")
    elif choice == "2":
        title = input("Название задачи: ")
        priority = int(input("Приоритет (1-3): ")) or 2
        create_task(title, priority)  # Предположим, что эта функция уже существует в проекте
        print("Задача создана!")
    elif choice == "3":
        skill = input("Навык исполнителя: ")
        executors = get_executors_by_skill(skill)  # Предположим, что эта функция уже существует в проекте
        for e in executors:
            print(f"Имя: {e['name']}, Навыки: {', '.join(e['skills'])}")
    elif choice == "4":
        history = get_task_history()  # Предположим, что эта функция уже существует в проекте
        for h in history:
            print(f"Задача: {h['task_title']}, Исполнитель: {h['executor_name']}, Статус: {h['status']}")
    elif choice == "5":
        print("Выход из программы.")
        return 0
    else:
        print("Неверный выбор. Попробуйте снова.")
    input("\nНажмите Enter для возврата в меню...")
    main_menu()
