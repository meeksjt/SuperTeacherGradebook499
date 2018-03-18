from Assignment import Assignment
from GlobalVariables import *
import re
"""
	Class to serve as our Base Class for various Assignment Categories
"""


class AssignmentCategoryBase:
	"""
		Constructor for AssignmentCategoryBase
	"""
	def __init__(self,tableName, categoryName, weight, drop_count):
		self.tableName=tableName+re.sub('\W+', '_',categoryName)
		print(self.tableName)
		self.weight = weight
		self.dropCount = drop_count
		self.assignmentList = []
		cursor.execute("CREATE TABLE IF NOT EXISTS `"+self.tableName+"` (`Name`	TEXT,`Semester`	TEXT,`Section`	TEXT);")
		connection.commit()

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

	def add_assignment(self, assignment_name, totalPoints, weight):
		assignment = Assignment(assignment_name, totalPoints, weight)
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
			weight = assignment.get_weight()
			total_points = assignment.get_total_points()
			assignment_values.append(total_points)
			assignment_scores.append((grade / total_points) * weight)

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

		return (student_points / total_points) * self.weight

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

jacob = AssignmentCategoryBase("CS499_", "Homework", "25", "0")

