import Authentication
import GlobalVariables
import sys

from PyQt5 import QtCore, QtWidgets, uic
from MainDisplay import MainDisplay
from CreateUser import Ui_IGPCreateUser
from Database import Database

class Ui_IGPLogin(object):

    def __init__(self):

        self.IGPLogin = QtWidgets.QDialog()
        self.ui = uic.loadUi('../assets/ui/Login.ui', self.IGPLogin)
        self.IGPLogin.loginButton.clicked.connect(self.login_button_clicked)
        self.IGPLogin.quitButton.clicked.connect(self.IGPLogin.close)
        self.IGPLogin.newUserButton.clicked.connect(self.new_user_button_clicked)

        self.IGPLogin.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.IGPLogin.show()

        self.main_window = None

    def new_user_button_clicked(self):
        self.myOtherWindow = Ui_IGPCreateUser()

    def close_button_clicked(self):
        self.IGPLogin.close()

    def login_button_clicked(self):
        username = self.IGPLogin.usernameField.displayText()
        password = self.IGPLogin.passwordField.text()

        if not username:
            self.bad_input('Error', 'You need to enter a username')
        elif not password:
            self.bad_input('Error', 'You need to enter a password')
        else:
            conn = Authentication.connect_to_db('../databases/users.db')
            Authentication.create_user_table(conn)
            legitimate = Authentication.validate_login_credentials(conn, username, password)

            if not legitimate:
                self.bad_input('Error', 'There is no user with the login credentials you entered.  Please try again.')
            else:
                GlobalVariables.database = Database(username)
                self.IGPLogin.close()
                self.main_window = MainDisplay()
                self.main_window.form.show()

    def bad_input(self, window_text, error_message):
        choice = QtWidgets.QMessageBox.question(self.IGPLogin, window_text, error_message,
                                                QtWidgets.QMessageBox.Cancel)
        if choice:
            pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = Ui_IGPLogin()
    sys.exit(app.exec_())

