from AssignmentCategory import AssignmentCategory

class AssignmentCategoryList(object):

    def __init__(self, category_list_uuid):
        self.assignment_category_list_uuid = category_list_uuid
        self.tableName = category_list_uuid + "_categories"
        self.assignment_categories = []

        # Jacob: Need to add loading in from database and saving to database if table already exists
        # Will also need to do the loading for all the assignment categories and everything below that

    def add_category(self, uuid, name, drop_count, student_list):
        category = AssignmentCategory(uuid, name, drop_count, student_list)
        self.assignment_categories.append(category)

    def get_category(self, category_id):
        for category in self.assignment_categories:
            if category.category_uuid == category_id:
                return category
