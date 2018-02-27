import sqlite3
import copy
from GlobalVariables import connection, cursor
#Status: Know how to INSERT and CREATE. Learn how to UPDATE, then how to
# SELECT and convert to an object.

class StudentList:
    """Really just a wrapper for a list of Students"""
    def __init__(self, course):
        self.students = []
        self.course = course
		
    def setEmail(self,id,email):
        for student in self.students:
            if student.id == id:
                print("Found one!")
                student.setEmail(email)
		
    def addStudent(self,dstudent):
        self.students.append(copy.deepcopy(dstudent))
    def removeStudent(self,id):
        for student in self.students:
            if student.id == id:
                student.removeStudent()
                self.loadStudents()
    def loadStudents(self):
        self.students.clear() #Erase what's in the list
        cursor.execute("SELECT * FROM `" + self.course + "`")
        results = cursor.fetchall()
        for row in results:
            newStudent = Student(row[0], row[1], row[2])
            self.students.append(copy.deepcopy(newStudent))
    def printStudents(self):
        for sstudent in self.students:
            sstudent.printStudent()

class Student:
#Need to reload students after setting name.
    def __init__(self,id,name,email):
        self.name = name
        self.email = email
        self.id = id
    def setEmail(self,email):
        self.email = email
        query = "UPDATE cs499_studentList SET email = '" + str(self.email) + "' WHERE id = '" + str(self.id) + "';"
        print(query)
        cursor.execute(query)
        connection.commit()
    def setName(self,name):
        """Tested"""
        self.name=name
        query = "UPDATE cs499_studentList SET name = '" + str(self.name) + "' WHERE id = " + str(self.id) + ";"
        print(query)
        cursor.execute(query)
        connection.commit()
    def setID(self,id):
        """Sets ID in object and in database"""
        self.id=id

        query = "UPDATE cs499_studentList SET id = '" + str(self.id) + "' WHERE name = '" + str(self.name) + "';"
        print(query)
        cursor.execute(query)
        connection.commit()
    def saveStudent(self):
        """Not needed, since set functions do this for us. Will be removed soon"""
        print("Function not implemented yet.")
        #This will save the student to the database.
        #Either UPDATE or INSERT here, depending on if the student exists or not.
    def printStudent(self):
        print("\nName: ", self.name)
        print("ID: ", self.id)
        print("Email: ", self.email)
    def removeStudent(self):
        query = "DELETE FROM cs499_studentList WHERE id = '" + str(self.id) + "';"
        print(query)
        cursor.execute(query)
        connection.commit()


def createTestDatabase():
    """A simple testing function for just this class"""
    print("Entered testing function...")

    cursor.execute('CREATE TABLE IF NOT EXISTS `cs499_studentList` (`ID`	INTEGER,`name`	TEXT,`email`	TEXT);')
    connection.execute("INSERT INTO cs499_studentList VALUES(1, 'Jacob Houck', 'jeh0029@uah.edu')")
    connection.execute("INSERT INTO cs499_studentList VALUES(4, 'Matt', 'jeh0029@uah.edu')")
    connection.execute("INSERT INTO cs499_studentList VALUES(3, 'Tyler Meeks', 'yomoma@hotmail.com')")
    connection.execute("INSERT INTO cs499_studentList VALUES(2, 'Chris Christopher', 'chris42@uah.edu')")
    connection.commit()
#Remember to find memes for the presentation. Be sure to get a HP one.

students = StudentList("cs499_studentList")
#createTestDatabase()

cursor.execute('SELECT * FROM `cs499_studentList`')
results = cursor.fetchall()
createTestDatabase()
for row in results:
    newStudent = Student(row[0],row[1],row[2])
    students.addStudent(newStudent)
students.setEmail(1994, "fhouck8@hotmail.com")
#x = input("What student do you want to change?")

students.printStudents()
#INSERT INTO `cs499_studentList`(`ID`,`name`,`email`) VALUES (NULL,NULL,NULL);
