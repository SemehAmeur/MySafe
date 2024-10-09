import sqlite3

import pyperclip
from PySide6.QtCore import QDate
from PySide6.QtWidgets import QWidget, QMessageBox


class UpdateData(QWidget, Ui_UpdateData):
    def __init__(self, app, data_to_modify, decryptPass, check_data_console):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.show()
        self.check_data_console = check_data_console
        self.data_to_modify = data_to_modify