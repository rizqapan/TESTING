# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: TaskBazaar
from rich.console import Console, Table
from rich.text import Text

console = Console()


def print_task_table(tasks=None):
    """Выводит список задач в формате таблицы."""
    if tasks is None:
        from taskbazaar.models.task import Task
        tasks = list(Task.find_all())
    if not tasks:
        console.print("[bold yellow]Нет активных задач.[/bold yellow]")
        return

    table = Table(title=f"Задач: {len(tasks)}", show_header=True, header_style="bold cyan")
    table.add_column("ID", style="dim", width=4)
    table.add_column("Название", style="white")
    table.add_column("Статус", justify="center", style="green3")
    table.add_column("Бюджет (₽)", justify="right", style="gold1")

    for task in tasks:
        status_color = "red" if task.is_done else ("yellow" if task.is_pending else "green")
        row = [task.id, task.title, f"[{status_color}]{task.status}[/{status_color}]", task.budget]
        table.add_row(*row)

    console.print(table)
