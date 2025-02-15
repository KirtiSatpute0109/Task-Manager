import sys
import json
from datetime import datetime
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

tasks = []

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            global tasks
            tasks = json.load(file)
    except FileNotFoundError:
        print(Fore.YELLOW + "No saved tasks found, starting fresh.")

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def add_task(task, due_date=None, priority=None, category=None):
    task_details = {"task": task, "completed": False, "due_date": due_date, "priority": priority, "category": category}
    tasks.append(task_details)
    print(Fore.GREEN + f'Added task: "{task}"')

def delete_task(task_index):
    try:
        removed_task = tasks.pop(task_index)
        print(Fore.RED + f'Deleted task: "{removed_task["task"]}"')
    except IndexError:
        print(Fore.RED + "Invalid task number")

def view_tasks():
    if not tasks:
        print(Fore.YELLOW + "No tasks available")
    else:
        print(Fore.CYAN + f"{'Task #':<6} {'Task Name':<30} {'Status':<15} {'Due Date':<15} {'Priority':<10} {'Category'}")
        print("-" * 90)
        for i, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Pending"
            due_date = task["due_date"] if task["due_date"] else "No due date"
            priority = task["priority"] if task["priority"] else "No priority"
            category = task["category"] if task["category"] else "No category"
            print(f"{i + 1:<6} {task['task']:<30} {status:<15} {due_date:<15} {priority:<10} {category}")
        print("-" * 90)

def mark_task_completed(task_index):
    try:
        tasks[task_index]["completed"] = True
        print(Fore.GREEN + f'Marked task as completed: "{tasks[task_index]["task"]}"')
    except IndexError:
        print(Fore.RED + "Invalid task number")

def search_tasks(keyword):
    results = [task for task in tasks if keyword.lower() in task["task"].lower()]
    if not results:
        print(Fore.YELLOW + "No matching tasks found")
    else:
        print(Fore.CYAN + f"{'Task #':<6} {'Task Name':<30} {'Status':<15} {'Due Date':<15} {'Priority':<10} {'Category'}")
        print("-" * 90)
        for i, task in enumerate(results):
            status = "Completed" if task["completed"] else "Pending"
            due_date = task["due_date"] if task["due_date"] else "No due date"
            priority = task["priority"] if task["priority"] else "No priority"
            category = task["category"] if task["category"] else "No category"
            print(f"{i + 1:<6} {task['task']:<30} {status:<15} {due_date:<15} {priority:<10} {category}")
        print("-" * 90)

def show_help():
    print(Fore.BLUE + """
    Available commands:
    -----------------------------------------------
    - add <task> <due_date (YYYY-MM-DD)> <priority> <category>
      : Add a new task with optional due date, priority, and category
    - delete <task_number>
      : Delete a task by its number
    - view
      : View all tasks with details
    - complete <task_number>
      : Mark a task as completed
    - search <keyword>
      : Search for tasks by keyword
    - help
      : Show this help message
    - exit
      : Exit the application
    """)

def main():
    print(Fore.GREEN + Style.BRIGHT + "Task Manager Application")
    load_tasks()
    show_help()
    
    while True:
        command = input(Fore.CYAN + "Enter command: ").strip().split()
        
        if not command:
            continue
        
        if command[0] == "add":
            if len(command) < 2:
                print(Fore.RED + "Error: You must specify a task to add.")
                continue
            
            task = " ".join(command[1:])
            due_date = input(Fore.MAGENTA + "Enter due date (YYYY-MM-DD) or press enter to skip: ").strip()
            priority = input(Fore.MAGENTA + "Enter priority (High/Medium/Low) or press enter to skip: ").strip()
            category = input(Fore.MAGENTA + "Enter category or press enter to skip: ").strip()
            add_task(task, due_date if due_date else None, priority if priority else None, category if category else None)
        
        elif command[0] == "delete":
            if len(command) > 1 and command[1].isdigit():
                delete_task(int(command[1]) - 1)
            else:
                print(Fore.RED + "Invalid command, use: delete <task_number>")
        
        elif command[0] == "view":
            view_tasks()
        
        elif command[0] == "complete":
            if len(command) > 1 and command[1].isdigit():
                mark_task_completed(int(command[1]) - 1)
            else:
                print(Fore.RED + "Invalid command, use: complete <task_number>")
        
        elif command[0] == "search":
            if len(command) > 1:
                search_tasks(" ".join(command[1:]))
            else:
                print(Fore.RED + "Invalid command, use: search <keyword>")
        
        elif command[0] == "help":
            show_help()
        
        elif command[0] == "exit":
            save_tasks()
            print(Fore.GREEN + "Exiting the application. Goodbye!")
            sys.exit()
        
        else:
            print(Fore.RED + "Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    main()
