from Assignment import Assignment
"""
	Class to serve as our Base Class for various Assignment Categories
"""


class AssignmentCategoryBase:
    """
        Constructor for AssignmentCategoryBase
    """
    def __init__(self, weight, drop_count):
        self.weight = weight
        self.dropCount = drop_count
        self.assignmentList = []

    """
        Function to get the weight of the AssignmentCategory
        Parameters:
            None
        Returns:
            self.weight : (float) the weight of the category
    """

    def get_category_weight(self):
        return self.weight

    """
        Function to set the weight of the AssignmentCategory
        Parameters:
            new_weight : (float) the new weight of the AssignmentCategory
        Returns:
            None
    """

    def set_category_weight(self, new_weight):
        self.weight = new_weight

    """
        Function to get the dropCount of the AssignmentCategory
        Parameters:
            None
        Returns:
            self.dropCount : (int) the number of assignments to be dropped from this category
    """

    def get_drop_count(self):
        return self.dropCount

    """
        Function to set the dropCount of the AssignmentCategory
        Parameters:
            new_drop_count : (int) the new drop count for this assignment category
        Returns:
            None
    """

    def set_drop_count(self, new_drop_count):
        self.dropCount = new_drop_count

    """
        Function to add a new Assignment to our assignmentList
        Parameters:
            assignment_name : (string) name of our new Assignment
            total : (float) total point value of the Assignment
            weight : (float) weight of the Assignment in the Assignment Category
    """

    def add_assignment(self, assignment_name, total, weight):
        assignment = Assignment(assignment_name, total, weight)
        self.assignmentList.append(assignment)

    """
        Function to delete an Assignment from our assignmentList
        Parameters:
            assignment_name : (string) name of our Assignment we are deleting
        Returns:
            None
    """

    def delete_assignment(self, assignment_name):
        for assignment in self.assignmentList:
            if assignment.assignmentName == assignment_name:
                self.assignmentList.remove(assignment)
                break

    """
        Function to get the student grade for this particular AssignmentCategory
        Accounts for the dropCount for that category
        Parameters:
            student_id : id of student that we are wanting to get the grade of
        Returns:
            None
    """

    def get_student_category_grade(self, student_id):

        student_points = 0
        total_points = 0

        for assignment in self.assignmentList:
            student_grade = assignment.get_student_grade(student_id)
            assignment_weight = assignment.get_weight()
            assignment_value = assignment.get_total_points()
            total_points += assignment_value
            student_points += (student_grade / assignment_value) * assignment_weight

        return (student_points / total_points) * self.weight


    def get_dropped_assignments(self, student_id):

        assignment_grades = {}

        for assignment in self.assignmentList:
            student_grade = assignment.get_student_grade(student_id)
            assignment_weight = assignment.get_weight()
            assignment_value = assignment.get_total_points()
            assignment_grades[assignment.get_assignment_name()] = \
                ((student_grade / assignment_value) * assignment_weight)




