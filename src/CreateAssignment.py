from PyQt5 import QtCore, QtWidgets, QtGui, uic
import GlobalVariables
import sys
import sqlite3
from sqlite3 import Error
from AssignmentCategory import AssignmentCategory
from AssignmentCategoryDict import AssignmentCategoryDict
from Student import StudentList
import uuid

"""
This is the class that deals with creating a new Assignment
"""


class CreateAssignment(object):

    def __init__(self, assignment_category_list, studentList):
        self.CAssignment = QtWidgets.QDialog()
        self.ui = uic.loadUi('../assets/ui/CreateAssignment.ui', self.CAssignment)
        self.CAssignment.show()

        self.studentList = studentList

        self.assignmentCategoryList = assignment_category_list

        for category in self.assignmentCategoryList.assignment_categories:
            self.CAssignment.assignmentCategoryDropdown.addItem(category.categoryName)

        self.CAssignment.createAssignmentButton.clicked.connect(self.add_assignment)

        self.CAssignment.exec()

    def add_assignment(self):

        category = str(self.CAssignment.assignmentCategoryDropdown.currentText())
        name = self.CAssignment.assignmentNameField.text()
        points = self.CAssignment.assignmentPointsField.text()

        if not name or not points:
            self.bad_input("Error", "Make sure you enter values for your assignment name and point values")

        if self.is_float(points):
            point_value = float(points)
            new_assignment_category = self.assignmentCategoryList.get_category(category)
            new_assignment_category.add_assignment(str(uuid.uuid4()), name, point_value, self.studentList)

    """
    Function to make sure that the string input can be turned into a float
    Parameters:
        None
    Returns:
        True if the string is a float, False otherwise
    """
    def is_float(self, s):

        try:
            float(s)
            return True
        except ValueError:
            return False


    """
        Function for telling the user they entered bad input
        Parameters:
            window_text: (string) the name of the window
            error_message: (string) the error message that is displayed to the user
    """

    def bad_input(self, window_text, error_message):
        choice = QtWidgets.QMessageBox.question(self.CAssignment, window_text, error_message,
                                                QtWidgets.QMessageBox.Cancel)
        if choice:
            pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    sl = StudentList('testingtesting')
    r = AssignmentCategoryDict('testingtesting', sl)
    x = CreateAssignment(r, sl)
    sys.exit(app.exec_())
