import random

class TimetableGenerator:
    def __init__(self, db):
        self.db = db
        self.time_slots = ["10:00-10:50", "10:50-11:40", "11:40-12:30", "12:30-13:20"]
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    def generate(self):
        subjects = self.db.get_subjects()
        timetable = {class_id: {day: {slot: None for slot in self.time_slots} for day in self.days} for class_id in self.db.get_class_ids()}
        
        for subject in subjects:
            subject_name, subject_code, teacher_id, class_id, lectures_per_week = subject
            slots_assigned = 0
            while slots_assigned < lectures_per_week:
                day = random.choice(self.days)
                time_slot = random.choice(self.time_slots)
                if self.is_slot_available(timetable, class_id, teacher_id, day, time_slot):
                    timetable[class_id][day][time_slot] = (subject_name, subject_code)
                    slots_assigned += 1
        return timetable

    def is_slot_available(self, timetable, class_id, teacher_id, day, time_slot):
        if timetable[class_id][day][time_slot] is not None:
            return False
        
        for day in self.days:
            if timetable[class_id][day][time_slot] == teacher_id:
                return False

        return True