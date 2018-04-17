from PyQt5 import QtCore, QtWidgets, uic
import sys
from Student import *

"""
This is the class that deals with editing a previously created Student
"""

class EditStudent(object):

    def __init__(self, student_uuid, student_name, student_id, student_email, studentList):

        self.EStudent = QtWidgets.QDialog()
        self.ui = uic.loadUi('../assets/ui/EditStudent.ui', self.EStudent)
        self.EStudent.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.EStudent.show()

        self.student_uuid = student_uuid
        self.student_name = student_name
        self.student_id = student_id
        self.student_email = student_email
        self.studentList = studentList

        self.EStudent.studentNameField.setText(self.student_name)
        self.EStudent.studentEmailField.setText(self.student_email)
        self.EStudent.studentIDField.setText(self.student_id)

        self.EStudent.saveStudentInfoButton.clicked.connect(self.edit_student)
        self.EStudent.exec()

    def edit_student(self):
        name = self.EStudent.studentNameField.text()
        email = self.EStudent.studentEmailField.text()
        id = self.EStudent.studentIDField.text()

        if name and email and id:
            self.studentList.set_email(self.student_uuid, email)
            self.studentList.set_name(self.student_uuid, name)
            self.studentList.set_id(self.student_uuid, id)
            self.EStudent.hide()
            # database setting functions for both our own student list and the global student list
            # reload the student list
