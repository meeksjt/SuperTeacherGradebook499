from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from CourseCreationFirst import CourseCreationFirst
from CourseCreationSecond import CourseCreationSecond
from CourseCreationThird import CourseCreationThird

class InitialCourseScreen(object):

    def __init__(self):

        self.next_screen = None
        self.ICScreen = QtWidgets.QDialog()
        self.ui = uic.loadUi('InitialCourseScreen.ui', self.ICScreen)
        self.ICScreen.newCourseButton.clicked.connect(self.create_new_course)
        self.ICScreen.newTemplateCourseButton.clicked.connect(self.create_new_template_course)

    def create_new_course(self):
        self.ICScreen.hide()
        self.next_screen = CourseCreationFirst()
        self.next_screen = CourseCreationSecond()
        # self.next_screen = CourseCreationThird()
        # insert code to set table with appropriate changes

    def create_new_template_course(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = InitialCourseScreen()
    sys.exit(app.exec_())
