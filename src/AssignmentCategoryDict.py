# Add some getters and setters and deletions
from AssignmentCategory import AssignmentCategory
from Student import *
import GlobalVariables

class AssignmentCategoryDict(object):

    # UUID gets passed in.
    def __init__(self, course_uuid, student_list):

        self.assignment_course_uuid = str(course_uuid)
        self.student_list = student_list
        self.assignment_categories = {}

        self.tableName = str(course_uuid) + "_categories"
        GlobalVariables.database.connection.execute("CREATE TABLE IF NOT EXISTS `" + self.tableName + "` (`uuid`	TEXT,`name` TEXT,`drop_count` TEXT);")
        GlobalVariables.database.connection.commit()
        self.reload_categories()

        # Jacob: Need to add loading in from database and saving to database if table already exists
        # Will also need to do the loading for all the assignment categories and everything below that

    def get_assignment_uuid(self, assignment_name):
        for category in self.assignment_categories.values():
            for assignment in category.assignment_dict.values():
                if assignment.assignmentName == assignment_name:
                    return assignment.assignmentID

    def add_category(self, uuid, name, drop_count, student_list):
        category = AssignmentCategory(str(uuid), name, drop_count, self.student_list)
        GlobalVariables.database.connection.execute("INSERT INTO `" + str(self.tableName) + "` VALUES('" + str(uuid) + "', '" + str(name) + "', '" + str(drop_count) + "')")
        GlobalVariables.database.connection.commit()
        self.reload_categories()
        return uuid

    def get_category(self, category_name):
        for category in self.assignment_categories.values():
            if category.categoryName == category_name:
                return category

    def reload_categories(self):
        self.assignment_categories.clear()
        GlobalVariables.database.cursor.execute("SELECT * FROM `" + self.tableName + "`")
        results = GlobalVariables.database.cursor.fetchall()
        for row in results:
            newAssignmentCategory = AssignmentCategory(row[0], row[1], row[2], self.student_list)
            self.assignment_categories[row[0]] = copy.deepcopy(newAssignmentCategory)

    def set_name(self, uuid, name):
        for x in self.assignment_categories.values():
            if x.uuid == uuid:
                query = "UPDATE `" + self.tableName + "` SET name = '" + str(name) + "' WHERE uuid = '" + str(x.uuid) + "';"
                GlobalVariables.database.cursor.execute(query)
                GlobalVariables.database.connection.commit()
                self.reload_categories()

    def set_drop_count(self,uuid, dropCount):
        for x in self.assignment_categories:
            if x.uuid == uuid:
                query = "UPDATE `" + self.tableName + "` SET name = '" + str(dropCount) + "' WHERE uuid = '" + str(x.uuid) + "';"
                GlobalVariables.database.connection.execute(query)
                GlobalVariables.database.connection.commit()
                self.reload_categories()

    def save_category_info(self, name, drop_count, uuid):
        query = "UPDATE `" + self.tableName + "` SET name = ?, drop_count = ? WHERE uuid = ?;"
        GlobalVariables.database.connection.execute(query, (name, drop_count, uuid))
        GlobalVariables.database.connection.commit()

    def delete_category(self, course, uuid):
        query = "DELETE FROM `" + self.tableName + "` WHERE uuid = '" + uuid + "';"
        GlobalVariables.database.connection.execute(query)
        GlobalVariables.database.connection.commit()
        course.assignment_category_dict.reload_categories()

