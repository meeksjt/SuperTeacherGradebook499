from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys

class AttendanceSheet(object):

    def __init__(self):
        self.ASheet = QtWidgets.QDialog()
        self.ui = uic.loadUi('Attendance.ui', self.ASheet)
        self.ASheet.studentAttendanceTable.setHorizontalHeaderLabels(['Student Name', 'Present?'])
        self.add_students(
            ['Georgie', 'Stephanie', 'Georgie', 'Stephanie Hammons', 'Georgie', 'Stephanie', 'Georgie', 'Stephanie'])
        self.ASheet.show()
        self.ASheet.saveAttendanceButton.clicked.connect(self.save_attendance)

    def add_students(self, names):
        for name in names:
            row_insert = self.ASheet.studentAttendanceTable.rowCount()
            self.ASheet.studentAttendanceTable.insertRow(row_insert)
            self.ASheet.studentAttendanceTable.setItem(row_insert, 0, QtWidgets.QTableWidgetItem(name))
            self.ASheet.studentAttendanceTable.setItem(row_insert, 1, QtWidgets.QTableWidgetItem(""))
        self.ASheet.studentAttendanceTable.resizeColumnsToContents()

    def save_attendance(self):
        row_count = self.ASheet.studentAttendanceTable.rowCount()
        output = []

        for row in range(0, row_count):
            try:
                td1 = self.ASheet.studentAttendanceTable.item(row, 0).text()
                td2 = self.ASheet.studentAttendanceTable.item(row, 1).text()
                output.append([td1, td2])
            except:
                break

        student_names = [output[i][0] for i in range(len(output))]
        student_presence = [output[j][1] for j in range(len(output))]

        for i in student_names:
            print(i)
        for j in student_presence:
            print(j)
        students_who_came = []
        for i in range(len(student_names)):
            if student_presence[i] != "":
                students_who_came.append(student_names[i])

        for i in students_who_came:
            print(i)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = AttendanceSheet()
    sys.exit(app.exec_())
