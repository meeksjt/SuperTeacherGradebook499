from MainDisplay import *

#Already existing CourseObject that has been linked with the database, and three booloans
def create_course_from_past_course(newCourse, course_uuid, grade_scale_bool, categories_bool, assignments_bool):
	#OK, so I need to check this stuff.
	newCourse.link_with_database()

	#Gets the Course we want to copy from.
	old_course = main_display.course_manager.get_course(course_uuid)
	# We want to copy the gradeScale.
	if grade_scale_bool == True:
		#Copes the gradescale
		newCourse.grade_scale.set_grade_scale(old_course.get_A_bottom_score(), old_course.get_B_bottom_score(), old_course.get_C_bottom_score(), old_course.get_D_bottom_score)

	#We only want to copy the categories.
	if categories_bool == True and assignments_bool == False:
		#Loops through category_dict and creates a new category for each one it finds.
		for category_uuid, category in old_course.assignment_category_dict.items:
			newCourse.assignment_category_dict.add_category(uuid.uuid4(), category.categoryName, category.drop_count, newCourse.student_list)

	#We want to copy the categories and assignments.
	if categories_bool == True and assignments_bool == True:
		#Loops through category_dict and creates a new category for each one it finds.
		for category_uuid, category in old_course.assignment_category_dict.items:
			temp_uuid = uuid.uuid4()
			newCourse.assignment_category_dict.add_category(temp_uuid, category.categoryName, category.drop_count, newCourse.student_list)
			for assignment_uuid, assignment in category.assignment_dict.items():
				newCourse.assignment_category_dict[temp_uuid].add_assignment(uuid.uuid4(), assignment.assignmentName, assignment.totalPoints, newCourse.student_list)

def test_dezz_nuts():
	x = Course("Red Silo Cup", "101", "01", "Fall", uuid.uuid4(), "2")
	create_course_from_past_course(x, "Senior Project", True, True, True)

	#def create_course_from_past_course(newCourse, course_uuid, grade_scale_bool, categories_bool, assignments_bool):


#test_dezz_nuts()