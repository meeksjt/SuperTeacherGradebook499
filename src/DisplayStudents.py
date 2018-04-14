from PyQt5 import QtCore, QtWidgets, uic
import GlobalVariables
import sys
from Student import Student, StudentList
import uuid

"""
Class for displaying students in a course
"""
class DisplayStudents(object):

    """
    Constructor for displaying students and student information
    Parameters:
        studentList: (StudentList) the list of students and associated variables we are displaying
    """
    def __init__(self, studentList):

        self.DStudents = QtWidgets.QDialog()
        self.ui = uic.loadUi('DisplayStudents.ui', self.DStudents)
        self.DStudents.studentDisplay.setHorizontalHeaderLabels(
            ['Student Name', 'Student ID', 'Student Email']
        )

        self.studentList = studentList
        self.setup_display()

        self.DStudents.show()
        self.DStudents.returnButton.clicked.connect(self.close)
        self.DStudents.saveStudentInfoButton.clicked.connect(self.save_table)

    def setup_display(self):
        for student in self.studentList.students:
            row_insert = self.DStudents.studentDisplay.rowCount()
            self.DStudents.studentDisplay.insertRow(row_insert)
            self.DStudents.studentDisplay.setItem(row_insert, 0, QtWidgets.QTableWidgetItem(student.get_name()))
            self.DStudents.studentDisplay.setItem(row_insert, 1, QtWidgets.QTableWidgetItem(student.get_id()))
            self.DStudents.studentDisplay.setItem(row_insert, 2, QtWidgets.QTableWidgetItem(student.get_email()))

    def save_table(self):
        

    def close(self):
        self.DStudents.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    x = StudentList('test5')
    x.add_student(uuid.uuid4(), "A25229169", "Tyler Geeks", "jtm0036@uah.edu")
    x.add_student(uuid.uuid4(), "A25229170", "Gyler Meeks", "jgm0036@uah.edu")
    x.add_student(uuid.uuid4(), "A24229171", "Gyler Teeks", "jgt0036@uah.edu")

    r = DisplayStudents(x)
    sys.exit(app.exec_())
