# Finished

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from Student import Student, StudentList
import sys
from GlobalVariables import *

"""
Wrapper class for a dictionary that maps attendance dates (string) to the students that
were present for that date (string delimited by semicolon)
"""


class AttendanceDictionary(object):

    def __init__(self, student_list):
        self.student_list = student_list
        self.attendance_sheets = {}
        self.total_days = 0
        # add loading in from a database if the attendance dictionary already exists
        # loads attendance sheets if already exists JACOB

    def add_sheet(self, dateString, studentsString):
        self.attendance_sheets[dateString] = studentsString
        # add saving to the database

    def get_student_presence_count(self, student_uuid):
        #name = ""
        self.total_days = 0
        present_days = 0

        # Get the name of the student whose uuid we have
        #for student in self.student_list.students:
        #    if student.uuid == student_uuid:
        #        name = student.name


        for day in self.attendance_sheets:
            present_students = self.attendance_sheets[day].split(';')
            if student_uuid in present_students:
                present_days += 1
            self.total_days += 1

        return present_days

"""
Class for an individual Attendance Sheet
"""

class AttendanceSheet(object):

    def __init__(self, attendanceDictionary, studentList, courseUUID):
        self.ASheet = QtWidgets.QDialog()
        self.ui = uic.loadUi('Attendance.ui', self.ASheet)
        self.ASheet.studentAttendanceTable.setHorizontalHeaderLabels(['Student Name', 'Present?'])
        self.attendanceDictionary = attendanceDictionary
        self.studentList = studentList

        # Get the current date and add our list of students
        current_date = self.ASheet.attendanceCalendar.selectedDate().toString("dd-MM-yyyy")
        self.add_students()

        # database stuff
        self.tableName = courseUUID + "_attendance"
        cursor.execute("CREATE TABLE IF NOT EXISTS `" + self.tableName + "` (`date`	TEXT,`students`	TEXT);")
        connection.commit()
        self.__load_attendance()
        # If the user is trying to modify the date they are currently in
        if current_date in self.attendanceDictionary:
            self.load_presence(self.attendanceDictionary[current_date])

        self.ASheet.show()
        self.ASheet.saveAttendanceButton.clicked.connect(self.save_attendance)
        self.ASheet.attendanceCalendar.clicked[QtCore.QDate].connect(self.load_new_date)

    # Function to load student presence into the studentAttendanceTable
    def load_presence(self, students_present):
        row_count = self.ASheet.studentAttendanceTable.rowCount()
        students = students_present.split(';')

        for row in range(0, row_count):
            if self.ASheet.studentAttendanceTable.item(row, 0).text() in students:
                self.ASheet.studentAttendanceTable.item(row, 1).setCheckState(QtCore.Qt.Checked)

    """
    Function to fill out table
    """
    def add_students(self):
        for student in self.studentList.students:
            row_insert = self.ASheet.studentAttendanceTable.rowCount()
            self.ASheet.studentAttendanceTable.insertRow(row_insert)
            self.ASheet.studentAttendanceTable.setItem(row_insert, 0, QtWidgets.QTableWidgetItem(student.name))

            chkBoxItem = QtWidgets.QTableWidgetItem()
            chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
            self.ASheet.studentAttendanceTable.setItem(row_insert, 1, chkBoxItem)
        self.ASheet.studentAttendanceTable.resizeColumnsToContents()

    def load_new_date(self):
        date = self.ASheet.attendanceCalendar.selectedDate().toString("dd-MM-yyyy")
        if date in self.attendanceDictionary:
            self.uncheck_names()
            self.load_presence(self.attendanceDictionary[date])
        else:
            self.uncheck_names()

    def uncheck_names(self):
        row_count = self.ASheet.studentAttendanceTable.rowCount()
        for row in range(0, row_count):
            self.ASheet.studentAttendanceTable.item(row, 1).setCheckState(QtCore.Qt.Unchecked)

    def __load_attendance(self):
        self.attendanceDictionary.clear()  # Erase what's in the list
        cursor.execute("SELECT * FROM `" + self.tableName + "`")
        results = cursor.fetchall()
        for row in results:
            self.attendanceDictionary[row[0]] = row[1]

    def save_attendance(self):
        row_count = self.ASheet.studentAttendanceTable.rowCount()
        output = []

        for row in range(0, row_count):
            if self.ASheet.studentAttendanceTable.item(row, 1).checkState() == QtCore.Qt.Checked:
                output.append(self.studentList.get_uuid_from_name(self.ASheet.studentAttendanceTable.item(row, 0).text()))

        output_string = ';'.join(output)
        date = self.ASheet.attendanceCalendar.selectedDate().toString("dd-MM-yyyy")
        # This is where we find the date in the database.
        self.attendanceDictionary[date] = output_string

        for i in self.attendanceDictionary:
            # i is the date, attendanceDicctionry[i] is the list of students
            print(i, self.attendanceDictionary[i])

            # if the date exists, we update it's entry in the database.
            results = connection.execute("SELECT * FROM `" + self.tableName + "` WHERE date='" + i + "' ;")
            connection.commit()
            if results.rowcount>0:
                # Then this date exists.
                query = "UPDATE " + self.tableName + " SET students = '" + str(self.attendanceDictionary[i]) + "' WHERE date = " + str(i) + ";"
                print(query)
                cursor.execute(query)
                connection.commit()
            # Else, we INSERT
            else:
                # Add database entry
                connection.execute("INSERT INTO " + str(self.tableName) + " VALUES('" + str(i) + "', '" + str(self.attendanceDictionary[i]) + "')")
                connection.commit()
