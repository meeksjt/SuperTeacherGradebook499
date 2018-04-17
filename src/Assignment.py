from Grades import Grades
import GlobalVariables

"""
    Class for each Assignment in the AssignmentCategoryBase
"""


class Assignment:
    """
        Constructor for the Assignment Class
        Instantiates an Assignment object
    """

    def __init__(self, assignment_uuid, assignment_name, total_points, student_list):
        self.assignmentID = assignment_uuid
        self.assignmentName = assignment_name
        self.totalPoints = total_points


        self.tableName = assignment_uuid + '_grades'
        self.studentList = student_list
        self.studentGrades = Grades()

        GlobalVariables.database.connection.execute("CREATE TABLE IF NOT EXISTS `" + self.tableName + "` (`student_uuid`	TEXT,`grade` TEXT);")
        GlobalVariables.database.connection.commit()
        self.__load_grades()
        self.add_grade_to_database()

    def reload_grades(self):
        self.__load_grades()
        self.add_grade_to_database()
    """
        Function to get assignmentName for an Assignment
        Parameters:
            None
        Returns:
            assignmentName : (string) name of Assignment
    """

    #def save_assignment(self):

        #GlobalVariables.database.connection.execute("INSERT INTO `" + str(self.tableName) + "` VALUES('" + str(student.uuid) + "','" + "-" + "')")
        #GlobalVariables.database.connection.commit()

    def add_grade_to_database(self):
        for student in self.studentList.students:
            if student.uuid not in self.studentGrades.assignmentGrades.keys():
                GlobalVariables.database.connection.execute("INSERT INTO `" + str(self.tableName) + "` VALUES('" + str(student.uuid) + "','" + "-" + "')")
                GlobalVariables.database.connection.commit()

    def get_assignment_name(self):
        return self.assignmentName

    """
        Function to set assignmentName for an Assignment
        Parameters:
            new_assignment_name : (string) new name for the Assignment
        Returns:
            None
        Might need to add error checking to make sure duplicate assignment_names aren't used
    """
    def set_assignment_name(self, new_assignment_name):
        self.assignmentName = new_assignment_name

    """
        Function to load the grades from the database to our Grades object
        Parameters:
            None
        Returns:
            None
    """
    def __load_grades(self):

        #Now everyone is in the GlobalVariables.database. So we can reload the GlobalVariables.database.
        self.studentGrades.clear_grades()
        GlobalVariables.database.cursor.execute("SELECT * FROM `" + self.tableName + "`")
        results = GlobalVariables.database.cursor.fetchall()
        for row in results:
            self.studentGrades.set_grade(row[0], row[1])

    """
        Function to get the totalPoints that an Assignment is worth 
        Parameters:
            None
        Returns:
            self.totalPoints : (float) the total points an Assignment is worth
    """
    def get_total_points(self):
        return self.totalPoints

    """
        Function to set the totalPoints that an Assignment is worth
        Parameters:
            new_total_points : (string) the total points an Assignment is worth
        Returns:
            None
    """
    def set_total_points(self, new_total_points):
        self.totalPoints = new_total_points

    """
        Function to get a specific Student's grade for the Assignment
        Parameters:
            student_id : (string) id of student we want to get Grade for
        Returns:
            grade : (string) grade of the student on this Assignment
    """
    def get_student_grade(self, student_uuid):
        try:
            return self.studentGrades.get_grade(student_uuid)
        except:
            self.add_grade_to_database()

    """
        Function to set a specific Student's grade for an Assignment
        Parameters:
            student_id : (string) id of the student we are setting the Grade for
            grade : (float) grade of the student on this Assignment
        Returns:
            None(`assignment_uuid`	TEXT,`assignment_name`	TEXT,`total_points`	TEX
    """



    def set_student_grade(self, student_uuid, grade):
        self.studentGrades.set_grade(student_uuid, grade)

    """
        Function to save the grades for the assignment to the database
        Parameters:
            None
        Returns:
            None
    """
    def save_grades(self):
        #Do the actual saving of the grades here.
        #Loops through the grades
        for xuuid, grade in self.studentGrades.assignmentGrades.items():
            query = "UPDATE `" + self.tableName + "` SET grade = '" + str(grade) + "' WHERE student_uuid = '" + str(xuuid) + "';"
            #print(query)
            GlobalVariables.database.cursor.execute(query)
            GlobalVariables.database.connection.commit()

"""
#students = StudentList("cs499")
#students.add_student("42","Jacob Houck", "YourMom@Gmail.com")
#test = Assignment("AUUID","Quiz 1","100",students)
#print(test.get_assignment_name(),test.assignmentID)
#test.set_student_grade("1c9e45e1-a1bb-4f98-ad17-50d4f5912db3","99")
#test.save_grades()
"""
