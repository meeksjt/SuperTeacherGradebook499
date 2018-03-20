from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from CourseCreationThird import CourseCreationThird


class CourseCreationSecond(object):

    def __init__(self, gradeDict={'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.0}):

        self.gradeDict = gradeDict

        self.next_screen = None
        self.CCSecond = QtWidgets.QDialog()
        self.ui = uic.loadUi('CourseCreationSecond.ui', self.CCSecond)
        self.CCSecond.gradeAField.setText(str(gradeDict['A']))
        self.CCSecond.gradeBField.setText(str(gradeDict['B']))
        self.CCSecond.gradeCField.setText(str(gradeDict['C']))
        self.CCSecond.gradeDField.setText(str(gradeDict['D']))
        self.CCSecond.show()

        if gradeDict['A'] == 0:
            print('good to go')
            self.CCSecond.nextButton.clicked.connect(self.validate_user_input)
        else:
            self.CCSecond.nextButton.setText("Save")
            self.CCSecond.nextButton.clicked.connect(self.validate_edited_user_input)

    def validate_edited_user_input(self):
        pass

    def validate_user_input(self):

        self.gradeDict['A'] = self.CCSecond.gradeAField.text()
        self.gradeDict['B'] = self.CCSecond.gradeBField.text()
        self.gradeDict['C'] = self.CCSecond.gradeCField.text()
        self.gradeDict['D'] = self.CCSecond.gradeDField.text()

        # Check to make sure the user entered something
        if not (self.gradeDict['A'] and self.gradeDict['B'] and self.gradeDict['C'] and self.gradeDict['D']):
            self.bad_input('Error', 'Make sure you enter in a number for each of the input fields')
        elif not (self.is_float(self.gradeDict['A']) and self.is_float(self.gradeDict['B']) and self.is_float(self.gradeDict['C']) and self.is_float(self.gradeDict['D'])):
            self.bad_input('Error', 'Make sure you enter numbers!')
        else:
            grade_scale_list = [float(self.gradeDict['A']), float(self.gradeDict['B']), float(self.gradeDict['C']), float(self.gradeDict['D'])]
            uniq_grade_scale_list = list(set(grade_scale_list))
            sorted_grade_scale_list = sorted(uniq_grade_scale_list, reverse=True)

            if sorted_grade_scale_list != grade_scale_list:
                self.bad_input('Error', 'Make sure your grade scales are correct!')
            else:
                self.CCSecond.hide()
                self.next_screen = CourseCreationThird()


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