from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from CourseCreationSecond import CourseCreationSecond

class CourseCreationFirst(object):

    def __init__(self):

        self.course_name = ""
        self.course_semester = ""
        self.section_number = ""
        self.next_screen = None
        self.CCFirst = QtWidgets.QDialog()
        self.ui = uic.loadUi('CourseCreationFirst.ui', self.CCFirst)
        self.CCFirst.show()
        self.CCFirst.nextButton.clicked.connect(self.validate_user_input)

    def validate_user_input(self):

        self.course_name = self.CCFirst.courseNameField.text()
        self.section_number = self.CCFirst.courseSectionField.text()
        self.course_semester = self.CCFirst.courseSemesterField.text()

        # Add error checking to make sure form data is valid
        if not self.course_name:
            self.bad_input('Error', 'Make sure you enter a valid course name!')
        elif not self.section_number:
            self.bad_input('Error', 'Make sure you enter a valid section number!')
        elif not self.course_semester:
            self.bad_input('Error', 'Make sure you enter a valid course semester!')
        # Add error checking to make sure EXACT course isn't already created (ignore case)

        else:
            self.CCFirst.hide()
            self.next_screen = CourseCreationSecond()
        # If everything is fine, proceed to the next form page (but also figure out a way to save the form data)

    def bad_input(self, window_text, error_message):
        choice = QtWidgets.QMessageBox.question(self.CCFirst, window_text, error_message,
                                                QtWidgets.QMessageBox.Cancel)
        if choice:
            pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = CourseCreationFirst()
    sys.exit(app.exec_())