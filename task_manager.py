import json
import os
from datetime import datetime

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1
        self.tasks_file = 'tasks.json'
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from JSON file if it exists."""
        if os.path.exists(self.tasks_file):
            try:
                with open(self.tasks_file, 'r') as f:
                    self.tasks = json.load(f)
                # Set next_id to max existing id + 1
                if self.tasks:
                    self.next_id = max(task['id'] for task in self.tasks) + 1
            except json.JSONDecodeError:
                print("Warning: tasks.json is corrupted. Starting with empty task list.")
                self.tasks = []
                self.next_id = 1

    def save_tasks(self):
        """Save tasks to JSON file."""
        with open(self.tasks_file, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, description, due_date):
        """Add a new task."""
        if not description.strip():
            print("Error: Task description cannot be empty.")
            return
        task = {
            'id': self.next_id,
            'description': description,
            'due_date': due_date,
            'completed': False
        }
        self.tasks.append(task)
        self.next_id += 1
        self.save_tasks()
        print(f"Task added: {description}")

    def mark_complete(self, task_id):
        """Mark a task as complete."""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                print(f"Task {task_id} marked as complete.")
                return
        print(f"Task {task_id} not found.")

    def view_tasks(self):
        """View all tasks."""
        if not self.tasks:
            print("No tasks found.")
            return
        for task in self.tasks:
            status = "Completed" if task['completed'] else "Pending"
            print(f"ID: {task['id']}, Description: {task['description']}, Due: {task['due_date']}, Status: {status}")

    def delete_task(self, task_id):
        """Delete a task."""
        original_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if task['id'] != task_id]
        if len(self.tasks) < original_count:
            self.save_tasks()
            print(f"Task {task_id} deleted.")
        else:
            print(f"Task {task_id} not found.")

    def run(self):
        """Main menu loop."""
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
                try:
                    datetime.strptime(due, '%Y-%m-%d')
                    self.add_task(desc, due)
                except ValueError:
                    print("Invalid date format. Use YYYY-MM-DD.")
            elif choice == '2':
                try:
                    tid = int(input("Enter task ID to mark complete: ").strip())
                    self.mark_complete(tid)
                except ValueError:
                    print("Invalid task ID.")
            elif choice == '3':
                self.view_tasks()
            elif choice == '4':
                try:
                    tid = int(input("Enter task ID to delete: ").strip())
                    self.delete_task(tid)
                except ValueError:
                    print("Invalid task ID.")
            elif choice == '5':
                print("Exiting.")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    tm = TaskManager()
    tm.run()