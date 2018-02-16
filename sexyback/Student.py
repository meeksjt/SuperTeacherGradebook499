import sqlite3
#Status: Know how to INSERT and CREATE. Learn how to UPDATE, then how to
# SELECT and convert to an object.

class Student:
    def __init__(self):
        self.name = "Harry Potter"
        self.email = "HP@Hotmail.com"
        self.id = 42
    def setEmail(self,email):
        self.email = email

    def setName(self,name):
        self.name=name

    def setID(self,id):
        self.id=id

    def saveStudent(self):
        """Saves the student to the database"""
        print("Function not implemented yet.")
        #This will save the student to the database.
        #Either UPDATE or INSERT here, depending on if the student exists or not.


def testStudent():
    """A simple testing function for just this class"""
    print("Entered testing function...")
    connection = sqlite3.connect('jacobstest.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS `cs499_studentList` (`ID`	INTEGER,`name`	TEXT,`email`	TEXT);')
    connection.execute("INSERT INTO cs499_studentList VALUES(42, 'Jacob Houck', 'jeh0029@uah.edu')")
    connection.commit()
#Remember to find memes for the presentation. Be sure to get a HP one.

testStudent()

#INSERT INTO `cs499_studentList`(`ID`,`name`,`email`) VALUES (NULL,NULL,NULL);
