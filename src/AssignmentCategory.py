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
    def __init__(self, id, categoryName, total_points, drop_count):
        self.categoryName = categoryName

        # put id stuff here
        #self.tableName = tableName+re.sub('\W+', '_',categoryName)
        self.tableName = id

        self.total_points = total_points
        self.dropCount = drop_count
        self.assignmentList = []
        cursor.execute("CREATE TABLE IF NOT EXISTS `"+self.tableName+"` (`Name`	TEXT,`Points`	TEXT,`DropCount`	TEXT);")
        connection.commit()

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
        Function to get the total_points of the AssignmentCategory
        Parameters:
            None
        Returns:
            self.total_points : (float) the total_points of the category
    """

    def get_category_total_points(self):
        return self.total_points

    """
        Function to set the total_points of the AssignmentCategory
        Parameters:
            new_total_points : (float) the new total_points of the AssignmentCategory
        Returns:
            None
    """

    def set_category_total_points(self, new_total_points):
        self.total_points = new_total_points

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
            total_points : (float) total_points of the Assignment in the Assignment Category
    """

    def add_assignment(self, assignment_name, totalPoints, total_points):
        assignment = Assignment(assignment_name, totalPoints, total_points)
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

        student_grades = []
        assignment_values = []
        assignment_scores = []

        for assignment in self.assignmentList:
            grade = assignment.get_student_grade(student_id)
            student_grades.append(grade)
            total_points = assignment.get_total_points()
            assignment_values.append(total_points)
            assignment_scores.append((grade / total_points) * total_points)

        return self.drop_grades(student_grades, assignment_values, assignment_scores)

    """
        Function to calculate the student score after dropping appropriate assignments
        Parameters:
            student_grades: (list) list of student grades
            assignment_values: (list) list of assignment values
            assignment_scores: (list) list of weighted student grades
    """

    def drop_grades(self, student_grades, assignment_values, assignment_scores):

        student_points = 0
        total_points = 0

        for i in range(self.dropCount):
            index = self.get_min_score(assignment_scores)
            del student_grades[i]
            del assignment_values[i]
            del assignment_scores[i]

        for i in range(len(student_grades)):
            student_points += student_grades[i]
            total_points += assignment_values[i]

        return (student_points / total_points) * self.total_points

    """
        Function to get the lowest score of a student for a particular list of scores
        Parameters:
            assignment_scores: (list) list of student scores
        Returns:
            min: (int) index of the lowest score in the student assignment list
    """

    def get_min_score(self, assignment_scores):

        min = 0
        for i in assignment_scores:
            if i < min:
                min = i

        return min

