from AssignmentCategory import *
import GlobalVariables
import copy
import re


class AssignmentCategoryManager:
	def __init__(self, tableName, categoryName, weight, drop_count):
		self.tableName = tableName+re.sub('\W+', '_',categoryName)
		self.weight = weight
		self.dropCount = drop_count
		self.assignmentList = []
		GlobalVariables.database.cursor.execute("CREATE TABLE IF NOT EXISTS `"+self.tableName+"` (`Name`	TEXT,`Weight`	TEXT,`DropCount`	TEXT);")
		GlobalVariables.database.connection.commit()

	"""
		Function for reloading a category
		Parameters:
			None
		Returns:
			None
	"""
	def __reloadCategory(self):
		# Loads a category list back.
		self.course_list.clear()  # Erase what's in the list
		# Get everything in the table
		GlobalVariables.database.cursor.execute("SELECT * FROM `courseList`")
		# Our results go into this as a list, I think.
		results = GlobalVariables.database.cursor.fetchall()
		# Go through each row
		for row in results:
			# Here, we pass the Name, Semester, and Section to the Course object, and it creates it.
			newCategory = AssignmentCategory(row[0], row[1], row[2])
			self.course_list.append(copy.deepcopy(newCategory))

jacob = AssignmentCategoryManager("CS499_", "Homework", "25", "0")