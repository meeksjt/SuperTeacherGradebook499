# Come back to this
import sqlite3
import copy
from Course import Course

from GlobalVariables import connection, cursor
#This class will read the CourseList table, and create a Course for each object in it.
#It will also create a Course.


class CourseManager:
    def __init__(self):
        self.course_list = []

        #Create the table if this is a new database.
        cursor.execute("CREATE TABLE IF NOT EXISTS `courseList` (`Course_UUID`  TEXT,`Name`	TEXT,`Number`   TEXT,`Semester`	TEXT,`Section`	TEXT);")
        connection.commit()

        # Reload existing courses if necessary
        self.__reload_courses()
        pass

    #Loads the course from the database.
    def __reload_courses(self):

        # Clears course list variable
        self.course_list.clear()

        #Get everything in the table
        cursor.execute("SELECT * FROM `courseList`")

        #Our results go into this as a list.
        results = cursor.fetchall()

        #Go through each row
        for row in results:
            #Here, we pass the Name, Semester, and Section to the Course object, and it creates it.
            new_course = Course(row[0], row[1], row[2], row[3], row[4])
            self.course_list.append(copy.deepcopy(new_course))

    #Adds a new course to the database
    def add_course(self, uuid, name, number, semester, section):

        newCourse = Course(uuid, name, number, semester, section)
        connection.execute(("INSERT INTO 'courseList' VALUES('" + str(name) + "', '" + str(semester) + "', '" + str(section) + "')"))
        connection.commit()
        self.__reload_courses()
        # newCourse.add_student("3","Jacob","email")
        # newCourse.add_student("5", "Matt", "email")
        # newCourse.add_student("8", "Tyler", "email")
        # newCourse.add_student("2", "Chris", "email")
        # newCourse.student_list.print_students()
        pass

    def delete_course(self, name):
        for coursea in self.course_list:
            if coursea.name == name:
                self.course_list.remove(coursea)
                cursor.execute("DELETE FROM 'courseList' where Name = '" + name + "';")
                connection.commit()

    def drop_course(self):
        pass

    def get_course(self):
        print("Nothing to see here.")


jacob = CourseManager()

for course in jacob.course_list:
    print("Course Name: ", course.name)
    for student in course.student_list.students:
        student.print_student()
jacob.delete_course("a")

jacob.add_course("1342323", "Senior Design", "CS 499", "Spring 2018", "01")
