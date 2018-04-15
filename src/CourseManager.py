# Come back to this
import copy
from Course import Course
import GlobalVariables
# these three classes represent the underlying data structure of the tree view
# that the user manges courses with
class StudentItem(object):
    def __init__(self, student_name, student_uuid):
        self.student_name = student_name
        self.student_uuid = student_uuid

class CourseListItem(object):

    def __init__(self, course_name, course_uuid, student_list):
        self.course_name = course_name
        self.course_uuid = course_uuid
        self.student_list = student_list

    def add_student(self, student_name, student_uuid):
        self.student_list.append(StudentItem(student_name, student_uuid))

    def drop_student(self, student_uuid):
        for i, student_item in enumerate(self.student_list):
            if student_item.student_uuid == student_uuid:
                del self.student_list[i]
                break

class CourseList(object):
    def __init__(self):
        self.course_list = []

    def add_course(self, course_name, course_uuid, student_list):
        self.course_list.append(CourseListItem(course_name, course_uuid, student_list))

    def add_course_at(self, index, course_name, course_uuid, student_list):
        self.course_list.insert(index, CourseListItem(course_name, course_uuid, student_list))

    def drop_course(self, course_uuid):
        for i, course_item in enumerate(self.course_list):
            if course_item.course_uuid == course_uuid:
                del self.course_list[i]
                break

    def drop_course_at(self, index):
        del self.course_list[index]

    def get_course_by_uuid(self, course_uuid):
        for i, course_item in enumerate(self.course_list):
            if course_item.course_uuid == course_uuid:
                return self.course_list[i]

    def get_course_by_index(self, index):
        return self.course_list[index]

    def print_tree_view(self):
        if len(self.course_list) < 0:
            print("course_list is empty")
            return
        for course in self.course_list:
            print(course.course_name)
            if len(course.student_list) < 0:
                return
            for student in course.student_list:
                print("    " + student.student_name)
        print('\n')


# This class will read the CourseList table, and create a Course for each object in it.
# It will also create a Course.
class CourseManager:
    def __init__(self):
        self.course_tree_labels = CourseList() # data structure to change labels based on database

        self.course_dict = {}

        self.currentCourse = None
        self.current_index = 0
        # Create the table if this is a new GlobalVariables.database.
        GlobalVariables.database.execute("CREATE TABLE IF NOT EXISTS `courseList` (`Name` TEXT, `Number` TEXT, `Section` TEXT, `Semester` TEXT, `Course_UUID` TEXT, `attendance_points` TEXT);")

        # Reload existing courses if necessary
        self.__reload_courses()

    def add_to_course_tree_labels(self, course):
        student_list_items = []
        if course.student_list is None:
            return
        for student in course.student_list.students:
            student_list_items.append(StudentItem(student.name, student.uuid))
        self.course_tree_labels.add_course(course.name, course.course_uuid, student_list_items)

    def __reload_courses(self):

        # Clears course list variable
        self.course_dict.clear()
        self.course_tree_labels.course_list.clear()

        # Get everything in the table
        GlobalVariables.database.cursor.execute("SELECT * FROM `courseList`")
        results = GlobalVariables.database.cursor.fetchall()

        # Go through each row
        for row in results:
            # Here, we pass the Name, Number, Section, Semester, and UUID to the Course object, and it creates it.
            new_course = Course(row[0], row[1], row[2], row[3], row[4], row[5])
            new_course.link_with_database()
            self.add_to_course_tree_labels(new_course)
            self.course_dict[row[4]] = copy.deepcopy(new_course)

    # Adds a new course to the database and course list
    def add_course(self, course):
        GlobalVariables.database.add_course(course)
        self.__reload_courses()
        return course.course_uuid

    def delete_course(self, uuid):
        if self.course_dict is None:
            return False

        found_course = self.course_dict[uuid]
        if found_course is None:
            return False

        GlobalVariables.database.drop_course(found_course)

        self.__reload_courses()

        return True

    def get_course(self, course_uuid):
        return self.course_dict[course_uuid]

    def set_current_course(self, course_uuid):
        self.currentCourse = self.course_dict[course_uuid]

    def get_current_course_uuid(self):
        return self.currentCourse.course_uuid

    def drop_student_from_course(self, course_uuid, student_uuid):
        found_course = self.course_dict[course_uuid]
        if found_course is None:
            return False

        self.set_current_course(course_uuid)
        if self.currentCourse.remove_student(student_uuid):
            self.__reload_courses()
            return True

        return False
