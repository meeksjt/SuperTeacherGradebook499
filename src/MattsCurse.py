import sqlite3
import copy
import re
from GlobalVariables import connection, cursor

class Course:

	# Just giving it default values, not sure if I should do this, probably not
	def __init__(self,name,semester,section):
		self.name = name
		self.section = section
		self.semester = semester
		self.tableName = self.tableName = re.sub('\W+', '_', (name+"_"+semester+"_"+section))
		cursor.execute("CREATE TABLE IF NOT EXISTS `"+self.tableName+"` (`ID`	INTEGER,`name`	TEXT,`section`	TEXT, 'semester'    TEXT);")

	# Not sure I am thinking about this correctly, but the create function must center around user input, right?
	# So, basically I am just imagining there are field boxes and when they want to create a course they are just typing the info in each box
	def create(self):
		print ("Fill out the fields to create a new course.")
		newCourse = Course()

	# ID field
		id = input("Course ID: ")
		newCourse.id = id

	# Course name field
		name = input("Course name: ")
		newCourse.name = name

	# Course section field
		section = input("Course section: ")
		newCourse.section = section

	# Course semester field
		semester = input("Course semester: ")
		newCourse.semester = semester

	# Insert the new values into the database
		connection.execute("INSERT INTO " + str(self.tableName) + " VALUES('" + str(newCourse.id) + "', '" + str(newCourse.name) + "', '" + str(newCourse.section) + "', '" + str(newCourse.semester) + "')")
		connection.commit()
		newCourse.setName("Yo Mama")
		newCourse.setSection("FAll")
		#newCourse.setID("353")
		newCourse.setSection("01")
	def create(self):
		print ("Fill out the fields to create a new course.")
		newCourse = Course()

	# ID field
		id = input("Course ID: ")
		newCourse.id = id

	# Course name field
		name = input("Course name: ")
		newCourse.name = name

	# Course section field
		section = input("Course section: ")
		newCourse.section = section

	# Course semester field
		semester = input("Course semester: ")
		newCourse.semester = semester

	# Insert the new values into the database
		connection.execute("INSERT INTO " + str(self.tableName) + " VALUES('" + str(newCourse.id) + "', '" + str(newCourse.name) + "', '" + str(newCourse.section) + "', '" + str(newCourse.semester) + "')")
		connection.commit()
		newCourse.setName("Yo Mama")
		newCourse.setSection("FAll")
		#newCourse.setID("353")
		newCourse.setSection("01")

# Does not work
# def delete(self):
# courseToDelete = input("Enter name of course to delete: ")
# cursor.execute("DELETE FROM " + str(self.tableName) + " WHERE courseToDelete = name")

# Prints the contents of the database, that is a list of all the course for this particular user
	def printCourseTable(self):
		cursor.execute("SELECT * FROM " + str(self.tableName) + "")
		print(cursor.fetchall())

	# Just followed Jacob's lead on these


	#def setID(self, id):
	#	self.id = id
	#	query = "UPDATE " + self.tableName + " SET id = '" + str(self.id) + "' WHERE name = '" + str(self.name) + ";"
	#	print(query)
	#	cursor.execute(query)
	#	connection.commit()


	def setName(self, name):
		self.name = name
		query = "UPDATE " + self.tableName + " SET Name = '" + str(self.name) + "' WHERE id = '" + str(self.id) + "';"
		print(query)
		cursor.execute(query)
		connection.commit()


	def setSection(self, section):
		self.section = section
		query = "UPDATE " + self.tableName + " SET section = '" + str(self.section) + "' WHERE id = '" + str(self.id) + "';"
		print(query)
		cursor.execute(query)
		connection.commit()


	def setSemester(self, semester):
		self.semester = semester
		query = "UPDATE " + self.tableName + " SET semester = '" + str(self.semester) + "' WHERE id = " + str(self.id) + ";"
		print(query)
		cursor.execute(query)
		connection.commit()


course = Course("Intro To C","Fall 2015", "02")
course.create()
course.printCourseTable()