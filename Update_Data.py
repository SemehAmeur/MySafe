import sqlite3

import pyperclip
from PySide6.QtCore import QDate
from PySide6.QtWidgets import QWidget, QMessageBox

import PassWordGenerator
from UI.ui_update_data import Ui_UpdateData
from encdec import EncryptDecrypt


class UpdateData(QWidget, Ui_UpdateData):
    def __init__(self, app, data_to_modify, decryptPass, check_data_console):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.show()
        self.check_data_console = check_data_console
        self.data_to_modify = data_to_modify
        self.decryptPass = decryptPass
        self.db_to_preview()
        self.generatePasswordPushButton.clicked.connect(self.generate_password_btn)
        self.updatePushButton.clicked.connect(self.update_btn)


    def db_to_preview(self):
        tableWidgetDict = {1: self.websiteNameLineEdit, 2: self.websiteLinkLineEdit, 3: self.linkedWebsiteLineEdit,
                           4: self.emailLineEdit,
                           5: self.secondEmailLineEdit, 6: self.usernameLineEdit, 7: self.firstNameLineEdit,
                           8: self.lastNameLineEdit, 9: self.birthDateEdit, 10: self.phoneNumerLineEdit,
                           11: self.passwordLineEdit, 12: self.securityQuestionLineEdit, 13: self.answerLineEdit,
                           14: self.mainDeviceLineEdit, 15: self.purposeOfUseLineEdit, 16: self.notePlainTextEdit}
        cr = EncryptDecrypt(self.decryptPass)
        for i in range(1, 16):
            if i != 9:
                tableWidgetDict[i].setText(cr.decrypt(self.data_to_modify[i]))
        self.notePlainTextEdit.setPlainText(cr.decrypt(self.data_to_modify[16]))
        d = cr.decrypt(self.data_to_modify[9])

        self.birthDateEdit.setDate(QDate(int(d[-4:]), int(d[3:5]), int(d[:2])))

    def check_inputs(self):
        param = [self.websiteNameLineEdit.text(), self.websiteLinkLineEdit.text(), self.linkedWebsiteLineEdit.text(),
                 self.emailLineEdit.text(), self.secondEmailLineEdit.text(), self.usernameLineEdit.text(),
                 self.firstNameLineEdit.text(), self.lastNameLineEdit.text(), self.birthDateEdit.text(),
                 self.phoneNumerLineEdit.text(), self.passwordLineEdit.text(), self.securityQuestionLineEdit.text(),
                 self.answerLineEdit.text(), self.mainDeviceLineEdit.text(), self.purposeOfUseLineEdit.text(),
                 self.notePlainTextEdit.toPlainText()]

        if (self.websiteNameLineEdit.text() != "" and (
                self.emailLineEdit.text() != "" or self.usernameLineEdit.text() != "") and
                self.passwordLineEdit.text() != ""):
            return True, param
        else:
            QMessageBox.critical(self, 'Hint',
                                 'Please make sure to insert a website name, \na username or an email, and a password.',
                                 QMessageBox.Ok)
            return False, None

    def update_btn(self):
        ret = QMessageBox.critical(self, 'Saving Changes',
                             'Are you sure that you want to save the changes',
                             QMessageBox.Yes | QMessageBox.No)
        if ret == QMessageBox.Yes:
            # Check for the inputs and get result
            bol, param = self.check_inputs()
            if bol:
                # crypt data
                cr = EncryptDecrypt(self.decryptPass)
                # Loop through the list of data to store inside the DB
                self.data_to_modify = list(self.data_to_modify)
                for i in range(len(param)):
                    self.data_to_modify[i + 1] = cr.encrypt(param[i])

                params = tuple(self.data_to_modify[1:-1])

                connection = sqlite3.Connection('safeconfig.db')
                cursor = connection.cursor()
                # Inserting Data inside the DataBase
                # statement = "INSERT INTO passwords VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
                statement = (
                    'UPDATE passwords SET password_website = ?, password_link = ?, password_linked_website = ?, '
                    'password_mail = ?, password_second_mail = ?, password_username = ?, password_first_name = '
                    '?, password_last_name = ?, password_birthdate = ?, password_phone = ?, password_password = ?,'
                    'password_security_question = ?, password_answer = ?, password_main_device = ?, '
                    'password_purpose_of_use = ?, password_note = ?  WHERE password_id = ?')

                params = params + (self.data_to_modify[0],)

                cursor.execute(statement, params)
                connection.commit()
                connection.close()

                self.check_data_console.preview_data()
                self.check_data_console.update_a_row()
                self.hide()
        elif ret == QMessageBox.No:
            re = QMessageBox.critical(self, 'Proceed Modification',
                                      'Do you want to continue the Modification?',
                                      QMessageBox.Yes | QMessageBox.No)
            if re == QMessageBox.No:
                self.hide()



    def generate_password_btn(self):
        lowercasecheckbox = self.lowerCaseCheckBox.isChecked()
        uppercasecheckbox = self.upperCaseCheckBox.isChecked()
        numberscasecheckbox = self.numbersCheckBox.isChecked()
        specialdigitscheckbox = self.specialDigitsCheckBox.isChecked()

        length = int(self.lengthPasswordSpinBox.text())

        if lowercasecheckbox or uppercasecheckbox or numberscasecheckbox or specialdigitscheckbox:
            ret = QMessageBox.critical(self, 'Attention',
                                       'Are you sure that you want to replace the old password?',
                                       QMessageBox.Yes | QMessageBox.No)
            if ret == QMessageBox.Yes:
                passwo = PassWordGenerator.PassWordGenerator()
                passtring = passwo.passgenerate(length, lowercasecheckbox, uppercasecheckbox, numberscasecheckbox,
                                                specialdigitscheckbox)

                # Insert the generated password into the password line edit (UI)
                self.passwordLineEdit.setText(passtring)

                # Copy the generated password to the clipboard
                pyperclip.copy(passtring)
