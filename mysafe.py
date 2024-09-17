import sys
from PySide6.QtWidgets import QApplication
from login import Login
from mydata import Safecon

dat = Safecon()
app = QApplication(sys.argv)
window = Login(app)
app.exec()
