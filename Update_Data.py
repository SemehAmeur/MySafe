import sqlite3

from PySide6.QtCore import QDate
from PySide6.QtWidgets import QWidget, QMessageBox

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
