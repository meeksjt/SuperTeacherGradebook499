import sqlite3

connection = sqlite3.connect('../databases/jacobstest.db')
cursor = connection.cursor()

all_students = '../databases/all_students.db'

is_student_creation_wizard_complete = False
is_course_creation_wizard_complete = False
