# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change_password.ui'
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

class Ui_createAccountForm(object):
    def setupUi(self, createAccountForm):
        if not createAccountForm.objectName():
            createAccountForm.setObjectName(u"createAccountForm")
        createAccountForm.resize(216, 129)
        createAccountForm.setMinimumSize(QSize(216, 129))
        createAccountForm.setMaximumSize(QSize(216, 129))
        self.gridLayout = QGridLayout(createAccountForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.oldPasswordLineEdit = QLineEdit(createAccountForm)
        self.oldPasswordLineEdit.setObjectName(u"oldPasswordLineEdit")
        self.oldPasswordLineEdit.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.oldPasswordLineEdit)

        self.newPasswordLineEdit = QLineEdit(createAccountForm)
        self.newPasswordLineEdit.setObjectName(u"newPasswordLineEdit")
        self.newPasswordLineEdit.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.newPasswordLineEdit)

        self.retypePasswordLineEdit = QLineEdit(createAccountForm)
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

        self.updatePasswordPushButton = QPushButton(createAccountForm)
        self.updatePasswordPushButton.setObjectName(u"updatePasswordPushButton")

        self.horizontalLayout.addWidget(self.updatePasswordPushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 1)

        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(createAccountForm)

        QMetaObject.connectSlotsByName(createAccountForm)
    # setupUi

    def retranslateUi(self, createAccountForm):
        createAccountForm.setWindowTitle(QCoreApplication.translate("createAccountForm", u"Change Password", None))
        self.oldPasswordLineEdit.setPlaceholderText(QCoreApplication.translate("createAccountForm", u"Old Password", None))
        self.newPasswordLineEdit.setPlaceholderText(QCoreApplication.translate("createAccountForm", u"New Password", None))
        self.retypePasswordLineEdit.setPlaceholderText(QCoreApplication.translate("createAccountForm", u"Retype The New Password", None))
        self.updatePasswordPushButton.setText(QCoreApplication.translate("createAccountForm", u"Update Password", None))
    # retranslateUi

