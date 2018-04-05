import sqlite3
import copy
from GlobalVariables import connection, cursor
#Status: Know how to INSERT and CREATE. Learn how to UPDATE, then how to
# SELECT and convert to an object.

class StudentList:
	"""Really just a wrapper for a list of Students"""
	def __init__(self, courseUUID):

		self.students = []
		#This holds the name of the course
		self.course = courseUUID
		self.tableName = courseUUID+"_student_list"
		cursor.execute("CREATE TABLE IF NOT EXISTS `"+self.tableName+"` (`uid`	TEXT,`ID`	INTEGER,`name`	TEXT,`email`	TEXT);")
		connection.commit()
		self.load_students()


	def set_email(self,id,email):
		for student in self.students:
			if student.id == id:
				print("Found one!")
				student.setEmail(email)
				self.load_students()

	def add_student(self,id,name,email):
		newStudent = Student(id, id,name,email)
		connection.execute(("INSERT INTO " + str(self.tableName) + " VALUES(" + str(newStudent.uuid) + "" + str(newStudent.id) + ", '" + str(newStudent.name) + "', '" + str(newStudent.email) + "')"))
		connection.commit()
		self.__add_student(newStudent)

	def __add_student(self,dstudent):
		self.students.append(copy.deepcopy(dstudent))

	def save_students(self):
		for student in self.students:
			student.save_student()

	def remove_student(self,id):
		for student in self.students:
			if student.id == id:
				student.remove_student()
				self.load_students()

	def load_students(self):
		self.students.clear() #Erase what's in the list
		cursor.execute("SELECT * FROM `" + self.tableName + "`")
		results = cursor.fetchall()
		for row in results:
			newStudent = Student(self.tableName, row[0], row[1], row[2])
			self.students.append(copy.deepcopy(newStudent))

	def print_students(self):
		for sstudent in self.students:
			sstudent.print_student()

class Student:
#Need to reload students after setting name.
	def __init__(self,tableName,id,name,email):
		self.tableName = tableName
		self.name = name
		self.email = email
		self.id = id

	#connection.execute("INSERT INTO cs499_studentList VALUES(1, 'Jacob Houck', 'jeh0029@uah.edu')")
	def set_email(self,email):
		self.email = email
		query = "UPDATE "+self.tableName+" SET email = '" + str(self.email) + "' WHERE id = '" + str(self.id) + "';"
		print(query)
		cursor.execute(query)
		connection.commit()

	def set_name(self,name):
		"""Tested"""
		self.name=name
		# I used a query to make it easier by creating our string, and just passing it to the cursor.
		query = "UPDATE "+self.tableName+" SET name = '" + str(self.name) + "' WHERE id = " + str(self.id) + ";"
		print(query)
		cursor.execute(query)
		connection.commit()

	def set_id(self,id):
		"""Sets ID in object and in database"""
		self.id=id

		query = "UPDATE "+self.tableName+" SET id = '" + str(self.id) + "' WHERE name = '" + str(self.name) + "';"
		print(query)
		cursor.execute(query)
		connection.commit()

	def save_student(self):
		"""Not needed, since set functions do this for us. Will be removed soon"""
		connection.execute("INSERT INTO " + str(self.tableName) + " VALUES(" + str(self.id) + ", '" + str(self.name) + "', '" + str(self.email) + "')")
		connection.commit()
		#This will save the student to the database.
		#Either UPDATE or INSERT here, depending on if the student exists or not.

	def print_student(self):
		print("\nName: ", self.name)
		print("ID: ", self.id)
		print("Email: ", self.email)

	def remove_student(self):
		query = "DELETE FROM "+self.tableName+" WHERE id = '" + str(self.id) + "';"
		print(query)
		cursor.execute(query)
		connection.commit()


def create_test_database():
	"""A simple testing function for just this class"""
	print("Entered testing function...")

	cursor.execute('CREATE TABLE IF NOT EXISTS `cs499_studentList` (`ID`	INTEGER,`name`	TEXT,`email`	TEXT);')
	connection.execute("INSERT INTO cs499_studentList VALUES(1, 'Jacob Houck', 'jeh0029@uah.edu')")
	connection.execute("INSERT INTO cs499_studentList VALUES(4, 'Matt', 'jeh0029@uah.edu')")
	connection.execute("INSERT INTO cs499_studentList VALUES(3, 'Tyler Meeks', 'yomoma@hotmail.com')")
	connection.execute("INSERT INTO cs499_studentList VALUES(2, 'Chris Christopher', 'chris42@uah.edu')")
	connection.commit()
#Remember to find memes for the presentation. Be sure to get a HP one.

students = StudentList("cs499")
students.add_student("1", "Tyler Meeks", "jtm0036@uah.edu")
#students.addStudent(id,name,email)
#students.removeStudent(id)
#students.students # This is an list you can iterate through, which has sets for email, id, and name.

#createTestDatabase()

#cursor.execute('SELECT * FROM `cs499studentList`')
#results = cursor.fetchall()
#createTestDatabase()
#for row in results:
#    newStudent = Student(row[0],row[1],row[2])
#    students.addStudent(newStudent)
#students.setEmail(1994, "fhouck8@hotmail.com")
#students.printStudents()
#students.setEmail(1, "!@#$%^&*(*&^%")
#x = input("What student do you want to change?")
#x = input("Enter a Student name: ")

#y = input("Enter a Student id: ")

#z = input("Enter a Student email: ")
#students.add_student(y,x,z)

#students.print_students()
#INSERT INTO `cs499_studentList`(`ID`,`name`,`email`) VALUES (NULL,NULL,NULL);
