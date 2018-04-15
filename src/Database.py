import sqlite3


class Database(object):
    def __init__(self, databaseName):
        self.connection = sqlite3.connect("../databases/" + str(databaseName) + ".db")
        self.cursor = self.connection.cursor()

    # execute arbitrary queries
    def execute(self, string):
        self.cursor.execute(string)
        self.connection.commit()

    def add_course(self, course):
        query = "INSERT INTO 'courseList' VALUES(?, ?, ?, ?, ?)"
        self.cursor.execute(query, (course.name, course.number, course.section, course.semester, course.course_uuid))
        self.connection.commit()

    def drop_course(self, course):
        query = "DELETE FROM 'courseList' WHERE Course_UUID = ?"
        self.cursor.execute(query, (course.course_uuid,))
        self.connection.commit()

    def edit_course(self, property, new_value, course_uuid):
        query = "UPDATE 'courseList' SET '" + str(property) + "' = ? WHERE Course_UUID = ?"
        self.cursor.execute(query, (new_value, course_uuid))
        self.connection.commit()

    def add_student(self, student):
        query = "INSERT INTO ? VALUES(?, ?, ?);"
        self.cursor.execute(query, (student.tableName, student.id, student.name, student.email))
        self.connection.commit()

    def drop_student(self, student):
        query = "DELTE FROM ? WHERE uuid = ?;"
        self.cursor.execute(query, (student.tableName, student.uuid))
        self.connection.commit()

    def edit_student(self, property, new_value, student):
        query = "UPDATE ? SET '" + str(property) + "' = ? WHERE uuid = ?;"
        self.cursor.execute(query, (student.tableName, new_value, student.uuid))
        self.connection.commit()

