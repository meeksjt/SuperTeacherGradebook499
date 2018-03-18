from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from CourseCreationFirst import CourseCreationFirst

class InitialCourseScreen(object):

    def __init__(self):

        self.ICScreen = QtWidgets.QDialog()
        self.ui = uic.loadUi('InitialCourseScreen.ui', self.ICScreen)
        self.ICScreen.show()
        self.ICScreen.newCourseButton.clicked.connect(self.create_new_course)
        self.ICScreen.newTemplateCourseButton.clicked.connect(self.create_new_template_course)

    def create_new_course(self):
        self.ICScreen.hide()
        self.next_screen = CourseCreationFirst()

    def create_new_template_course(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = InitialCourseScreen()
    sys.exit(app.exec_())