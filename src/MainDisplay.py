# This is the main view for the instructor grade book
import CourseWizard

from PyQt5 import QtGui, QtCore, QtWidgets
from Course import Course
from CourseManager import CourseManager

from CreateNewStudent import *
from AssignmentStats import *
from CreateAssignment import *
from StyleSheetData import  *
from EditAssignment import EditAssignment
from EditStudent import EditStudent


class MainDisplay(object):
    def __init__(self):
        self.cc_form = None                     # course creation form
        self.new_student_form = None            # student creation form
        self.course_manager = CourseManager()   # add course, students through this manager
        self.model = QtGui.QStandardItemModel() # QTreeView underlying model

        # widget that displays courses and their students
        self.course_tree_view = QtWidgets.QTreeView()
        self.course_tree_view.setModel(self.model)
        self.course_tree_view.setAnimated(True)
        self.course_tree_view.setObjectName("course_tree")
        self.course_tree_view.setStyleSheet(tree_view_style)
        self.course_tree_view.setHeaderHidden(True)
        self.course_tree_view.setUniformRowHeights(True)

        self.selection_model = self.course_tree_view.selectionModel()
        self.selection_model.selectionChanged.connect(self.load_grade_sheet)

        self.form = QtWidgets.QWidget() # main form that holds all widgets
        self.form.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.form.setObjectName("Form")
        self.form.resize(1366, 768)

        # resizable divider setup
        self.splitter = QtWidgets.QSplitter(self.form)
        self.splitter.setGeometry(QtCore.QRect(0, 0, 1366, 768))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.splitter.setStyleSheet(splitter_style)

        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget.setStyleSheet(layout_widget_style)

        self.splitter.setSizes([1, 800]) # call this after adding to the splitter

        # grade sheet setup
        self.grade_sheet = QtWidgets.QTableWidget(self.splitter)
        self.grade_sheet.setObjectName("grade_sheet")
        self.grade_sheet.setStyleSheet(grade_sheet_style)
        self.grade_sheet.viewportSizeHint()

        self.horizontal_header_view = self.grade_sheet.horizontalHeader()
        self.horizontal_header_view.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.horizontal_header_view.setStyleSheet(horiz_header_style)

        self.vertical_header_view = self.grade_sheet.verticalHeader()
        self.vertical_header_view.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.vertical_header_view.setStyleSheet(vert_header_style)

        # buttons
        self.get_stats = QtWidgets.QPushButton(self.layoutWidget)
        self.get_stats.setText("Get Statistics")
        self.get_stats.setStyleSheet(push_button_style)
        self.get_stats.released.connect(self.calculate_statistics)

        self.del_course = QtWidgets.QPushButton(self.layoutWidget)
        self.del_course.setObjectName("del_course")
        self.del_course.setToolTip("Deletes the selected entry.")
        self.del_course.setStyleSheet(delete_button_style)
        self.del_course.released.connect(self.del_selected_item)

        self.add_course = QtWidgets.QPushButton(self.layoutWidget)
        self.add_course.setObjectName("add_course")
        self.add_course.setToolTip("Creates a new course.")
        self.add_course.setStyleSheet(add_button_style)

        self.save_grades = QtWidgets.QPushButton(self.layoutWidget)
        self.save_grades.setText("Save Gradesheet")
        self.save_grades.setStyleSheet(push_button_style)
        self.save_grades.released.connect(self.save_grade_sheet)

        # holds bottom left row of buttons
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.addWidget(self.get_stats)
        self.horizontalLayout.addWidget(self.del_course)
        self.horizontalLayout.addWidget(self.add_course)
        self.horizontalLayout.addWidget(self.save_grades)

        # holds the button row on the bottom and
        # holds the course view above it
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.addWidget(self.course_tree_view)
        self.verticalLayout.addLayout(self.horizontalLayout)

        # add button is a menu with many options, so handle connections differently
        menu = QtWidgets.QMenu()

        add_course_sub = QtWidgets.QAction(QtGui.QIcon("../assets/add_course_button.png"), "Add Course", self.add_course)
        add_course_sub.setStatusTip("Add new course to the grade book")
        add_course_sub.triggered.connect(self.add_course_fn)

        add_student_sub = QtWidgets.QAction(QtGui.QIcon("../assets/add_course_button.png"), "Add Student", self.add_course)
        add_student_sub.setStatusTip("Add new student to a course")
        add_student_sub.triggered.connect(self.add_student_fn)

        create_assignment_sub = QtWidgets.QAction(QtGui.QIcon("../assets/add_course_button.png"), "Create New Assignment", self.add_course)
        create_assignment_sub.setStatusTip("Create a New Assignment")
        create_assignment_sub.triggered.connect(self.add_assignment_fn)

        edit_assignment_sub = QtWidgets.QAction(QtGui.QIcon("../assets/add_course_button.png"), "Edit Selected Assignment", self.add_course)
        edit_assignment_sub.setStatusTip("Edit Selected Assignment Name, Category, or Point Values")
        edit_assignment_sub.triggered.connect(self.edit_assignment_fn)

        edit_student_sub = QtWidgets.QAction(QtGui.QIcon("../assets/add_course_button.png"), "Edit Selected Student", self.add_course)
        edit_student_sub.setStatusTip("Modify Student Information")
        edit_student_sub.triggered.connect(self.edit_student_fn)

        menu.addAction(add_course_sub)
        menu.addAction(add_student_sub)
        menu.addAction(create_assignment_sub)
        menu.addAction(edit_assignment_sub)
        menu.addAction(edit_student_sub)

        self.add_course.setMenu(menu)

        self.update_tree_view()

    # creates the underlying tree structure for the course view
    # by reading a tree structure represented in parenthetical/list
    # form like ( A B ( C D ( E F G ) ) )
    def update_tree_view(self):
        self.model.clear()
        for course in self.course_manager.course_tree_labels.course_list:
             item = QtGui.QStandardItem(course.course_name)
             item.setAccessibleDescription(course.course_uuid)
             for student in course.student_list:
                 s = QtGui.QStandardItem(student.student_name)
                 s.setAccessibleDescription(student.student_uuid)
                 item.appendRow(s)
             self.model.appendRow(item)
        self.course_tree_view.setModel(self.model)

    # CALL THIS IF YOU WANT TO GET THE CURRENTLY SELECTED COURSE
    # sets the course manager's current course and the Course label list current index
    def update_current_course(self):
        index = self.course_tree_view.currentIndex()
        current_item = self.model.itemFromIndex(index)
        if not index.isValid():
            return
        if current_item.parent() is not None:
            current_item = current_item.parent()
        self.course_manager.set_current_course(current_item.accessibleDescription())

    def add_student_fn(self):
        self.new_student_form = CreateNewStudent(self.course_manager.currentCourse.student_list)
        if not self.new_student_form.is_complete:
            print("form not completed, so no new student")
            return

        self.update_current_course()
        self.course_manager.currentCourse.add_student(self.new_student_form.new_student)

        index = self.course_tree_view.currentIndex()
        if not index.isValid():
            return

        current_item = self.model.itemFromIndex(index)
        if current_item.parent() is not None:
            current_item = current_item.parent()

        student = QtGui.QStandardItem(self.new_student_form.new_student.name)
        student.setAccessibleDescription(self.new_student_form.new_student.uuid)
        current_item.appendRow(student)

        self.course_manager.currentCourse.reload_grades()
        self.load_grade_sheet()

    def add_assignment_fn(self):
        self.add_assignment = CreateAssignment(self.course_manager.currentCourse.assignment_category_dict,
                                               self.course_manager.currentCourse.student_list)
        self.load_grade_sheet()

    def edit_student_fn(self):

        checked_indices = []
        for i in range(1, self.grade_sheet.rowCount()):
            if self.grade_sheet.item(i, 0).checkState() == QtCore.Qt.Checked:
                checked_indices.append(i)

        if len(checked_indices) != 1:
            print("You fucked up")
        else:
            # we need the student id, student name, student email, student uuid
            student_uuid = self.grade_sheet.verticalHeaderItem(checked_indices[0]).get_student_uuid()
            student_name = self.grade_sheet.verticalHeaderItem(checked_indices[0]).get_student_name()
            student_email = self.course_manager.currentCourse.student_list.get_email(student_uuid)
            student_id = self.course_manager.currentCourse.student_list.get_id(student_uuid)

            edit_student = EditStudent(student_uuid, student_name, student_email, student_id, self.course_manager.currentCourse.student_list)

            self.load_grade_sheet()


    def edit_assignment_fn(self):
        checked_indices = []
        for i in range(1, self.grade_sheet.columnCount()):
            if self.grade_sheet.item(0, i).checkState() == QtCore.Qt.Checked:
                checked_indices.append(i)

        if len(checked_indices) != 1:
            print("You fucked up")
        else:
            assignment_name = self.grade_sheet.horizontalHeaderItem(checked_indices[0]).get_assignment_name()
            assignment_uuid = self.grade_sheet.horizontalHeaderItem(checked_indices[0]).get_assignment_uuid()
            assignment_points = self.grade_sheet.horizontalHeaderItem(checked_indices[0]).get_assignment_points()
            category_uuid = self.grade_sheet.horizontalHeaderItem(checked_indices[0]).get_category_uuid()
            edit_assignment = EditAssignment(assignment_name, assignment_points, assignment_uuid,
                               self.course_manager.currentCourse.assignment_category_dict.assignment_categories[category_uuid],
                               self.course_manager.currentCourse.student_list)
            self.load_grade_sheet()

    # if the current row that is selected has children (is a course)
    # then add a new course... else add a student
    def add_course_fn(self):
        self.course_manager.currentCourse = Course()
        index = self.course_tree_view.currentIndex()
        if not index.isValid():
            self.cc_form = CourseWizard.InitialCourseScreen(self.course_manager)
            if self.course_manager.currentCourse.is_complete is False:
                return
            course = QtGui.QStandardItem(self.course_manager.currentCourse.name)
            course.setAccessibleDescription(self.course_manager.currentCourse.course_uuid)
            self.model.appendRow(course)
            self.grade_sheet.setColumnCount(0)
            self.grade_sheet.setRowCount(0)
            return

        current_item = self.model.itemFromIndex(index)
        self.cc_form = CourseWizard.InitialCourseScreen(self.course_manager)
        if self.course_manager.currentCourse.is_complete is False:
            return

        course = QtGui.QStandardItem(self.course_manager.currentCourse.name + " " +
                                     self.course_manager.currentCourse.section)
        course.setAccessibleDescription(self.course_manager.currentCourse.course_uuid)

        location = index.row() + 1
        if current_item.parent() is not None:
            location = current_item.parent().row() + 1
        if location - 1 == self.model.rowCount():
            self.model.appendRow(course)
        else:
            self.model.insertRow(location, course)
            self.grade_sheet.setColumnCount(0)
            self.grade_sheet.setRowCount(0)
        self.load_grade_sheet()

    # delete selected item (row or student) from tree view
    def del_selected_item(self):
        index = self.course_tree_view.currentIndex()
        if not index.isValid():
           return
        item = self.model.itemFromIndex(index)

        if item.parent() is None: # no parent? must be a course
            if self.course_manager.delete_course(item.accessibleDescription()):
                self.grade_sheet.setRowCount(0)
                self.grade_sheet.setColumnCount(0)
                self.model.removeRow(index.row())
        else:
            course_uuid = item.parent().accessibleDescription()
            student_uuid = item.accessibleDescription()
            if self.course_manager.drop_student_from_course(course_uuid, student_uuid):
                self.model.removeRow(index.row(), index.parent())
            self.course_manager.currentCourse.reload_grades()
        self.load_grade_sheet()

    def load_header_cells(self):
        header_list = []
        # Loop through the assignment categories
        for category_id, category in self.course_manager.currentCourse.assignment_category_dict.assignment_categories.items():
            # Loop through the assignments
            for assignment in category.assignment_dict.values():
                # Get the assignment details, create a new HeaderCell
                header_list.append(HeaderCell(assignment.assignmentID, assignment.assignmentName, assignment.totalPoints, category_id))
        return header_list

    def load_vertical_header_cells(self):
        header_list = []
        # Loop through the students
        for student in self.course_manager.currentCourse.student_list.students:
            header_list.append(VerticalHeaderCell(student.name, student.uuid))
        return header_list

    def save_grade_sheet(self):
        index = self.course_tree_view.currentIndex()
        if not index.isValid():
            return

        item = self.model.itemFromIndex(index)
        if item.parent(): # if there is a parent, then there is nothing to save
            return

        row_count = self.grade_sheet.rowCount()
        col_count = self.grade_sheet.columnCount()
        for col in range(1, col_count):
            assignment_id = self.grade_sheet.horizontalHeaderItem(col).get_assignment_uuid()
            category_id = self.grade_sheet.horizontalHeaderItem(col).get_category_uuid()
            for row in range(1, row_count):
                student_id = self.grade_sheet.verticalHeaderItem(row).get_student_uuid()
                grade = str(self.grade_sheet.item(row, col).text())
                if grade == "":
                    grade = "-"
                self.course_manager.currentCourse.assignment_category_dict.assignment_categories[category_id].assignment_dict[assignment_id].set_student_grade(student_id, grade)
            self.course_manager.currentCourse.assignment_category_dict.assignment_categories[category_id].assignment_dict[assignment_id].save_grades()

    # when the user clicks a course, the grade sheet changes to that course
    def load_grade_sheet(self):
        self.update_current_course()
        self.grade_sheet.clear()

        index = self.course_tree_view.currentIndex()
        if not index.isValid():
            return

        item = self.model.itemFromIndex(index)
        if item.parent() is None: # no parent? then this is a course, so load the grade sheet
            header_labels = self.load_header_cells()
            vertical_labels = self.load_vertical_header_cells()

            row_count = len(vertical_labels) + 1
            col_count = len(header_labels) + 1

            self.grade_sheet.setRowCount(row_count)
            self.grade_sheet.setColumnCount(col_count)

            for i in range(1, col_count):
                self.grade_sheet.setHorizontalHeaderItem(i, header_labels[i - 1])
                self.grade_sheet.horizontalHeaderItem(i).setText(self.grade_sheet.horizontalHeaderItem(i).get_assignment_name())

            for i in range(1, row_count):
                self.grade_sheet.setVerticalHeaderItem(i, vertical_labels[i - 1])
                self.grade_sheet.verticalHeaderItem(i).setText(self.grade_sheet.verticalHeaderItem(i).get_student_name())

            # Add the checkboxes
            #for i in range(0, len(vertical_labels)):
            for i in range(1, row_count):
                chkBoxItem = QtWidgets.QTableWidgetItem()
                chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
                self.grade_sheet.setItem(i, 0, chkBoxItem)

            # Add more checkboxes
            for i in range(1, col_count):
                chkBoxItem = QtWidgets.QTableWidgetItem()
                chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                chkBoxItem.setCheckState(QtCore.Qt.Unchecked)

                self.grade_sheet.setItem(0, i, chkBoxItem)


            for col in range(1, col_count):
                assignment_id = self.grade_sheet.horizontalHeaderItem(col).get_assignment_uuid()
                category_id = self.grade_sheet.horizontalHeaderItem(col).get_category_uuid()
                for row in range(1, row_count):
                    student_id = self.grade_sheet.verticalHeaderItem(row).get_student_uuid()
                    student_grade = self.course_manager.currentCourse.assignment_category_dict.assignment_categories[category_id].assignment_dict[assignment_id].get_student_grade(student_id)

                    self.grade_sheet.setItem(row, col, GradeCell(
                        self.grade_sheet.horizontalHeaderItem(col).get_assignment_name(),
                        assignment_id,
                        category_id,
                        self.course_manager.currentCourse.assignment_category_dict.assignment_categories[category_id].get_drop_count(),
                        student_id,
                        self.grade_sheet.verticalHeaderItem(row).get_student_name(),
                        student_grade,
                        self.grade_sheet.horizontalHeaderItem(row).get_assignment_points()
                    ))
                    self.grade_sheet.item(row, col).setTextGradeCell(str(self.grade_sheet.item(row, col).current_grade))

            self.horizontal_header_view.resizeSections(QtWidgets.QHeaderView.Stretch)
        else:
            self.grade_sheet.setRowCount(0)
            self.grade_sheet.setColumnCount(0)

    def course_or_name_change(self):
        pass
        # insert database logic here

    def calculate_statistics(self):
        self.a_stats = AssignmentStats(self.course_manager.currentCourse.student_list,
                                       self.grade_sheet,
                                       self.course_manager.currentCourse.name,
                                       self.course_manager.currentCourse.semester)


class VerticalHeaderCell(QtWidgets.QTableWidgetItem):
    def __init__(self, s_name="", s_uuid=""):
        QtWidgets.QTableWidgetItem.__init__(self)
        self.student_name = s_name
        self.student_uuid = s_uuid

    def setText(self, new_name):
        self.student_name = new_name
        super(VerticalHeaderCell, self).setText(self.student_name)

    def set_student_name(self, new_name):
        self.student_name = new_name

    def get_student_name(self):
        return self.student_name

    def set_student_uuid(self, new_uuid):
        self.student_uuid = new_uuid

    def get_student_uuid(self):
        return self.student_uuid


class HeaderCell(QtWidgets.QTableWidgetItem):
    def __init__(self, a_uuid="", a_name="", a_points="", c_uuid=""):
        QtWidgets.QTableWidgetItem.__init__(self)
        self.assignment_uuid = a_uuid
        self.assignment_name = a_name
        self.assignment_points = a_points
        self.category_uuid = c_uuid

    def setText(self, new_name):
        self.assignment_name = new_name
        super(HeaderCell, self).setText(self.assignment_name)

    def set_assignment_uuid(self, new_uuid):
        self.assignment_uuid = new_uuid

    def get_assignment_uuid(self):
        return self.assignment_uuid

    def get_assignment_name(self):
        return self.assignment_name

    def set_assignment_points(self, new_points):
        self.assignment_points = new_points

    def get_assignment_points(self):
        return self.assignment_points

    def set_category_uuid(self, new_cat_uuid):
        self.category_uuid = new_cat_uuid

    def get_category_uuid(self):
        return self.category_uuid


class GradeCell(QtWidgets.QTableWidgetItem):
    def __init__(self, a_name="", a_uuid="", c_uuid="", c_drop_count="", s_uuid="", s_name="", c_grade="", c_points=""):

        QtWidgets.QTableWidgetItem.__init__(self)
        self.assignment_name = a_name
        self.assignment_uuid = a_uuid
        self.category_uuid = c_uuid
        self.category_drop_count = c_drop_count
        self.student_uuid = s_uuid
        self.student_name = s_name
        self.current_grade = c_grade
        self.current_points = c_points

    def setTextGradeCell(self, grade):
        self.current_grade = grade
        super(GradeCell, self).setText(self.current_grade)

    def get_assignment_name(self):
        return self.assignment_name

    def set_assignment_name(self, x):
        self.assignment_name = x

    def get_assignment_uuid(self):
        return self.assignment_uuid

    def set_assignment_uuid(self, x):
        self.assignment_uuid = x

    def get_category_uuid(self):
        return self.category_uuid

    def set_category_uuid(self, x):
        self.category_uuid = x

    def get_student_uuid(self):
        return self.student_uuid

    def set_student_uuid(self, x):
        self.student_uuid = x

    def get_student_name(self):
        return self.student_name

    def set_student_name(self, x):
        self.student_name = x

    def get_current_grade(self):
        return self.current_grade

    def set_current_grade(self, x):
        self.current_grade = x

    def get_current_points(self):
        return self.current_points

    def set_current_points(self, x):
        self.current_points = x

#Already existing CourseObject that has been linked with the database, and three booloans
def create_course_from_past_course(newCourse, course_uuid, grade_scale_bool, categories_bool, assignments_bool):
    #OK, so I need to check this stuff.
    newCourse.link_with_database()

    #Gets the Course we want to copy from.
    old_course = main_display.course_manager.get_course(course_uuid)
    # We want to copy the gradeScale.
    if grade_scale_bool:
        #Copes the gradescale
        newCourse.grade_scale.set_grade_scale(old_course.get_A_bottom_score(), old_course.get_B_bottom_score(),
                                              old_course.get_C_bottom_score(), old_course.get_D_bottom_score)

    #We only want to copy the categories.
    if categories_bool and assignments_bool:
        #Loops through category_dict and creates a new category for each one it finds.
        for category_uuid, category in old_course.assignment_category_dict.items:
            newCourse.assignment_category_dict.add_category(uuid.uuid4(), category.categoryName,
                                                            category.drop_count, newCourse.student_list)

    #We want to copy the categories and assignments.
    if categories_bool and assignments_bool:
        #Loops through category_dict and creates a new category for each one it finds.
        for category_uuid, category in old_course.assignment_category_dict.items:
            temp_uuid = uuid.uuid4()
            newCourse.assignment_category_dict.add_category(temp_uuid, category.categoryName,
                                                            category.drop_count, newCourse.student_list)
            for assignment_uuid, assignment in category.assignment_dict.items():
                newCourse.assignment_category_dict[temp_uuid].add_assignment(uuid.uuid4(), assignment.assignmentName,
                                                                             assignment.totalPoints, newCourse.student_list)

if __name__ == "__main__":
   import sys
   app = QtWidgets.QApplication(sys.argv)
   main_display = MainDisplay()
   main_display.form.show()
   sys.exit(app.exec_())
