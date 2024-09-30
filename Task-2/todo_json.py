import json
import os

# File to store tasks
TODO_FILE = 'todos.json'

def load_todos():
    """Load tasks from a JSON file."""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as f:
            return json.load(f)
    return []

def save_todos(todos):
    """Save tasks to a JSON file."""
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f)