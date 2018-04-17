from PyQt5 import QtCore, QtWidgets, uic
import GlobalVariables
import sys
from Student import Student, StudentList
import uuid
import os
import Statistics

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
        #self.FGStats.saveStatsButton.clicked.connect()

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
        pass