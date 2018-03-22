import re
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
        self.assignmentCategoryList = []

        self.gradeScale = gradeScale.clone()

        #Calls Student List, which creates all that garbage
        self.student_list = StudentList(self.table_name)
        #self.add_student("5","Matt","Email")

        pass

    def add_assignment(self):

        pass

    def drop_assignment(self):
        pass

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

#funk = Course("CS 399", "Fall", "01")