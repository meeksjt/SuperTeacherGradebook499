# Finished
"""
   Class to hold Grades for a particular Assignment
"""


class Grades:

    """
        Constructor for Grades class.
        Instantiates an empty dictionary for mapping StudentIDs to grades.
        Parameters: None
        Returns: None
    """
    def __init__(self):
        self.assignmentGrades = {}

    """
        Function to set the grade for a particular Student
        Parameters:
            student_id: (string) id of the Student we want to change the grade for
            grade: (float) grade that we want to give the Student
        Returns:
            Nothing
    """
    def set_grade(self, student_id, grade):
        self.assignmentGrades[student_id] = grade

    """
        Function to get the grade for a particular Student
        Parameters:
            student_id: (string) id of the Student we want to get the grade for
        Return:
            self.assignmentGrades[student_id] - (string) student grade
    """
    def get_grade(self, student_id):
        #return self.assignmentGrades[student_id]
        try:
            return self.assignmentGrades[student_id]
        except:
            self.assignmentGrades[student_id] = "-"
            return "-"

    """
        Function to clear the grades for an Assignment
        Parameters:
            None
        Returns:
            None
    """
    def clear_grades(self):
        self.assignmentGrades.clear()
