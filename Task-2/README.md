# To-Do List

 # Overview
This is a simple command-line application to manage tasks. It allows you to add, remove, and display tasks, and stores tasks persistently in a file.

# Features
Add a new task
Remove a task
Display all tasks
Store tasks in a text file for persistence
User-friendly command-line interface
# Project Setup
Clone the repository:

Clone the project to your local machine:
bash
Copy code
git clone https://github.com/your-repo/todo_list.git
Set up a virtual environment:

Create a virtual environment for the project:
bash
Copy code
cd todo_list
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies (if any):

If there are any dependencies, install them using:
bash
Copy code
pip install -r requirements.txt
# Usage
Command-line Interface (CLI)
Run the To-Do List application:

After setting up, you can run the application using:
bash
Copy code
python todo_list.py
Application Functionality:

The application will present a menu with the following options:
Add a task
Remove a task
Display all tasks
Exit
Example usage:

When you run the application, it will prompt you with options. Here's how the user can interact with the program:

Add a task:

Select option 1.
Enter the task description.
Remove a task:

Select option 2.
Enter the task ID to remove the specific task.
Display all tasks:

Select option 3 to see the list of all tasks.
Exit the application:

Select option 4 to exit the program.
