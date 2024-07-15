import pandas as pd

def export_to_csv(timetable, db):
    for class_id, schedule in timetable.items():
        class_info = db.get_class_info(class_id)
        file_name = f'{class_info[0]}_{class_info[1]}.csv'
        
        # Prepare timetable data
        data = {day: [] for day in ["Time Slot"] + list(schedule.keys())}
        for time_slot in schedule[list(schedule.keys())[0]].keys():
            row = [time_slot]
            for day in schedule.keys():
                subject_info = schedule[day][time_slot]
                if subject_info is not None:
                    row.append(subject_info[0])  # Use subject name instead of code
                else:
                    row.append('')
            for i, key in enumerate(data.keys()):
                data[key].append(row[i])
        
        df_timetable = pd.DataFrame(data)
        
        # Prepare subjects-teachers data
        subjects_teachers = db.get_subjects_with_teacher_names(class_id)
        df_subjects_teachers = pd.DataFrame(subjects_teachers, columns=["Subject Name", "Teacher Name"])
        
        # Export to CSV
        with open(file_name, 'w', newline='') as f:
            df_timetable.to_csv(f, index=False)
            f.write("\n")
            df_subjects_teachers.to_csv(f, index=False)

