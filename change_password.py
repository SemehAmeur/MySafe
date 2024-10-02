import hashlib

from PySide6.QtWidgets import QWidget, QMessageBox
from UI.ui_change_password import Ui_createAccountForm
import sqlite3


class ChangePassword(QWidget, Ui_createAccountForm):
    def __init__(self, app, user):
        super().__init__()
        self.user = user
        self.setupUi(self)
        self.app = app
        self.show()
        self.updatePasswordPushButton.clicked.connect(self.update_password_btn)


    def update_password_btn(self):
        if self.oldPasswordLineEdit.text() != '' and self.newPasswordLineEdit.text() != '' and self.retypePasswordLineEdit.text() != '':

            if self.newPasswordLineEdit.text() == self.retypePasswordLineEdit.text():
                # connecting to the db
                try:
                    statement = 'SELECT user_password FROM users WHERE user_name = "' + self.user + '"'
                    connection = sqlite3.connect("safeconfig.db")
                    cursor = connection.cursor()

                    cursor.execute(statement)
                    output = cursor.fetchall()
                    connection.commit()
                    connection.close()

                    # Store the password into a variable to make it less writing
                    old_password = self.oldPasswordLineEdit.text()
                    if hashlib.sha256(old_password.encode()).hexdigest() != output[0][0]:

                        ret = QMessageBox.critical(self, 'Invalid Information',
                                                   'Old Password is incorrect',
                                                   QMessageBox.Retry | QMessageBox.Cancel)
                        self.oldPasswordLineEdit.setText('')
                        self.retypePasswordLineEdit.setText('')
                        self.newPasswordLineEdit.setText('')
                        if ret == QMessageBox.Cancel:
                            self.hide()

                    else:
                        QMessageBox.information(self, 'Password was updated successfully',
                                                'The Password was updated successfully',
                                                QMessageBox.Ok)
                        # update the data base
                        try:
                            statement = ('UPDATE users SET user_password = "'
                                         + hashlib.sha256((self.newPasswordLineEdit.text()).encode()).hexdigest() +
                                         '" WHERE user_name = "' + self.user + '"')
                            connection = sqlite3.connect("safeconfig.db")
                            cursor = connection.cursor()
                            cursor.execute(statement)
                            connection.commit()
                            connection.close()


                        except:
                            QMessageBox.critical(self, 'Error',
                                                 'An error occured while udating the password',
                                                 QMessageBox.Ok)
                        self.oldPasswordLineEdit.setText('')
                        self.retypePasswordLineEdit.setText('')
                        self.newPasswordLineEdit.setText('')
                        # Hide the updating password window
                        self.hide()


                except:
                    QMessageBox.critical(self, 'Error',
                                         'Problem while connecting to the database',
                                         QMessageBox.Ok)
                    self.oldPasswordLineEdit.setText('')
                    self.retypePasswordLineEdit.setText('')
                    self.newPasswordLineEdit.setText('')
                    self.hide()

            else:
                ret = QMessageBox.critical(self, 'Unmatched Data',
                                           'Verify that you inserted all data correctly',
                                           QMessageBox.Ok | QMessageBox.Cancel)
                self.oldPasswordLineEdit.setText('')
                self.newPasswordLineEdit.setText('')
                self.retypePasswordLineEdit.setText('')
                if ret == QMessageBox.Cancel:
                    self.hide()
        else:
            # one at least is written
            if self.oldPasswordLineEdit.text() != '':
                # Both new password and retype password fields are empty
                if self.newPasswordLineEdit.text() == '' and self.retypePasswordLineEdit.text() == '':
                    ret = QMessageBox.critical(self, 'Missing Information',
                                               'Insert the new Password and retype it',
                                               QMessageBox.Ok | QMessageBox.Cancel)
                    if ret == QMessageBox.Cancel:
                        self.oldPasswordLineEdit.setText('')
                        self.hide()

                # new password field is empty
                elif self.newPasswordLineEdit.text() == '' and self.retypePasswordLineEdit.text() != '':
                    ret = QMessageBox.critical(self, 'Missing information',
                                               'Insert the new Password',
                                               QMessageBox.OK | QMessageBox.Cancel)
                    if ret == QMessageBox.Cancel:
                        self.oldPasswordLineEdit.setText('')
                        self.retypePasswordLineEdit.setText('')
                        self.hide()

                # Retype password field is empty
                elif self.newPasswordLineEdit.text() != '' and self.retypePasswordLineEdit.text() == '':
                    ret = QMessageBox.critical(self, 'Missing Information',
                                               'Retype your new Password',
                                               QMessageBox.Ok | QMessageBox.Cancel)
                    if ret == QMessageBox.Cancel:
                        self.oldPasswordLineEdit.setText('')
                        self.newPasswordLineEdit.setText('')
                        self.hide()


            else:
                # The new password field is empty
                ret = QMessageBox.critical(self, 'Missing Information',
                                           'Insert your old Password',
                                           QMessageBox.Ok | QMessageBox.Cancel)
                if ret == QMessageBox.Cancel:
                    self.newPasswordLineEdit.setText('')
                    self.retypePasswordLineEdit.setText('')
                    self.hide()
