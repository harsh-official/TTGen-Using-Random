# College Timetable Generator

This project is designed to automatically generate a college timetable. It includes a user interface for taking input, a database to store data, and a feature to export the generated timetable to a CSV file. The timetable ensures that a teacher doesn't get consecutive classes.

## Features

1. **User Interface**: Built using `tkinter` for easy input of data.
2. **Database**: Uses `sqlite3` to store data about teachers, rooms, classes, and subjects.
3. **Timetable Generation**: Uses a simple algorithm to generate timetables while avoiding consecutive classes for any teacher.
4. **CSV Export**: Exports the generated timetable to a CSV file with subject names instead of codes and includes a mapping of subjects to teacher names.

## Requirements

- Python 3.x
- `pandas` library

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>