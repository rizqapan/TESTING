# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: TaskBazaar
def _validate_date(date_str: str) -> tuple[datetime.date, str]:
    """Парсит дату и возвращает (parsed_date, error_message). Если ошибка — msg != ''.
    
    Примеры:
        "2024-01-15" → (date(2024, 1, 15), '')
        "abc" → (None, 'Некорректная дата')
        '' → (None, 'Пустая строка не является датой')
    """
    if not date_str or not isinstance(date_str, str):
        return None, 'Пустая строка не является датой'
    
    formats = ['%Y-%m-%d', '%d.%m.%y', '%Y/%m/%d']
    for fmt in formats:
        try:
            parsed = datetime.strptime(date_str.strip(), fmt)
            return parsed, ''
        except ValueError:
            continue
    
    return None, 'Некорректная дата'


def parse_date_safe(date_input: str) -> tuple[datetime.date | None, str]:
    """Глобальная функция для безопасного парсинга дат в TaskBazaar.
    
    Принимает строку с датой и возвращает:
        - (parsed_date, '') если дата корректна;
        - (None, error_msg) если ошибка.
    
    Примеры использования:
        date_str = "2024-01-15"
        parsed_date, err = parse_date_safe(date_str)
        if err:
            print(f'Ошибка: {err}')
        else:
            print(f'Дата: {parsed_date}')
    """
    return _validate_date(date_input)


# Пример использования в TaskBazaar (можно добавить в конец файла):
if __name__ == '__main__':
    test_cases = [
        "2024-01-15",
        "abc",
        "",
        None,
        123,
        "2024/01/15",
        "15.01.24",
    ]
    
    print('Тестирование функции parse_date_safe:')
    for case in test_cases:
        result = parse_date_safe(case)
        if isinstance(result, tuple):
            parsed_date, error_msg = result
            status = 'OK' if error_msg == '' else f'ERROR: {error_msg}'
            print(f'  Ввод: {case!r:>15} → {status}')
        else:
            print(f'  Ввод: {case!r:>15} → Ошибка: {result}')
