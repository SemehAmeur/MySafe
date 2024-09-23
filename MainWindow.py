from UI.ui_mainwindow import Ui_MainWindow
import sqlite3

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app, user, decryptPass, consoleOldWindow):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.show()
        self.allDataTableWidget.setColumnHidden(0, True)
        self.allDataTableWidget.setColumnHidden(11, True)
        self.db_to_preview()
        self.addPushButton.clicked.connect(self.add_to_db)
        self.generatePasswordPushButton.clicked.connect(self.generate_password_btn)
        self.copyPushButton.clicked.connect(self.copy_pass_word)
        self.deletePushButton.clicked.connect(self.delete_password)
        self.updatePushButton.clicked.connect(self.update_btn)
        self.actionChange_Password.triggered.connect(self.change_password)
        self.actionLog_Out.triggered.connect(self.logout)
        self.actionClose.triggered.connect(self.closemyapp)
        self.actionHowToUse.triggered.connect(self.how_to_use)
        self.actionAbout_this_Software.triggered.connect(self.about_this_software)
        self.visualizeDataPushButton.clicked.connect(self.check_data_btn)
        self.actionHistory.triggered.connect(self.history_btn)
