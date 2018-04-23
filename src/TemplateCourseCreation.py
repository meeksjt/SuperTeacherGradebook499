from PyQt5 import QtWidgets, QtGui, QtCore, uic
from Course import Course
import uuid
import GlobalVariables

class TemplateCourseCreation(object):

    def __init__(self, course_manager, add_course_fn):

        self.course_manager = course_manager
        self.add_course_fn = add_course_fn

        self.TCCreation = QtWidgets.QDialog()
        self.ui = uic.loadUi('../assets/ui/TemplateCourseCreation.ui', self.TCCreation)

        GlobalVariables.database.execute("SELECT * FROM templateCourses")
        results = GlobalVariables.database.cursor.fetchall()

        self.course_dict = {}
        for c in results:
            course = GlobalVariables.database.get_template_course(c[4])
            if course is not None:
                self.course_dict[c[4]] = GlobalVariables.database.get_template_course(c[4])

        for course in self.course_dict.values():
            display_msg = course.name + " ; " + course.number + " ; " + course.section + " ; " + course.semester
            self.TCCreation.courseChoiceBox.addItem(str(display_msg))

        self.TCCreation.show()
        self.TCCreation.createCourseButton.clicked.connect(self.create_course_from_past_course)

    # Already existing CourseObject that has been linked with the database, and three booloans
    def create_course_from_past_course(self):

        # Here is where we get the course_uuid from the drop-down box
        selected_course = str(self.TCCreation.courseChoiceBox.currentText())

        c = [i.strip() for i in selected_course.split(';')]

        course_uuid = ""
        name = self.TCCreation.courseNameField.text()
        number = self.TCCreation.courseNumberField.text()
        section = self.TCCreation.courseSectionField.text()
        semester = self.TCCreation.courseSemesterField.text()
        attendance_points = self.TCCreation.attendancePointsField.text()

        for course in self.course_dict.values():
            if c[0] == course.name and c[1] == course.number and c[2] == course.section and c[3] == course.semester:
                course_uuid = course.course_uuid

        # Gets the Course we want to copy from.
        old_course = self.course_manager.get_template_course(course_uuid)
        new_uuid = str(uuid.uuid4())
        new_course = Course(name, number, section, semester, new_uuid, attendance_points)
        new_course.link_with_database()

        # We want to copy the gradeScale.
        # Copies the gradescale
        new_course.grade_scale.set_grade_scale(str(old_course.grade_scale.get_A_bottom_score()),
                                               str(old_course.grade_scale.get_B_bottom_score()),
                                               str(old_course.grade_scale.get_C_bottom_score()),
                                               str(old_course.grade_scale.get_D_bottom_score()))

        # Loops through category_dict and creates a new category for each one it finds.
        for category_uuid, category in old_course.assignment_category_dict.assignment_categories.items():
            new_cat_uuid = str(uuid.uuid4())
            new_course.assignment_category_dict.add_category(new_cat_uuid, category.categoryName,
                                                            category.drop_count, new_course.student_list)
            for assignment_uuid, assignment in category.assignment_dict.items():
                new_course.assignment_category_dict.assignment_categories[new_cat_uuid].add_assignment(str(uuid.uuid4()),
                                                                             assignment.assignmentName,
                                                                             assignment.totalPoints,
                                                                             new_course.student_list)
        self.course_manager.add_course(new_course)
        self.course_manager.set_current_course(new_course)
        self.add_course_fn(new_course)

