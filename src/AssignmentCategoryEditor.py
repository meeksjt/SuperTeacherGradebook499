from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from AssignmentCategory import AssignmentCategory

"""
This is the class used for editing the third part of creating a course
It allows the user to edit the categories used for making a course
"""


class AssignmentCategoryEditor(object):

    """
    Constructor for AssignmentCategoryEditor
    """
    def __init__(self, assignment_categories):

        # Table column headers
        col_headers = ['Category Name', 'Category Weight (%)', 'Drop Count']

        # variable for extra categories for the CourseManager to create
        self.categories_to_create = []

        self.ACEditor = QtWidgets.QDialog()
        self.ui = uic.loadUi('AssignmentCategoryEditor.ui', self.ACEditor)
        self.ACEditor.categoryTable.setHorizontalHeaderLabels(col_headers)
        self.ACEditor.categoryTable.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

        for category in assignment_categories:
            row_insert = self.ACEditor.categoryTable.rowCount()
            self.add_category()
            self.ACEditor.categoryTable.setItem(row_insert, 0, QtWidgets.QTableWidgetItem(category.categoryName))
            self.ACEditor.categoryTable.setItem(row_insert, 1, QtWidgets.QTableWidgetItem(str(category.weight)))
            self.ACEditor.categoryTable.setItem(row_insert, 2, QtWidgets.QTableWidgetItem(str(category.dropCount)))

        self.original_row_count = self.ACEditor.categoryTable.rowCount() - 1

        self.ACEditor.addCategoryButton.clicked.connect(self.add_category)
        self.ACEditor.removeSelectedCategory.clicked.connect(self.remove_category)

        self.ACEditor.show()

    """
    Function to add a new row to our category table
    Parameters:
        None
    Returns:
        None
    """
    def add_category(self):
        self.ACEditor.categoryTable.insertRow(self.ACEditor.categoryTable.rowCount())


    """
        Function to remove the current row from the list of categories.
        Won't remove the first row (Attendance)
        Won't remove any of the original rows without confirmation from user
            This is due to the AssignmentCategory holding grades
        Parameters:
            None
        Returns:
            None    
    """
    def remove_category(self):
        row = self.ACEditor.categoryTable.currentRow()
        if row > self.original_row_count:
            self.ACEditor.categoryTable.removeRow(row)

    """
    Function for telling the user they entered bad input
    Parameters:
        window_text: (string) the name of the window
        error_message: (string) the error message that is displayed to the user
    """
    def bad_input(self, window_text, error_message):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = AssignmentCategoryEditor([AssignmentCategory("", "Attendance", 25, 0),
                                     AssignmentCategory("", "Tests", 60, 0),
                                     AssignmentCategory("", "Quizzes", 15, 0)])
    sys.exit(app.exec_())