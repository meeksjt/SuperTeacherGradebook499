# Delete Course
import re
import Assignment
from AssignmentCategoryDict import AssignmentCategoryDict
from Student import *
from GradeScale import GradeScale
from Attendance import AttendanceDictionary


class Course(object):

    def __init__(self, course_uuid="invalid", name="", number="", section="", semester=""):
        self.name = name
        self.number = number
        self.section = section
        self.semester = semester
        self.course_uuid = course_uuid

        # generate an id because one doesn't exist
        if self.course_uuid == "invalid":
            self.course_uuid = uuid.uuid4()

        self.student_list = None
        self.grade_scale = None
        self.assignment_category_dict = None
        self.attendance_dictionary = None

    def link_with_database(self):
        self.student_list = StudentList(self.course_uuid)
        self.grade_scale = GradeScale(self.course_uuid)
        self.assignment_category_dict = AssignmentCategoryDict(self.course_uuid, self.student_list)
        self.attendance_dictionary = AttendanceDictionary(self.course_uuid, self.student_list)

    def add_student(self, student_uuid, student_id, name, email):
        self.student_list.add_student(student_uuid, student_id, name, email)

    def remove_student(self, uuid):
        self.student_list.remove_student(uuid)

    def set_grade_scale(self, a, b, c, d):
        self.grade_scale.set_grade_scale(a, b, c, d)

    def delete_course(self):
        # Will be implemented later
        pass
