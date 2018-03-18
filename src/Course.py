import re
from Student import *

class Course:

	def __init__(self, name, semester, section):
		#Need to know what to put here
		self.name = name
		self.section =section
		self.semester=semester
		self.table_name = re.sub('\W+', '_', (name+"_"+semester+"_"+section))
		#print("Course Name: "+self.table_name)

		#Change This Later.
		self.assignmentCategoryList = []

		self.gradeScale = dict()
		self.gradeScale["A"] = 90.0
		self.gradeScale["B"] = 80.0
		self.gradeScale["C"] = 70.0
		self.gradeScale["D"] = 60.0

		#Calls Student List, which creates all that garbage
		self.student_list = StudentList(self.table_name)
		#self.add_student("5","Matt","Email")

		pass

	def add_assignment(self):

		pass

	def drop_assignment(self):
		pass

	def add_student(self,id,name,email):
		self.student_list.add_student(id,name,email)
		pass

	def remove_student(self,id):
		self.student_list.remove_student(id)

	#What is this function for?
	def display_category(self):

		pass

	def set_grade_scale(self,a,b,c,d):
		self.gradeScale['A'] = a
		self.gradeScale['B'] = b
		self.gradeScale['C'] = c
		self.gradeScale['D'] = d


	def change_category_weight(self):
		pass
	def delete_course(self):
		#Will be implemented later
		pass

#funk = Course("CS 399", "Fall", "01")