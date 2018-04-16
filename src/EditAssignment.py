from PyQt5 import QtCore, QtWidgets, uic
import sys
from AssignmentCategoryDict import AssignmentCategoryDict
from Student import StudentList

"""
This is the class that deals with editing a previously created Assignment
"""

class EditAssignment(object):

    def __init__(self, assignment_uuid, assignment_category, studentList):
        self.EAssignment = QtWidgets.QDialog()
        self.ui = uic.loadUi('../assets/ui/EditAssignment.ui', self.EAssignment)
        self.EAssignment.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.EAssignment.show()

        self.assignment_uuid = assignment_uuid
        self.assignmentCategory = assignment_category
        self.studentList = studentList

        self.EAssignment.saveAssignmentButton.clicked.conncect(self.edit_assignment)
        self.EAssignment.exec()

    def edit_assignment(self):
        name = self.EAssignment.assignmentNameField.text()
        points = self.EAssignment.assignmentPointsField.text()

        if not name and not points:
            self.assignmentCategory.assignment_dict[self.assignment_uuid].set_assignment_name(name)
            self.assignmentCategory.assignment_dict[self.assignment_uuid].set_total_points(points)
