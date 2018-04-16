from PyQt5 import QtCore, QtWidgets, uic

"""
This is the class that deals with editing a previously created Assignment
"""

class EditAssignment(object):

    def __init__(self, assignment_name, assignment_points, assignment_uuid, assignment_category, studentList):
        self.EAssignment = QtWidgets.QDialog()
        self.ui = uic.loadUi('../assets/ui/EditAssignment.ui', self.EAssignment)
        self.EAssignment.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.EAssignment.show()

        self.assignment_uuid = assignment_uuid
        self.assignmentCategory = assignment_category
        self.studentList = studentList

        self.EAssignment.assignmentNameField.setText(assignment_name)
        self.EAssignment.assignmentPointsField.setText(assignment_points)

        self.EAssignment.saveAssignmentButton.clicked.connect(self.edit_assignment)
        self.EAssignment.exec()

    def edit_assignment(self):
        name = self.EAssignment.assignmentNameField.text()
        points = self.EAssignment.assignmentPointsField.text()

        if name and points:
            self.assignmentCategory.set_assignment_name(self.assignment_uuid, name)
            self.assignmentCategory.set_assignment_total_points(self.assignment_uuid, points)
            self.assignmentCategory.reload_assignments()

        self.EAssignment.hide()

