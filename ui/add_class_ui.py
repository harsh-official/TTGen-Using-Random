import tkinter as tk
from tkinter import messagebox
from database import Database

class AddClassUI:
    def __init__(self, parent):
        self.db = Database()
        self.frame = parent
        self.create_widgets()
        self.refresh_class_list()
    
    def create_widgets(self):
        tk.Label(self.frame, text="Class ID:").grid(row=0, column=0)
        self.class_id_entry = tk.Entry(self.frame)
        self.class_id_entry.grid(row=0, column=1)

        tk.Label(self.frame, text="Branch Name:").grid(row=1, column=0)
        self.branch_name_entry = tk.Entry(self.frame)
        self.branch_name_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="Semester:").grid(row=2, column=0)
        self.semester_entry = tk.Entry(self.frame)
        self.semester_entry.grid(row=2, column=1)

        tk.Button(self.frame, text="Add Class", command=self.add_class).grid(row=3, columnspan=2)

        self.class_listbox = tk.Listbox(self.frame)
        self.class_listbox.grid(row=4, columnspan=2)

        tk.Button(self.frame, text="Delete Class", command=self.delete_class).grid(row=5, columnspan=2)
    
    def add_class(self):
        class_id = self.class_id_entry.get()
        branch_name = self.branch_name_entry.get()
        semester = self.semester_entry.get()
        self.db.add_class(class_id, branch_name, semester)
        messagebox.showinfo("Success", "Class added successfully")
        self.refresh_class_list()

    def delete_class(self):
        selected_class = self.class_listbox.get(tk.ACTIVE)
        if selected_class:
            class_id = selected_class.split()[0]
            self.db.delete_class(class_id)
            messagebox.showinfo("Success", "Class deleted successfully")
            self.refresh_class_list()

    def refresh_class_list(self):
        self.class_listbox.delete(0, tk.END)  # Clear existing items
        classes = self.db.get_classes()  # Assuming this returns a list of tuples like [('C1', 'Computer Science', '1st'), ('E1', 'Electrical Engineering', '2nd')]
        for cls in classes:
            class_str = f"{cls[0]} {cls[1]} {cls[2]}"  # Format class data as a string
            self.class_listbox.insert(tk.END, class_str)  # Insert formatted string into Listbox

