from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from Course import *
from CourseManager import *
import AssignmentCategoryEditor
import AssignmentCategoryList


class CourseCreatorWidget(object):

    def __init__(self, course_manager, gradeDict={'A': 90.0, 'B': 80.0, 'C': 70.0, 'D': 60.0}):
        self.course_name = ""
        self.course_number = ""
        self.section_number = ""
        self.course_semester = ""

        self.course_manager = course_manager

        self.gradeDict = gradeDict.copy()

        self.frame = QtWidgets.QDialog()
        self.ui = uic.loadUi('CourseWizard.ui', self.frame)
        self.ui.save_course_button.clicked.connect(self.save_course_data)
        self.ui.add_assignment_category_button.clicked.connect(self.add_category)
        # self.ui.drop_assignment_category_button.clicked.connect(self.drop_category)
        # self.ui.drop_assignment_category_button.clicked.connect(self.drop_category)

        self.course_manager = CourseManager()

        self.frame.exec()

    # save the course data into a temporary course object and
    # hide the window iff the data is valid
    def save_course_data(self):
        if self.validate_course_info() and self.validate_grade_scale():
            # save temporary created info

            self.course_manager.add_course(self.course_name, self.course_number,
                                           self.section_number, self.course_semester)

            # ideally we have a buffer for assignments if the user backs out

            # hide current window
            self.frame.hide()

    def add_category(self):
        student_list = StudentList(self.course_uuid)
        category_list = AssignmentCategoryList()
        category_editor = AssignmentCategoryEditor(category_list, )


    # returns true if the information entered int he course info tab is valid
    def validate_course_info(self):

        # Get input field values
        self.course_name = self.ui.course_name_line_edit.text()
        self.course_number = self.ui.course_number_line_edit.text()
        self.section_number = self.ui.section_number_line_edit.text()
        self.course_semester = self.ui.course_semester_line_edit.text()

        # Make sure form data is valid
        # In this case, form data validity is just form data being present
        if not self.course_number:
            self.bad_input('Error', 'Make sure you enter a valid course number on the Course Info tab!')
            return False
        elif not self.course_name:
            self.bad_input('Error', 'Make sure you enter a valid course name on the Course Info tab!')
            return False
        elif not self.section_number:
            self.bad_input('Error', 'Make sure you enter a valid section number on the Course Info tab!')
            return False
        elif not self.course_semester:
            self.bad_input('Error', 'Make sure you enter a valid course semester on the Course Info tab!')
            return False

        # Add error checking to make sure EXACT course isn't already created (ignore case)
        return True

    # returns true if the information entered in the grade scale tab is valid
    def validate_grade_scale(self):

        # Get the grades from the user input fields
        self.gradeDict['A'] = self.ui.a_line_edit.text()
        self.gradeDict['B'] = self.ui.b_line_edit.text()
        self.gradeDict['C'] = self.ui.c_line_edit.text()
        self.gradeDict['D'] = self.ui.d_line_edit.text()

        # Check to make sure the user entered something
        if not (self.gradeDict['A'] and self.gradeDict['B'] and self.gradeDict['C'] and self.gradeDict['D']):
            self.bad_input('Error', 'Make sure you enter in a number for all input fields on the Grade Scale tab')
            return False

        # Check to make sure user entered floats
        if not (self.is_float and self.is_float and self.is_float and self.is_float):
            self.bad_input('Error', 'Make sure you enter numbers on the Grade Scale tab')
            return False

        # Check to make sure that the user entered unique values in a descending order
        grade_scale_list = [float(self.gradeDict['A']), float(self.gradeDict['B']),
                            float(self.gradeDict['C']), float(self.gradeDict['D'])]
        unique_grade_scale_list = list(set(grade_scale_list))
        sorted_grade_scale_list = sorted(unique_grade_scale_list, reverse=True)

        if sorted_grade_scale_list != grade_scale_list:
            self.bad_input('Error', 'Make sure your grade scales on the Grade Scale tab are correct')
            return False

        return True

    def is_float(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def bad_input(self, window_text, error_message):
        choice = QtWidgets.QMessageBox.question(self.ui, window_text, error_message, QtWidgets.QMessageBox.Cancel)
        if choice:
            pass


class InitialCourseScreen(object):

    def __init__(self, course_manager):

        self.course_manager = course_manager
        self.next_screen = None
        self.ICScreen = QtWidgets.QDialog()
        self.ui = uic.loadUi('InitialCourseScreen.ui', self.ICScreen)
        self.ICScreen.newCourseButton.clicked.connect(self.create_new_course)
        self.ICScreen.newTemplateCourseButton.clicked.connect(self.create_new_template_course)
        self.ICScreen.exec()

    def create_new_course(self):
        self.ICScreen.hide()
        self.next_screen = CourseCreatorWidget(self.course_manager)
        # self.next_screen = CourseCreationThird()
        # insert code to set table with appropriate changes

    def create_new_template_course(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    course_manager = CourseManager()
    main = InitialCourseScreen(course_manager)
    sys.exit(app.exec_())
