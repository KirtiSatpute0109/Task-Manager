import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter import ttk

tasks = []

def add_task():
    task = task_entry.get()
    if task:
        due_date = askstring("Due Date", "Enter due date (YYYY-MM-DD) or leave blank:")
        priority = askstring("Priority", "Enter priority (High/Medium/Low) or leave blank:")
        category = askstring("Category", "Enter category or leave blank:")
        task_details = {
            "task": task,
            "completed": False,
            "due_date": due_date if due_date else "No due date",
            "priority": priority if priority else "No priority",
            "category": category if category else "No category"
        }
        tasks.append(task_details)
        update_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        update_tasks()
    else:
        messagebox.showwarning("Warning", "No task selected!")

def complete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        tasks[selected_task_index[0]]["completed"] = True
        update_tasks()
    else:
        messagebox.showwarning("Warning", "No task selected!")

def search_tasks():
    keyword = search_entry.get()
    if keyword:
        search_results = [task for task in tasks if keyword.lower() in task["task"].lower()]
        task_listbox.delete(0, tk.END)
        for task in search_results:
            status = "Completed" if task["completed"] else "Pending"
            task_listbox.insert(tk.END, f'{task["task"]} [{status}] - Due: {task["due_date"]} - Priority: {task["priority"]} - Category: {task["category"]}')
    else:
        messagebox.showwarning("Warning", "Search keyword cannot be empty!")

def update_tasks():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        task_listbox.insert(tk.END, f'{task["task"]} [{status}] - Due: {task["due_date"]} - Priority: {task["priority"]} - Category: {task["category"]}')

def clear_all_tasks():
    tasks.clear()
    update_tasks()

# Create the main window
root = tk.Tk()
root.title("Task Manager")
root.geometry("600x600")
root.config(bg="#f5f5f5")  # Lighter background color

# Title Label
title_label = tk.Label(root, text="Task Manager", font=("Helvetica", 18, "bold"), bg="Pink", fg="white")
title_label.pack(pady=20)

# Create and place the widgets
task_label = tk.Label(root, text="Enter a task:", font=("Helvetica", 12), bg="Pink")
task_label.pack(pady=5)

task_entry = ttk.Entry(root, font=("Helvetica", 12), width=40)
task_entry.pack(pady=5)

# Add Task Button
add_button = ttk.Button(root, text="Add Task", command=add_task, width=20)
add_button.pack(pady=10)

# Delete Task Button
delete_button = ttk.Button(root, text="Delete Task", command=delete_task, width=20, style="TButton")
delete_button.pack(pady=5)

# Complete Task Button
complete_button = ttk.Button(root, text="Complete Task", command=complete_task, width=20, style="TButton")
complete_button.pack(pady=5)

# Search Label and Entry
search_label = tk.Label(root, text="Search tasks:", font=("Helvetica", 12), bg="Green")
search_label.pack(pady=5)

search_entry = ttk.Entry(root, font=("Helvetica", 12), width=40)
search_entry.pack(pady=5)

# Search Button
search_button = ttk.Button(root, text="Search", command=search_tasks, width=20, style="TButton")
search_button.pack(pady=10)

# Clear All Tasks Button
clear_button = ttk.Button(root, text="Clear All Tasks", command=clear_all_tasks, width=20, style="TButton")
clear_button.pack(pady=10)

# Task Listbox with styling
task_listbox = tk.Listbox(root, font=("Helvetica", 12), width=50, height=15, selectmode=tk.SINGLE, bg="#ffffff", bd=2, relief="sunken")
task_listbox.pack(pady=10)

# Add style to the buttons
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10, background="#4CAF50", foreground="white", width=20)
style.map("TButton", background=[('active', '#45a049')])

# Start the main loop
root.mainloop()
