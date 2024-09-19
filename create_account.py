import hashlib
from PySide6.QtWidgets import QWidget, QMessageBox
from UI.ui_createaccount import Ui_CreateAccount
import sqlite3


class CreateAccount(QWidget, Ui_CreateAccount):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.show()
        self.createAccountPushButton.clicked.connect(self.create_account)

    def create_account(self):
        if (self.usernameLineEdit.text() != "" and self.passwordLineEdit.text() != ""
                and self.retypePasswordLineEdit.text() != ""):
            if self.passwordLineEdit.text() == self.retypePasswordLineEdit.text():
                if not self.exist(self.usernameLineEdit.text()):
                    input_pass = self.passwordLineEdit.text()
                    param = [self.usernameLineEdit.text(), hashlib.sha256(input_pass.encode()).hexdigest()]

                    params = tuple(param)
                    statement = "INSERT INTO users VALUES (NULL, ?, ?)"

                    # Connecting and executing statement to the DataBase
                    connection = sqlite3.connect("safeconfig.db")
                    cursor = connection.cursor()
                    cursor.execute(statement, params)
                    connection.commit()
                    # Close the connection
                    connection.close()
                    self.usernameLineEdit.setText("")
                    self.passwordLineEdit.setText("")
                    self.retypePasswordLineEdit.setText("")
                    self.hide()
                else:
                    QMessageBox().critical(self, 'Pick up an other Username',
                                           'The Username that you chose already exists Please choose an other Username',
                                           QMessageBox.Ok)
                    self.usernameLineEdit.setText("")
                    self.passwordLineEdit.setText("")
                    self.retypePasswordLineEdit.setText("")
            else:
                QMessageBox().critical(self, "Passwords doesn't match",
                                       'Please make sure you type in the same password twice',
                                       QMessageBox.Ok)
                self.passwordLineEdit.setText('')
                self.retypePasswordLineEdit.setText('')
        else:
            ret = QMessageBox().critical(self, 'Empty inputs',
                                         'Please make sure to fill in all the fields',
                                         QMessageBox.Ok)

