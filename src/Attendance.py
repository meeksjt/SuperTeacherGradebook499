from PyQt5 import QtCore, QtGui, QtWidgets, uic
from Student import Student
import sys
from GlobalVariables import *

"""
Wrapper class for a dictionary that maps attendance dates (string) to the students that
were present for that date (string delimited by semicolon)
"""


class AttendanceDictionary(object):
	def __init__(self):
		self.attendance_sheets = {}

	def add_sheet(self, dateString, studentsString):
		self.attendance_sheets[dateString] = studentsString


"""
Class for an individual Attendance Sheet
"""


class AttendanceSheet(object):

	def __init__(self, attendanceDictionary, studentList, tablePrefix):
		self.prefix = tablePrefix;
		self.ASheet = QtWidgets.QDialog()
		self.ui = uic.loadUi('Attendance.ui', self.ASheet)
		self.ASheet.studentAttendanceTable.setHorizontalHeaderLabels(['Student Name', 'Present?'])
		self.attendanceDictionary = attendanceDictionary.attendance_sheets



		# Get the current date and add our list of students
		current_date = self.ASheet.attendanceCalendar.selectedDate().toString("dd-MM-yyyy")
		self.add_students(studentList)
		self.tableName = tablePrefix + "_attendance"
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
	def add_students(self, students):
		for student in students:
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
			self.attendanceDictionary[row[0]] = row[1];

	def save_attendance(self):
		row_count = self.ASheet.studentAttendanceTable.rowCount()
		output = []

		for row in range(0, row_count):
			if self.ASheet.studentAttendanceTable.item(row, 1).checkState() == QtCore.Qt.Checked:
				output.append(self.ASheet.studentAttendanceTable.item(row, 0).text())

		output_string = ';'.join(output)
		date = self.ASheet.attendanceCalendar.selectedDate().toString("dd-MM-yyyy")
		#This is where we find the date in the database.
		self.attendanceDictionary[date] = output_string

		for i in self.attendanceDictionary:
			#i is the date, attendanceDicctionry[i] is the list of students
			print(i, self.attendanceDictionary[i])

			#if the date exists, we update it's entry in the database.
			results = connection.execute("SELECT * FROM `" + self.tableName + "` WHERE date='" + i + "' ;")
			connection.commit()
			if results.rowcount>0:
				#Then this date exists.
				query = "UPDATE " + self.tableName + " SET students = '" + str(self.attendanceDictionary[i]) + "' WHERE date = " + str(i) + ";"
				print(query)
				cursor.execute(query)
				connection.commit();
			#Else, we INSERT
			else:
				#Add database entry
				connection.execute("INSERT INTO " + str(self.tableName) + " VALUES('" + str(i) + "', '" + str(self.attendanceDictionary[i]) + "')")
				connection.commit()



if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	ad = AttendanceDictionary()
	ad.add_sheet('26-03-2018', 'Tyler Meeks;Samantha Boggs')
	main = AttendanceSheet(ad, [Student('', 1, 'Tyler Meeks', 'jtm0036@uah.edu'), Student('', 2, 'Samantha Boggs', 'sjb0034@uah.edu')], "YourMom")
	sys.exit(app.exec_())
