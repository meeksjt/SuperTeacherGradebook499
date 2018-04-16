from PyQt5 import QtCore, QtWidgets, uic
import GlobalVariables
import sys
from Student import Student, StudentList
import uuid
import os
import Statistics


"""
Class for displaying students in a course
"""
class AssignmentStats(object):

    """
    Constructor for displaying students and student information
    Parameters:
        studentList: (StudentList) the list of students and associated variables we are displaying
    """
    def __init__(self, studentList, gradesheetTable, course_name, course_semester):
        self.AStats = QtWidgets.QDialog()
        self.ui = uic.loadUi('AssignmentStats.ui', self.AStats)
        self.AStats.statsTable.setHorizontalHeaderLabels(
            ['Assignment Name', 'Assignment Point Value', 'Mean', 'Median', 'Mode', 'Standard Deviation']
        )
        #self.AStats.statsTable.resizeColumnsToContents()
        self.studentList = studentList
        self.gradesheetTable = gradesheetTable
        self.course_name = course_name
        self.course_semester = course_semester

        self.setup_display()
        self.AStats.show()
        self.AStats.saveStatsButton.clicked.connect(self.save_assignment_statistics)

    def save_assignment_statistics(self):
        if os.path.isfile(("../student_assignment_statistics/" + str(self.course_name)+" " +str(self.course_semester)+" Assignment Statistics.txt")):
            overwrite = self.display_message("Overwrite?", "Do you want to overwrite the previous student roster for this course?")
        else:
            overwrite = True
        if overwrite:
            x = QtWidgets.QMessageBox.question(self.AStats, "Finished!",
                                               "Your file has been saved in the 'student_assignment_statistics' directory.",
                                               QtWidgets.QMessageBox.Ok)
            with open(("../student_assignment_statistics/" + str(self.course_name)+" " +str(self.course_semester)+" Assignment Statistics.txt"), 'w') as f:
                header_line = "Assignment Name\t - \tAssignment Points - Mean - Median - Mode - Standard Deviation\n"
                f.write(header_line)
                row_count = self.AStats.statsTable.rowCount()
                for row in range(row_count):
                    f.write(self.AStats.statsTable.item(row, 0).text().ljust(23))
                    f.write(self.AStats.statsTable.item(row, 1).text().rjust(15))
                    f.write(self.AStats.statsTable.item(row, 2).text().ljust(8))
                    f.write(self.AStats.statsTable.item(row, 3).text().ljust(8))
                    f.write(self.AStats.statsTable.item(row, 4).text().ljust(8))
                    f.write(self.AStats.statsTable.item(row, 5).text().ljust(8) + "\n")


                    #f.write("%-12s%-12s%-12s%-12s%-12s%-12s".format(self.AStats.statsTable.item(row, 0).text(),
                    #        self.AStats.statsTable.item(row, 1).text(),
                    #        self.AStats.statsTable.item(row, 2).text(),
                    #        self.AStats.statsTable.item(row, 3).text(),
                    #        self.AStats.statsTable.item(row, 4).text(),
                    #        self.AStats.statsTable.item(row, 5).text()
                    #        ))

    def display_message(self, window_text, window_message):
        choice = QtWidgets.QMessageBox.question(self.AStats, window_text, window_message, QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Cancel)
        if choice == QtWidgets.QMessageBox.Ok:
            x = QtWidgets.QMessageBox.question(self.AStats, "Finished!", "Your file has been saved in the 'student_rosters' directory.", QtWidgets.QMessageBox.Ok)
            return True
        else:
            return False

    def setup_display(self):
        row_count = self.gradesheetTable.rowCount()
        col_count = self.gradesheetTable.columnCount() - 2

        student_grades = []
        #Loop through our grade table
        for col in range(1, col_count):
            row_insert = self.AStats.statsTable.rowCount()
            self.AStats.statsTable.insertRow(row_insert)
            assignment_grades = []
            assignment_name = self.gradesheetTable.horizontalHeaderItem(col).get_assignment_name()
            assignment_points = self.gradesheetTable.horizontalHeaderItem(col).get_assignment_points()

            self.AStats.statsTable.setItem(row_insert, 0, QtWidgets.QTableWidgetItem(assignment_name))
            self.AStats.statsTable.setItem(row_insert, 1, QtWidgets.QTableWidgetItem(assignment_points))

            assignment_grades.append(assignment_name)
            assignment_grades.append(assignment_points)
            assignment_grades.append({})
            for row in range(1, row_count):
                student_id = self.gradesheetTable.verticalHeaderItem(row).get_student_uuid()
                grade = self.gradesheetTable.item(row, col).text()
                if grade == "" or grade == "-":
                    grade = 0
                assignment_grades[2][student_id] = float(grade)

            student_grades.append(assignment_grades)

        for counter, assignment in enumerate(student_grades):
            mean = Statistics.calculate_mean(assignment[2].values())
            median = Statistics.calculate_median(assignment[2].values())
            mode = Statistics.calculate_mode(assignment[2].values())
            std_dev = Statistics.calculate_std_dev(assignment[2].values())
            self.AStats.statsTable.setItem(counter, 2, QtWidgets.QTableWidgetItem(str(mean)))
            self.AStats.statsTable.setItem(counter, 3, QtWidgets.QTableWidgetItem(str(median)))
            self.AStats.statsTable.setItem(counter, 4, QtWidgets.QTableWidgetItem(str(mode)))
            self.AStats.statsTable.setItem(counter, 5, QtWidgets.QTableWidgetItem(str(std_dev)))

        self.AStats.statsTable.resizeColumnsToContents()


    def close(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

