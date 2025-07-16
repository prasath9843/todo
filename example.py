import json
import os

FILE_NAME = "todo.json"

# Initialize the JSON file if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        json.dump([], f)

def load_tasks():
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def create_task():
    task = input("Enter the new task: ")
    tasks = load_tasks()
    tasks.append({"id": len(tasks) + 1, "task": task, "done": False})
    save_tasks(tasks)
    print("✅ Task added.")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
    else:
        for t in tasks:
            status = "✔️" if t["done"] else "❌"
            print(f'{t["id"]}. {t["task"]} [{status}]')

def update_task():
    list_tasks()
    tid = int(input("Enter task ID to update: "))
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == tid:
            print("1. Mark as Done\n2. Edit Task Text")
            choice = input("Choose an option: ")
            if choice == "1":
                task["done"] = True
            elif choice == "2":
                task["task"] = input("Enter new task text: ")
            save_tasks(tasks)
            print("✅ Task updated.")
            return
    print("❌ Task not found.")

def delete_task():
    list_tasks()
    tid = int(input("Enter task ID to delete: "))
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != tid]
    # Reassign IDs
    for i, t in enumerate(tasks):
        t["id"] = i + 1
    save_tasks(tasks)
    print("🗑️ Task deleted.")

def main():
    while True:
        print("\n📋 TO-DO APP")
        print("1. Create Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            create_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid choice")

if __name__ == "__main__":
    main()
