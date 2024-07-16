import tkinter as tk
from tkinter import messagebox
from database import Database

class AddRoomUI:
    def __init__(self, parent):
        self.db = Database()
        self.frame = parent
        self.create_widgets()
        self.refresh_room_list()
    
    def create_widgets(self):
        tk.Label(self.frame, text="Room Number:").grid(row=0, column=0)
        self.room_number_entry = tk.Entry(self.frame)
        self.room_number_entry.grid(row=0, column=1)

        tk.Button(self.frame, text="Add Room", command=self.add_room).grid(row=1, columnspan=2)

        self.room_listbox = tk.Listbox(self.frame)
        self.room_listbox.grid(row=2, columnspan=2)

        tk.Button(self.frame, text="Delete Room", command=self.delete_room).grid(row=3, columnspan=2)
    
    def add_room(self):
        room_number = self.room_number_entry.get()
        self.db.add_room(room_number)
        messagebox.showinfo("Success", "Room added successfully")
        self.refresh_room_list()

    def delete_room(self):
        selected_room = self.room_listbox.get(tk.ACTIVE)
        if selected_room:
            self.db.delete_room(selected_room)
            messagebox.showinfo("Success", "Room deleted successfully")
            self.refresh_room_list()

    def refresh_room_list(self):
        self.room_listbox.delete(0, tk.END)
        rooms = self.db.get_rooms()
        for room in rooms:
            self.room_listbox.insert(tk.END, room)
