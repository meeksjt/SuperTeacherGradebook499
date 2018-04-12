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




# a good portion of this class was auto-generated with pyuic5 to
# convert .ui files to .py for more customization/hacking
class MainDisplay(object):
    def __init__(self):
        self.course_manager = CourseManager()

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
        # self.add_items(self.model, self.data_tree.tree_view_data)
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
                self.cc_form = InitialCourseScreen(self.course_manager)

                if not course_temp.name == "":
                    course = QtGui.QStandardItem("new course")
                    self.model.insertRow(index.row() + 1, course)
                    course.appendRow(student)

            else:
                self.new_student_form = CreateNewStudent()
                current_item.parent().appendRow(student)
                # insert database logic here

                #
        else:
            self.cc_form = InitialCourseScreen(self.course_manager)

            course = QtGui.QStandardItem(main_display.course_manager.currentCourse.name)
            self.model.insertRow(index.row() + 1, course)
            course.appendRow(student)

        self.load_grade_sheet()

    # delete selected item (row or student) from tree view
    def del_selected_item(self):
        index = self.course_tree.currentIndex()
        self.model.removeRow(index.row(), index.parent())
        self.load_grade_sheet()
        # insert database logic here

    def save_gradebook(self):
        col_count = self.grade_sheet.columnCount()
        row_count = self.grade_sheet.rowCount()

        for col in range(0, col_count):
            assignment_name = self.grade_sheet.horizontalHeaderItem(col).text()
            assignment_uuid = self.course_manager.currentCourse.assignment_category_list.get_assignment_uuid(assignment_name)
            for row in range(0, row_count):
                pass

    def load_gradebook(self):
        pass

    def load_header_cells(self):
        header_list = []
        # Loop through the assignment categories
        for category in self.course_manager.currentCourse.assignment_category_dict:
            # Loop through the assignments
            for assignment in self.course_manager.currentCourse.assignment_category_dict[category].assignment_dict.values():
                # Get the assignment details, create a new HeaderCell
                header_list.append(HeaderCell(assignment.assignmentID, assignment.assignmentName, assignment.totalPoints, category))

        return header_list

    def load_vertical_header_cells(self):
        header_list = []
        # Loop through the students
        for student in self.course_manager.currentCourse.student_list:
            header_list.append(VerticalHeaderCell(student.name, student.id))

        return header_list

    # when the user clicks a course, the grade sheet changes to that course
    def load_grade_sheet(self):
        self.grade_sheet.clear()
        index = self.course_tree.currentIndex()
        item = self.model.itemFromIndex(index)
        if index.isValid() and item.hasChildren():
            #columns = self.load_gradebook()
            #col = 0
            #row = 0
            #grade_labels = []
            #for column in columns:
            #    if row == 0:
            #        grade_labels.append(column[0])
            #    else:
            #        row = 0
            #        for cell in column[1]:
            #            self.grade_sheet.setItem(row, col, cell.grade)
            #            row += 1
            #        col += 1
            #grade_labels = ["HW 1", "HW 2", "HW 3", "Test 1", "Test 2", "Test 3", "Final"]
            # grade_labels = []

            #self.grade_sheet.setColumnCount(len(grade_labels))
            #self.grade_sheet.setHorizontalHeaderLabels(grade_labels)

            print("Made it past Tyler's buggy code!")

            header_labels = self.

            row_count = len(self.course_manager.currentCourse.student_list.students)

            self.grade_sheet.setRowCount(row_count)
            row = 0
            col = 0

            # This is where we left off

            #for column in columns:
            #    self.grade_sheet.setItem(row, col, column[row])


            #if item.hasChildren():
            #    for row in range(0, item.rowCount()):
            #        name = item.child(row).text()
            #        #This is where the student names will go.
            #        labels.append(name)

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

    def set_category_uuid(self, new_cat_uuid):
        self.category_uuid = new_cat_uuid

    def get_category_uuid(self):
        return self.category_uuid


class GradeCell(QtWidgets.QTableWidgetItem):
    def __init__(self):

        QtWidgets.QTableWidgetItem.__init__(self)
        self.assignment_uuid = ""
        self.category_uuid = ""
        self.student_uuid = ""
        self.current_grade = ""
        self.student_name = ""

        pass

    def setText(self, grade):
        self.current_grade = grade
        super(GradeCell, self).setText(self.current_grade)

    def set_student_name(self, x):
        self.student_name = x

    def get_student_name(self):
        return self.student_name

    def set_assignment_uuid(self, x):
        self.assignment_uuid = x

    def set_category_uuid(self, x):
        self.category_uuid = x

    def set_student_uuid(self, x):
        self.student_uuid = x

    def get_assignment_uuid(self):
        return self.assignment_uuid

    def get_category_uuid(self):
        return self.category_uuid

    def get_student_uuid(self):
        return self.student_uuid


if __name__ == "__main__":
   import sys

   #course = Course("Senior Project", "sg", "jtyjt", "4645754", "4343")

   #for category in course.assignment_category_list.assignment_categories:
   #    category.add_assignment("244", "Quiz 1", "3", course.student_list)


   app = QtWidgets.QApplication(sys.argv)
   main_display = MainDisplay()
   course_uuid = main_display.course_manager.add_course("Senior Project","gdg","dfg","gdg")
   main_display.course_manager.set_current_course(course_uuid)
   main_display.course_manager.currentCourse.student_list.add_student("1", "42", "Tyler Bomb", "Hotmail@gmail.com")
   yo = main_display.course_manager.currentCourse.assignment_category_list.add_category("Red Fighter 1", "jgfgjfg", "0", main_display.course_manager.currentCourse.student_list)
   main_display.course_manager.currentCourse.assignment_category_list.assignment_categories[yo].add_assignment("AUUID", "Oceans Eleven", "24", main_display.course_manager.currentCourse.student_list)
   main_display.course_manager.currentCourse.assignment_category_list.assignment_categories[yo].add_assignment("AUUID2", "Hunger Games", "24", main_display.course_manager.currentCourse.student_list)
   main_display.course_manager.currentCourse.assignment_category_list.assignment_categories[yo].add_assignment("AUUID3", "Age of Ultron", "24", main_display.course_manager.currentCourse.student_list)
   main_display.course_manager.currentCourse.assignment_category_list.assignment_categories[yo].add_assignment("AUUID4", "Tylers Mom", "24", main_display.course_manager.currentCourse.student_list)



   #main_display.load_gradebook()
   main_display.form.show()
   sys.exit(app.exec_())

   # ct.add_student(1, "muuuuu")
   # ct.drop_course('Math')
