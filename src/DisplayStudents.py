import sys
import os
import csv

from PyQt5 import QtCore, QtWidgets, uic
from Student import Student, StudentList


"""
Class for displaying students in a course
"""
class DisplayStudents(object):

    """
    Constructor for displaying students and student information
    Parameters:
        studentList: (StudentList) the list of students and associated variables we are displaying
    """
    def __init__(self, studentList, course_name, course_semester):

        self.DStudents = QtWidgets.QDialog()
        self.ui = uic.loadUi('../assets/ui/DisplayStudents.ui', self.DStudents)
        self.DStudents.studentDisplay.setHorizontalHeaderLabels(
            ['Student Name', 'Student ID', 'Student Email']
        )

        self.studentList = studentList
        self.course_name = course_name
        self.course_semester = course_semester
        self.setup_display()

        self.DStudents.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
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
        # CourseName+CourseSemester+Student_Rster+txt
        if os.path.isfile(("../student_rosters/" + str(self.course_name)+" " +str(self.course_semester)+" Student Roster.txt")):
            overwrite = QtWidgets.QMessageBox.question(self.DStudents, "Overwrite?", "Do you want to overwrite the previous student roster for this course?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        else:
            overwrite = QtWidgets.QMessageBox.Yes
        if overwrite == QtWidgets.QMessageBox.Yes:
            x = QtWidgets.QMessageBox.question(self.DStudents, "Finished!",
                                               "Your file has been saved in the 'student_rosters' directory under the name '"+ str(self.course_name)+" " +str(self.course_semester)+" Student Roster.csv'",
                                               QtWidgets.QMessageBox.Ok)
            with open(("../student_rosters/" + str(self.course_name)+" " +str(self.course_semester)+" Student Roster.csv"), 'w+') as f:

                writer = csv.writer(f)
                writer.writerow(['Student Name', 'Student ID', 'Student Email'])

                for student in self.studentList.students:
                    writer.writerow([student.get_name(),student.get_id(),student.get_email()])
        # Write table contents to a file

    def close(self):
        self.DStudents.close()

    def display_message(self, window_text, window_message):
        choice = QtWidgets.QMessageBox.question(self.DStudents, window_text, window_message, QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Cancel)
        if choice == QtWidgets.QMessageBox.Ok:
            x = QtWidgets.QMessageBox.question(self.DStudents, "Finished!", "Your file has been saved in the 'student_rosters' directory.", QtWidgets.QMessageBox.Ok)
            return True
        else:
            return False

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    x = StudentList('test5')
    # add Student objects now like this: Student(tablename, id, name, email, uuid)
    # table name could be anything since the student list supplies the table name

    x.add_student(Student("tbl", "A25229169", "Tyler Geeks", "jtm0036@uah.edu"))
    x.add_student(Student("tbl", "A252291h3", "Tyler Teeks", "jtm0227@uah.edu"))
    x.add_student(Student("tbl", "A25229122", "Tyler Seeks", "jtm0083@uah.edu"))

    r = DisplayStudents(x, "Senior Design", "Spring 2018")
    sys.exit(app.exec_())
