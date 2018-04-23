from PyQt5 import QtCore, QtWidgets, uic
import GlobalVariables
import sys
from Student import Student, StudentList
import uuid
import os
import Statistics
import csv

class FinalGradeStats(object):

    def __init__(self, name, number, section, semester, studentGrades):
        self.FGStats = QtWidgets.QDialog()
        self.ui = uic.loadUi('../assets/ui/FinalGradeStats.ui', self.FGStats)
        self.FGStats.statsTable.setHorizontalHeaderLabels(
            ['Course Name', 'Course Number', 'Course Section', 'Course Semester', 'Mean', 'Median', 'Mode', 'Standard Deviation']
        )

        self.name = name
        self.number = number
        self.section = section
        self.semester = semester
        self.studentGrades = studentGrades

        self.setup_display()
        self.FGStats.show()
        self.FGStats.saveStatsButton.clicked.connect(self.save_student_statistics)

    def setup_display(self):
        self.FGStats.statsTable.insertRow(0)
        self.FGStats.statsTable.setItem(0, 0, QtWidgets.QTableWidgetItem(self.name))
        self.FGStats.statsTable.setItem(0, 1, QtWidgets.QTableWidgetItem(self.number))
        self.FGStats.statsTable.setItem(0, 2, QtWidgets.QTableWidgetItem(self.section))
        self.FGStats.statsTable.setItem(0, 3, QtWidgets.QTableWidgetItem(self.semester))
        self.FGStats.statsTable.setItem(0, 4, QtWidgets.QTableWidgetItem(str(Statistics.calculate_mean(self.studentGrades))))
        self.FGStats.statsTable.setItem(0, 5, QtWidgets.QTableWidgetItem(str(Statistics.calculate_median(self.studentGrades))))
        self.FGStats.statsTable.setItem(0, 6, QtWidgets.QTableWidgetItem(str(Statistics.calculate_mode(self.studentGrades))))
        self.FGStats.statsTable.setItem(0, 7, QtWidgets.QTableWidgetItem(str(Statistics.calculate_std_dev(self.studentGrades))))
        self.FGStats.statsTable.resizeColumnsToContents()

    def save_student_statistics(self):
        if os.path.isfile(("../final_grades_stats/" + str(self.name) + " " + str(
                self.semester) + " Final Grade Statistics.csv")):
            overwrite = QtWidgets.QMessageBox.question(self.FGStats, "Overwrite?",
                                                       "Do you want to overwrite the previous student assignments stats file for this course?",
                                                       QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        else:
            overwrite = QtWidgets.QMessageBox.Yes
        if overwrite == QtWidgets.QMessageBox.Yes:
            x = QtWidgets.QMessageBox.question(self.FGStats, "Finished!",
                                               "Your file has been saved in the 'final_grade_stats' directory with the filename '" + str(
                                                   self.name) + " " + str(
                                                   self.semester) + " Final Grade Statistics.csv'",
                                               QtWidgets.QMessageBox.Ok)
            with open(("../final_grades_stats/" + str(self.name) + " " + str(
                    self.semester) + " Final Grade Statistics.csv"), 'w') as f:
                writer = csv.writer(f)

                writer.writerow(
                    ['Course Name', 'Course Number', 'Course Section', 'Course Semester', 'Mean', 'Median', 'Mode',
                     'Standard Deviation'])

                row_data = []
                for column in range(self.FGStats.statsTable.columnCount()):
                    item = self.FGStats.statsTable.item(0, column)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append('')
                writer.writerow(row_data)
