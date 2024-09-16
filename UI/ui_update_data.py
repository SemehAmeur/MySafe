# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'update_data.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QGridLayout,
    QHBoxLayout, QLayout, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_UpdateData(object):
    def setupUi(self, UpdateData):
        if not UpdateData.objectName():
            UpdateData.setObjectName(u"UpdateData")
        UpdateData.resize(862, 246)
        self.gridLayout_2 = QGridLayout(UpdateData)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.websiteNameLineEdit = QLineEdit(UpdateData)
        self.websiteNameLineEdit.setObjectName(u"websiteNameLineEdit")

        self.gridLayout.addWidget(self.websiteNameLineEdit, 0, 0, 1, 1)

        self.emailLineEdit = QLineEdit(UpdateData)
        self.emailLineEdit.setObjectName(u"emailLineEdit")

        self.gridLayout.addWidget(self.emailLineEdit, 0, 3, 1, 1)

        self.passwordLineEdit = QLineEdit(UpdateData)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")

        self.gridLayout.addWidget(self.passwordLineEdit, 3, 0, 1, 1)

        self.websiteLinkLineEdit = QLineEdit(UpdateData)
        self.websiteLinkLineEdit.setObjectName(u"websiteLinkLineEdit")

        self.gridLayout.addWidget(self.websiteLinkLineEdit, 0, 1, 1, 1)

        self.lastNameLineEdit = QLineEdit(UpdateData)
        self.lastNameLineEdit.setObjectName(u"lastNameLineEdit")

        self.gridLayout.addWidget(self.lastNameLineEdit, 2, 2, 1, 1)

        self.mainDeviceLineEdit = QLineEdit(UpdateData)
        self.mainDeviceLineEdit.setObjectName(u"mainDeviceLineEdit")

        self.gridLayout.addWidget(self.mainDeviceLineEdit, 3, 3, 1, 1)

        self.securityQuestionLineEdit = QLineEdit(UpdateData)
        self.securityQuestionLineEdit.setObjectName(u"securityQuestionLineEdit")

        self.gridLayout.addWidget(self.securityQuestionLineEdit, 3, 1, 1, 1)

        self.answerLineEdit = QLineEdit(UpdateData)
        self.answerLineEdit.setObjectName(u"answerLineEdit")

        self.gridLayout.addWidget(self.answerLineEdit, 3, 2, 1, 1)

        self.purposeOfUseLineEdit = QLineEdit(UpdateData)
        self.purposeOfUseLineEdit.setObjectName(u"purposeOfUseLineEdit")

        self.gridLayout.addWidget(self.purposeOfUseLineEdit, 3, 4, 1, 1)

        self.firstNameLineEdit = QLineEdit(UpdateData)
        self.firstNameLineEdit.setObjectName(u"firstNameLineEdit")

        self.gridLayout.addWidget(self.firstNameLineEdit, 2, 1, 1, 1)

        self.linkedWebsiteLineEdit = QLineEdit(UpdateData)
        self.linkedWebsiteLineEdit.setObjectName(u"linkedWebsiteLineEdit")

        self.gridLayout.addWidget(self.linkedWebsiteLineEdit, 0, 2, 1, 1)

        self.phoneNumerLineEdit = QLineEdit(UpdateData)
        self.phoneNumerLineEdit.setObjectName(u"phoneNumerLineEdit")

        self.gridLayout.addWidget(self.phoneNumerLineEdit, 2, 4, 1, 1)

        self.usernameLineEdit = QLineEdit(UpdateData)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")

        self.gridLayout.addWidget(self.usernameLineEdit, 2, 0, 1, 1)

        self.secondEmailLineEdit = QLineEdit(UpdateData)
        self.secondEmailLineEdit.setObjectName(u"secondEmailLineEdit")

        self.gridLayout.addWidget(self.secondEmailLineEdit, 0, 4, 1, 1)

        self.birthDateEdit = QDateEdit(UpdateData)
        self.birthDateEdit.setObjectName(u"birthDateEdit")

        self.gridLayout.addWidget(self.birthDateEdit, 2, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.notePlainTextEdit = QPlainTextEdit(UpdateData)
        self.notePlainTextEdit.setObjectName(u"notePlainTextEdit")

        self.verticalLayout.addWidget(self.notePlainTextEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.specialDigitsCheckBox = QCheckBox(UpdateData)
        self.specialDigitsCheckBox.setObjectName(u"specialDigitsCheckBox")
        self.specialDigitsCheckBox.setChecked(True)

        self.horizontalLayout.addWidget(self.specialDigitsCheckBox)

        self.numbersCheckBox = QCheckBox(UpdateData)
        self.numbersCheckBox.setObjectName(u"numbersCheckBox")
        self.numbersCheckBox.setChecked(True)

        self.horizontalLayout.addWidget(self.numbersCheckBox)

        self.upperCaseCheckBox = QCheckBox(UpdateData)
        self.upperCaseCheckBox.setObjectName(u"upperCaseCheckBox")
        self.upperCaseCheckBox.setChecked(True)

        self.horizontalLayout.addWidget(self.upperCaseCheckBox)

        self.lowerCaseCheckBox = QCheckBox(UpdateData)
        self.lowerCaseCheckBox.setObjectName(u"lowerCaseCheckBox")
        self.lowerCaseCheckBox.setChecked(True)

        self.horizontalLayout.addWidget(self.lowerCaseCheckBox)

        self.lengthPasswordSpinBox = QSpinBox(UpdateData)
        self.lengthPasswordSpinBox.setObjectName(u"lengthPasswordSpinBox")
        self.lengthPasswordSpinBox.setMinimum(1)
        self.lengthPasswordSpinBox.setValue(8)

        self.horizontalLayout.addWidget(self.lengthPasswordSpinBox)

        self.generatePasswordPushButton = QPushButton(UpdateData)
        self.generatePasswordPushButton.setObjectName(u"generatePasswordPushButton")

        self.horizontalLayout.addWidget(self.generatePasswordPushButton)

        self.updatePushButton = QPushButton(UpdateData)
        self.updatePushButton.setObjectName(u"updatePushButton")

        self.horizontalLayout.addWidget(self.updatePushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 5)
        self.verticalLayout.setStretch(2, 1)

        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(UpdateData)

        QMetaObject.connectSlotsByName(UpdateData)
    # setupUi

    def retranslateUi(self, UpdateData):
        UpdateData.setWindowTitle(QCoreApplication.translate("UpdateData", u"Update Informations", None))
        self.websiteNameLineEdit.setPlaceholderText(QCoreApplication.translate("UpdateData", u"Website", None))
        self.emailLineEdit.setPlaceholderText(QCoreApplication.translate("UpdateData", u"E-mail", None))
        self.passwordLineEdit.setPlaceholderText(QCoreApplication.translate("UpdateData", u"Password", None))
        self.websiteLinkLineEdit.setText("")
        self.websiteLinkLineEdit.setPlaceholderText(QCoreApplication.translate("UpdateData", u"Link", None))
        self.lastNameLineEdit.setPlaceholderText(QCoreApplication.translate("UpdateData", u"Last Name", None))
        self.mainDeviceLineEdit.setPlaceholderText(QCoreApplication.translate("UpdateData", u"Main Device", None))
        self.securityQuestionLineEdit.setPlaceholderText(QCoreApplication.translate("UpdateData", u"Security Question 1", None))
        self.answerLineEdit.setPlaceholderText(QCoreApplication.translate("UpdateData", u"Answer 1", None))
        self.purposeOfUseLineEdit.setPlaceholderText(QCoreApplication.translate("UpdateData", u"Purpose of Use", None))
        self.firstNameLineEdit.setPlaceholderText(QCoreApplication.translate("UpdateData", u"First Name", None))
        self.linkedWebsiteLineEdit.setPlaceholderText(QCoreApplication.translate("UpdateData", u"Linked Website", None))
        self.phoneNumerLineEdit.setPlaceholderText(QCoreApplication.translate("UpdateData", u"Phone Number", None))
        self.usernameLineEdit.setPlaceholderText(QCoreApplication.translate("UpdateData", u"UserName", None))
        self.secondEmailLineEdit.setPlaceholderText(QCoreApplication.translate("UpdateData", u"Second E-mail", None))
        self.notePlainTextEdit.setPlaceholderText(QCoreApplication.translate("UpdateData", u"Notes", None))
        self.specialDigitsCheckBox.setText(QCoreApplication.translate("UpdateData", u"Special Digitis", None))
        self.numbersCheckBox.setText(QCoreApplication.translate("UpdateData", u"Numbers", None))
        self.upperCaseCheckBox.setText(QCoreApplication.translate("UpdateData", u"Upper Case", None))
        self.lowerCaseCheckBox.setText(QCoreApplication.translate("UpdateData", u"Lower Case", None))
        self.generatePasswordPushButton.setText(QCoreApplication.translate("UpdateData", u"Generate Password", None))
        self.updatePushButton.setText(QCoreApplication.translate("UpdateData", u"Update", None))
    # retranslateUi

