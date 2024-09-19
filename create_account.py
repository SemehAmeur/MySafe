from PySide6.QtWidgets import QWidget, QMessageBox
from UI.ui_createaccount import Ui_CreateAccount

class CreateAccount(QWidget, Ui_CreateAccount):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.show()
