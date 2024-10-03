from PySide6.QtWidgets import QWidget, QMessageBox
from UI.ui_check_data import Ui_CheckData

from Update_Data import UpdateData
import sqlite3



class CheckData(QWidget, Ui_CheckData):
    def __init__(self, app, oldConsoleWindow, data_to_check_id, decryptPass):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.show()
        self.modify_data = None
        self.data_to_check_id = data_to_check_id
        self.oldConsoleWindow = oldConsoleWindow
        self.output = None
        self.preview_data()
        self.copyPasswordPushButton.clicked.connect(self.copy_pass_word_btn)
        self.deletePushButton.clicked.connect(self.delete_password_btn)
        self.modifyPushButton.clicked.connect(self.modify_btn)