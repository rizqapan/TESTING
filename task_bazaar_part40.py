# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: TaskBazaar
import argparse


def main():
    parser = argparse.ArgumentParser(description="TaskBazaar CLI")
    parser.add_argument("command", choices=["list", "create", "assign", "history"], help="Main operation")
    parser.add_argument("-t", "--task-id", help="Task ID")
    parser.add_argument("-u", "--user-id", help="User ID")
    parser.add_argument("-s", "--status", help="Status filter")
    parser.add_argument("-p", "--priority", help="Priority filter")
    args = parser.parse_args()
    if args.command == "list":
        print("Listing tasks...")
    elif args.command == "create":
        print("Creating task...")
    elif args.command == "assign":
        print("Assigning task...")
    elif args.command == "history":
        print("Task history...")


if __name__ == "__main__":
    main()
