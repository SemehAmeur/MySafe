# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(216, 124)
        Login.setMinimumSize(QSize(216, 124))
        Login.setMaximumSize(QSize(216, 124))
        self.gridLayout = QGridLayout(Login)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.usernameLineEdit = QLineEdit(Login)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")

        self.verticalLayout.addWidget(self.usernameLineEdit)

        self.passwordLineEdit = QLineEdit(Login)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.passwordLineEdit)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.createAccountPushButton = QPushButton(Login)
        self.createAccountPushButton.setObjectName(u"createAccountPushButton")

        self.horizontalLayout.addWidget(self.createAccountPushButton)

        self.horizontalSpacer = QSpacerItem(193, 21, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.loginPushButton = QPushButton(Login)
        self.loginPushButton.setObjectName(u"loginPushButton")

        self.horizontalLayout.addWidget(self.loginPushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 1)

        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Login", None))
        self.usernameLineEdit.setPlaceholderText(QCoreApplication.translate("Login", u"User Name", None))
        self.passwordLineEdit.setPlaceholderText(QCoreApplication.translate("Login", u"Password", None))
        self.createAccountPushButton.setText(QCoreApplication.translate("Login", u"Create Account", None))
        self.loginPushButton.setText(QCoreApplication.translate("Login", u"Log In", None))
    # retranslateUi

