import tkinter as tk
from tkinter import messagebox
from database import Database

class AddTeacherUI:
    def __init__(self, parent):
        self.db = Database()
        self.frame = parent
        self.create_widgets()
        self.refresh_teacher_list()
    
    def create_widgets(self):
        tk.Label(self.frame, text="Teacher ID:").grid(row=0, column=0)
        self.teacher_id_entry = tk.Entry(self.frame)
        self.teacher_id_entry.grid(row=0, column=1)

        tk.Label(self.frame, text="Teacher Name:").grid(row=1, column=0)
        self.teacher_name_entry = tk.Entry(self.frame)
        self.teacher_name_entry.grid(row=1, column=1)

        tk.Button(self.frame, text="Add Teacher", command=self.add_teacher).grid(row=2, columnspan=2)

        self.teacher_listbox = tk.Listbox(self.frame)
        self.teacher_listbox.grid(row=3, columnspan=2)

        tk.Button(self.frame, text="Delete Teacher", command=self.delete_teacher).grid(row=4, columnspan=2)
    
    def add_teacher(self):
        teacher_id = self.teacher_id_entry.get()
        teacher_name = self.teacher_name_entry.get()
        self.db.add_teacher(teacher_id, teacher_name)
        messagebox.showinfo("Success", "Teacher added successfully")
        self.refresh_teacher_list()

    def delete_teacher(self):
        selected_teacher = self.teacher_listbox.get(tk.ACTIVE)
        if selected_teacher:
            teacher_id = selected_teacher.split()[0]
            self.db.delete_teacher(teacher_id)
            messagebox.showinfo("Success", "Teacher deleted successfully")
            self.refresh_teacher_list()

    def refresh_teacher_list(self):
        self.teacher_listbox.delete(0, tk.END)
        teachers = self.db.get_teachers()
        for teacher in teachers:
            self.teacher_listbox.insert(tk.END, f"{teacher[0]} {teacher[1]}")

