
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
            student_id: (int) id of the Student we want to change the grade for
            grade: (float) grade that we want to give the Student
        Returns:
            Nothing
    """
    def set_grade(self, student_id, grade):
        self.assignmentGrades[student_id] = grade

    """
        Function to get the grade for a particular Student
        Parameters:
            student_id: (int) id of the Student we want to get the grade for
    """
    def get_grade(self, student_id):
        return self.assignmentGrades[student_id]
