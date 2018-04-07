from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
import time
from AssignmentCategory import AssignmentCategory
from GlobalVariables import *

"""
This is the class used for the third part of creating the course
It allows the user to both create the categories for the course
"""


class CourseCreationThird(object):

    """
    Constructor for CourseCreationThird
    """
    def __init__(self):

        # Table column headers
        col_headers = ['Category Name', 'Drop Count']

        # variable for categories for the CourseManager to create
        self.categories_to_create = []

        self.CCThird = QtWidgets.QDialog()
        self.ui = uic.loadUi('CourseCreationThird.ui', self.CCThird)
        self.CCThird.categoryTable.setHorizontalHeaderLabels(col_headers)
        self.CCThird.categoryTable.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)

        self.CCThird.exec()

        # Link our buttons
        self.CCThird.addCategoryButton.clicked.connect(self.add_category)
        self.CCThird.removeSelectedCategory.clicked.connect(self.remove_category)
        self.CCThird.createCourseButton.clicked.connect(self.save_table_data)

    """
        Function to remove the current row from the list of categories
        Parameters:
            None
        Returns:
            None
    """
    def remove_category(self):
        row = self.CCThird.categoryTable.currentRow()
        self.CCThird.categoryTable.removeRow(row)

    """
    Function to add a new row to our category table
    Parameters:
        None
    Returns:
        None
    """
    def add_category(self):
        row_insert = self.CCThird.categoryTable.rowCount()
        self.CCThird.categoryTable.insertRow(self.CCThird.categoryTable.rowCount())
        self.CCThird.categoryTable.setItem(row_insert, 0, QtWidgets.QTableWidgetItem(""))
        self.CCThird.categoryTable.setItem(row_insert, 1, QtWidgets.QTableWidgetItem(""))

    """
    Function to try to save our data to create new AssignmentCategories
    Parameters:
        None
    Returns:
        None
    """
    def save_table_data(self):
        row_count = self.CCThird.categoryTable.rowCount()
        output = []

        # Loop through and get data from the table
        for row in range(0, row_count):
            cat_name = self.CCThird.categoryTable.item(row, 0).text()
            cat_drop_count = self.CCThird.categoryTable.item(row, 1).text()
            output.append([cat_name, cat_drop_count])

        # Make sure that our data is valid
        valid = self.error_checking(output)

        # Add the assignmentcategorylist creation here if valid is valid
        if valid:
            for category in output:
                # This is the class variable that the Course will user to create its new categories
                self.categories_to_create.append(category[:].copy())
            self.CCThird.hide()

    """
    Function to do error checking on our input
    Parameters:
        user_input: (list of lists) the category table data
    Returns:
        True if the category table data is valid, False otherwise
    """
    def error_checking(self, user_input):

        # variables for the names, weights, and drop counts of each category
        category_names = [user_input[i][0] for i in range(len(user_input))]
        category_drop_counts = [user_input[j][1] for j in range(len(user_input))]

        for i in category_names:
            if i == "":
                self.bad_input('Error', 'Please enter a category name for all categories')
                return False

        # check the drop counts
        for i in category_drop_counts:

            if "." in i:
                return False

            try:
                x = int(i.strip())
                if x < 0:
                    return False
            except ValueError:
                self.bad_input('Error', 'You have a drop count that is not a nonnegative integer.  Please try again.')
                return False

        # global is_course_creation_wizard_complete
        # is_course_creation_wizard_complete = True

        return True

    """
    Function for telling the user they entered bad input
    Parameters:
        window_text: (string) the name of the window
        error_message: (string) the error message that is displayed to the user
    """

    def bad_input(self, window_text, error_message):
        choice = QtWidgets.QMessageBox.question(self.CCThird, window_text, error_message,
                                                QtWidgets.QMessageBox.Cancel)
        if choice:
            pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = CourseCreationThird()
    sys.exit(app.exec_())
