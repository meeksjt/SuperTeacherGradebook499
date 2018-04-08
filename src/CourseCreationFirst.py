import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from Course import *

# from CourseCreationSecond import CourseCreationSecond
# from GlobalVariables import *

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
    def __init__(self, t_course):

        # set class variables
        self.temp_course = t_course
        self.course_name = ""
        self.course_number = ""
        self.section_number = ""
        self.course_semester = ""

        # next screen variable is for the CourseCreationSecond if we are creating a course
        self.next_screen = None

        # load the ui
        self.CCFirst = QtWidgets.QDialog()
        self.ui = uic.loadUi('CourseCreationFirst.ui', self.CCFirst)

        # set the initial values for the user input fields
        self.CCFirst.courseNumberField.setText(self.course_number)
        self.CCFirst.courseNameField.setText(self.course_name)
        self.CCFirst.courseSectionField.setText(self.section_number)
        self.CCFirst.courseSemesterField.setText(self.course_semester)
        self.CCFirst.nextButton.clicked.connect(self.save_course_data)

        # set the functionality of the button depending on usage of class (creation vs editing)
        if self.course_name != "":
            self.CCFirst.nextButton.setText('Save')

        self.CCFirst.exec()
    """
    Function to call when saving course data for course creation
    Parameters:
        None
    Returns:
        None
    """
    def save_course_data(self):
        if self.validate_user_input():
            # save temporary created info
            self.temp_course.name = self.course_name
            self.temp_course.number = self.course_number
            self.temp_course.section = self.section_number
            self.temp_course.semester = self.course_semester

            # hide current window
            self.CCFirst.hide()

    """
    Function that is called when the user is creating/editing a course
    Makes sure that all of the fields have at least some value in them when we are creating a course
    Parameters:
        None
    Returns:
        True if input is valid, False otherwise
    """
    def validate_user_input(self):

        # Get input field values
        self.course_number = self.CCFirst.courseNumberField.text()
        self.course_name = self.CCFirst.courseNameField.text()
        self.section_number = self.CCFirst.courseSectionField.text()
        self.course_semester = self.CCFirst.courseSemesterField.text()

        # Make sure form data is valid
        # In this case, form data validity is just form data being present
        if not self.course_number:
            self.bad_input('Error', 'Make sure you enter a valid course number!')
        elif not self.course_name:
            self.bad_input('Error', 'Make sure you enter a valid course name!')
        elif not self.section_number:
            self.bad_input('Error', 'Make sure you enter a valid section number!')
        elif not self.course_semester:
            self.bad_input('Error', 'Make sure you enter a valid course semester!')

        # Add error checking to make sure EXACT course isn't already created (ignore case)

        else:
            return True

        return False

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
    course = Course()
    main = CourseCreationFirst(course)
    sys.exit(app.exec_())
