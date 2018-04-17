from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
import GlobalVariables

class EditingGradeDict(object):

    def __init__(self, course):

        self.EGDict = QtWidgets.QDialog()
        self.ui = uic.loadUi('../assets/ui/EditingGradeDict.ui', self.EGDict)

        self.course = course
        self.EGDict.gradeAField.setText(str(self.course.grade_scale.get_A_bottom_score()))
        self.EGDict.gradeBField.setText(str(self.course.grade_scale.get_B_bottom_score()))
        self.EGDict.gradeCField.setText(str(self.course.grade_scale.get_C_bottom_score()))
        self.EGDict.gradeDField.setText(str(self.course.grade_scale.get_D_bottom_score()))

        self.EGDict.show()

        self.EGDict.saveButton.clicked.connect(self.edit_grade_scale)

    def edit_grade_scale(self):

        gradeA = self.EGDict.gradeAField.text()
        gradeB = self.EGDict.gradeBField.text()
        gradeC = self.EGDict.gradeCField.text()
        gradeD = self.EGDict.gradeDField.text()

        if self.validate_user_input(gradeA, gradeB, gradeC, gradeD):
            self.course.grade_scale.set_grade_scale(gradeA, gradeB, gradeC, gradeD)
            self.EGDict.hide()

    def validate_user_input(self, gradeA, gradeB, gradeC, gradeD):

        # Check to make sure the user entered something
        if not (gradeA and gradeB and gradeC and gradeD):
            self.bad_input('Error', 'Make sure you enter in a number for each of the input fields')

        # Check to make sure user entered floats
        elif not (self.is_float(gradeA) and self.is_float(gradeB) and
                  self.is_float(gradeC) and self.is_float(gradeD)):
            self.bad_input('Error', 'Make sure you enter numbers!')

        # Check to make sure that the user entered unique values in a descending order
        else:
            grade_scale_list = [float(gradeA), float(gradeB),
                                float(gradeC), float(gradeD)]
            uniq_grade_scale_list = list(set(grade_scale_list))
            sorted_grade_scale_list = sorted(uniq_grade_scale_list, reverse=True)

            if sorted_grade_scale_list != grade_scale_list:
                self.bad_input('Error', 'Make sure your grade scales are correct!')
            else:
                return True
        return False

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
       Returns:
           None
       """

    def bad_input(self, window_text, error_message):
        choice = QtWidgets.QMessageBox.question(self.EGDict, window_text, error_message,
                                                QtWidgets.QMessageBox.Cancel)
        if choice:
            pass
