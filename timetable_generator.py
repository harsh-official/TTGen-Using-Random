# timetable_generator.py
from database import Database
import random

class TimetableGenerator:
    def __init__(self, db):
        self.db = db

    def generate(self):
        classes = self.db.get_classes()
        teachers = self.db.get_teachers()
        subjects = self.db.get_subjects()

        # Initialize an empty timetable
        timetable = {cls[0]: {day: [''] * 4 for day in range(6)} for cls in classes}

        # Helper dictionary to track teacher's timetable to avoid consecutive lectures
        teacher_timetable = {teacher[0]: {day: [''] * 4 for day in range(6)} for teacher in teachers}

        # Place subjects in the timetable
        for subject in subjects:
            class_id = subject[3]
            teacher_id = subject[2]
            subject_name = subject[0]  # Use subject name instead of subject code
            lectures_per_week = int(subject[4])

            placed_lectures = 0
            daily_lectures = {day: 0 for day in range(6)}

            while placed_lectures < lectures_per_week:
                day = random.randint(0, 5)
                slot = random.randint(0, 3)
                
                if lectures_per_week <= 6 and daily_lectures[day] > 0:
                    continue

                if timetable[class_id][day][slot] == '' and teacher_timetable[teacher_id][day][slot] == '':
                    # Check if the teacher has consecutive lectures
                    if slot == 0 or (teacher_timetable[teacher_id][day][slot-1] == '' and (slot == 3 or teacher_timetable[teacher_id][day][slot+1] == '')):
                        timetable[class_id][day][slot] = subject_name
                        teacher_timetable[teacher_id][day][slot] = subject_name
                        placed_lectures += 1
                        daily_lectures[day] += 1

        return timetable
