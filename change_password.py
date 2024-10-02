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