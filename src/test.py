import CourseManager

courses = CourseManager()
courses.add_course("Senior Project","499","01","Fall")
for course in courses.course_dict().items():
	pass