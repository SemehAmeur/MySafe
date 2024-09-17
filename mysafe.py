import sys
from PySide6.QtWidgets import QApplication
from login import Login

#dat = databaseclass()
app = QApplication(sys.argv)
window = Login(app)
app.exec()