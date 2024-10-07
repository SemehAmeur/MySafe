import sqlite3

from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem

from UI.ui_history import Ui_History
from encdec import EncryptDecrypt


class History(QWidget, Ui_History):
    def __init__(self, app, username):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.show()
        self.username = username
