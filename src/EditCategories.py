from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from AssignmentCategoryDict import AssignmentCategoryDict
from Assignment import Assignment
import uuid

class EditCategories(object):

    def __init__(self, course):

        col_headers = ['Category Name', 'Drop Count']

        self.ECategories = QtWidgets.QDialog()
        self.ui = uic.loadUi('../assets/ui/EditCategories.ui', self.ECategories)
        self.ECategories.categoryTable.setHorizontalHeaderLabels(col_headers)

        self.course = course
        self.ECategories.show()
        self.category_uuids = []
        self.setup_display()

        self.original_row_count = self.ECategories.categoryTable.rowCount()

        self.ECategories.removeSelectedCategoryButton.clicked.connect(self.remove_category)
        self.ECategories.addCategoryButton.clicked.connect(self.add_category)
        self.ECategories.saveCategoriesButton.clicked.connect(self.save_table_data)

    def setup_display(self):
        for category in self.course.assignment_category_dict.assignment_categories.values():
            row_insert = self.ECategories.categoryTable.rowCount()
            self.add_category()
            self.ECategories.categoryTable.setItem(row_insert, 0, QtWidgets.QTableWidgetItem(category.categoryName))
            self.ECategories.categoryTable.setItem(row_insert, 1, QtWidgets.QTableWidgetItem(category.drop_count))
            print(category.category_uuid)
            self.category_uuids.append(category.category_uuid)

    def add_category(self):
        row_insert = self.ECategories.categoryTable.rowCount()
        self.ECategories.categoryTable.insertRow(self.ECategories.categoryTable.rowCount())
        self.ECategories.categoryTable.setItem(row_insert, 0, QtWidgets.QTableWidgetItem(""))
        self.ECategories.categoryTable.setItem(row_insert, 1, QtWidgets.QTableWidgetItem(""))

    def remove_category(self):
        row = self.ECategories.categoryTable.currentRow()
        if row > self.original_row_count:
            self.ECategories.categoryTable.removeRow(row)
        else:
            choice = QtWidgets.QMessageBox.question(self.ECategories, "Warning",
                                                    "You are about to delete one of your original categories.  Continue?",
                                                    QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
            if choice == QtWidgets.QMessageBox.Yes:
                cat_to_delete_uuid = self.category_uuids[row]
                self.course.assignment_category_dict.delete_category(self.course, cat_to_delete_uuid)
                self.original_row_count = self.original_row_count - 1
                del self.category_uuids[row]
                self.ECategories.categoryTable.removeRow(row)

    def save_table_data(self):
        row_count = self.ECategories.categoryTable.rowCount()
        output = []
        for row in range(0, row_count):
            cat_name = self.ECategories.categoryTable.item(row, 0).text()
            cat_drop_count = self.ECategories.categoryTable.item(row, 1).text()
            output.append([cat_name, cat_drop_count])

        valid = self.error_checking(output)

        if valid:
            for i in range(len(output)):
                if i < self.original_row_count:
                    self.course.assignment_category_dict.save_category_info(output[i][0], output[i][1], self.category_uuids[i])
                    # Add the database update function
                else:
                    self.course.assignment_category_dict.add_category(str(uuid.uuid4()), output[i][0], output[i][1], self.course.student_list)
                    # Add the database create function

    def error_checking(self, user_input):

        category_names = [user_input[i][0] for i in range(len(user_input))]
        category_drop_counts = [user_input[i][1] for i in range(len(user_input))]

        for i in category_names:
            if i == "":
                self.bad_input('Error', 'Please enter a category name for all categories')
                return False

        for i in category_drop_counts:

            if "." in i:
                return False

            try:
                x = int(i.strip())
                if x < 0:
                    return False
            except ValueError:
                self.bad_input('Error', 'You have a drop count that is a nonnegative integer.  Please try again.')
                return False

        return True
    """
        Function for telling the user they entered bad input
        Parameters:
            window_text: (string) the name of the window
            error_message: (string) the error message that is displayed to the user
    """

    def bad_input(self, window_text, error_message):
        choice = QtWidgets.QMessageBox.question(self.ECategories, window_text, error_message,
                                                QtWidgets.QMessageBox.Cancel)
        if choice:
            pass