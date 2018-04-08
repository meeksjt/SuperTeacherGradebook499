# This is the main view for the instructor grade book

from PyQt5 import QtCore, QtGui, QtWidgets

from InitialCourseScreen import *
from CreateNewStudent import *
from CourseManager import *
# from Course import *

# This class is the underlying representation
# for the tree view
class CourseTree(object):
    def __init__(self):
        # parenthetical form of a tree
        self.tree_view_data = [
            ("Math", [
                "Bob",
                "Chris",
                "Gerard",
                "Marphi",
                "Eddie",
                "Edward",
                "Hank",
                "Lard",
                "Lawler",
                "Pinchwood",
            ]),
            ("English", [
                "Jake Paul",
                "Jake Saul",
                "Jake Maul",
                "Bob Jake"
            ]),
            ("Biology", [
                "Paula Dean",
                "Michael",
                "Mark"
            ])
        ]

    # set new data
    def set_tree_data(self, tree_data):
        self.tree_view_data = tree_data

    # add student to class given by class index
    def add_student(self, class_index, student):
        self.tree_view_data[class_index][1].append(student)

    # remove student given by class index
    def drop_student(self, class_index, student):
        self.tree_view_data[class_index][1].remove(student)
       # self.tree_view_data[class_index].remove(student)

    def add_course(self, course):
        self.tree_view_data.append((course, []))

    def drop_course(self, course):
        index = 0
        for course_name, student_list in self.tree_view_data:
            if course_name == course:
                self.tree_view_data.pop(index)
                return
            index += 1

    def print_tree(self):
        print(self.tree_view_data)


class GradeSheet(object):
    def __init__(self, course_tree):
        pass

# a good portion of this class was auto-generated with pyuic5 to
# convert .ui files to .py for more customization/hacking
class MainDisplay(object):
    def __init__(self):
        self.form = QtWidgets.QWidget()
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

        self.course_tree = QtWidgets.QTreeView()
        self.course_tree.setAnimated(True)
        self.course_tree.setObjectName("course_tree")
        self.course_tree.setStyleSheet(
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

        self.verticalLayout.addWidget(self.course_tree)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

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

        self.horizontal_header_view = self.grade_sheet.horizontalHeader()
        self.vertical_header_view = self.grade_sheet.verticalHeader()
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

        self.data_tree = CourseTree()
        self.model = QtGui.QStandardItemModel()
        self.add_items(self.model, self.data_tree.tree_view_data)
        self.course_tree.setModel(self.model)

        # connection for when add button is released
        self.add_course.released.connect(self.add_item)

        # connection for when delete button is released
        self.del_course.released.connect(self.del_selected_item)

        # connection for when a course is selected
        self.selection_model = self.course_tree.selectionModel()
        self.selection_model.selectionChanged.connect(self.load_grade_sheet)

        # connection for when a tree item is renamed
        self.model.itemChanged.connect(self.course_or_name_change)

        self.course_tree.setHeaderHidden(True)
        self.course_tree.setUniformRowHeights(True)

        self.splitter.setSizes([1, 800])

        # course creation wizard
        self.cc_form = None
        self.new_student_form = None

        # self.form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.form.show()

    # creates the underlying tree structure for the course view
    # by reading a tree structure represented in parenthetical/list
    # form like ( A B ( C D ( E F G ) ) )
    def add_items(self, parent, elements):
        for text, children in elements:
            item = QtGui.QStandardItem(text)
            parent.appendRow(item)
            if children:
                self.add_items(item, children)

    # if the current row that is selected has children (is a course)
    # then add a new course... else add a student
    def add_item(self):
        index = self.course_tree.currentIndex()

        # every option adds a student
        student = QtGui.QStandardItem("Enter Student Name")

        # if the current index is invalid, always add a course
        if index.isValid():
            current_item = self.model.itemFromIndex(index)

            # append a new course with one student
            # since a course needs at least one student
            if current_item.hasChildren():
                course_temp = Course()
                self.cc_form = InitialCourseScreen(course_temp)

                if not course_temp.name == "":
                    course = QtGui.QStandardItem(course_temp.name)
                    self.model.insertRow(index.row() + 1, course)
                    course.appendRow(student)

            else:
                self.new_student_form = CreateNewStudent()
                current_item.parent().appendRow(student)
                # insert database logic here

                #
        else:
            course_temp = Course()
            self.cc_form = InitialCourseScreen(course_temp)

            if not course_temp.name == "":
                course = QtGui.QStandardItem(course_temp.name)
                self.model.insertRow(index.row() + 1, course)
                course.appendRow(student)

        self.load_grade_sheet()

    # delete selected item (row or student) from tree view
    def del_selected_item(self):
        index = self.course_tree.currentIndex()
        self.model.removeRow(index.row(), index.parent())
        self.load_grade_sheet()
        # insert database logic here

        #

    # when the user clicks a course, the grade sheet changes to that course
    def load_grade_sheet(self):
        self.grade_sheet.clear()
        index = self.course_tree.currentIndex()
        item = self.model.itemFromIndex(index)
        if index.isValid() and item.hasChildren():

            grade_labels = ["HW 1", "HW 2", "HW 3", "Test 1", "Test 2", "Test 3", "Final"]
            self.grade_sheet.setColumnCount(len(grade_labels))
            self.grade_sheet.setHorizontalHeaderLabels(grade_labels)

            labels = []
            self.grade_sheet.setRowCount(item.rowCount())
            if item.hasChildren():
                for row in range(0, item.rowCount()):
                    name = item.child(row).text()
                    labels.append(name)
                self.grade_sheet.setVerticalHeaderLabels(labels)
                self.horizontal_header_view.resizeSections(QtWidgets.QHeaderView.Stretch)
        else:
            self.grade_sheet.setRowCount(0)
            self.grade_sheet.setColumnCount(0)

    # when a user edits the name of a tree view row
    # update accordingly
    def course_or_name_change(self):
        pass
        # insert database logic here

        #


if __name__ == "__main__":
   import sys

   #app = QtWidgets.QApplication(sys.argv)
   #main_display = MainDisplay()
   #main_display.form.show()
   #sys.exit(app.exec_())

   ct = CourseTree()
   # ct.add_student(1, "muuuuu")
   #ct.drop_course('Math')


