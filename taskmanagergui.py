import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

tasks = []

def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "completed": False})
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

def update_tasks():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        task_listbox.insert(tk.END, f'{task["task"]} [{status}]')

def clear_all_tasks():
    tasks.clear()
    update_tasks()

root = tk.Tk()
root.title("Task Manager")
root.geometry("500x500")
root.config(bg="#f0f0f0")  


title_label = tk.Label(root, text="Task Manager", font=("Arial", 20, "bold"), bg="#f0f0f0", fg="Red")
title_label.pack(pady=20)


task_label = tk.Label(root, text="Enter a task:", font=("Arial", 12), bg="#f0f0f0")
task_label.pack(pady=5)

task_entry = ttk.Entry(root, font=("Arial", 12), width=40)
task_entry.pack(pady=5)

add_button = ttk.Button(root, text="Add Task", command=add_task, width=20)
add_button.pack(pady=10)

delete_button = ttk.Button(root, text="Delete Task", command=delete_task, width=20)
delete_button.pack(pady=5)

complete_button = ttk.Button(root, text="Complete Task", command=complete_task, width=20)
complete_button.pack(pady=5)

clear_button = ttk.Button(root, text="Clear All Tasks", command=clear_all_tasks, width=20)
clear_button.pack(pady=10)

task_listbox = tk.Listbox(root, font=("Arial", 12), width=50, height=15, selectmode=tk.SINGLE, bg="#ffffff", bd=2, relief="sunken")
task_listbox.pack(pady=10)


root.mainloop()
