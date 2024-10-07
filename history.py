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

        self.preview_history()

    def preview_history(self):
        print(self.username)
        stamtment = '''SELECT * FROM activities WHERE user_name = ?'''
        connection = sqlite3.connect('safeconfig.db')
        cursor = connection.cursor()
        param = tuple(self.username)
        cursor.execute(stamtment, param)
        output = cursor.fetchall()
        connection.commit()
        connection.close()
        for el in output:
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            self.tableWidget.setItem(row_position, 0, QTableWidgetItem((el[1])))
            self.tableWidget.setItem(row_position, 1, QTableWidgetItem((el[2])))
            self.tableWidget.setItem(row_position, 2, QTableWidgetItem((el[3])))
            self.tableWidget.setItem(row_position, 3, QTableWidgetItem((el[4])))

