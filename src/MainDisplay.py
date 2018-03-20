# This is the main view for the instructor grade book

from PyQt5 import QtCore, QtGui, QtWidgets


# might not even need this class...
class CourseTree(object):
    def __init__(self):
        # parenthetical form of a tree
        self.tree_view_data = [
            ("Math", [
                ("Bob", []),
                ("Chris", []),
                ("Gerard", []),
                ("Marphi", []),
                ("Eddie", []),
                ("Edward", []),
                ("Hank", []),
                ("Lard", []),
                ("Lawler", []),
                ("Pinchwood", []),
            ]),
            ("English", [
                ("Jake Paul", []),
                ("Jake Saul", []),
                ("Jake Maul", []),
                ("Bob Jake", [])
            ]),
            ("Biology", [
                ("Paula Dean", []),
                ("Michael", []),
                ("Mark", [])
            ])
        ]

    def set_tree_data(self, tree_data):
        self.tree_view_data = tree_data


# a good portion of this class was auto-generated with pyuic5 to
# convert .ui files to .py for more customization/hacking
class MainDisplay(object):
    def __init__(self):
        self.form = QtWidgets.QWidget()
        self.form.setObjectName("Form")
        self.form.resize(1366, 768)

        self.splitter = QtWidgets.QSplitter(self.form)
        self.splitter.setGeometry(QtCore.QRect(1, 1, 1364, 766))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")

        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.course_tree = QtWidgets.QTreeView()
        self.course_tree.setAlternatingRowColors(True)
        self.course_tree.setAnimated(True)
        self.course_tree.setObjectName("course_tree")

        self.verticalLayout.addWidget(self.course_tree)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.del_course = QtWidgets.QPushButton(self.layoutWidget)
        self.del_course.setObjectName("del_course")
        self.del_course.setToolTip("Deletes the selected entry.")
        self.horizontalLayout.addWidget(self.del_course)

        self.add_course = QtWidgets.QPushButton(self.layoutWidget)
        self.add_course.setObjectName("add_course")
        self.add_course.setToolTip("Creates a new course.")
        self.horizontalLayout.addWidget(self.add_course)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.grade_sheet = QtWidgets.QTableWidget(self.splitter)
        self.grade_sheet.setObjectName("grade_sheet")
        self.grade_sheet.setAlternatingRowColors(True)
        self.grade_sheet.setShowGrid(True)
        self.horizontal_header_view = self.grade_sheet.horizontalHeader()
        self.vertical_header_view = self.grade_sheet.verticalHeader()

        self.data_tree = CourseTree()
        self.model = QtGui.QStandardItemModel()
        self.course_tree.setModel(self.model)

        # initializes the data model with a given tree's data
        self.add_items(self.model, self.data_tree.tree_view_data)

        # connection for when add button is released
        self.add_course.released.connect(self.add_item)
        self.add_course.setText("+")

        # connection for when delete button is released
        self.del_course.released.connect(self.del_selected_item)
        self.del_course.setText("-")

        # connection for when a course is selected
        self.selection_model = self.course_tree.selectionModel()
        self.selection_model.selectionChanged.connect(self.load_grade_sheet)

        # connection for when a tree item is renamed
        self.model.itemChanged.connect(self.course_or_name_change)

        self.course_tree.setHeaderHidden(True)
        self.course_tree.setUniformRowHeights(True)

        self.splitter.setSizes([1, 800])
        self.form.show()

        self.anim = QtCore.QPropertyAnimation(self.del_course, b"color")
        self.anim.setDuration(2000)
        self.anim.setLoopCount(2)
        self.anim.setStartValue(QtGui.QColor(0, 0, 0))
        self.anim.setEndValue(QtGui.QColor(255, 255, 255))

    # creates the underlying tree structure for the course view
    # by reading a tree structure represented in parenthetical/list
    # form like ( A B ( C D ( E F G ) ) )
    def add_items(self, parent, elements):
        for text, children in elements:
            item = QtGui.QStandardItem(text)
            parent.appendRow(item)
            if children:
                self.add_items(item, children)

    # add a row to the course tree view (new row = course)
    def add_item(self):
        index = self.course_tree.currentIndex()
        item = QtGui.QStandardItem()
        item.setText("Enter Course Name")
        self.model.insertRow(index.row() + 1, item)
        # insert database logic here

        #

    # delete selected item (row or student) from tree view
    def del_selected_item(self):
        index = self.course_tree.currentIndex()
        self.model.removeRow(index.row(), index.parent())
        # insert database logic here

        #

    # when the user clicks a course, the grade sheet changes to that course
    def load_grade_sheet(self):
        index = self.course_tree.currentIndex()
        if index.isValid():
            item = self.model.itemFromIndex(index)

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
            self.grade_sheet.clear()

    # when a user edits the name of a tree view row
    # update accordingly
    def course_or_name_change(self):
        pass
        # insert database logic here

        #


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_display = MainDisplay()
    sys.exit(app.exec_())

