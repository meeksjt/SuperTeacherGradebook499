# Come back to this
import sqlite3
import copy
from Course import Course
import uuid

from GlobalVariables import connection, cursor


# these three classes represent the underlying data structure of the tree view
class StudentItem(object):
    def __init__(self, student_name, student_uuid):
        self.student_name = student_name
        self.student_uuid = student_uuid

class CourseListItem(object):

    def __init__(self, course_name, course_uuid, student_list):
        self.course_name = course_name
        self.course_uuid = course_uuid
        self.student_list = student_list

    def add_student(self, student_name, student_uuid):
        self.student_list.append(StudentItem(student_name, student_uuid))

    def drop_student(self, student_uuid):
        for i, student_item in enumerate(self.student_list):
            if student_item.student_uuid == student_uuid:
                del self.student_list[i]
                break

class CourseList(object):
    def __init__(self):
        self.course_list = []

    def add_course(self, course_name, course_uuid, student_list):
        self.course_list.append(CourseListItem(course_name, course_uuid, student_list))

    def drop_course(self, course_uuid):
        for i, course_item in enumerate(self.course_list):
            if course_item.course_uuid == course_uuid:
                del self.course_list[i]
                break

    def get_course_by_uuid(self, course_uuid):
        for i, course_item in enumerate(self.course_list):
            if course_item.course_uuid == course_uuid:
                return self.course_list[i]

    def get_course_by_index(self, index):
        return self.course_list[index]

    def print_tree_view(self):
        print("print tree view")
        if not self.course_list:
            print("course_list is empty")
            return
        for course in self.course_list:
            print("hello")
            for student in course.student_list.students:
                print("    " + student.name)



# This class will read the CourseList table, and create a Course for each object in it.
# It will also create a Course.
class CourseManager:
    def __init__(self):
        self.course_dict = {}
        self.course_tree_view = CourseList()

        self.currentCourse = None
        # Create the table if this is a new database.
        cursor.execute("CREATE TABLE IF NOT EXISTS `courseList` (`Name`	TEXT, `Number`   TEXT, `Section`	TEXT, `Semester`	TEXT, `Course_UUID`  TEXT);")
        connection.commit()

        # Reload existing courses if necessary
        self.__reload_courses()

    def add_to_course_tree_view(self, course):
        student_list_items = []
        if course.student_list is None:
            return
        for student in course.student_list.students:
            student_list_items.append(StudentItem(student.name, student.uuid))
        self.course_tree_view.add_course(course.name, course.course_uuid, student_list_items)

    def __reload_courses(self):

        # Clears course list variable
        self.course_dict.clear()
        self.course_tree_view.course_list.clear()

        # Get everything in the table
        cursor.execute("SELECT * FROM `courseList`")

        # Our results go into this as a list.
        results = cursor.fetchall()

        # Go through each row
        for row in results:
            # Here, we pass the Name, Number, Section, Semester, and UUID to the Course object, and it creates it.
            new_course = Course(row[0], row[1], row[2], row[3], row[4])
            new_course.link_with_database()
            self.add_to_course_tree_view(new_course)
            self.course_dict[row[4]] = copy.deepcopy(new_course)


    # Adds a new course to the database and course list
    def add_course(self, course):
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