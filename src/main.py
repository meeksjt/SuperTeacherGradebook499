from Login import *
from CourseManager import *

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    course_manager = CourseManager()
    current_window = Ui_IGPLogin()
    sys.exit(app.exec_())
