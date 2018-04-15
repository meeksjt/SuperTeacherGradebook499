# Finished for Right Now
# Might have to add creating new assignments/grades for each added student
from PyQt5 import QtCore, QtWidgets, QtGui, uic
import GlobalVariables
import sys
import sqlite3
from sqlite3 import Error
from Student import Student, StudentList
import uuid

"""
Class for the adding of new students to a course
"""
class AddingStudents(object):

    """
    Constructor for the adding of students
    Parameters:
        studentList: (StudentList) the list of students and associated variables
    """
    def __init__(self, studentList):

        self.AStudents = QtWidgets.QDialog()
        self.ui = uic.loadUi('../assets/ui/AddingStudents.ui', self.AStudents)
        self.AStudents.studentTable.setHorizontalHeaderLabels(
            ['Student ID', 'Student Name', 'Student Email', 'Add Student?']
        )

        self.studentList = studentList
        self.studentIDs = {}
        self.setup_display()

        self.AStudents.show()
        self.AStudents.addSelectedStudentsButton.clicked.connect(self.add_students)

    def add_students(self):

        row_count = self.AStudents.studentTable.rowCount()
        output = []

        for row in range(0, row_count):
            if self.AStudents.studentTable.item(row, 3).checkState() == QtCore.Qt.Checked:
                output.append([
                    self.studentIDs[self.AStudents.studentTable.item(row, 0).text()],
                    self.AStudents.studentTable.item(row, 0).text(),
                    self.AStudents.studentTable.item(row, 1).text(),
                    self.AStudents.studentTable.item(row, 2).text()])

        for i in output:
            print(i[0], i[1], i[2], i[3])
            self.studentList.add_student(Student(i[0], i[1], i[2], i[3]))
            # Might have to add creating everything for that new student

        self.AStudents.hide()


    def setup_display(self):

        #Get all the students
        conn = sqlite3.connect(GlobalVariables.all_students)
        c = conn.cursor()
        display = []

        # get our list of all potential students to be displayed
        for line in c.execute('SELECT * from students'):
            display.append([line[0], line[1], line[2], line[3]])

        # get the IDs of all the existing students
        current_student_IDs = []
        for student in self.studentList.students:
            current_student_IDs.append(student.uuid)

        # Get rid of the students already in the class
        for student in display:
            if student[0] in current_student_IDs:
                display.remove(student)

        # show students not in class
        for student in display:
            row_insert = self.AStudents.studentTable.rowCount()
            self.AStudents.studentTable.insertRow(row_insert)
            self.AStudents.studentTable.setItem(row_insert, 0, QtWidgets.QTableWidgetItem(student[1]))
            self.AStudents.studentTable.setItem(row_insert, 1, QtWidgets.QTableWidgetItem(student[2]))
            self.AStudents.studentTable.setItem(row_insert, 2, QtWidgets.QTableWidgetItem(student[3]))

            self.studentIDs[student[1]] = student[0]

            chkBoxItem = QtWidgets.QTableWidgetItem()
            chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
            self.AStudents.studentTable.setItem(row_insert, 3, chkBoxItem)

        self.AStudents.studentTable.resizeColumnsToContents()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    x = StudentList('test4')
    #x.add_student(uuid.uuid4(), "A25229170", "Tyler Geeks", "jtm0036@uah.edu")

    add = AddingStudents(x)
    sys.exit(app.exec_())
