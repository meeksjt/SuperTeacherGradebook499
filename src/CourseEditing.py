from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys

"""
This is the class used for editing the name, number, section, semester, and attendance points of a course
"""

class CourseEditing(object):

    def __init__(self, course, set_name):

        self.CEditing = QtWidgets.QDialog()
        self.ui = uic.loadUi('../assets/ui/CourseEditing.ui', self.CEditing)

        self.course = course
        self.CEditing.courseNameField.setText(self.course.name)
        self.CEditing.courseNumberField.setText(self.course.number)
        self.CEditing.courseSectionField.setText(self.course.section)
        self.CEditing.courseSemesterField.setText(self.course.semester)
        self.CEditing.attendancePointsField.setText(self.course.attendance_points)

        self.CEditing.saveButton.clicked.connect(self.edit_course)
        self.set_name = set_name

        self.CEditing.exec()


    def edit_course(self):
        name = self.CEditing.courseNameField.text()
        number = self.CEditing.courseNumberField.text()
        section = self.CEditing.courseSectionField.text()
        semester = self.CEditing.courseSemesterField.text()
        ap = self.CEditing.attendancePointsField.text()

        if self.validate_input(name, number, section, semester, ap):
            self.course.update_course(self.course.course_uuid, name, number, section, semester, ap)
            self.set_name(name + '-' + section)
            self.CEditing.hide()

    def validate_input(self, name, number, section, semester, attendance_points):
        if name and number and section and semester:
            try:
                float(attendance_points)
                return True
            except Exception:
                return False