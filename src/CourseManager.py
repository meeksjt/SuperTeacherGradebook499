import GlobalVariables

from Course import Course


# the CourseList class just holds a list representing the labels
# the MainDisplay uses this to fill the tree on startup
class StudentItem(object):
    def __init__(self, student_name, student_uuid):
        self.student_name = student_name
        self.student_uuid = student_uuid


class CourseListItem(object):
    def __init__(self, course_name, course_section, course_semester, course_uuid, student_list):
        self.course_name = course_name
        self.course_section = course_section
        self.course_semester = course_semester
        self.course_uuid = course_uuid
        self.student_list = student_list


class CourseList(object):
    def __init__(self):
        self.course_list = []
        self.current_course_item = None

    def add_course(self, course_name, course_section, course_semester, course_uuid, student_list):
        self.course_list.append(CourseListItem(course_name, course_section, course_semester, course_uuid, student_list))

# This class will read the CourseList table, and create a Course for each object in it.
# It will also create a Course.
class CourseManager(object):
    def __init__(self):
        self.course_tree_labels = CourseList() # data structure to change labels based on database
        self.course_dict = {}
        self.currentCourse = None
        GlobalVariables.database.execute("CREATE TABLE IF NOT EXISTS 'courseList' ("
                                         "Name TEXT, "
                                         "Number TEXT, "
                                         "Section TEXT, "
                                         "Semester TEXT, "
                                         "Course_UUID TEXT, "
                                         "Attendance_Points TEXT"
                                         ");")

        GlobalVariables.database.execute("CREATE TABLE IF NOT EXISTS 'templateCourses' ("
                                         "Name TEXT, "
                                         "Number TEXT, "
                                         "Section TEXT, "
                                         "Semester TEXT, "
                                         "Course_UUID TEXT, "
                                         "Attendance_Points TEXT"
                                         ");")
        self.reload_courses()

    def __add_to_course_tree_labels(self, course):
        student_list_items = []
        if course.student_list is None:
            return
        for student in course.student_list.students:
            student_list_items.append(StudentItem(student.name, student.uuid))
        self.course_tree_labels.add_course(course.name, course.section, course.semester, course.course_uuid, student_list_items)

    def reload_courses(self):
        GlobalVariables.database.execute("SELECT * FROM `courseList` ORDER BY Name;")
        results = GlobalVariables.database.cursor.fetchall()

        self.course_tree_labels.course_list.clear()
        for row in results:
            new_course = Course(row[0], row[1], row[2], row[3], row[4], row[5])
            new_course.link_with_database()
            self.__add_to_course_tree_labels(new_course)

        GlobalVariables.database.execute("SELECT * FROM `templateCourses` ORDER BY Name;")

    def add_course(self, course):
        GlobalVariables.database.add_course(course)
        self.reload_courses()
        return course.course_uuid

    def add_template_course(self, course):
        GlobalVariables.database.add_template_course(course)
        self.reload_courses()
        return

    def delete_course(self, course_uuid):
        GlobalVariables.database.drop_course(course_uuid)
        self.reload_courses()
        return True

    def get_course(self, course_uuid):
        return GlobalVariables.database.get_course(course_uuid)

    def get_template_course(self, course_uuid):
        return GlobalVariables.database.get_template_course(course_uuid)

    def set_current_course(self, course_uuid):
        self.currentCourse = self.get_course(course_uuid)

    def add_student_to_course(self, course, student):
        course.add_student(student)

    def drop_student_from_course(self, course_uuid, student_uuid):
        found_course = self.get_course(course_uuid)
        if found_course is None:
            return False

        self.set_current_course(course_uuid)
        if self.currentCourse.remove_student(student_uuid):
            self.reload_courses()
            return True

        return False
