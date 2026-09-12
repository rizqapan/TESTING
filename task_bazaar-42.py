# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: TaskBazaar
def print_colored(text, color):
    codes = {
        'red': '\033[91m', 'green': '\033[92m', 'yellow': '\033[93m',
        'blue': '\033[94m', 'magenta': '\033[95m', 'cyan': '\033[96m',
        'white': '\033[97m', 'reset': '\033[0m', 'bold': '\033[1m',
    }
    if color not in codes:
        color = 'white'
    return codes.get(color, '') + text + codes['reset']

class BazaarColors:
    RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, BOLD = 'red','green','yellow','blue','magenta','cyan','white','bold'

    @staticmethod
    def colorize(text, color):
        return print_colored(text, color)

    @staticmethod
    def banner(title):
        return BazaarColors.colorize(f'\n═══ {title} ═══', BOLD)

    @staticmethod
    def success(msg):
        return BazaarColors.colorize(f'  ✓ {msg}', GREEN)

    @staticmethod
    def warning(msg):
        return BazaarColors.colorize(f'  ⚠ {msg}', YELLOW)

    @staticmethod
    def info(msg):
        return BazaarColors.colorize(f'  ℹ {msg}', CYAN)

    @staticmethod
    def error(msg):
        return BazaarColors.colorize(f'  ✗ {msg}', RED)

    @staticmethod
    def task_header(task):
        name = task.get('title', 'Unknown')
        prio = task.get('priority', 'medium')
        prio_map = {'low': BLUE, 'medium': CYAN, 'high': RED, 'urgent': RED}
        return BazaarColors.colorize(f'  ┌─ {name} ─{prio_map.get(prio, BLUE)}', prio_map.get(prio, BLUE))

    @staticmethod
    def task_footer(task):
        return BazaarColors.colorize(f'  └────────────────────────────────────────', CYAN)

    @staticmethod
    def history_entry(entry):
        status = entry.get('status', 'pending')
        status_map = {'pending': CYAN, 'accepted': GREEN, 'rejected': RED, 'done': GREEN}
        return BazaarColors.colorize(f'  ─→ {entry.get("task", "?")} [{status_map.get(status, CYAN)}]', status_map.get(status, CYAN))

def print_colored_text(text, color):
    if color == 'off':
        return text
    return print_colored(text, color)

def colored_output(text, color='white'):
    return print_colored_text(text, color)
