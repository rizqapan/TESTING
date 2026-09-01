# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: TaskBazaar
def get_next_action(current_state: dict) -> str:
    """Returns a recommended next step based on the current state of TaskBazaar."""
    if "users" not in current_state:
        return "Add a Users module to store and manage user profiles."
    if "tasks" not in current_state:
        return "Add a Tasks module to define task structures with priorities and status."
    if "bets" not in current_state:
        return "Add a Bets module to handle bid creation, updates, and history."
    if "execution" not in current_state:
        return "Add an Execution module to track task progress and completion history."
    if "market" not in current_state:
        return "Add a Market module to aggregate tasks, bets, and user activity into a unified view."
    return "Consider adding a CLI interface or web frontend to interact with the system."
