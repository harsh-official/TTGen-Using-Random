import tkinter as tk
from tkinter import messagebox
from database import Database

class AddSubjectUI:
    def __init__(self, parent):
        self.db = Database()
        self.frame = parent
        self.create_widgets()
        self.refresh_subject_list()

    def create_widgets(self):
        tk.Label(self.frame, text="Subject Name:").grid(row=0, column=0)
        self.subject_name_entry = tk.Entry(self.frame)
        self.subject_name_entry.grid(row=0, column=1)

        tk.Label(self.frame, text="Subject Code:").grid(row=1, column=0)
        self.subject_code_entry = tk.Entry(self.frame)
        self.subject_code_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="Teacher ID:").grid(row=2, column=0)
        self.teacher_id_var = tk.StringVar(self.frame)
        self.teacher_id_dropdown = tk.OptionMenu(self.frame, self.teacher_id_var, [])
        self.teacher_id_dropdown.grid(row=2, column=1)

        tk.Label(self.frame, text="Class ID:").grid(row=3, column=0)
        self.class_id_var = tk.StringVar(self.frame)
        self.class_id_dropdown = tk.OptionMenu(self.frame, self.class_id_var, [])
        self.class_id_dropdown.grid(row=3, column=1)

        tk.Label(self.frame, text="Lectures per Week:").grid(row=4, column=0)
        self.lectures_per_week_entry = tk.Entry(self.frame)
        self.lectures_per_week_entry.grid(row=4, column=1)

        tk.Button(self.frame, text="Add Subject", command=self.add_subject).grid(row=5, columnspan=2)

        self.subject_listbox = tk.Listbox(self.frame)
        self.subject_listbox.grid(row=6, columnspan=2)

        tk.Button(self.frame, text="Delete Subject", command=self.delete_subject).grid(row=7, columnspan=2)

        tk.Button(self.frame, text="Refresh", command=self.refresh_data).grid(row=8, columnspan=2)

        self.refresh_dropdowns()

    def add_subject(self):
        subject_name = self.subject_name_entry.get()
        subject_code = self.subject_code_entry.get()
        teacher_id = self.teacher_id_var.get()
        class_id = self.class_id_var.get()
        lectures_per_week = self.lectures_per_week_entry.get()
        self.db.add_subject(subject_name, subject_code, teacher_id, class_id, lectures_per_week)
        messagebox.showinfo("Success", "Subject added successfully")
        self.refresh_subject_list()
        self.refresh_dropdowns()

    def delete_subject(self):
        selected_subject = self.subject_listbox.get(tk.ACTIVE)
        if selected_subject:
            subject_code = selected_subject.split()[0]
            self.db.delete_subject(subject_code)
            messagebox.showinfo("Success", "Subject deleted successfully")
            self.refresh_subject_list()
            self.refresh_dropdowns()

    def refresh_subject_list(self):
        self.subject_listbox.delete(0, tk.END)
        subjects = self.db.get_subjects()
        for subject in subjects:
            self.subject_listbox.insert(tk.END, f"{subject[1]} {subject[0]} {subject[2]} {subject[3]} {subject[4]}")

    def get_teacher_ids(self):
        teachers = self.db.get_teachers()
        return [teacher[0] for teacher in teachers]

    def get_class_ids(self):
        classes = self.db.get_classes()
        return [cls[0] for cls in classes]

    def refresh_dropdowns(self):
        teacher_ids = self.get_teacher_ids()
        if teacher_ids:
            self.teacher_id_var.set(teacher_ids[0])
        self.teacher_id_dropdown['menu'].delete(0, 'end')
        for teacher_id in teacher_ids:
            self.teacher_id_dropdown['menu'].add_command(label=teacher_id, command=tk._setit(self.teacher_id_var, teacher_id))

        class_ids = self.get_class_ids()
        if class_ids:
            self.class_id_var.set(class_ids[0])
        self.class_id_dropdown['menu'].delete(0, 'end')
        for class_id in class_ids:
            self.class_id_dropdown['menu'].add_command(label=class_id, command=tk._setit(self.class_id_var, class_id))

    def refresh_data(self):
        self.refresh_subject_list()
        self.refresh_dropdowns()

if __name__ == "__main__":
    root = tk.Tk()
    app = AddSubjectUI(parent=root)
    root.mainloop()
