from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys


class CourseCreationThird(object):

    def __init__(self):

        col_headers = ['Category Name', 'Category Weight']
        self.CCThird = QtWidgets.QDialog()
        self.ui = uic.loadUi('CourseCreationThird.ui', self.CCThird)
        self.CCThird.categoryTable.setHorizontalHeaderLabels(col_headers)
        self.CCThird.show()
        self.CCThird.addCategoryButton.clicked.connect(self.add_category)
        self.CCThird.createCourseButton.clicked.connect(self.save_table_data)
        self.CCThird.removeSelectedCategory.clicked.connect(self.remove_category)

    def remove_category(self):
        row = self.CCThird.categoryTable.currentRow()
        self.CCThird.categoryTable.removeRow(row)

    def add_category(self):
        self.CCThird.categoryTable.insertRow(self.CCThird.categoryTable.rowCount())

    def save_table_data(self):
        row_count = self.CCThird.categoryTable.rowCount()
        output = []

        for row in range(0, row_count):
            try:
                td1 = self.CCThird.categoryTable.item(row, 0).text()
                td2 = self.CCThird.categoryTable.item(row, 1).text()

                if td1 != "" and td2 != "":
                    output.append([td1, td2])
            except:
                break

        valid = self.error_checking(output)

    def error_checking(self, user_input):
        print("Got here")
        category_names = [user_input[i][0] for i in range(len(user_input))]
        category_weights = [user_input[j][1] for j in range(len(user_input))]

        # Check category weights
        weight_sum = 0
        for i in category_weights:
            s = i.replace('%', '')

            # Make sure we are adding numbers
            try:
                weight_sum += float(s.strip())
            except ValueError:
                self.bad_input('Error', 'Category Weights need to be numerical values!')
                return False

        # Make sure that the category weights sum to 100
        if weight_sum != 100:
            self.bad_input('Error', 'Category Weights need to total 100')
            return False

    """
    Function for telling the user they entered bad input
    Parameters:
        window_text: (string) the name of the window
        error_message: (string) the error message that is displayed to the user
    """

    def bad_input(self, window_text, error_message):
        choice = QtWidgets.QMessageBox.question(self.CCThird, window_text, error_message,
                                                QtWidgets.QMessageBox.Cancel)
        if choice:
            pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = CourseCreationThird()
    sys.exit(app.exec_())
