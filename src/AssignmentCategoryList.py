from AssignmentCategory import AssignmentCategory
from GlobalVariables import *
from Student import *
import uuid

class AssignmentCategoryList(object):

	#UUID gets passed in.
	def __init__(self, category_list_uuid,student_list):
		self.assignment_category_list_uuid = category_list_uuid
		self.tableName = category_list_uuid + "_categories"
		self.assignment_categories = []
		self.student_list = student_list
		connection.execute("CREATE TABLE IF NOT EXISTS `" + self.tableName + "` (`uuid`	TEXT,`name` TEXT,`drop_count` TEXT);")
		connection.commit()
		self.__reload_categories(self.student_list)



		# Jacob: Need to add loading in from database and saving to database if table already exists
		# Will also need to do the loading for all the assignment categories and everything below that

	def add_category(self, uuid, name, drop_count, student_list):
		category = AssignmentCategory(str(uuid), name, drop_count, self.student_list)
		connection.execute("INSERT INTO `" + str(self.tableName) + "` VALUES('" + str(uuid) + "', '" + str(name) + "', '" + str(drop_count) + "')")
		connection.commit()
		self.__reload_categories(student_list)


		self.assignment_categories.append(category)

	def get_category(self, category_id):
		for category in self.assignment_categories:
			if category.category_uuid == category_id:
				return category

	def __reload_categories(self, studentlist):
		cursor.execute("SELECT * FROM `" + self.tableName + "`")
		results = cursor.fetchall()
		for row in results:
			#print("Here is the row:", row)
			# '4b9a8f74-3dd4-4cc8-b5fa-7f181c1b866a', 42, 'Jacob Houck', 'YourMom@Gmail.com'
			newAssignment = AssignmentCategory(row[0], row[1], row[2], self.student_list)

			self.assignment_categories.append(copy.deepcopy(newAssignment))
			for assignmentCategory in self.assignment_categories:
				print("Here is the BLEEPING NAME! ",assignmentCategory.category_uuid)

	def set_name(self,uuid, name):
		"""Sets ID in object and in database"""
		for x in self.assignment_categories:
			if x.uuid == uuid:
				x.set_name(name)

#students = StudentList("cs399")
#test = AssignmentCategoryList("TERG",students)
#test.add_category(uuid.uuid4(), "Ante Up", "5", students)
#for x in test.assignment_categories:#
#	print(x.get_name())