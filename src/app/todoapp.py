import tkinter as tk
from app.tasks import load_tasks, save_tasks, get_next_task_id
from tkinter import messagebox

class TodoApp():
    
    def __init__(self, root):
        self.root = root
        self.root.title("Todo manager")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        self.tasks = load_tasks()
        self.create_widgets()
        self.refresh_task_list()
            
    def create_widgets(self):
        ...
        
    def refresh_task_list(self):
        ...
        
    def add_task(self):
        ...
    
    def mark_done(self):
        ...
        
    def delete_task(self):
        ...
