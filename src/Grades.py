import re

"""
   Holds one grade.
   May have a testGrade and a actualGrade, and have a setGrade function to test a grade,
   and a saveGrade function to save the grade to the database.
"""


class Grades:


    def __init__(self):
    # We HAVE to have the StudentID, or we have no way of accessing the grade from the database.
		self.assignment_grades = {}


	def set_grade(self, student_id, grade):
		self.assignment_grades[student_id] = grade


	#Just returns the grade
	def get_grade(self, student_id):
		return self.grade
	
	#Call this when you want to save the grade to the database
	def s
	
#Holds all the grades for one assignment
#basically an advanced List, a la AssignmentList
class GradeList:
	#Needs these three variables to compute the name of the database table.
	#Includes CategoryName to avoid collision between categories
	def __init__(self, courseName, assignmentCategoryName, assignmentName):
		self.tableName = courseName+assignmentCategoryName+assignmentName
		self.tableName = re.sub('[^A-Za-z0-9]+', '', self.tableName)
		self.gradeList = []
	def setGrade(self,id,grade):
		for grad in self.gradeList:
			if grad.id == id:
				grad.setGrade(grade)
			else:
				self.gradeList.append(Grade(id, grade,self.tableName))
stuff = GradeList("CS499", "Tests", "Test1")
