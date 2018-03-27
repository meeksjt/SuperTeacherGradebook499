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

        self.ACEditor.categoryTable.item(0, 0).setFlags(QtCore.Qt.ItemIsEnabled)

        self.original_row_count = self.ACEditor.categoryTable.rowCount() - 1

        self.categories_to_create = []

        self.assignment_categories = assignment_categories

        self.ACEditor.addCategoryButton.clicked.connect(self.add_category)
        self.ACEditor.removeSelectedCategory.clicked.connect(self.remove_category)
        self.ACEditor.saveCategoriesButton.clicked.connect(self.save_table_data)

        self.ACEditor.show()

    """
    Function to add a new row to our category table
    Parameters:
        None
    Returns:
        None
    """
    def add_category(self):
        row_insert = self.ACEditor.categoryTable.rowCount()
        self.ACEditor.categoryTable.insertRow(self.ACEditor.categoryTable.rowCount())
        self.ACEditor.categoryTable.setItem(row_insert, 0, QtWidgets.QTableWidgetItem(""))
        self.ACEditor.categoryTable.setItem(row_insert, 1, QtWidgets.QTableWidgetItem(""))
        self.ACEditor.categoryTable.setItem(row_insert, 2, QtWidgets.QTableWidget(""))

    """
        Function to remove the current row from the list of categories.
        Won't remove the first row (Attendance)
        Won't remove any of the original rows
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

    def save_table_data(self):
        row_count = self.ACEditor.categoryTable.rowCount()
        output = []

        for row in range(0, row_count):
            cat_name = self.ACEditor.categoryTable.item(row, 0).text()
            cat_weight = self.ACEditor.categoryTable.item(row, 1).text()
            cat_drop_count = self.CCThird.categoryTable.item(row, 2).text()
            output.append([cat_name, cat_weight, cat_drop_count])

        valid = self.error_checking(output)

        if valid:
            for i in range(len(output)):
                if i < self.original_row_count:
                    # Need to add saving new fields to the database and to the course
                    # Need an assignment_category_list
                    pass

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
        category_weights = [user_input[j][1] for j in range(len(user_input))]
        category_drop_counts = [user_input[k][2] for k in range(len(user_input))]

        for i in category_names:
            if i == "":
                self.bad_input('Error', 'Please enter a category name for all categories')
                return False

        # check the drop counts
        for i in category_drop_counts:
            try:
                x = int(i.strip())
                if x < 0:
                    return False
            except ValueError:
                self.bad_input('Error', 'You have a drop count that is not a nonnegative integer.  Please try again.')
                return False

        # Check category weights
        point_sum = 0
        for i in category_weights:
            # Make sure we are adding numbers
            try:
                point_sum += float(i.strip())
            except ValueError:
                self.bad_input('Error', 'Category Weights need to be numerical values!')
                return False

        return True

    """
    Function for telling the user they entered bad input
    Parameters:
        window_text: (string) the name of the window
        error_message: (string) the error message that is displayed to the user
    """
    def bad_input(self, window_text, error_message):
        choice = QtWidgets.QMessageBox.question(self.ACEditor, window_text, error_message,
                                                QtWidgets.QMessageBox.Cancel)
        if choice:
            pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = AssignmentCategoryEditor([AssignmentCategory("", "Attendance", 25, 0),
                                     AssignmentCategory("", "Tests", 60, 0),
                                     AssignmentCategory("", "Quizzes", 15, 0)])
    sys.exit(app.exec_())