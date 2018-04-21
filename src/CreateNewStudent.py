import sys
import sqlite3
import GlobalVariables

from PyQt5 import QtCore, QtWidgets, uic
from sqlite3 import Error
from Student import Student


"""
This is the class that deals with creating a new student to add to our database of all students
"""


class CreateNewStudent(object):

    def __init__(self, student_list, add_student_fn):

        # Create the dialog box
        self.student_list = student_list
        self.CNStudent = QtWidgets.QDialog()
        self.ui = uic.loadUi('../assets/ui/CreateNewStudent.ui', self.CNStudent)
        self.add_student_fn = add_student_fn

        # Link the button functionality
        self.CNStudent.createNewStudentButton.clicked.connect(self.create_student)
        self.CNStudent.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.CNStudent.exec()

    """
    Function to begin creating a new student
    Parameters:
        None
    Returns:
        None
    """
    def create_student(self):

        # Get the values from the input fields
        student_name = self.CNStudent.studentNameField.text()
        student_email = self.CNStudent.studentEmailField.text()
        student_id = self.CNStudent.studentIDField.text()

        # Make sure that the input fields contain some content
        if student_name == "":
            # TODO: throw an error dialog box asking for valid data
            return

        # TODO: check for existing student
        student = Student(self.student_list.tableName, student_id, student_name, student_email)
        QtWidgets.QMessageBox.question(self.CNStudent, '', 'You successfully created the student "{0}"'
                                          ' with the student ID "{1}"'.format(student.name, student.id),
                                          QtWidgets.QMessageBox.Ok)
        self.add_student_fn(student)

    """
    Function to check if the student already exists in our database
    Parameters:
        conn: (sqlite3 connection) the connection to our all_students database
        student_name: (string) name of the student we want to add
        student_email: (string) email of the student we want to add
    Returns:
        True if the student does not already exist, False otherwise
    """
    def check_for_existing_student(self, conn, student_name, student_email, student_id):
        c = conn.cursor()
        try:
            count = 0
            for _ in c.execute('SELECT * FROM students WHERE name="{f}" AND email="{s}" AND id="{t}"'
                                          .format(f=student_name, s=student_email, t=student_id)):
                count += 1
            if count == 0:
                return True
            else:
                return False
        except Error:
            pass
        return False

    """
    Function to create our students table in our all_students database
    Parameters:
        conn: (sqlite3 connection) the connection to our all_students database
    Returns:
        None
    """
    def create_students_table(self, conn):
        c = conn.cursor()

        first_column = "uuid text NOT NULL UNIQUE"
        second_column = "id text NOT NULL UNIQUE"
        third_column = "name text NOT NULL"
        fourth_column = "email text NOT NULL"
        try:
            c.execute('CREATE TABLE students ({f}, {s}, {t}, {r})'.format(f=first_column, s=second_column, t=third_column, r=fourth_column))
            conn.commit()
        except sqlite3.OperationalError:
            pass

    """
    Function for telling the user they entered bad input
    Parameters:
        window_text: (string) the name of the window
        error_message: (string) the error message that is displayed to the user
    """
    def bad_input(self, window_text, error_message):
        choice = QtWidgets.QMessageBox.question(self.CNStudent, window_text, error_message,
                                                QtWidgets.QMessageBox.Cancel)
        if choice:
            pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    x = CreateNewStudent()
    sys.exit(app.exec_())