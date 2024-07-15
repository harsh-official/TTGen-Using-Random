import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('timetable.db')
        self.create_tables()
    
    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS teachers (
                            teacher_id TEXT PRIMARY KEY,
                            teacher_name TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS rooms (
                            room_number TEXT PRIMARY KEY)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS classes (
                            class_id TEXT PRIMARY KEY,
                            branch_name TEXT,
                            semester INTEGER)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS subjects (
                            subject_name TEXT,
                            subject_code TEXT PRIMARY KEY,
                            teacher_id TEXT,
                            class_id TEXT,
                            lectures_per_week INTEGER,
                            FOREIGN KEY(teacher_id) REFERENCES teachers(teacher_id),
                            FOREIGN KEY(class_id) REFERENCES classes(class_id))''')
        self.conn.commit()

    def add_teacher(self, teacher_id, teacher_name):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO teachers VALUES (?, ?)", (teacher_id, teacher_name))
        self.conn.commit()

    def add_room(self, room_number):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO rooms VALUES (?)", (room_number,))
        self.conn.commit()

    def add_class(self, class_id, branch_name, semester):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO classes VALUES (?, ?, ?)", (class_id, branch_name, semester))
        self.conn.commit()

    def add_subject(self, subject_name, subject_code, teacher_id, class_id, lectures_per_week):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO subjects VALUES (?, ?, ?, ?, ?)", (subject_name, subject_code, teacher_id, class_id, lectures_per_week))
        self.conn.commit()

    def get_teacher_ids(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT teacher_id FROM teachers")
        return [row[0] for row in cursor.fetchall()]

    def get_class_ids(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT class_id FROM classes")
        return [row[0] for row in cursor.fetchall()]

    def get_subjects(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM subjects")
        return cursor.fetchall()
    def get_class_info(self, class_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT branch_name, semester FROM classes WHERE class_id=?", (class_id,))
        return cursor.fetchone()

    def get_subjects_with_teacher_names(self, class_id):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT subjects.subject_name, teachers.teacher_name 
            FROM subjects 
            JOIN teachers ON subjects.teacher_id = teachers.teacher_id 
            WHERE subjects.class_id = ?
        ''', (class_id,))
        return cursor.fetchall()
