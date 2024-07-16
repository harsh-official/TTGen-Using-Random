#database.py
import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('college.db')
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS teachers (
                                    teacher_id TEXT PRIMARY KEY,
                                    teacher_name TEXT)''')
            self.conn.execute('''CREATE TABLE IF NOT EXISTS rooms (
                                    room_number TEXT PRIMARY KEY)''')
            self.conn.execute('''CREATE TABLE IF NOT EXISTS classes (
                                    class_id TEXT PRIMARY KEY,
                                    branch_name TEXT,
                                    semester TEXT)''')
            self.conn.execute('''CREATE TABLE IF NOT EXISTS subjects (
                                    subject_name TEXT,
                                    subject_code TEXT PRIMARY KEY,
                                    teacher_id TEXT,
                                    class_id TEXT,
                                    lectures_per_week INTEGER,
                                    FOREIGN KEY (teacher_id) REFERENCES teachers (teacher_id),
                                    FOREIGN KEY (class_id) REFERENCES classes (class_id))''')

    def add_teacher(self, teacher_id, teacher_name):
        with self.conn:
            self.conn.execute("INSERT INTO teachers (teacher_id, teacher_name) VALUES (?, ?)",
                              (teacher_id, teacher_name))

    def get_teachers(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM teachers")
        return cur.fetchall()

    def delete_teacher(self, teacher_id):
        with self.conn:
            self.conn.execute("DELETE FROM teachers WHERE teacher_id = ?", (teacher_id,))

    def add_room(self, room_number):
        with self.conn:
            self.conn.execute("INSERT INTO rooms (room_number) VALUES (?)", (room_number,))

    def get_rooms(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM rooms")
        return cur.fetchall()

    def delete_room(self, room_number):
        with self.conn:
            self.conn.execute("DELETE FROM rooms WHERE room_number = ?", (room_number,))

    def add_class(self, class_id, branch_name, semester):
        with self.conn:
            self.conn.execute("INSERT INTO classes (class_id, branch_name, semester) VALUES (?, ?, ?)",
                              (class_id, branch_name, semester))

    def get_classes(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM classes")
        return cur.fetchall()

    def delete_class(self, class_id):
        with self.conn:
            self.conn.execute("DELETE FROM classes WHERE class_id = ?", (class_id,))

    def add_subject(self, subject_name, subject_code, teacher_id, class_id, lectures_per_week):
        with self.conn:
            self.conn.execute("INSERT INTO subjects (subject_name, subject_code, teacher_id, class_id, lectures_per_week) VALUES (?, ?, ?, ?, ?)",
                              (subject_name, subject_code, teacher_id, class_id, lectures_per_week))

    def get_subjects(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM subjects")
        return cur.fetchall()

    def delete_subject(self, subject_code):
        with self.conn:
            self.conn.execute("DELETE FROM subjects WHERE subject_code = ?", (subject_code,))
    def get_subjects_by_class_id(self, class_id):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM subjects WHERE class_id = ?", (class_id,))
        return cur.fetchall()

    def get_teacher(self, teacher_id):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM teachers WHERE teacher_id = ?", (teacher_id,))
        return cur.fetchone()
