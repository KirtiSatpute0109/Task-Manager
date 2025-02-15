import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("400x400")
        self.tasks = []

        # Title Label
        self.title_label = tk.Label(root, text="Task Manager", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=20)

        # Task Input Frame
        self.task_frame = tk.Frame(root)
        self.task_frame.pack(pady=10)

        self.task_label = tk.Label(self.task_frame, text="Enter a task:", font=("Arial", 12))
        self.task_label.grid(row=0, column=0, padx=10)

        self.task_entry = tk.Entry(self.task_frame, font=("Arial", 12), width=25)
        self.task_entry.grid(row=0, column=1, padx=10)

        self.add_button = tk.Button(self.task_frame, text="Add Task", font=("Arial", 12), command=self.add_task)
        self.add_button.grid(row=0, column=2, padx=10)

        # Task Listbox to display tasks
        self.task_listbox = tk.Listbox(root, font=("Arial", 12), width=40, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Buttons to Remove or Mark tasks as completed
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.remove_button = tk.Button(self.button_frame, text="Remove Task", font=("Arial", 12), command=self.remove_task)
        self.remove_button.grid(row=0, column=0, padx=10)

        self.complete_button = tk.Button(self.button_frame, text="Mark as Completed", font=("Arial", 12), command=self.complete_task)
        self.complete_button.grid(row=0, column=1, padx=10)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.task_listbox.get(selected_task_index)
            self.tasks.remove(task)
            self.update_task_list()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to remove.")

    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.task_listbox.get(selected_task_index)
            completed_task = f"{task} (Completed)"
            self.tasks[self.tasks.index(task)] = completed_task
            self.update_task_list()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
