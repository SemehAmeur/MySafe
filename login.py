import hashlib

from PySide6.QtWidgets import QWidget, QMessageBox

import MainWindow
from create_account import CreateAccount
from UI.ui_login import Ui_Login

import sqlite3


class Login(QWidget, Ui_Login):
    def __init__(self, app):
        super().__init__()
        self.createaccount = None
        self.mymain = None
        self.setupUi(self)
        self.app = app
        self.show()
        self.user = self.usernameLineEdit.text()
        self.createAccountPushButton.clicked.connect(self.create_account)
        self.loginPushButton.clicked.connect(self.connect_btn)

    def create_account(self):
        self.createaccount = CreateAccount(self.app)
        self.createaccount.show()

    def myshow(self):
        self.show()

    def connect_btn(self):
        # Empty fields
        if self.usernameLineEdit.text() == "" and self.passwordLineEdit.text() == "":
            ret = QMessageBox.warning(self, 'Missing fields',
                                      'insert the username and password',
                                      QMessageBox.Ok | QMessageBox.Close)
            if ret == QMessageBox.Close:
                self.close()

        # Empty username only
        elif self.usernameLineEdit.text() == "":
            ret = QMessageBox.warning(self, 'Missing field',
                                      'Type in your username',
                                      QMessageBox.Ok | QMessageBox.Close)
            if ret == QMessageBox.Close:
                self.close()

        # Empty Password only
        elif self.passwordLineEdit.text() == "":
            ret = QMessageBox.warning(self, 'Missing fields',
                                      'Type in your password',
                                      QMessageBox.Ok | QMessageBox.Close)
            if ret == QMessageBox.Close:
                self.close()

        else:
            try:
                statement = 'SELECT user_password FROM users WHERE user_name = "' + self.usernameLineEdit.text() + '"'
                connection = sqlite3.connect("safeconfig.db")
                cursor = connection.cursor()

                cursor.execute(statement)
                output = cursor.fetchall()
                connection.commit()
                connection.close()

                # Store the password into a variable to make it less writing
                input_pass = self.passwordLineEdit.text()

                if hashlib.sha256(input_pass.encode()).hexdigest() == output[0][0]:

                    self.mymain = MainWindow.MainWindow(self.app, self.usernameLineEdit.text(), self.usernameLineEdit.text(), self)

                    self.hide()
                    self.usernameLineEdit.setText('')
                    self.passwordLineEdit.setText('')


                else:
                    QMessageBox.critical(self, 'Invalid Information',
                                         'Username or Password wes/were incorrect',
                                         QMessageBox.Ok)
                    self.usernameLineEdit.setText('')
                    self.passwordLineEdit.setText('')

            except:
                QMessageBox.critical(self, 'Invalid Information',
                                     'Username or Password wes/were incorrect',
                                     QMessageBox.Ok)
                self.usernameLineEdit.setText('')
                self.passwordLineEdit.setText('')
