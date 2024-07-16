# export_csv.py
import csv
from database import Database

def export_to_csv(timetable):
    db = Database()
    classes = db.get_classes()

    time_slots = ["10:00-10:50", "10:50-11:40", "11:40-12:30", "12:30-13:20"]

    for cls in classes:
        class_id = cls[0]
        branch_name = cls[1]
        semester = cls[2]
        filename = f"{branch_name}_{semester}.csv"

        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Timeslot', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])

            for idx, timeslot in enumerate(time_slots):
                row = [timeslot] + [timetable[class_id][day][idx] for day in range(6)]
                writer.writerow(row)

            writer.writerow([])
            writer.writerow(['Subject Name', 'Teacher Name'])

            subjects = db.get_subjects_by_class_id(class_id)
            for subject in subjects:
                teacher = db.get_teacher(subject[2])
                writer.writerow([subject[0], teacher[1]])

    print(f"Timetable exported to CSV files for each class.")
