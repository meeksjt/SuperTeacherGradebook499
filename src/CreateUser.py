# Finished
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
import Authentication


"""
Class for the GUI Window and operations of user creation
"""


class Ui_IGPCreateUser(object):

    """
    Constructor for user creation
    """
    def __init__(self):

        # Create Window
        self.IGPCreateUser = QtWidgets.QDialog()

        # Display Window
        self.ui = uic.loadUi('../assets/ui/CreateUser.ui', self.IGPCreateUser)
        self.IGPCreateUser.show()

        # Link buttons
        self.IGPCreateUser.quitButton.clicked.connect(self.close_button_clicked)
        self.IGPCreateUser.createAccountButton.clicked.connect(self.create_account_button_clicked)

    def bad_input(self, window_text, error_message):
        choice = QtWidgets.QMessageBox.question(self.IGPCreateUser, window_text, error_message,
                                                QtWidgets.QMessageBox.Cancel)
        if choice:
            pass

    def close_button_clicked(self):
        self.IGPCreateUser.close()

    def create_account_button_clicked(self):
        username = self.IGPCreateUser.usernameField.displayText()
        password = self.IGPCreateUser.passwordField.text()
        verifyPassword = self.IGPCreateUser.verifyPasswordField.text()

        if not username:
            self.bad_input('Error', 'You need to enter a username')
        elif not password:
            self.bad_input('Error', 'You need to enter a password')
        elif not verifyPassword:
            self.bad_input('Error', 'You need to enter a verify password')
        elif password != verifyPassword:
            self.bad_input('Error', 'Your password and verify password do not match!')
        else:
            conn = Authentication.connect_to_db('../databases/users.db')
            Authentication.create_user_table(conn)
            added = Authentication.add_login_credentials(conn, username, password)

            if not added:
                self.bad_input('Error', 'User is already in the database.\nPlease select a new username.')
            else:
                print("Credentials added")
                print("This is where we return to our Login Gui Frame")
                self.close_button_clicked()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = Ui_IGPCreateUser()
    sys.exit(app.exec_())

