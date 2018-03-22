from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from CourseCreationThird import CourseCreationThird

"""
This is the class used for the second part of creating/editing the course
It allows the user to both create and edit the grade scale for the course
"""


class CourseCreationSecond(object):

    """
    Constructor for CourseCreationSecond
    Parameters:
        gradeDict: (dictionary) an initial mapping of each letter to a float grade
    """
    def __init__(self, gradeDict={'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.0}):

        # get our gradeDictionary
        self.gradeDict = gradeDict.copy()

        # next screen for course creation
        self.next_screen = None

        # Create our QDialog window and load in the UI
        self.CCSecond = QtWidgets.QDialog()
        self.ui = uic.loadUi('CourseCreationSecond.ui', self.CCSecond)

        # set the initial values in the grade input fields
        self.CCSecond.gradeAField.setText(str(gradeDict['A']))
        self.CCSecond.gradeBField.setText(str(gradeDict['B']))
        self.CCSecond.gradeCField.setText(str(gradeDict['C']))
        self.CCSecond.gradeDField.setText(str(gradeDict['D']))

        # Show our beautiful GUI to the user
        self.CCSecond.show()

        # We are using default value for gradeDict, which means we are mapping to Course Creation instead of Editing
        if gradeDict['A'] == 0:
            self.CCSecond.nextButton.clicked.connect(self.save_course_data)
        # Otherwise, change the button label
        else:
            self.CCSecond.nextButton.setText("Save")
            self.CCSecond.nextButton.clicked.connect(self.save_edited_course_data)

    """
    Function to call when saving course data for course creation
    Parameters:
        None
    Returns:
        None
    """
    def save_course_data(self):
        if self.validate_user_input():
            self.CCSecond.hide()
            self.next_screen = CourseCreationThird()

    """
    Function to call when saving course data for course editing
    Parameters:
        None
    Returns:
        None
    """
    def save_edited_course_data(self):
        if self.validate_user_input():
            self.CCSecond.hide()

    """
    Function that is called when the user is creating a course
    Parameters:
        None
    Returns:
        True if input is valid, False otherwise
    """
    def validate_user_input(self):

        # Get the grades from the user input fields
        self.gradeDict['A'] = self.CCSecond.gradeAField.text()
        self.gradeDict['B'] = self.CCSecond.gradeBField.text()
        self.gradeDict['C'] = self.CCSecond.gradeCField.text()
        self.gradeDict['D'] = self.CCSecond.gradeDField.text()

        # Check to make sure the user entered something
        if not (self.gradeDict['A'] and self.gradeDict['B'] and self.gradeDict['C'] and self.gradeDict['D']):
            self.bad_input('Error', 'Make sure you enter in a number for each of the input fields')

        # Check to make sure user entered floats
        elif not (self.is_float(self.gradeDict['A']) and self.is_float(self.gradeDict['B']) and
                  self.is_float(self.gradeDict['C']) and self.is_float(self.gradeDict['D'])):
            self.bad_input('Error', 'Make sure you enter numbers!')

        # Check to make sure that the user entered unique values in a descending order
        else:
            grade_scale_list = [float(self.gradeDict['A']), float(self.gradeDict['B']),
                                float(self.gradeDict['C']), float(self.gradeDict['D'])]
            uniq_grade_scale_list = list(set(grade_scale_list))
            sorted_grade_scale_list = sorted(uniq_grade_scale_list, reverse=True)

            if sorted_grade_scale_list != grade_scale_list:
                self.bad_input('Error', 'Make sure your grade scales are correct!')
            else:
                return True
        return False

    """
    Function to make sure that the string input can be turned into a float
    Parameters:
        None
    Returns:
        True if the string is a float, False otherwise
    """
    def is_float(self, s):

        try:
            float(s)
            return True
        except ValueError:
            return False

    """
    Function for telling the user they entered bad input
    Parameters:
        window_text: (string) the name of the window
        error_message: (string) the error message that is displayed to the user
    Returns:
        None
    """
    def bad_input(self, window_text, error_message):
        choice = QtWidgets.QMessageBox.question(self.CCSecond, window_text, error_message,
                                                QtWidgets.QMessageBox.Cancel)
        if choice:
            pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = CourseCreationSecond()
    sys.exit(app.exec_())