# Come back to this one
import re
import Assignment
from AssignmentCategoryList import AssignmentCategoryList
from Student import *
from GradeScale import GradeScale
from Attendance import AttendanceDictionary


class Course(object):

    def __init__(self, course_uuid="", name="", number="", section="", semester=""):
        self.course_uuid = course_uuid
        self.name = name
        self.number = number
        self.section = section
        self.semester = semester

        self.student_list = StudentList(self.course_uuid)
        self.grade_scale = GradeScale(self.course_uuid)
        self.assignment_category_list = AssignmentCategoryList(self.course_uuid, self.student_list)
        self.attendance_dictionary = AttendanceDictionary(self.course_uuid, self.student_list)

        # Add Attendance

    ######### Above is basically what we need from Course #########

    # Adds an assignment to assignment_list
    def add_student(self, id, name, email):
        self.student_list.add_student(id, name, email)
        pass

    def remove_student(self, uuid):
        self.student_list.remove_student(uuid)

    # What is this function for?
    def display_category(self):
        pass

    def set_grade_scale(self, a, b, c, d):
        self.grade_scale.set_grade_scale(a, b, c, d)

    def delete_course(self):
        # Will be implemented later
        pass
