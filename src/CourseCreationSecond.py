from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from CourseCreationThird import CourseCreationThird

class CourseCreationSecond(object):

    def __init__(self):

        self.CCSecond = QtWidgets.QDialog()
        self.ui = uic.loadUi('CourseCreationSecond.ui', self.CCSecond)
        self.CCSecond.show()
        self.CCSecond.nextButton.clicked.connect(self.validate_user_input)

    def validate_user_input(self):

        gradeA = self.CCSecond.gradeAField.text()
        gradeB = self.CCSecond.gradeBField.text()
        gradeC = self.CCSecond.gradeCField.text()
        gradeD = self.CCSecond.gradeDField.text()

        # Check to make sure the user entered something
        if not (gradeA and gradeB and gradeC and gradeD):
            self.bad_input('Error', 'Make sure you enter in a number for each of the input fields')
        elif not (self.is_float(gradeA) and self.is_float(gradeB) and self.is_float(gradeC) and self.is_float(gradeD)):
            self.bad_input('Error', 'Make sure you enter numbers!')
        else:
            grade_scale_list = [float(gradeA), float(gradeB), float(gradeC), float(gradeD)]
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

    def bad_input(self, window_text, error_message):
        choice = QtWidgets.QMessageBox.question(self.CCSecond, window_text, error_message,
                                                QtWidgets.QMessageBox.Cancel)
        if choice:
            pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = CourseCreationSecond()
    sys.exit(app.exec_())