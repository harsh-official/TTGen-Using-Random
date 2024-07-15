import tkinter as tk
from tkinter import ttk, messagebox
from database import Database
from timetable_generator import TimetableGenerator
from export_csv import export_to_csv

class TimetableUI:
    def __init__(self):
        self.db = Database()
        self.root = tk.Tk()
        self.root.title("College Timetable Generator")
        self.create_widgets()
    
    def create_widgets(self):
        # Add Teacher
        self.teacher_frame = tk.Frame(self.root)
        self.teacher_frame.pack(pady=10)
        tk.Label(self.teacher_frame, text="Teacher ID:").grid(row=0, column=0)
        self.teacher_id_entry = tk.Entry(self.teacher_frame)
        self.teacher_id_entry.grid(row=0, column=1)
        tk.Label(self.teacher_frame, text="Teacher Name:").grid(row=1, column=0)
        self.teacher_name_entry = tk.Entry(self.teacher_frame)
        self.teacher_name_entry.grid(row=1, column=1)
        tk.Button(self.teacher_frame, text="Add Teacher", command=self.add_teacher).grid(row=2, columnspan=2)

        # Add Room
        self.room_frame = tk.Frame(self.root)
        self.room_frame.pack(pady=10)
        tk.Label(self.room_frame, text="Room Number:").grid(row=0, column=0)
        self.room_number_entry = tk.Entry(self.room_frame)
        self.room_number_entry.grid(row=0, column=1)
        tk.Button(self.room_frame, text="Add Room", command=self.add_room).grid(row=1, columnspan=2)

        # Add Class
        self.class_frame = tk.Frame(self.root)
        self.class_frame.pack(pady=10)
        tk.Label(self.class_frame, text="Class ID:").grid(row=0, column=0)
        self.class_id_entry = tk.Entry(self.class_frame)
        self.class_id_entry.grid(row=0, column=1)
        tk.Label(self.class_frame, text="Branch Name:").grid(row=1, column=0)
        self.branch_name_entry = tk.Entry(self.class_frame)
        self.branch_name_entry.grid(row=1, column=1)
        tk.Label(self.class_frame, text="Semester:").grid(row=2, column=0)
        self.semester_entry = tk.Entry(self.class_frame)
        self.semester_entry.grid(row=2, column=1)
        tk.Button(self.class_frame, text="Add Class", command=self.add_class).grid(row=3, columnspan=2)

        # Add Subject
        self.subject_frame = tk.Frame(self.root)
        self.subject_frame.pack(pady=10)
        tk.Label(self.subject_frame, text="Subject Name:").grid(row=0, column=0)
        self.subject_name_entry = tk.Entry(self.subject_frame)
        self.subject_name_entry.grid(row=0, column=1)
        tk.Label(self.subject_frame, text="Subject Code:").grid(row=1, column=0)
        self.subject_code_entry = tk.Entry(self.subject_frame)
        self.subject_code_entry.grid(row=1, column=1)
        tk.Label(self.subject_frame, text="Teacher ID:").grid(row=2, column=0)
        self.teacher_id_combobox = ttk.Combobox(self.subject_frame)
        self.teacher_id_combobox.grid(row=2, column=1)
        tk.Label(self.subject_frame, text="Class ID:").grid(row=3, column=0)
        self.class_id_combobox = ttk.Combobox(self.subject_frame)
        self.class_id_combobox.grid(row=3, column=1)
        tk.Label(self.subject_frame, text="No. of Lectures per Week:").grid(row=4, column=0)
        self.lectures_entry = tk.Entry(self.subject_frame)
        self.lectures_entry.grid(row=4, column=1)
        tk.Button(self.subject_frame, text="Add Subject", command=self.add_subject).grid(row=5, columnspan=2)

        # Generate Timetable
        tk.Button(self.root, text="Generate Timetable", command=self.generate_timetable).pack(pady=20)

    def add_teacher(self):
        teacher_id = self.teacher_id_entry.get()
        teacher_name = self.teacher_name_entry.get()
        self.db.add_teacher(teacher_id, teacher_name)
        self.update_comboboxes()
        messagebox.showinfo("Success", "Teacher added successfully")
    
    def add_room(self):
        room_number = self.room_number_entry.get()
        self.db.add_room(room_number)
        messagebox.showinfo("Success", "Room added successfully")
    
    def add_class(self):
        class_id = self.class_id_entry.get()
        branch_name = self.branch_name_entry.get()
        semester = self.semester_entry.get()
        self.db.add_class(class_id, branch_name, semester)
        self.update_comboboxes()
        messagebox.showinfo("Success", "Class added successfully")
    
    def add_subject(self):
        subject_name = self.subject_name_entry.get()
        subject_code = self.subject_code_entry.get()
        teacher_id = self.teacher_id_combobox.get()
        class_id = self.class_id_combobox.get()
        lectures_per_week = self.lectures_entry.get()
        self.db.add_subject(subject_name, subject_code, teacher_id, class_id, lectures_per_week)
        messagebox.showinfo("Success", "Subject added successfully")

    def update_comboboxes(self):
        self.teacher_id_combobox['values'] = self.db.get_teacher_ids()
        self.class_id_combobox['values'] = self.db.get_class_ids()

    def generate_timetable(self):
        timetable_generator = TimetableGenerator(self.db)
        timetable = timetable_generator.generate()
        export_to_csv(timetable, self.db)
        messagebox.showinfo("Success", "Timetable generated and exported to CSV")


    def run(self):
        self.root.mainloop()
