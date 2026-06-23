# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: TaskBazaar
def delete_task(task_id):
    if task_id not in tasks:
        print(f"Задача #{task_id} не найдена.")
        return False
    del tasks[task_id]
    if task_id in completed_tasks:
        del completed_tasks[task_id]
    if task_id in pending_tasks:
        del pending_tasks[task_id]
    print(f"Задача #{task_id} успешно удалена.")
    return True

def delete_user(user_id):
    if user_id not in users:
        print(f"Пользователь #{user_id} не найден.")
        return False
    del users[user_id]
    
    for task_id, task_data in list(tasks.items()):
        if task_data.get('executor') == user_id:
            tasks[task_id]['executor'] = None
    
    print(f"Пользователь #{user_id} успешно удален.")
    return True

def delete_bid(bid_id):
    bids_map = {b['bidder']: b for b in bids if 'bidder' in b and isinstance(b['bidder'], int)}
    
    if bid_id not in bids_map:
        print(f"Ставка #{bid_id} не найдена.")
        return False
    
    bidder = bids_map[bid_id]['bidder']
    task_id = bids_map[bid_id].get('task')
    
    del bids_map[bid_id]
    
    if task_id and bid_id in tasks.get(task_id, {}).get('bids', []):
        tasks[task_id]['bids'].remove(bid_id)
        
    print(f"Ставка #{bid_id} успешно удалена.")
    return True
