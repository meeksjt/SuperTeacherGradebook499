# Finished
from PyQt5 import QtCore, QtWidgets, uic
import GlobalVariables

"""
Wrapper class for a dictionary that maps attendance dates (string) to the students that
were present for that date (string delimited by semicolon)
"""


class AttendanceDictionary(object):

    def __init__(self, course_uuid, student_list):
        self.student_list = student_list
        self.attendance_sheets = {}
        self.total_days = 0
        self.course_uuid = course_uuid
        self.table_name = str(course_uuid) + "_attendance"

        GlobalVariables.database.cursor.execute("CREATE TABLE IF NOT EXISTS `" + self.table_name + "` (`date`	TEXT,`students`	TEXT);")
        GlobalVariables.database.connection.commit()
        self.__load_attendance()
        # add loading in from a database if the attendance dictionary already exists
        # loads attendance sheets if already exists JACOB

    def add_sheet(self, dateString, studentsString):
        self.attendance_sheets[dateString] = studentsString
        # add saving to the database

    def __load_attendance(self):
        self.attendance_sheets.clear()  # Erase what's in the list
        GlobalVariables.database.execute("SELECT * FROM `" + self.table_name+ "`")
        results = GlobalVariables.database.cursor.fetchall()
        for row in results:
            self.attendance_sheets[row[0]] = row[1]

    def get_student_presence_count(self, student_uuid):
        #name = ""
        self.total_days = 0
        present_days = 0

        for day in self.attendance_sheets:
            present_students = self.attendance_sheets[day].split(';')
            if student_uuid in present_students:
                present_days += 1
            self.total_days += 1

        return present_days / self.total_days

"""
Class for an individual Attendance Sheet
"""

class AttendanceSheet(object):

    def __init__(self, attendanceDictionary, studentList, courseUUID):
        self.ASheet = QtWidgets.QDialog()
        self.ui = uic.loadUi('../assets/ui/Attendance.ui', self.ASheet)
        self.ASheet.studentAttendanceTable.setHorizontalHeaderLabels(['Student Name', 'Present?'])
        self.attendanceDictionary = attendanceDictionary
        self.studentList = studentList

        # Get the current date and add our list of students
        current_date = self.ASheet.attendanceCalendar.selectedDate().toString("dd-MM-yyyy")
        self.student_uuids = []
        self.add_students()

        # database stuff
        self.tableName = courseUUID + "_attendance"
        GlobalVariables.database.cursor.execute("CREATE TABLE IF NOT EXISTS `" + self.tableName + "` (`date`	TEXT,`students`	TEXT);")
        GlobalVariables.database.connection.commit()
        self.__load_attendance()
        # If the user is trying to modify the date they are currently in
        if current_date in self.attendanceDictionary.attendance_sheets:
            self.load_presence(self.attendanceDictionary.attendance_sheets[current_date])
        self.ASheet.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.ASheet.show()
        self.ASheet.saveAttendanceButton.clicked.connect(self.save_attendance)
        self.ASheet.attendanceCalendar.clicked[QtCore.QDate].connect(self.load_new_date)

    # Function to load student presence into the studentAttendanceTable
    def load_presence(self, students_present):
        row_count = self.ASheet.studentAttendanceTable.rowCount()
        students = students_present.split(';')

        for row in range(0, row_count):
            if self.student_uuids[row] in students:
                self.ASheet.studentAttendanceTable.item(row, 1).setCheckState(QtCore.Qt.Checked)

    """
    Function to fill out table
    """
    def add_students(self):
        for student in self.studentList.students:
            row_insert = self.ASheet.studentAttendanceTable.rowCount()
            self.ASheet.studentAttendanceTable.insertRow(row_insert)
            self.ASheet.studentAttendanceTable.setItem(row_insert, 0, QtWidgets.QTableWidgetItem(student.name))
            self.student_uuids.append(student.uuid)

            chkBoxItem = QtWidgets.QTableWidgetItem()
            chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
            self.ASheet.studentAttendanceTable.setItem(row_insert, 1, chkBoxItem)
        self.ASheet.studentAttendanceTable.resizeColumnsToContents()

    def load_new_date(self):
        date = self.ASheet.attendanceCalendar.selectedDate().toString("dd-MM-yyyy")
        if date in self.attendanceDictionary.attendance_sheets:
            self.uncheck_names()
            self.load_presence(self.attendanceDictionary.attendance_sheets[date])
        else:
            self.uncheck_names()

    def uncheck_names(self):
        row_count = self.ASheet.studentAttendanceTable.rowCount()
        for row in range(0, row_count):
            self.ASheet.studentAttendanceTable.item(row, 1).setCheckState(QtCore.Qt.Unchecked)

    def __load_attendance(self):
        self.attendanceDictionary.attendance_sheets.clear()  # Erase what's in the list
        GlobalVariables.database.cursor.execute("SELECT * FROM `" + self.tableName + "`")
        results = GlobalVariables.database.cursor.fetchall()
        for row in results:
            self.attendanceDictionary.attendance_sheets[row[0]] = row[1]

    def save_attendance(self):
        row_count = self.ASheet.studentAttendanceTable.rowCount()
        output = []

        for row in range(0, row_count):
            if self.ASheet.studentAttendanceTable.item(row, 1).checkState() == QtCore.Qt.Checked:
                output.append(self.student_uuids[row])

        output_string = ';'.join(output)
        date = self.ASheet.attendanceCalendar.selectedDate().toString("dd-MM-yyyy")
        # This is where we find the date in the GlobalVariables.database.
        self.attendanceDictionary.attendance_sheets[date] = output_string

        for i in self.attendanceDictionary.attendance_sheets:
            # i is the date, attendanceDicctionry[i] is the list of students
            print(i, self.attendanceDictionary.attendance_sheets[i])

            # if the date exists, we update it's entry in the GlobalVariables.database.
            results = GlobalVariables.database.connection.execute("SELECT * FROM `" + self.tableName + "` WHERE date='" + i + "' ;")
            GlobalVariables.database.connection.commit()
            if results.rowcount>0:
                # Then this date exists.
                query = "UPDATE " + self.tableName + " SET students = '" + str(self.attendanceDictionary[i]) + "' WHERE date = " + str(i) + ";"
                print(query)
                GlobalVariables.database.cursor.execute(query)
                GlobalVariables.database.connection.commit()
            # Else, we INSERT
            else:
                # Add database entry
                GlobalVariables.database.connection.execute("INSERT INTO `" + str(self.tableName) + "` VALUES('" + str(i) + "', '" + str(self.attendanceDictionary.attendance_sheets[i]) + "')")
                GlobalVariables.database.connection.commit()
