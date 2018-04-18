import sqlite3
from Course import Course

class Database(object):
    def __init__(self, databaseName):
        self.connection = sqlite3.connect("../databases/" + str(databaseName) + ".db")
        self.cursor = self.connection.cursor()

    def __execute_internal(self, database_fn, *args):
        try:
            return database_fn(*args)
        except sqlite3.IntegrityError as e:
            print("SQL integrity error: {}".format(e.args[0]))
            return None
        except sqlite3.ProgrammingError as e:
            print("SQL programming error: {}".format(e.args[0]))
            return None
        except sqlite3.DataError as e:
            print("SQL data error: {}".format(e.args[0]))
            return None
        except Exception as e:
            print("Error: {}".format(e.args))
            return None


    #### INTERNAL functions that are called behind the scenes to test queries ####
    def __execute(self, string):
        self.cursor.execute(string)
        self.connection.commit()

    def __add_course(self, course):
        query = "INSERT INTO 'courseList' VALUES('{}', '{}', '{}', '{}', '{}', '{}');"
        self.cursor.execute(query.format(course.name, course.number, course.section,
                                         course.semester, course.course_uuid, course.attendance_points))
        self.connection.commit()
    def __drop_course(self, course_uuid):
        query = "DELETE FROM 'courseList' WHERE Course_UUID = '{}';"
        self.cursor.execute(query.format(course_uuid))
        self.connection.commit()

    def __edit_course(self, property, new_value, course_uuid):
        query = "UPDATE 'courseList' SET '" + str(property) + "' = ? WHERE Course_UUID = ?;"
        self.cursor.execute(query, (new_value, course_uuid))
        self.connection.commit()

    def __get_course(self, course_uuid):
        query = "SELECT * FROM 'courseList' WHERE Course_UUID = '{}';"
        self.cursor.execute(query.format(course_uuid))
        row = self.cursor.fetchall()[0]
        course = Course(row[0], row[1], row[2], row[3], row[4], row[5])
        course.link_with_database()
        return course

    def __add_student(self, student):
        query = "INSERT INTO '" + student.tableName + "' VALUES(?, ?, ?, ?);"
        self.cursor.execute(query, (student.uuid, student.id, student.name, student.email))
        self.connection.commit()

    def __drop_student(self, student):
        query = "DELETE FROM '" + student.tableName + "' WHERE uuid = ?;"
        self.cursor.execute(query, (student.uuid,))
        self.connection.commit()

    def __edit_student(self, property, new_value, course_uuid, student_uuid):
        query = "UPDATE '" + course_uuid + "_student_list' SET '" + str(property) + "' = ? WHERE uuid = ?;"
        self.cursor.execute(query, (new_value, student_uuid))
        self.connection.commit()

    def __get_student_from_course(self, course_uuid, student_uuid):
        query = "SELECT * FROM '" + str(course_uuid) + "_student_list' WHERE uuid = ?;"
        self.cursor.execute(query, (student_uuid,))
        student_info = self.cursor.fetchall()[0]
        return student_info


    # these are called outside the class
    def execute(self, string): # execute specific queries not handled in other functions
        self.__execute_internal(self.__execute, string)

    def add_course(self, course):
        self.__execute_internal(self.__add_course, course)

    def drop_course(self, course):
        self.__execute_internal(self.__drop_course, course)

    def edit_course(self, course):
        self.__execute_internal(self.__edit_course, course)

    def get_course(self, course_uuid):
        return self.__execute_internal(self.__get_course, course_uuid)

    def add_student(self, student):
        self.__execute_internal(self.__add_student, student)

    def drop_student(self, student):
        self.__execute_internal(self.__drop_student, student)

    def edit_student(self, property, new_value, course_uuid, student_uuid):
        self.__execute_internal(self.__edit_student, property, new_value, course_uuid, student_uuid)

    def get_student_from_course(self, course_uuid, student_uuid):
        return self.__execute_internal(self.__get_student_from_course, course_uuid, student_uuid)







