from CourseManager import CourseManager
from Course import Course
from CreateAssignment import *


class CourseCreatorWidget(object):
    def __init__(self, course_manager, add_course_fn, gradeDict={'A': 90.0, 'B': 80.0, 'C': 70.0, 'D': 60.0}):

        self.categories_to_create = []
        self.new_course = Course()
        self.course_manager = course_manager
        self.add_course_fn = add_course_fn

        self.gradeDict = gradeDict.copy()

        self.frame = QtWidgets.QDialog()
        self.ui = uic.loadUi('../assets/ui/CourseWizard.ui', self.frame)

        col_headers = ['Category Name', 'Drop Count']
        self.ui.tableWidget.setHorizontalHeaderLabels(col_headers)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)

        self.ui.save_course_button.clicked.connect(self.save_course_data)
        self.ui.add_assignment_category_button.clicked.connect(self.add_category)
        self.ui.drop_assignment_category_button.clicked.connect(self.drop_category)

        self.ui.course_name_line_edit.setText("Name")
        self.ui.course_number_line_edit.setText("Number")
        self.ui.section_number_line_edit.setText("Section")
        self.ui.course_semester_line_edit.setText("Semester")

        self.frame.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.frame.exec()

    # save the course data into a temporary course object and
    # hide the window iff the data is valid
    def save_course_data(self):
        if not self.validate_course_info():
            print("failed to validate course info")
            return
        if not self.validate_grade_scale():
            print("failed to validate grade scale")
            return
        if not self.validate_assignment_categories():
            print("failed to validate assignment categories")
            return

        self.save_table_data()
        self.add_course_fn(self.new_course)
        self.course_manager.add_course(self.new_course)
        self.course_manager.set_current_course(self.new_course.course_uuid)
        QtWidgets.QMessageBox.question(self.frame, '', 'Created new course', QtWidgets.QMessageBox.Ok)
        self.new_course = Course()

        # self.frame.hide()

    def add_category(self):
        row_insert = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
        self.ui.tableWidget.setItem(row_insert, 0, QtWidgets.QTableWidgetItem(""))
        self.ui.tableWidget.setItem(row_insert, 1, QtWidgets.QTableWidgetItem(""))

    def drop_category(self):
        row = self.ui.tableWidget.currentRow()
        self.ui.tableWidget.removeRow(row)

    def save_table_data(self):
        row_count = self.ui.tableWidget.rowCount()
        output = []

        # Loop through and get data from the table
        for row in range(0, row_count):
            cat_name = self.ui.tableWidget.item(row, 0).text()
            cat_drop_count = self.ui.tableWidget.item(row, 1).text()
            output.append([cat_name, cat_drop_count])

        # Make sure that our data is valid
        valid = self.category_error_checking(output)

        # Add the assignmentcategorylist creation here if valid is valid
        if valid:
            for category in output:
                # This is the class variable that the Course will user to create its new categories
                self.categories_to_create.append(category[:].copy())
                self.new_course.assignment_category_dict.add_category(str(uuid.uuid4()), category[0], category[1], self.new_course.student_list)

    def validate_assignment_categories(self):
        row_count = self.ui.tableWidget.rowCount()
        output = []

        if row_count <= 0:
            print("no rows")
            return True

        # Loop through and get data from the table
        for row in range(0, row_count):
            cat_name = self.ui.tableWidget.item(row, 0).text()
            cat_drop_count = self.ui.tableWidget.item(row, 1).text()
            output.append([cat_name, cat_drop_count])

        # Make sure that our data is valid
        if not self.category_error_checking(output):
            return False

        # Add the assignmentcategorylist creation here if valid is valid
        for category in output:
            # This is the class variable that the Course will user to create its new categories
            self.categories_to_create.append(category[:].copy())
        return True

    def category_error_checking(self, user_input):
        # variables for the names, weights, and drop counts of each category
        category_names = [user_input[i][0] for i in range(len(user_input))]
        category_drop_counts = [user_input[j][1] for j in range(len(user_input))]

        if not category_names:
            self.bad_input('Error', 'no category names')
            return False

        if not category_drop_counts:
            self.bad_input('Error', 'no drop counts')
            return False

        for i in category_names:
            if i == "":
                self.bad_input('Error', 'Please enter a category name for all categories')
                return False

        # check the drop counts
        for i in category_drop_counts:
            if "." in i:
                self.bad_input('Error', 'enter drop count')
                return False
            try:
                x = int(i.strip())
                if x < 0:
                    self.bad_input('Error', 'negative drop count')
                    return False
            except ValueError:
                self.bad_input('Error', 'You have a drop count that is not a non-negative integer.  Please try again.')
                return False

        return True

    # returns true if the information entered int he course info tab is valid
    def validate_course_info(self):

        # Make sure form data is valid
        # In this case, form data validity is just form data being present
        if not self.ui.course_name_line_edit.text():
            self.bad_input('Error', 'Make sure you enter a valid course number on the Course Info tab!')
            return False
        elif not self.ui.course_number_line_edit.text():
            self.bad_input('Error', 'Make sure you enter a valid course name on the Course Info tab!')
            return False
        elif not self.ui.section_number_line_edit.text():
            self.bad_input('Error', 'Make sure you enter a valid section number on the Course Info tab!')
            return False
        elif not self.ui.course_semester_line_edit.text():
            self.bad_input('Error', 'Make sure you enter a valid course semester on the Course Info tab!')
            return False

        self.new_course.name = self.ui.course_name_line_edit.text()
        self.new_course.number = self.ui.course_number_line_edit.text()
        self.new_course.section = self.ui.section_number_line_edit.text()
        self.new_course.semester = self.ui.course_semester_line_edit.text()
        self.new_course.link_with_database()
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

    def __init__(self, course_manager, add_course_fn):
        self.course_manager = course_manager
        self.add_course_fn = add_course_fn
        self.next_screen = None
        self.ICScreen = QtWidgets.QDialog()
        self.ui = uic.loadUi('../assets/ui/CourseWizardFirst.ui', self.ICScreen)
        self.ICScreen.newCourseButton.clicked.connect(self.create_new_course)
        self.ICScreen.newTemplateCourseButton.clicked.connect(self.create_new_template_course)
        self.ICScreen.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.ICScreen.exec()

    def create_new_course(self):
        self.ICScreen.hide()
        self.next_screen = CourseCreatorWidget(self.course_manager, self.add_course_fn)

    def create_new_template_course(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    course_manager = CourseManager()
    main = InitialCourseScreen(course_manager)
    sys.exit(app.exec_())
