import GlobalVariables
import copy
import uuid

"""Really just a wrapper for a list of Students"""
class StudentList:
    def __init__(self, courseUUID):
        self.students = []
        self.course = courseUUID
        self.tableName = str(courseUUID) + "_student_list"
        GlobalVariables.database.execute("CREATE TABLE IF NOT EXISTS '" + self.tableName + "' (uuid TEXT, ID TEXT, name TEXT, email TEXT);")
        self.load_students()

    def set_email(self,uuid,email):
        for student in self.students:
            if student.uuid == uuid:
                print("Found one!")
                student.set_email(email)
                self.load_students()

    def set_name(self,uuid,name):
        for student in self.students:
            if student.uuid == uuid:
                print("Found one!")
                student.set_name(name)
                self.load_students()

    def set_id(self,uuid,id):
        for student in self.students:
            if student.uuid == uuid:
                print("Found one!")
                student.set_id(id)
                self.load_students()

    def get_name(self,uuid):
        for student in self.students:
            if student.uuid == uuid:
                return student.get_name()

    def get_email(self,uuid):
        for student in self.students:
            if student.uuid == uuid:
                return student.get_email()

    def get_id(self,uuid):
        for student in self.students:
            if student.uuid == uuid:
                return student.get_id()

    def get_uuid_from_name(self, name):
        for student in self.students:
            if student.name == name:
                return student.uuid

    def add_student(self, student):
        GlobalVariables.database.add_student(student)

    def add_student_and_create_object(self,uuid,id,name,email):
        newStudent = Student(self.tableName, id, name, email, uuid)
        GlobalVariables.database.execute("INSERT INTO '" + str(self.tableName) + "' VALUES('" + str(newStudent.uuid) + "','" + str(newStudent.id) + "', '" + str(newStudent.name) + "', '" + str(newStudent.email) + "')")
        self.__add_student(newStudent)

    def __add_student(self, dstudent):
        self.students.append(copy.deepcopy(dstudent))

    def save_students(self):
        for student in self.students:
            student.save_student()

    def remove_student(self, uuid):
        for student in self.students:
            if student.uuid == uuid:
                query = "DELETE FROM `"+self.tableName+"` WHERE uuid='" + str(student.uuid) + "';"
                GlobalVariables.database.cursor.execute(query)
                GlobalVariables.database.connection.commit()
                self.load_students()
                return True
        return False

    def load_students(self):
        self.students.clear() #Erase what's in the list
        GlobalVariables.database.cursor.execute("SELECT * FROM `" + self.tableName + "`")
        results = GlobalVariables.database.cursor.fetchall()
        for row in results:
            # print("Here is the row:", row)
            #'4b9a8f74-3dd4-4cc8-b5fa-7f181c1b866a', 42, 'Jacob Houck', 'YourMom@Gmail.com'
            newStudent = Student(self.tableName, row[1], row[2], row[3], row[0])
            self.students.append(copy.deepcopy(newStudent))

    def print_students(self):
        for sstudent in self.students:
            sstudent.print_student()

class Student(object):
#Need to reload students after setting name.
    def __init__(self, tableName="", id="", name="", email="", xuuid="invalid", dropped=False):
        self.tableName = tableName
        self.dropped = dropped
        self.name = name
        self.email = email
        self.id = id
        self.uuid = xuuid
        if self.uuid == "invalid":
            self.uuid = str(uuid.uuid4())

    #connection.execute("INSERT INTO cs499_studentList VALUES(1, 'Jacob Houck', 'jeh0029@uah.edu')")

    def set_dropped(self, bool):
        self.dropped = bool


    def get_email(self):
        return self.email

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_uuid(self):
        return self.uuid


    def set_email(self,email):
        self.email = email
        #query = "UPDATE "+self.tableName+" SET email = '" + str(self.email) + "' WHERE uuid = '" + str(self.uuid) + "';"
        GlobalVariables.database.cursor.execute("UPDATE `" + self.tableName + "` SET email = ? WHERE uuid = ?;", (self.email, self.uuid))
        GlobalVariables.database.connection.commit()

    def set_name(self,name):
        """Tested"""
        self.name = name
        GlobalVariables.database.cursor.execute("UPDATE `" + self.tableName + "` SET name = ? WHERE uuid = ?;", (self.name, self.uuid))
        GlobalVariables.database.connection.commit()

    def set_id(self,id):
        """Sets ID in object and in database"""
        self.id=id

        GlobalVariables.database.cursor.execute("UPDATE `" + self.tableName + "` SET ID = ? WHERE uuid = ?;", (self.id, self.uuid))
        GlobalVariables.database.connection.commit()

    def save_student(self):
        """Not needed, since set functions do this for us. Will be removed soon"""
        #GlobalVariables.database.connection.execute("INSERT INTO " + str(self.tableName) + " VALUES(" + str(self.id) + ", '" + str(self.name) + "', '" + str(self.email) + "')")
        GlobalVariables.database.connection.execute("INSERT INTO ? VALUES(?, ?, ?)",
                                                    (self.tableName, self.id, self.name, self.email))
        GlobalVariables.database.connection.commit()
        #This will save the student to the GlobalVariables.GlobalVariables.database.
        #Either UPDATE or INSERT here, depending on if the student exists or not.

    def print_student(self):
        print("\nName: ", self.name)
        print("ID: ", self.id)
        print("UUID: ",self.uuid)
        print("Email: ", self.email)

    def remove_student(self):
        query = "DELETE FROM "+self.tableName+" WHERE uuid = '" + str(self.uuid) + "';"
        print(query)
        GlobalVariables.database.cursor.execute(query)
        GlobalVariables.database.connection.commit()


def create_test_database():
    """A simple testing function for just this class"""
    print("Entered testing function...")

    GlobalVariables.database.cursor.execute('CREATE TABLE IF NOT EXISTS `cs499_studentList` (`ID`	INTEGER,`name`	TEXT,`email`	TEXT);')
    GlobalVariables.database.connection.execute("INSERT INTO cs499_studentList VALUES(1, 'Jacob Houck', 'jeh0029@uah.edu')")
    GlobalVariables.database.connection.execute("INSERT INTO cs499_studentList VALUES(4, 'Matt', 'jeh0029@uah.edu')")
    GlobalVariables.database.connection.execute("INSERT INTO cs499_studentList VALUES(3, 'Tyler Meeks', 'yomoma@hotmail.com')")
    GlobalVariables.database.connection.execute("INSERT INTO cs499_studentList VALUES(2, 'Chris Christopher', 'chris42@uah.edu')")
    GlobalVariables.database.connection.commit()
#Remember to find memes for the presentation. Be sure to get a HP one.

#students = StudentList("cs499")
#students.print_students()
#students.add_student("id","name","gmail")
#students.set_email("711bc1b8-265f-4236-a6b2-395bd2107879","HOLYMOLY@BATMAN.CSU")
#students.set_id("711bc1b8-265f-4236-a6b2-395bd2107879","LET THE BODIES HIT THE FLOOR!")
#students.set_name("711bc1b8-265f-4236-a6b2-395bd2107879","STAN")
#print("Hello?!?!")
#print(students.get_id("711bc1b8-265f-4236-a6b2-395bd2107879"), students.get_email("711bc1b8-265f-4236-a6b2-395bd2107879"),students.get_name("711bc1b8-265f-4236-a6b2-395bd2107879"))
#students.print_students()
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
# students.setEmail(1994, "fhouck8@hotmail.com")
# students.printStudents()
# students.setEmail(1, "!@#$%^&*(*&^%")
# x = input("What student do you want to change?")
# x = input("Enter a Student name: ")

# y = input("Enter a Student id: ")

# z = input("Enter a Student email: ")
# students.add_student(y,x,z)

# students.print_students()
# INSERT INTO `cs499_studentList`(`ID`,`name`,`email`) VALUES (NULL,NULL,NULL);
