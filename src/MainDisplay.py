# This is the main view for the instructor grade book
from PyQt5 import QtGui, QtCore, QtWidgets

from CourseWizard import *
from CreateNewStudent import *
from CourseManager import *
from Student import *
from AssignmentStats import *


# a good portion of this class was auto-generated with pyuic5 to
# convert .ui files to .py for more customization/hacking
class MainDisplay(object):
    def __init__(self):
        self.model = QtGui.QStandardItemModel()
        self.course_tree_view = QtWidgets.QTreeView()
        self.course_tree_view.setModel(self.model)
        self.course_manager = CourseManager()
        self.update_tree_view()

        self.form = QtWidgets.QWidget()
        self.form.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.form.setObjectName("Form")
        self.form.resize(1366, 768)

        self.splitter = QtWidgets.QSplitter(self.form)
        self.splitter.setGeometry(QtCore.QRect(0, 0, 1366, 768))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.splitter.setStyleSheet(
           "QSplitter::handle:vertical { border-color: #2b303b; width: 0px }"
        )

        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.layoutWidget.setStyleSheet(
           "background-color: #2b303b;"
        )

        self.course_tree_view.setAnimated(True)
        self.course_tree_view.setObjectName("course_tree")
        self.course_tree_view.setStyleSheet(
            "QTreeView { "
                "border: none;"
                "color: #eff1f5; "
                "background-color: transparent; "
                "selection-background-color: transparent;"
                "selection-color: transparent;"
                "show-decoration-selected: 1;"
            "}"
            "QTreeView::item:hover {"
                "background: #65737e;"
            "}"
            "QTreeView::item:selected {"
                "color: white;"
                "background: #65737e;"
            "}"
            "QTreeView::branch:has-children:!has-siblings:closed,"
            "QTreeView::branch:closed:has-children:has-siblings"
            "{"
                "border-image: none;"
                "image: url(../assets/images/branch_closed.png);"
            "}"
            "QTreeView::branch:open:has-children:!has-siblings,"
            "QTreeView::branch:open:has-children:has-siblings"
            "{"
                "border-image: none;"
                "image: url(../assets/images/branch_open.png);"
            "}"
        )

        self.verticalLayout.addWidget(self.course_tree_view)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")


        self.get_stats = QtWidgets.QPushButton(self.layoutWidget)
        self.get_stats.setText("Get Statistics")
        self.get_stats.setStyleSheet(
            "QPushButton {"
            "   color: rgb(255,255,255)"
            "}"
        )
        self.horizontalLayout.addWidget(self.get_stats)

        self.del_course = QtWidgets.QPushButton(self.layoutWidget)
        self.del_course.setObjectName("del_course")
        self.del_course.setToolTip("Deletes the selected entry.")
        self.del_course.setStyleSheet(
            "QPushButton { "
                "background-color: transparent;"
                "border-image: url(../assets/images/del_course_button.png);"
                "background: none;"
                "border: none;"
                "background-repeat: none;"
                "min-width: 32px;"
                "max-width: 32px;"
                "min-height: 32px;"
                "max-height: 32px;"
            "}"
            "QPushButton:hover { "
                "border-image: url(../assets/images/del_course_button_highlight.png); "
            "}"
            "QPushButton:pressed { "
                "border-image: url(../assets/images/del_course_button_pressed.png); "
            "}"
        )
        self.horizontalLayout.addWidget(self.del_course)

        self.add_course = QtWidgets.QPushButton(self.layoutWidget)
        self.add_course.setObjectName("add_course")
        self.add_course.setToolTip("Creates a new course.")
        self.add_course.setStyleSheet(
            "QPushButton { "
                "background-color: transparent;"
                "border-image: url(../assets/images/add_course_button.png);"
                "background: none;"
                "border: none;"
                "background-repeat: none;"
                "min-width: 32px;"
                "max-width: 32px;"
                "min-height: 32px;"
                "max-height: 32px;"
            "}"
            "QPushButton:hover { "
                "border-image: url(../assets/images/add_course_button_highlight.png); "
            "}"
            "QPushButton:pressed { "
                "border-image: url(../assets/images/add_course_button_pressed.png); "
            "}"
        )
        self.horizontalLayout.addWidget(self.add_course)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.save_grades = QtWidgets.QPushButton(self.layoutWidget)
        self.save_grades.setText("Save Gradesheet")
        self.save_grades.setStyleSheet(
            "QPushButton {"
            "   color: rgb(255,255,255)"
            "}"
        )
        self.horizontalLayout.addWidget(self.save_grades)

        self.grade_sheet = QtWidgets.QTableWidget(self.splitter)
        self.grade_sheet.setObjectName("grade_sheet")
        self.grade_sheet.setStyleSheet(
            "QTableWidget {"
                "border: none;"
                "background-color: #eff1f5;"
                "selection-background-color: #b48ead;"
            "}"
            "QTableCornerButton::section {"
                "background-color: red;"
                "border: 2px transparent red;"
                "border-radius: 0px;"
            "}"
            "QTableWidget::indicator {"
            "   background-color: black;"
            "}"
        )
        self.grade_sheet.viewportSizeHint()

        self.horizontal_header_view = self.grade_sheet.horizontalHeader()
        self.vertical_header_view = self.grade_sheet.verticalHeader()
        self.horizontal_header_view.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.vertical_header_view.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.horizontal_header_view.setStyleSheet(
            "QHeaderView::section{ border: none; background-color: #c0c5ce}"
            "QHeaderView::section:checked { background-color: #bf616a}"
        )
        self.vertical_header_view.setStyleSheet(
            "QHeaderView::section{ "
                "border: none;"
                "padding: 6px;"
                "background-color: #c0c5ce"
            "}"
            "QHeaderView::section:checked { background-color: #bf616a}"
        )

        menu = QtWidgets.QMenu()

        add_course_sub = QtWidgets.QAction(QtGui.QIcon("../assets/add_course_button.png"), "Add Course", self.add_course)
        add_course_sub.setStatusTip("Add new course to the grade book")
        add_course_sub.triggered.connect(self.add_course_fn)

        add_student_sub = QtWidgets.QAction(QtGui.QIcon("../assets/add_course_button.png"), "Add Student", self.add_course)
        add_student_sub.setStatusTip("Add new student to a course")
        add_student_sub.triggered.connect(self.add_student_fn)

        menu.addAction(add_course_sub)
        menu.addAction(add_student_sub)

        self.add_course.setMenu(menu)

        '''
        menu = QtWidgets.QMenu()

        del_course_sub = QtWidgets.QAction(QtGui.QIcon("../assets/add_course_button.png"), "Delete Course", self.del_course)
        del_course_sub.setStatusTip("Add new course to the grade book")
        del_course_sub.triggered.connect(self.del_selected_item)

        del_student_sub = QtWidgets.QAction(QtGui.QIcon("../assets/add_course_button.png"), "Delete Student", self.del_course)
        del_student_sub.setStatusTip("Add new student to a course")
        del_student_sub.triggered.connect(self.del_selected_item)

        menu.addAction(del_course_sub)
        menu.addAction(del_student_sub)
        '''

        # self.del_course.setMenu(menu)
        # create underlying model

        #connections
        # self.add_course.released.connect(self.add_item)
        self.get_stats.released.connect(self.calculate_statistics)
        self.del_course.released.connect(self.del_selected_item)
        self.get_stats.released.connect(self.menu_event)
        self.save_grades.released.connect(self.save_grade_sheet)

        # connection for when a course is selected
        self.selection_model = self.course_tree_view.selectionModel()
        self.selection_model.selectionChanged.connect(self.load_grade_sheet)

        # connection for when a tree item is renamed
        # self.model.itemChanged.connect(self.course_or_name_change)

        self.course_tree_view.setHeaderHidden(True)
        self.course_tree_view.setUniformRowHeights(True)

        self.splitter.setSizes([1, 800])

        # course creation wizard
        self.cc_form = None
        self.new_student_form = None

        # senior_project = Course("Senior Project", "CS 499", "01", "Spring 18")
        # senior_project.link_with_database()
        # senior_project.student_list.add_student(Student(senior_project.course_uuid, "42", "Tyler Bomb", "Hotmail@gmail.com"))
        # senior_project.student_list.add_student(Student(senior_project.course_uuid, "43", "Tyler Bomba", "Hotmail@gmail.com"))
        # senior_project.student_list.add_student(Student(senior_project.course_uuid, "44", "Tyler Bombas", "Hotmail@gmail.com"))
        # senior_project.student_list.add_student(Student(senior_project.course_uuid, "45", "Tyler Bombast", "Hotmail@gmail.com"))
        # a = senior_project.assignment_category_dict.add_category("Red Fighter 1", "jgfgjfg", "0", senior_project.student_list)
        # b = senior_project.assignment_category_dict.add_category("Red Fighter 2", "jgfgjfg", "0", senior_project.student_list)
        # c = senior_project.assignment_category_dict.add_category("Red Fighter 3", "jgfgjfg", "0", senior_project.student_list)
        # senior_project.assignment_category_dict.assignment_categories[a].add_assignment("AUUID", "Oceans Eleven", "24", senior_project.student_list)
        # senior_project.assignment_category_dict.assignment_categories[b].add_assignment("AUUID2", "Hunger Games", "24", senior_project.student_list)
        # senior_project.assignment_category_dict.assignment_categories[c].add_assignment("AUUID3", "Age of Ultron", "24", senior_project.student_list)
        # senior_project.assignment_category_dict.assignment_categories[c].add_assignment("AUUID4", "Age of Notron", "24", senior_project.student_list)
        # senior_project.assignment_category_dict.assignment_categories[c].add_assignment("AUUID5", "Darkness of Notron", "24", senior_project.student_list)
        # senior_project.assignment_category_dict.assignment_categories[c].add_assignment("AUUID5", "I tell you hwat", "24", senior_project.student_list)
        #self.course_manager.add_course(senior_project)

        self.update_tree_view()


    def menu_event(self):
        pass

    # creates the underlying tree structure for the course view
    # by reading a tree structure represented in parenthetical/list
    # form like ( A B ( C D ( E F G ) ) )
    def update_tree_view(self):
        self.model.clear()
        for course in self.course_manager.course_tree_labels.course_list:
            item = QtGui.QStandardItem(course.course_name)
            for student in course.student_list:
                item.appendRow(QtGui.QStandardItem(student.student_name))
            self.model.appendRow(item)
        # self.course_tree_view.setModel(self.model)

    def add_student_fn(self):
        index = self.course_tree_view.currentIndex()
        current_item = self.model.itemFromIndex(index)
        if not index.isValid():
           return

        student = Student("temp", "temp", "temp", "temp")
        self.new_student_form = CreateNewStudent(student)

        if current_item.parent() is None:
            current_item.appendRow(QtGui.QStandardItem(student.name))
        else:
            current_item.parent().appendRow(QtGui.QStandardItem(student.name))

    def add_course(self):
        pass

    # if the current row that is selected has children (is a course)
    # then add a new course... else add a student
    def add_course_fn(self):
        self.course_manager.currentCourse = Course()

        index = self.course_tree_view.currentIndex()
        if not index.isValid():
            self.cc_form = InitialCourseScreen(self.course_manager)
            if self.course_manager.currentCourse.is_complete is False:
                return
            course = QtGui.QStandardItem(self.course_manager.currentCourse.name)
            self.model.appendRow(course)
            self.grade_sheet.setColumnCount(0)
            self.grade_sheet.setRowCount(0)
            return

        current_item = self.model.itemFromIndex(index)
        self.cc_form = InitialCourseScreen(self.course_manager)
        if self.course_manager.currentCourse.is_complete is False:
            return

        course = QtGui.QStandardItem(self.course_manager.currentCourse.name)

        location = index.row() + 1
        if current_item.parent() is not None:
            location = current_item.parent().row() + 1
        if location - 1 == self.model.rowCount():
            self.model.appendRow(course)
        else:
            self.model.insertRow(location, course)
            cc = self.course_manager.course_tree_labels.course_list[location - 1]
            self.course_manager.course_tree_labels.add_course_at(location,
                                                                 cc.course_name,
                                                                 cc.course_uuid,
                                                                 cc.student_list)
            temp = self.course_manager.course_tree_labels.course_list[-1]
            self.course_manager.course_tree_labels.course_list[location] = temp
            del self.course_manager.course_tree_labels.course_list[-1]

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
            course_uuid = str(self.course_manager.course_tree_labels.get_course_by_index(index.row()).course_uuid)
            if self.course_manager.delete_course(course_uuid):
                self.grade_sheet.setRowCount(0)
                self.grade_sheet.setColumnCount(0)
                self.model.removeRow(index.row())
        else:
            course = self.course_manager.course_tree_labels.get_course_by_index(item.parent().row())
            student = course.student_list[item.row()]
            print(student.student_uuid)
            if self.course_manager.drop_student_from_course(str(course.course_uuid), str(student.student_uuid)):
                self.model.removeRow(index.row(), index.parent())
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
        for col in range(col_count):
            assignment_id = self.grade_sheet.horizontalHeaderItem(col).get_assignment_uuid()
            category_id = self.grade_sheet.horizontalHeaderItem(col).get_category_uuid()
            for row in range(row_count):
                student_id = self.grade_sheet.verticalHeaderItem(row).get_student_uuid()
                grade = str(self.grade_sheet.item(row, col).text())
                if grade == "":
                    grade = "-"
                self.course_manager.currentCourse.assignment_category_dict.assignment_categories[category_id].assignment_dict[assignment_id].set_student_grade(student_id, grade)
            self.course_manager.currentCourse.assignment_category_dict.assignment_categories[category_id].assignment_dict[assignment_id].save_grades()

    # when the user clicks a course, the grade sheet changes to that course
    def load_grade_sheet(self):
        self.grade_sheet.clear()
        index = self.course_tree_view.currentIndex()
        if not index.isValid():
            return
        item = self.model.itemFromIndex(index)

        if item.parent() is None: # no parent? then this is a course, so load the grade sheet
            max = len(self.course_manager.course_tree_labels.course_list)
            cc = self.course_manager.course_tree_labels.get_course_by_index(index.row() % max)
            self.course_manager.set_current_course(cc.course_uuid)

            header_labels = self.load_header_cells()
            vertical_labels = self.load_vertical_header_cells()

            row_count = len(vertical_labels)
            col_count = len(header_labels)

            self.grade_sheet.setRowCount(row_count)
            self.grade_sheet.setColumnCount(col_count)

            for i in range(len(header_labels)):
                self.grade_sheet.setHorizontalHeaderItem(i, header_labels[i])
                self.grade_sheet.horizontalHeaderItem(i).setText(self.grade_sheet.horizontalHeaderItem(i).get_assignment_name())

            for i in range(len(vertical_labels)):
                self.grade_sheet.setVerticalHeaderItem(i, vertical_labels[i])
                self.grade_sheet.verticalHeaderItem(i).setText(self.grade_sheet.verticalHeaderItem(i).get_student_name())


            for col in range(0, len(header_labels)):
                assignment_id = self.grade_sheet.horizontalHeaderItem(col).get_assignment_uuid()
                category_id = self.grade_sheet.horizontalHeaderItem(col).get_category_uuid()
                for row in range(0, len(vertical_labels)):
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
                        # self.grade_sheet.horizontalHeaderItem(row).get_assignment_points()
                    ))
                    self.grade_sheet.item(row, col).setTextGradeCell(str(self.grade_sheet.item(row, col).current_grade))

            self.horizontal_header_view.resizeSections(QtWidgets.QHeaderView.Stretch)
        else:
            self.grade_sheet.setRowCount(0)
            self.grade_sheet.setColumnCount(0)

    # when a user edits the name of a tree view row
    # update accordingly
    def course_or_name_change(self):
        pass
        # insert database logic here

    def calculate_statistics(self):
        self.a_stats = AssignmentStats(self.course_manager.currentCourse.student_list, self.grade_sheet, self.course_manager.currentCourse.name, self.course_manager.currentCourse.semester)


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
        newCourse.grade_scale.set_grade_scale(old_course.get_A_bottom_score(), old_course.get_B_bottom_score(), old_course.get_C_bottom_score(), old_course.get_D_bottom_score)

    #We only want to copy the categories.
    if categories_bool and assignments_bool:
        #Loops through category_dict and creates a new category for each one it finds.
        for category_uuid, category in old_course.assignment_category_dict.items:
            newCourse.assignment_category_dict.add_category(uuid.uuid4(), category.categoryName, category.drop_count, newCourse.student_list)

    #We want to copy the categories and assignments.
    if categories_bool and assignments_bool:
        #Loops through category_dict and creates a new category for each one it finds.
        for category_uuid, category in old_course.assignment_category_dict.items:
            temp_uuid = uuid.uuid4()
            newCourse.assignment_category_dict.add_category(temp_uuid, category.categoryName, category.drop_count, newCourse.student_list)
            for assignment_uuid, assignment in category.assignment_dict.items():
                newCourse.assignment_category_dict[temp_uuid].add_assignment(uuid.uuid4(), assignment.assignmentName, assignment.totalPoints, newCourse.student_list)

if __name__ == "__main__":
   import sys
   app = QtWidgets.QApplication(sys.argv)
   main_display = MainDisplay()
   main_display.form.show()
   sys.exit(app.exec_())
