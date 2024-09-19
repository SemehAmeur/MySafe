import MainWindow
from create_account import CreateAccount
from UI.ui_login import Ui_Login

import sqlite3

class Login(QWidget, Ui_Login):
    def __init__(self, app):
        super().__init__()
        self.createaccount = None
        self.mymain = None
        self.setupUi(self)
        self.app = app
        self.show()
        self.user = self.usernameLineEdit.text()
        self.createAccountPushButton.clicked.connect(self.create_account)
        self.loginPushButton.clicked.connect(self.connect_btn)
    
    def create_account(self): 
        pass
    def myshow(self): 
        pass
    def connect_btn(self): 
        pass
