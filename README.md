# Python Task Manager

A simple command-line task management application built with Python. This project demonstrates core programming concepts including functions, data structures, file I/O, error handling, and user input validation.

## Features

- Add tasks with descriptions and due dates
- Mark tasks as complete
- View all tasks (pending and completed)
- Delete tasks
- Persistent storage using JSON file
- Input validation and error handling

## Setup

### Prerequisites

- Python 3.x installed on your system

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/akasom-creator/python-task-manager.git
   cd python-task-manager
   ```

2. Run the application:
   ```
   python task_manager.py
   ```

## Usage

The application provides a menu-driven interface:

1. **Add Task**: Enter a description and due date (YYYY-MM-DD format)
2. **Mark Task Complete**: Enter the task ID to mark as completed
3. **View Tasks**: Display all tasks with their status
4. **Delete Task**: Enter the task ID to delete
5. **Exit**: Save tasks and exit the application

### Example

```
Task Manager Menu:
1. Add Task
2. Mark Task Complete
3. View Tasks
4. Delete Task
5. Exit
Choose an option: 1
Enter task description: Buy groceries
Enter due date (YYYY-MM-DD): 2026-01-30
Task added: Buy groceries
```

## File Structure

- `task_manager.py`: Main application code
- `tasks.json`: JSON file for task persistence (created automatically)
- `README.md`: This documentation file

## Error Handling

- Validates date formats (YYYY-MM-DD)
- Prevents empty task descriptions
- Handles invalid task IDs gracefully
- Recovers from corrupted JSON files safely
