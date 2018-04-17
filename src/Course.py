import Student
import uuid

from AssignmentCategoryDict import AssignmentCategoryDict
from GradeScale import GradeScale
from Attendance import AttendanceDictionary
from PyQt5 import QtWidgets
import GlobalVariables

class Course(object):

    def __init__(self, name="", number="", section="", semester="", course_uuid="invalid", attendance_points="0"):
        self.name = name
        self.number = number
        self.section = section
        self.semester = semester
        self.course_uuid = course_uuid
        self.attendance_points = attendance_points
        self.is_complete = False

        # generate an id because one doesn't exist
        if self.course_uuid == "invalid":
            self.course_uuid = str(uuid.uuid4())

        self.student_list = None
        self.grade_scale = None
        self.assignment_category_dict = None
        self.attendance_dictionary = None

    def update_course(self, uuid, name, number, section, semester, points):
        query = "UPDATE `courseList` SET Name = ?, Number = ?, Section = ?, Semester = ?, Attendance_Points = ? WHERE Course_UUID = ?;"
        GlobalVariables.database.connection.execute(query, (name, number, section, semester, points, uuid))
        GlobalVariables.database.connection.commit()

    def set_attendance_points(self, points):
        self.attendance_points = points

    def link_with_database(self):
        self.student_list = Student.StudentList(self.course_uuid)
        self.grade_scale = GradeScale(self.course_uuid)
        self.assignment_category_dict = AssignmentCategoryDict(self.course_uuid, self.student_list)
        self.attendance_dictionary = AttendanceDictionary(self.course_uuid, self.student_list)

    def add_student(self, student):
        self.student_list.add_student(student)

    def remove_student(self, uuid):
        if self.student_list.remove_student(uuid):
            return True
        return False

    def set_grade_scale(self, a, b, c, d):
        self.grade_scale.set_grade_scale(a, b, c, d)
    def reload_grades(self):
        self.assignment_category_dict = AssignmentCategoryDict(self.course_uuid, self.student_list)

    def get_property_list(self):
        return (self.name, self.number, self.section, self.semester, self.course_uuid, self.attendance_points)