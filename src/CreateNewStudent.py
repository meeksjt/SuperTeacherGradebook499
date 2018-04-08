from PyQt5 import QtCore, QtWidgets, QtGui, uic
import GlobalVariables
import sys
import sqlite3
from sqlite3 import Error
import uuid


"""
This is the class that deals with creating a new student to add to our database of all students
"""


class CreateNewStudent(object):

    """
    Constructor for the CreateNewStudent class
    """
    def __init__(self):

        # Create the dialog box
        self.CNStudent = QtWidgets.QDialog()
        self.ui = uic.loadUi('CreateNewStudent.ui', self.CNStudent)

        # Link the button functionality
        self.CNStudent.createNewStudentButton.clicked.connect(self.create_student)

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

        # Make sure that the input fields contain some content
        if student_name == "" or student_email == "":
            return

        conn = sqlite3.connect(GlobalVariables.all_students)

        # Create the students table if this is our first time
        self.create_students_table(conn)

        # Make sure that we don't already have a student with that name and email
        valid = self.check_for_existing_student(conn, student_name, student_email)
        if valid:
            self.add_student(conn, student_name, student_email)
            self.CNStudent.hide()
        else:
            self.bad_input('Error', 'There already exists a student with that name and email')

    """
    Function to add the student
    Parameters:
        conn: (sqlite3 connection) the connection to our all_students database
        student_name: (string) name of the student we want to add
        student_email: (string) email of the student we want to add
    Returns:
        None
    """
    def add_student(self, conn, student_name, student_email):

        # Generate a random id for the student
        id = str(uuid.uuid4())
        c = conn.cursor()

        try:
            # Create the user and tell them what we have done
            c.execute('INSERT INTO students VALUES ("{f}", "{s}", "{t}")'.format(f=id, s=student_name, t=student_email))
            conn.commit()

            choice = QtWidgets.QMessageBox.question(self.CNStudent, 'Congrats!', 'You successfully created the student "{0}"'
                                                                                 ' with the student ID "{1}"'.format(student_name, id),
                                                QtWidgets.QMessageBox.Ok)
            if choice:
                pass

        except sqlite3.IntegrityError:
            pass

    """
    Function to check if the student already exists in our database
    Parameters:
        conn: (sqlite3 connection) the connection to our all_students database
        student_name: (string) name of the student we want to add
        student_email: (string) email of the student we want to add
    Returns:
        True if the student does not already exist, False otherwise
    """
    def check_for_existing_student(self, conn, student_name, student_email):
        c = conn.cursor()
        try:
            count = 0
            for line in c.execute('SELECT * FROM students WHERE name="{f}" AND email="{s}"'
                                          .format(f=student_name, s=student_email)):
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

        first_column = "id text NOT NULL UNIQUE"
        second_column = "name text NOT NULL"
        third_column = "email text NOT NULL"
        try:
            c.execute('CREATE TABLE students ({f}, {s}, {t})'.format(f=first_column, s=second_column, t=third_column))
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