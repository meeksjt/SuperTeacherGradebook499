from Grades import Grades

"""
    Class for each Assignment in the AssignmentCategoryBase
"""


class Assignment:
    """
        Constructor for the Assignment Class
        Instantiates an Assignment object
    """

    def __init__(self, assignment_uuid, assignment_name, total_points, student_list):
        self.assignmentID = assignment_uuid
        self.assignmentName = assignment_name
        self.totalPoints = total_points
        self.tableName = assignment_uuid + '_grades'
        self.studentList = student_list
        self.studentGrades = Grades()
        ###Jacob###
        #Need to create the grades table for this assignment if it doesn't already exist
        #If it does already exist, you need to load up the assignment with the grades for it

    """
        Function to get assignmentName for an Assignment
        Parameters:
            None
        Returns:
            assignmentName : (string) name of Assignment
    """
    def get_assignment_name(self):
        return self.assignmentName

    """
        Function to set assignmentName for an Assignment
        Parameters:
            new_assignment_name : (string) new name for the Assignment
        Returns:
            None
        Might need to add error checking to make sure duplicate assignment_names aren't used
    """
    def set_assignment_name(self, new_assignment_name):
        self.assignmentName = new_assignment_name

    """
        Function to get the totalPoints that an Assignment is worth 
        Parameters:
            None
        Returns:
            self.totalPoints : (float) the total points an Assignment is worth
    """
    def get_total_points(self):
        return self.totalPoints

    """
        Function to set the totalPoints that an Assignment is worth
        Parameters:
            new_total_points : (float) the total points an Assignment is worth
        Returns:
            None
    """
    def set_total_points(self, new_total_points):
        self.totalPoints = new_total_points

    """
        Function to get a specific Student's grade for the Assignment
        Parameters:
            student_id : (string) id of student we want to get Grade for
        Returns:
            grade : (float) grade of the student on this Assignment
    """
    def get_student_grade(self, student_id):
        grade = self.studentGrades.get_grade(student_id)
        return grade

    """
        Function to set a specific Student's grade for an Assignment
        Parameters:
            student_id : (string) id of the student we are setting the Grade for
            grade : (float) grade of the student on this Assignment
        Returns:
            None
    """
    def set_student_grade(self, student_id, grade):
        self.studentGrades.set_grade(student_id, grade)
