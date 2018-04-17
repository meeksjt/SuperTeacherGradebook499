from PyQt5 import QtCore, QtWidgets, uic
import sys
from Student import *
import GlobalVariables

"""
This is the class that deals with editing a previously created Student
"""

class EditStudent(object):

    def __init__(self, student_uuid, student_id, student_name, student_email, course_uuid):

        self.EStudent = QtWidgets.QDialog()
        self.ui = uic.loadUi('../assets/ui/EditStudent.ui', self.EStudent)
        self.EStudent.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.EStudent.show()

        self.student_id = student_id
        self.student_name = student_name
        self.student_email = student_email
        self.student_uuid = student_uuid
        self.course_uuid = course_uuid
        #self.studentList = studentList

        self.EStudent.studentIDField.setText(self.student_id)
        self.EStudent.studentNameField.setText(self.student_name)
        self.EStudent.studentEmailField.setText(self.student_email)

        self.EStudent.saveStudentInfoButton.clicked.connect(self.edit_student)
        self.EStudent.exec()

    def edit_student(self):
        id = self.EStudent.studentIDField.text()
        name = self.EStudent.studentNameField.text()
        email = self.EStudent.studentEmailField.text()

        if name and email and id:
            GlobalVariables.database.edit_student("id", id, self.course_uuid, self.student_uuid)
            GlobalVariables.database.edit_student("name", name, self.course_uuid, self.student_uuid)
            GlobalVariables.database.edit_student("email", email, self.course_uuid, self.student_uuid)
            self.EStudent.hide()
            # self.studentList.set_id(self.student_uuid, id)
            # self.studentList.set_name(self.student_uuid, name)
            # self.studentList.set_email(self.student_uuid, email)
            # database setting functions for both our own student list and the global student list
            # reload the student list
