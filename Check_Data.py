import pyperclip
from PySide6.QtWidgets import QWidget, QMessageBox
from UI.ui_check_data import Ui_CheckData

from Update_Data import UpdateData
import sqlite3

from encdec import EncryptDecrypt


class CheckData(QWidget, Ui_CheckData):
    def __init__(self, app, oldConsoleWindow, data_to_check_id, decryptPass):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.show()
        self.modify_data = None
        self.data_to_check_id = data_to_check_id
        self.oldConsoleWindow = oldConsoleWindow
        self.decryptPass = decryptPass
        self.output = None
        self.preview_data()
        self.copyPasswordPushButton.clicked.connect(self.copy_pass_word_btn)
        self.deletePushButton.clicked.connect(self.delete_password_btn)
        self.modifyPushButton.clicked.connect(self.modify_btn)

    def preview_data(self):
        statement = 'SELECT * FROM passwords WHERE password_id = ?'
        connection = sqlite3.connect("safeconfig.db")
        cursor = connection.cursor()
        param = (self.data_to_check_id,)
        cursor.execute(statement, param)
        self.output = cursor.fetchone()
        connection.commit()
        connection.close()
        tableWidgetDict = {1: self.websiteLabel, 2: self.linkLabel, 3: self.linkedWebsiteLabel, 4: self.mailLablel,
                           5: self.secondMailLabel, 6: self.usernameLabel, 7: self.firstNameLabel,
                           8: self.lastNameLabel, 9: self.birthdateLabel, 10: self.phoneNumberLabel,
                           11: self.passwordLabel, 12: self.securityQuestionLabel, 13: self.ansewerLabel,
                           14: self.mainDeviseLabel, 15: self.purposeOfUseLabel, 16: self.notePlainTextEdit}
        cr = EncryptDecrypt(self.decryptPass)
        for i in range(1, 16):
            tableWidgetDict[i].setText(cr.decrypt(self.output[i]))
        self.notePlainTextEdit.setPlainText(cr.decrypt(self.output[16]))

    def copy_pass_word_btn(self):
        pyperclip.copy(self.passwordLabel.text())


    def delete_password_btn(self):
        pass

    def modify_btn(self):
        pass
    def update_a_row(self):
        pass
