from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from CourseCreationSecond import CourseCreationSecond

"""
This is the class used for the first part of creating/editing the course
It allows the user to both create and edit the course name, section, and semester
"""


class CourseCreationFirst(object):

    """
    Constructor for CourseCreationFirst
    Parameters:
        name: (string) name of the course (if we are loading in a previous course)
        section: (string) section of the course (if we are loading in a previous course
        semester: (string) semester of the course (if we are loading in a previous course)
    """
    def __init__(self, name="", section="", semester=""):

        # set class variables
        self.course_name = name
        self.course_semester = semester
        self.section_number = section

        # next screen variable is for the CourseCreationSecond if we are creating a course
        self.next_screen = None

        # load the ui
        self.CCFirst = QtWidgets.QDialog()
        self.ui = uic.loadUi('CourseCreationFirst.ui', self.CCFirst)

        # set the initial values for the user input fields
        self.CCFirst.courseNameField.setText(self.course_name)
        self.CCFirst.courseSectionField.setText(self.section_number)
        self.CCFirst.courseSemesterField.setText(self.course_semester)
        self.CCFirst.show()

        # set the functionality of the button depending on usage of class (creation vs editing)
        if self.course_name == "":
            self.CCFirst.nextButton.clicked.connect(self.validate_user_input)
        else:
            self.CCFirst.nextButton.setText('Save')
            self.CCFirst.nextButton.clicked.connect(self.validate_edited_user_input)

    """
    Function that is called when the user is editing a course
    """
    def validate_edited_user_input(self):

        # Get input field values
        self.course_name = self.CCFirst.courseNameField.text()
        self.section_number = self.CCFirst.courseSectionField.text()
        self.course_semester = self.CCFirst.courseSemesterField.text()

        # Make sure form data is valid
        # In this case, form data validity is just form data being present
        if not self.course_name:
            self.bad_input('Error', 'Make sure you enter a valid course name!')
        elif not self.section_number:
            self.bad_input('Error', 'Make sure you enter a valid section number!')
        elif not self.course_semester:
            self.bad_input('Error', 'Make sure you enter a valid course semester!')

        # Add error checking to make sure EXACT course isn't already created (ignore case)
        # This will require a database check

        else:
            self.CCFirst.hide()

    """
    Function that is called when the user is creating a course
    """
    def validate_user_input(self):

        # Get input field values
        self.course_name = self.CCFirst.courseNameField.text()
        self.section_number = self.CCFirst.courseSectionField.text()
        self.course_semester = self.CCFirst.courseSemesterField.text()

        # Make sure form data is valid
        # In this case, form data validity is just form data being present
        if not self.course_name:
            self.bad_input('Error', 'Make sure you enter a valid course name!')
        elif not self.section_number:
            self.bad_input('Error', 'Make sure you enter a valid section number!')
        elif not self.course_semester:
            self.bad_input('Error', 'Make sure you enter a valid course semester!')

        # Add error checking to make sure EXACT course isn't already created (ignore case)
        # This will require a database check

        else:
            self.CCFirst.hide()
            # Proceed to next screen
            self.next_screen = CourseCreationSecond()

    """
    Function for telling the user they entered bad input
    Parameters:
        window_text: (string) the name of the window
        error_message: (string) the error message that is displayed to the user
    """
    def bad_input(self, window_text, error_message):
        choice = QtWidgets.QMessageBox.question(self.CCFirst, window_text, error_message,
                                                QtWidgets.QMessageBox.Cancel)
        if choice:
            pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = CourseCreationFirst('Test', 'Test', 'Test')
    sys.exit(app.exec_())