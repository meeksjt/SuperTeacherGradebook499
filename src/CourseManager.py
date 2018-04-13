# Come back to this
import sqlite3
import copy
from Course import Course
import uuid

from GlobalVariables import connection, cursor
# This class will read the CourseList table, and create a Course for each object in it.
# It will also create a Course.


class CourseManager:
    def __init__(self):
        self.course_dict = {}

        self.currentCourse = None
        # Create the table if this is a new database.
        cursor.execute("CREATE TABLE IF NOT EXISTS `courseList` (`Name`	TEXT, `Number`   TEXT, `Section`	TEXT, `Semester`	TEXT, `Course_UUID`  TEXT);")
        connection.commit()

        # Reload existing courses if necessary
        self.__reload_courses()

    def __reload_courses(self):

        # Clears course list variable
        self.course_dict.clear()

        # Get everything in the table
        cursor.execute("SELECT * FROM `courseList`")

        # Our results go into this as a list.
        results = cursor.fetchall()

        # Go through each row
        for row in results:
            # Here, we pass the Name, Number, Section, Semester, and UUID to the Course object, and it creates it.
            new_course = Course(row[0], row[1], row[2], row[3], row[4])
            self.course_dict[row[4]] = copy.deepcopy(new_course)

    # Adds a new course to the database and course list
    def add_course(self, course):

        # course_uuid = uuid.uuid4()
        # newCourse = Course(name, number, section, semester, str(course_uuid))

        connection.execute(("INSERT INTO 'courseList' VALUES('" + str(course.name) + "','" + str(course.number) +
                            "', '" + str(course.section) + "', '" + str(course.semester) + "', '" + str(course.course_uuid) +
                            "')"))
        connection.commit()
        self.__reload_courses()
        # newCourse.add_student("3","Jacob","email")
        # newCourse.add_student("5", "Matt", "email")
        # newCourse.add_student("8", "Tyler", "email")
        # newCourse.add_student("2", "Chris", "email")
        # newCourse.student_list.print_students()
        return course.course_uuid

    def delete_course(self, uuid):
        for course in self.course_dict:
            if course.course_uuid == uuid:
                cursor.execute("DELETE FROM 'courseList' where Course_UUID = '" + uuid + "';")
                connection.commit()
                self.__reload_courses()

    def get_course(self, course_uuid):
        return self.course_dict[course_uuid]

    def set_current_course(self, course_uuid):
        self.currentCourse = self.course_dict[course_uuid]

    def get_current_course_uuid(self):
        return self.currentCourse.course_uuid

"""
jacob = CourseManager()
x=10
while x > 1:
    jacob.add_course("Senior Project", "399", "03", "Fall")
    x=x-1
    print("1")
"""
"""
    def get_grades(self):
        grade_list = []
        category_grades = []

        for student in self.currentCourse.student_list:
            for category in self.currentCourse.assignment_category_dict.values().assignment_dict.values():
                #for assignment in category.assignment_list:
                    category_grades.append(assignment.get_student_grade(student.uuid))
            grade_list.append(category_grades)
        # give gradelist to student and repeat
"""