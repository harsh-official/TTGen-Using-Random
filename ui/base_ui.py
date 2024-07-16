import tkinter as tk
from tkinter import ttk
from .add_teacher_ui import AddTeacherUI
from .add_room_ui import AddRoomUI
from .add_class_ui import AddClassUI
from .add_subject_ui import AddSubjectUI
from .timetable_ui import GenerateTimetableUI

class TimetableUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("College Timetable Generator")
        self.create_widgets()
    
    def create_widgets(self):
        tab_control = ttk.Notebook(self.root)

        add_teacher_tab = ttk.Frame(tab_control)
        AddTeacherUI(add_teacher_tab)
        tab_control.add(add_teacher_tab, text='Add Teacher')

        add_room_tab = ttk.Frame(tab_control)
        AddRoomUI(add_room_tab)
        tab_control.add(add_room_tab, text='Add Room')

        add_class_tab = ttk.Frame(tab_control)
        AddClassUI(add_class_tab)
        tab_control.add(add_class_tab, text='Add Class')

        add_subject_tab = ttk.Frame(tab_control)
        AddSubjectUI(add_subject_tab)
        tab_control.add(add_subject_tab, text='Add Subject')

        generate_timetable_tab = ttk.Frame(tab_control)
        GenerateTimetableUI(generate_timetable_tab)
        tab_control.add(generate_timetable_tab, text='Generate Timetable')

        tab_control.pack(expand=1, fill='both')

    def run(self):
        self.root.mainloop()
