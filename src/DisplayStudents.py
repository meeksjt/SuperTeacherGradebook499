from PyQt5 import QtCore, QtWidgets, uic
import GlobalVariables
import sys
from Student import Student, StudentList
import uuid
import os



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
        self.ui = uic.loadUi('DisplayStudents.ui', self.DStudents)
        self.DStudents.studentDisplay.setHorizontalHeaderLabels(
            ['Student Name', 'Student ID', 'Student Email']
        )

        self.studentList = studentList
        self.course_name = course_name
        self.course_semester = course_semester
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
        # CourseName+CourseSemester+Student_Rster+txt
        if os.path.isfile(("../student_rosters/" + str(self.course_name)+" " +str(self.course_semester)+" Student Roster.txt")):
            overwrite = self.display_message("Overwrite?", "Do you want to overwrite the previous student roster for this course?")
        else:
            overwrite = True
        if overwrite:
            x = QtWidgets.QMessageBox.question(self.DStudents, "Finished!",
                                               "Your file has been saved in the 'student_rosters' directory.",
                                               QtWidgets.QMessageBox.Ok)
            with open(("../student_rosters/" + str(self.course_name)+" " +str(self.course_semester)+" Student Roster.txt"), 'w') as f:
                f.write((str(self.course_name)+" - " +str(self.course_semester)+" - Student Roster\n\n"))
                for student in self.studentList.students:
                    f.write(student.id+"\t"+student.get_name()+"\t"+student.get_email()+"\n")
            pass
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
    x.add_student(uuid.uuid4(), "A25229169", "Tyler Geeks", "jtm0036@uah.edu")
    x.add_student(uuid.uuid4(), "A25229170", "Gyler Meeks", "jgm0036@uah.edu")
    x.add_student(uuid.uuid4(), "A24229171", "Gyler Teeks", "jgt0036@uah.edu")

    r = DisplayStudents(x, "Senior Design", "Spring 2018")
    sys.exit(app.exec_())
