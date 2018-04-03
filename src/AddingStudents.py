from PyQt5 import QtCore, QtWidgets, QtGui, uic
import GlobalVariables
import sys
import sqlite3
from sqlite3 import Error
from Student import Student, StudentList

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
        self.ui = uic.loadUi('AddingStudents.ui', self.AStudents)
        self.AStudents.studentTable.setHorizontalHeaderLabels(
            ['Student Name', 'Student Email', 'Add Student?'])

        self.studentList = studentList
        self.studentIDs = {}
        self.setup_display()

        self.AStudents.show()
        self.AStudents.addSelectedStudentsButton.clicked.connect(self.add_students)

    def add_students(self):
        row_count = self.AStudents.studentTable.rowCount()
        output = []

        for row in range(0, row_count):
            if self.AStudents.studentTable.item(row, 2).checkState() == QtCore.Qt.Checked:
                output.append([
                    self.studentIDs[self.AStudents.studentTable.item(row, 1).text()],
                    self.AStudents.studentTable.item(row, 0).text(),
                    self.AStudents.studentTable.item(row, 1).text()])

        for i in output:
            print(i[0], i[1], i[2])

        for i in output:
            self.studentList.add_student(i[0], i[1], i[2])

    def setup_display(self):

        #Get all the students
        conn = sqlite3.connect(GlobalVariables.all_students)
        c = conn.cursor()
        display = []

        # get our list of all potential students to be displayed
        for line in c.execute('SELECT * from students'):
            display.append([line[0], line[1], line[2]])

        # get the IDs of all the existing students
        current_student_IDs = []
        for student in self.studentList.students:
            current_student_IDs.append(student.id)

        # Get rid of the students already in the class
        for student in display:
            if student[0] in current_student_IDs:
                display.remove(student)

        for student in display:
            row_insert = self.AStudents.studentTable.rowCount()
            self.AStudents.studentTable.insertRow(row_insert)
            self.AStudents.studentTable.setItem(row_insert, 0, QtWidgets.QTableWidgetItem(student[1]))
            self.AStudents.studentTable.setItem(row_insert, 1, QtWidgets.QTableWidgetItem(student[2]))

            self.studentIDs[student[2]] = student[0]

            chkBoxItem = QtWidgets.QTableWidgetItem()
            chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
            self.AStudents.studentTable.setItem(row_insert, 2, chkBoxItem)

        self.AStudents.studentTable.resizeColumnsToContents()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    students = [Student("", "420d57c6-994f-445d-b341-5c9da40c9737", "Tyler Meeks", "jtm0036@uah.edu"),
                Student("", "2", "Melissa Anderson", "mja0005@uah.edu"),
                Student("", "3", "Paul Hudson", "pwh0034@uah.edu"),
                Student("", "4", "Leandra Caywood", "lmc0002@uah.edu"),
                Student("", "5", "Noah Latham", "nbl0098@uah.edu"),
                Student("", "6", "Lucas McClanahan", "ltm0213@uah.edu"),
                Student("", "7", "Emma Donnelly-Bullington", "edb0001@uah.edu")]

    add = AddingStudents(students)
    sys.exit(app.exec_())
