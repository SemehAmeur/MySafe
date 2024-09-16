# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_account.ui'
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

class Ui_CreateAccount(object):
    def setupUi(self, CreateAccount):
        if not CreateAccount.objectName():
            CreateAccount.setObjectName(u"CreateAccount")
        CreateAccount.resize(216, 129)
        CreateAccount.setMinimumSize(QSize(216, 124))
        CreateAccount.setMaximumSize(QSize(216, 129))
        self.gridLayout = QGridLayout(CreateAccount)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.usernameLineEdit = QLineEdit(CreateAccount)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")

        self.verticalLayout.addWidget(self.usernameLineEdit)

        self.passwordLineEdit = QLineEdit(CreateAccount)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.passwordLineEdit)

        self.retypePasswordLineEdit = QLineEdit(CreateAccount)
        self.retypePasswordLineEdit.setObjectName(u"retypePasswordLineEdit")
        self.retypePasswordLineEdit.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.retypePasswordLineEdit)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.createAccountPushButton = QPushButton(CreateAccount)
        self.createAccountPushButton.setObjectName(u"createAccountPushButton")

        self.horizontalLayout.addWidget(self.createAccountPushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 1)

        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(CreateAccount)

        QMetaObject.connectSlotsByName(CreateAccount)
    # setupUi

    def retranslateUi(self, CreateAccount):
        CreateAccount.setWindowTitle(QCoreApplication.translate("CreateAccount", u"Create Account", None))
        self.usernameLineEdit.setPlaceholderText(QCoreApplication.translate("CreateAccount", u"User Name", None))
        self.passwordLineEdit.setPlaceholderText(QCoreApplication.translate("CreateAccount", u"Password", None))
        self.retypePasswordLineEdit.setPlaceholderText(QCoreApplication.translate("CreateAccount", u"Retype Password", None))
        self.createAccountPushButton.setText(QCoreApplication.translate("CreateAccount", u"Create Account", None))
    # retranslateUi

