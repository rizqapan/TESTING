# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: TaskBazaar
import json

def load_profiles(path='profiles.json'):
    if not os.path.exists(path):
        return {}
    with open(path) as f:
        return json.load(f)

def save_profiles(profiles, path='profiles.json'):
    with open(path, 'w') as f:
        json.dump(profiles, f, indent=2)

def register_user(username, email, role='user'):
    profiles = load_profiles()
    if username in profiles:
        print(f"Username '{username}' already exists.")
        return
    profiles[username] = {'username': username, 'email': email, 'role': role}
    save_profiles(profiles)
    print(f"User '{username}' registered successfully.")

def login_user(username, password):
    profiles = load_profiles()
    user = profiles.get(username)
    if not user:
        print("User not found.")
        return None
    user['password'] = password
    save_profiles(profiles)
    return user

def get_user(username):
    return load_profiles().get(username)
