import tkinter as tk
from tkinter import messagebox
from timetable_generator import TimetableGenerator
from export_csv import export_to_csv
from database import Database

class GenerateTimetableUI:
    def __init__(self, parent):
        self.db = Database()
        self.frame = parent
        self.create_widgets()
    
    def create_widgets(self):
        tk.Button(self.frame, text="Generate Timetable", command=self.generate_timetable).pack()
    
    def generate_timetable(self):
        generator = TimetableGenerator(self.db)
        timetable = generator.generate()
        export_to_csv(timetable)
        messagebox.showinfo("Success", "Timetable generated and exported to CSV successfully")
