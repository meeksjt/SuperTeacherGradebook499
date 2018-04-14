# Add some getters and setters and deletions
from AssignmentCategory import AssignmentCategory
from GlobalVariables import *
from Student import *
import uuid


class AssignmentCategoryDict(object):

    # UUID gets passed in.
    def __init__(self, course_uuid, student_list):

        self.assignment_course_uuid = course_uuid
        self.student_list = student_list
        self.assignment_categories = {}

        self.tableName = course_uuid + "_categories"
        connection.execute("CREATE TABLE IF NOT EXISTS `" + self.tableName + "` (`uuid`	TEXT,`name` TEXT,`drop_count` TEXT);")
        connection.commit()
        self.__reload_categories()

        # Jacob: Need to add loading in from database and saving to database if table already exists
        # Will also need to do the loading for all the assignment categories and everything below that

    def get_assignment_uuid(self, assignment_name):
        for category in self.assignment_categories.values():
            for assignment in category.assignment_dict.values():
                if assignment.assignmentName == assignment_name:
                    return assignment.assignmentID

    def add_category(self, uuid, name, drop_count, student_list):
        category = AssignmentCategory(str(uuid), name, drop_count, self.student_list)
        connection.execute("INSERT INTO `" + str(self.tableName) + "` VALUES('" + str(uuid) + "', '" + str(name) + "', '" + str(drop_count) + "')")
        connection.commit()
        self.__reload_categories()
        return uuid


        #self.assignment_categories.append(category)

    def get_category(self, category_name):
        for category in self.assignment_categories.values():
            if category.categoryName == category_name:
                return category

    def __reload_categories(self):
        cursor.execute("SELECT * FROM `" + self.tableName + "`")
        results = cursor.fetchall()
        for row in results:
            #print("Here is the row:", row)
            # '4b9a8f74-3dd4-4cc8-b5fa-7f181c1b866a', 42, 'Jacob Houck', 'YourMom@Gmail.com'
            newAssignmentCategory = AssignmentCategory(row[0], row[1], row[2], self.student_list)
            self.assignment_categories[row[0]] = copy.deepcopy(newAssignmentCategory)

    def set_name(self, uuid, name):
        """Sets ID in object and in database"""

        for x in self.assignment_categories.values():
            if x.uuid == uuid:
                #(`uuid`	TEXT,`name` TEXT,`drop_count` TEXT)

                query = "UPDATE `" + self.tableName + "` SET name = '" + str(name) + "' WHERE uuid = '" + str(x.uuid) + "';"
                print(query)
                cursor.execute(query)
                connection.commit()
                self.__reload_categories()
                #x.set_name(name)

    def set_drop_count(self,uuid, dropCount):
        """Sets ID in object and in database"""

        for x in self.assignment_categories:
            if x.uuid == uuid:
                #(`uuid`	TEXT,`name` TEXT,`drop_count` TEXT)

                query = "UPDATE `" + self.tableName + "` SET name = '" + str(dropCount) + "' WHERE uuid = '" + str(x.uuid) + "';"
                print(query)
                cursor.execute(query)
                connection.commit()
                self.__reload_categories()
                #x.set_name(name)


#students = StudentList("cs399")
#students.add_student("a","b","c","d")
#test = AssignmentCategoryDict("TERG",students)

#test.add_category(uuid.uuid4(), "Ante Up", "5", students)
#for x in test.assignment_categories:
#    print(x.get_name())