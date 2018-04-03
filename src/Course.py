import re
import Assignment
from AssignmentCategoryList import AssignmentCategoryList
from Student import *

class Course:

    def __init__(self, id, number, name, section, semester, gradeScale):
        #Need to know what to put here
        self.number = number
        self.name = name
        self.section = section
        self.semester = semester
        self.table_name = id
        #print("Course Name: "+self.table_name)

        #Change This Later.
        self.assignmentCategoryList = AssignmentCategoryList()

        self.gradeScale = gradeScale.clone()

        #Calls Student List, which creates all that garbage
        self.student_list = StudentList(self.table_name)
        #self.add_student("5","Matt","Email")

        # Assignment list
        self.assignment_list = []

        cursor.execute("CREATE TABLE IF NOT EXISTS `assignment_list` (`Assignment_ID`   INT,`Name`  TEXT,`Total`    INT,`Weight`    INT);")
        connection.commit()

        pass

    # Adds an assignment to assignment_list
    def add_assignment(self, id, name, total, weight):

        # Creates instance of Assignment
        assignment = Assignment(id, name, total, weight)

        # Adds the instance to assignment_list
        self.assignment_list.append(assignment)

        # Inserts the assignment vales into the database
        connection.execute(("INSERT INTO 'assignment_list' VALUES('" + str(assignment.id) + "', '" + str(assignment.name) + "', '" + str(assignment.total) + "', '" + str(assignment.weight) + "')"))
        connection.commit()

    # Drops an assignment from assignment_list
    def drop_assignment(self, name):

        # Drops the assignment based on the assignment name
        for assignment in self.assignment_list:
			if assignment.name == name:
				self.assignment_list.remove(assignment)
				cursor.execute("DELETE FROM 'assignment_list' where Name = '" + name + "';")
				connection.commit()

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

