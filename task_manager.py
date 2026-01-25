import json
import os
from datetime import datetime

# Global list to hold tasks
tasks = []

# File to save tasks
TASKS_FILE = 'tasks.json'

def load_tasks():
    """Load tasks from JSON file if it exists."""
    global tasks
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            tasks = json.load(f)

def save_tasks():
    """Save tasks to JSON file."""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(description, due_date):
    """Add a new task."""
    task_id = len(tasks) + 1
    task = {
        'id': task_id,
        'description': description,
        'due_date': due_date,
        'completed': False
    }
    tasks.append(task)
    print(f"Task added: {description}")

def mark_complete(task_id):
    """Mark a task as complete."""
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            print(f"Task {task_id} marked as complete.")
            return
    print(f"Task {task_id} not found.")

def view_tasks():
    """View all tasks."""
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        status = "Completed" if task['completed'] else "Pending"
        print(f"ID: {task['id']}, Description: {task['description']}, Due: {task['due_date']}, Status: {status}")

def delete_task(task_id):
    """Delete a task."""
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    print(f"Task {task_id} deleted.")

def main():
    load_tasks()
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Mark Task Complete")
        print("3. View Tasks")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            desc = input("Enter task description: ").strip()
            due = input("Enter due date (YYYY-MM-DD): ").strip()
            # Basic validation
            try:
                datetime.strptime(due, '%Y-%m-%d')
                add_task(desc, due)
            except ValueError:
                print("Invalid date format. Use YYYY-MM-DD.")
        elif choice == '2':
            try:
                tid = int(input("Enter task ID to mark complete: ").strip())
                mark_complete(tid)
            except ValueError:
                print("Invalid task ID.")
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            try:
                tid = int(input("Enter task ID to delete: ").strip())
                delete_task(tid)
            except ValueError:
                print("Invalid task ID.")
        elif choice == '5':
            save_tasks()
            print("Tasks saved. Exiting.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()