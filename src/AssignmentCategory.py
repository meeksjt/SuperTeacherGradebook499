from Assignment import Assignment
from GlobalVariables import *
import copy
import re
"""
    Class to serve as our Base Class for various Assignment Categories
"""


class AssignmentCategory:
    """
        Constructor for AssignmentCategoryBase
    """
    def __init__(self, category_uuid, category_name, drop_count, student_list):
        self.categoryName = category_name

        self.category_uuid = category_uuid
        self.table_name = category_uuid + '_assignments'

        self.drop_count = drop_count
        self.student_list = student_list
        self.assignment_list = []

        self.total_category_points = 0

        # Need to check if table already exists
        # If it does, load the contents of that table into self.assignmentList by creating new
        # Assignment objects and reading in the grade tables for those Assignment objects


        #cursor.execute("CREATE TABLE IF NOT EXISTS `"+self.tableName+"` (`Name`	TEXT,`Points`	TEXT,`DropCount`	TEXT);")
        #connection.commit()
    """
    def __reloadCategory(self):
        #Loads a category list back.

        #FIX THIS JACOB

        self.course_list.clear()  # Erase what's in the list
        # Get everything in the table
        cursor.execute("SELECT * FROM `courseList`")
        # Our results go into this as a list, I think.
        results = cursor.fetchall()
        # Go through each row
        for row in results:
            # Here, we pass the Name, Semester, and Section to the Course object, and it creates it.
            newCategory = AssignmentCategory(row[0], row[1], row[2])
            self.course_list.append(copy.deepcopy(newCategory))
    """

    """
        Function to get the dropCount of the AssignmentCategory
        Parameters:
            None
        Returns:
            self.dropCount : (int) the number of assignments to be dropped from this category
    """

    def get_drop_count(self):
        return self.drop_count

    """
        Function to set the dropCount of the AssignmentCategory
        Parameters:
            new_drop_count : (int) the new drop count for this assignment category
        Returns:
            None
    """

    def set_drop_count(self, new_drop_count):
        self.drop_count = new_drop_count

    """
        Function to add a new Assignment to our assignmentList
        Parameters:
            assignment_name : (string) name of our new Assignment
            total : (float) total point value of the Assignment
            total_points : (float) total_points of the Assignment in the Assignment Category
    """

    def add_assignment(self, assignment_uuid, assignment_name, total_points, student_list):
        assignment = Assignment(assignment_uuid, assignment_name, total_points, student_list)
        self.assignment_list.append(assignment)

    """
        Function to delete an Assignment from our assignmentList
        Parameters:
            assignment_uuid : (string) uuid of our Assignment we are deleting
        Returns:
            None
    """

    def delete_assignment(self, assignment_uuid):
        for assignment in self.assignment_list:
            if assignment.assignmentID == assignment_uuid:
                self.assignment_list.remove(assignment)
                # Add the database deletion
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

        self.total_category_points = 0

        student_grades = []
        assignment_total_points = []
        assignment_score_deficits = []

        for assignment in self.assignment_list:
            grade = assignment.get_student_grade(student_id)
            student_grades.append(grade)
            total_points = assignment.get_total_points()
            assignment_total_points.append(total_points)
            assignment_score_deficits.append(total_points - grade)

        return self.drop_grades(student_grades.copy(), assignment_total_points.copy(), assignment_score_deficits.copy())

    """
        Function to calculate the student score after dropping appropriate assignments
        Parameters:
            student_grades: (list) list of student grades
            assignment_values: (list) list of assignment values
            assignment_scores: (list) list of weighted student grades
    """

    def drop_grades(self, student_grades, assignment_total_points, assignment_score_deficits):

        student_points = 0

        for i in range(self.drop_count):
            index = self.get_max_deficit(assignment_score_deficits)
            del student_grades[index]
            del assignment_total_points[index]
            del assignment_score_deficits[index]

        for i in range(len(student_grades)):
            student_points += student_grades[i]
            self.total_category_points += assignment_total_points[i]

        return student_points

    """
        Function to get the lowest score of a student for a particular list of scores
        Parameters:
            assignment_scores: (list) list of student scores
        Returns:
            min: (int) index of the lowest score in the student assignment list
    """
    def get_max_deficit(self, assignment_score_deficits):

        max = 0
        for i in assignment_score_deficits:
            if i > max:
                max = i

        return max
