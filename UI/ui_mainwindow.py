# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QGridLayout,
    QHBoxLayout, QHeaderView, QLayout, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(864, 544)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setSizeIncrement(QSize(0, 0))
        self.actionHistory = QAction(MainWindow)
        self.actionHistory.setObjectName(u"actionHistory")
        self.actionChange_Password = QAction(MainWindow)
        self.actionChange_Password.setObjectName(u"actionChange_Password")
        self.actionLog_Out = QAction(MainWindow)
        self.actionLog_Out.setObjectName(u"actionLog_Out")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        self.actionImprot = QAction(MainWindow)
        self.actionImprot.setObjectName(u"actionImprot")
        self.actionDelete_All = QAction(MainWindow)
        self.actionDelete_All.setObjectName(u"actionDelete_All")
        self.actionDelete_Everything = QAction(MainWindow)
        self.actionDelete_Everything.setObjectName(u"actionDelete_Everything")
        self.actionHowToUse = QAction(MainWindow)
        self.actionHowToUse.setObjectName(u"actionHowToUse")
        self.actionAbout_this_Software = QAction(MainWindow)
        self.actionAbout_this_Software.setObjectName(u"actionAbout_this_Software")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setSizeIncrement(QSize(1, 1))
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.websiteNameLineEdit = QLineEdit(self.centralwidget)
        self.websiteNameLineEdit.setObjectName(u"websiteNameLineEdit")

        self.gridLayout.addWidget(self.websiteNameLineEdit, 0, 0, 1, 1)

        self.emailLineEdit = QLineEdit(self.centralwidget)
        self.emailLineEdit.setObjectName(u"emailLineEdit")

        self.gridLayout.addWidget(self.emailLineEdit, 0, 3, 1, 1)

        self.passwordLineEdit = QLineEdit(self.centralwidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")

        self.gridLayout.addWidget(self.passwordLineEdit, 3, 0, 1, 1)

        self.websiteLinkLineEdit = QLineEdit(self.centralwidget)
        self.websiteLinkLineEdit.setObjectName(u"websiteLinkLineEdit")

        self.gridLayout.addWidget(self.websiteLinkLineEdit, 0, 1, 1, 1)

        self.lastNameLineEdit = QLineEdit(self.centralwidget)
        self.lastNameLineEdit.setObjectName(u"lastNameLineEdit")

        self.gridLayout.addWidget(self.lastNameLineEdit, 2, 2, 1, 1)

        self.mainDeviceLineEdit = QLineEdit(self.centralwidget)
        self.mainDeviceLineEdit.setObjectName(u"mainDeviceLineEdit")

        self.gridLayout.addWidget(self.mainDeviceLineEdit, 3, 3, 1, 1)

        self.securityQuestionLineEdit = QLineEdit(self.centralwidget)
        self.securityQuestionLineEdit.setObjectName(u"securityQuestionLineEdit")

        self.gridLayout.addWidget(self.securityQuestionLineEdit, 3, 1, 1, 1)

        self.answerLineEdit = QLineEdit(self.centralwidget)
        self.answerLineEdit.setObjectName(u"answerLineEdit")

        self.gridLayout.addWidget(self.answerLineEdit, 3, 2, 1, 1)

        self.purposeOfUseLineEdit = QLineEdit(self.centralwidget)
        self.purposeOfUseLineEdit.setObjectName(u"purposeOfUseLineEdit")

        self.gridLayout.addWidget(self.purposeOfUseLineEdit, 3, 4, 1, 1)

        self.firstNameLineEdit = QLineEdit(self.centralwidget)
        self.firstNameLineEdit.setObjectName(u"firstNameLineEdit")

        self.gridLayout.addWidget(self.firstNameLineEdit, 2, 1, 1, 1)

        self.linkedWebsiteLineEdit = QLineEdit(self.centralwidget)
        self.linkedWebsiteLineEdit.setObjectName(u"linkedWebsiteLineEdit")

        self.gridLayout.addWidget(self.linkedWebsiteLineEdit, 0, 2, 1, 1)

        self.phoneNumerLineEdit = QLineEdit(self.centralwidget)
        self.phoneNumerLineEdit.setObjectName(u"phoneNumerLineEdit")

        self.gridLayout.addWidget(self.phoneNumerLineEdit, 2, 4, 1, 1)

        self.usernameLineEdit = QLineEdit(self.centralwidget)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")

        self.gridLayout.addWidget(self.usernameLineEdit, 2, 0, 1, 1)

        self.secondEmailLineEdit = QLineEdit(self.centralwidget)
        self.secondEmailLineEdit.setObjectName(u"secondEmailLineEdit")

        self.gridLayout.addWidget(self.secondEmailLineEdit, 0, 4, 1, 1)

        self.birthDateEdit = QDateEdit(self.centralwidget)
        self.birthDateEdit.setObjectName(u"birthDateEdit")
        self.birthDateEdit.setDateTime(QDateTime(QDate(1993, 1, 1), QTime(0, 0, 0)))
        self.birthDateEdit.setMaximumDate(QDate(2100, 12, 31))

        self.gridLayout.addWidget(self.birthDateEdit, 2, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.notePlainTextEdit = QPlainTextEdit(self.centralwidget)
        self.notePlainTextEdit.setObjectName(u"notePlainTextEdit")

        self.verticalLayout.addWidget(self.notePlainTextEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.specialDigitsCheckBox = QCheckBox(self.centralwidget)
        self.specialDigitsCheckBox.setObjectName(u"specialDigitsCheckBox")
        self.specialDigitsCheckBox.setChecked(True)

        self.horizontalLayout.addWidget(self.specialDigitsCheckBox)

        self.numbersCheckBox = QCheckBox(self.centralwidget)
        self.numbersCheckBox.setObjectName(u"numbersCheckBox")
        self.numbersCheckBox.setChecked(True)

        self.horizontalLayout.addWidget(self.numbersCheckBox)

        self.upperCaseCheckBox = QCheckBox(self.centralwidget)
        self.upperCaseCheckBox.setObjectName(u"upperCaseCheckBox")
        self.upperCaseCheckBox.setChecked(True)

        self.horizontalLayout.addWidget(self.upperCaseCheckBox)

        self.lowerCaseCheckBox = QCheckBox(self.centralwidget)
        self.lowerCaseCheckBox.setObjectName(u"lowerCaseCheckBox")
        self.lowerCaseCheckBox.setChecked(True)

        self.horizontalLayout.addWidget(self.lowerCaseCheckBox)

        self.lengthPasswordSpinBox = QSpinBox(self.centralwidget)
        self.lengthPasswordSpinBox.setObjectName(u"lengthPasswordSpinBox")
        self.lengthPasswordSpinBox.setMinimum(1)
        self.lengthPasswordSpinBox.setValue(8)

        self.horizontalLayout.addWidget(self.lengthPasswordSpinBox)

        self.generatePasswordPushButton = QPushButton(self.centralwidget)
        self.generatePasswordPushButton.setObjectName(u"generatePasswordPushButton")

        self.horizontalLayout.addWidget(self.generatePasswordPushButton)

        self.addPushButton = QPushButton(self.centralwidget)
        self.addPushButton.setObjectName(u"addPushButton")

        self.horizontalLayout.addWidget(self.addPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.allDataTab = QWidget()
        self.allDataTab.setObjectName(u"allDataTab")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.allDataTab.sizePolicy().hasHeightForWidth())
        self.allDataTab.setSizePolicy(sizePolicy1)
        self.gridLayout_3 = QGridLayout(self.allDataTab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.allDataTableWidget = QTableWidget(self.allDataTab)
        if (self.allDataTableWidget.columnCount() < 16):
            self.allDataTableWidget.setColumnCount(16)
        __qtablewidgetitem = QTableWidgetItem()
        self.allDataTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.allDataTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.allDataTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.allDataTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.allDataTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.allDataTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.allDataTableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.allDataTableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.allDataTableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.allDataTableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.allDataTableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.allDataTableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.allDataTableWidget.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.allDataTableWidget.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.allDataTableWidget.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.allDataTableWidget.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        self.allDataTableWidget.setObjectName(u"allDataTableWidget")
        self.allDataTableWidget.setGridStyle(Qt.SolidLine)
        self.allDataTableWidget.setSortingEnabled(True)
        self.allDataTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.allDataTableWidget.horizontalHeader().setDefaultSectionSize(90)
        self.allDataTableWidget.horizontalHeader().setStretchLastSection(True)
        self.allDataTableWidget.verticalHeader().setVisible(True)
        self.allDataTableWidget.verticalHeader().setProperty("showSortIndicator", False)

        self.gridLayout_3.addWidget(self.allDataTableWidget, 0, 0, 1, 1)

        self.tabWidget.addTab(self.allDataTab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tableWidget_2 = QTableWidget(self.tab_2)
        if (self.tableWidget_2.columnCount() < 15):
            self.tableWidget_2.setColumnCount(15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(9, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(10, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(11, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(12, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(13, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(14, __qtablewidgetitem30)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(90)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_4.addWidget(self.tableWidget_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.copyPushButton = QPushButton(self.centralwidget)
        self.copyPushButton.setObjectName(u"copyPushButton")

        self.horizontalLayout_2.addWidget(self.copyPushButton)

        self.deletePushButton = QPushButton(self.centralwidget)
        self.deletePushButton.setObjectName(u"deletePushButton")

        self.horizontalLayout_2.addWidget(self.deletePushButton)

        self.updatePushButton = QPushButton(self.centralwidget)
        self.updatePushButton.setObjectName(u"updatePushButton")

        self.horizontalLayout_2.addWidget(self.updatePushButton)

        self.visualizeDataPushButton = QPushButton(self.centralwidget)
        self.visualizeDataPushButton.setObjectName(u"visualizeDataPushButton")

        self.horizontalLayout_2.addWidget(self.visualizeDataPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 7)
        self.verticalLayout.setStretch(4, 1)

        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 864, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionHistory)
        self.menuFile.addAction(self.actionChange_Password)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionLog_Out)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuAbout.addAction(self.actionHowToUse)
        self.menuAbout.addAction(self.actionAbout_this_Software)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MySafe", None))
        self.actionHistory.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.actionChange_Password.setText(QCoreApplication.translate("MainWindow", u"Change Password", None))
        self.actionLog_Out.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.actionImprot.setText(QCoreApplication.translate("MainWindow", u"Improt", None))
        self.actionDelete_All.setText(QCoreApplication.translate("MainWindow", u"Delete All Passwords On This Account", None))
        self.actionDelete_Everything.setText(QCoreApplication.translate("MainWindow", u"Delete Everything", None))
        self.actionHowToUse.setText(QCoreApplication.translate("MainWindow", u"How to use?", None))
        self.actionAbout_this_Software.setText(QCoreApplication.translate("MainWindow", u"About this Software", None))
        self.websiteNameLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Website", None))
        self.emailLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.passwordLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.websiteLinkLineEdit.setText("")
        self.websiteLinkLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Link", None))
        self.lastNameLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.mainDeviceLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Main Device", None))
        self.securityQuestionLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Security Question 1", None))
        self.answerLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Answer 1", None))
        self.purposeOfUseLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Purpose of Use", None))
        self.firstNameLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.linkedWebsiteLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Linked Website", None))
        self.phoneNumerLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.usernameLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UserName", None))
        self.secondEmailLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Second E-mail", None))
        self.notePlainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Notes", None))
        self.specialDigitsCheckBox.setText(QCoreApplication.translate("MainWindow", u"Special Digitis", None))
        self.numbersCheckBox.setText(QCoreApplication.translate("MainWindow", u"Numbers", None))
        self.upperCaseCheckBox.setText(QCoreApplication.translate("MainWindow", u"Upper Case", None))
        self.lowerCaseCheckBox.setText(QCoreApplication.translate("MainWindow", u"Lower Case", None))
        self.generatePasswordPushButton.setText(QCoreApplication.translate("MainWindow", u"Generate Password", None))
        self.addPushButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        ___qtablewidgetitem = self.allDataTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem1 = self.allDataTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Website", None));
        ___qtablewidgetitem2 = self.allDataTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Link", None));
        ___qtablewidgetitem3 = self.allDataTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Linked Website", None));
        ___qtablewidgetitem4 = self.allDataTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"E-mail", None));
        ___qtablewidgetitem5 = self.allDataTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Second Email", None));
        ___qtablewidgetitem6 = self.allDataTableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"UserName", None));
        ___qtablewidgetitem7 = self.allDataTableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"First Name", None));
        ___qtablewidgetitem8 = self.allDataTableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Last Name", None));
        ___qtablewidgetitem9 = self.allDataTableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Birthdate", None));
        ___qtablewidgetitem10 = self.allDataTableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None));
        ___qtablewidgetitem11 = self.allDataTableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Password", None));
        ___qtablewidgetitem12 = self.allDataTableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Security Question", None));
        ___qtablewidgetitem13 = self.allDataTableWidget.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Answer", None));
        ___qtablewidgetitem14 = self.allDataTableWidget.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Main Device", None));
        ___qtablewidgetitem15 = self.allDataTableWidget.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Purpose Of Use", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.allDataTab), QCoreApplication.translate("MainWindow", u"All Data", None))
        ___qtablewidgetitem16 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"#", None));
        ___qtablewidgetitem17 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Website", None));
        ___qtablewidgetitem18 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Link", None));
        ___qtablewidgetitem19 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Linked Website", None));
        ___qtablewidgetitem20 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"E-mail", None));
        ___qtablewidgetitem21 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Second Email", None));
        ___qtablewidgetitem22 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"UserName", None));
        ___qtablewidgetitem23 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"First Name", None));
        ___qtablewidgetitem24 = self.tableWidget_2.horizontalHeaderItem(8)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Last Name", None));
        ___qtablewidgetitem25 = self.tableWidget_2.horizontalHeaderItem(9)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Birthdate", None));
        ___qtablewidgetitem26 = self.tableWidget_2.horizontalHeaderItem(10)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None));
        ___qtablewidgetitem27 = self.tableWidget_2.horizontalHeaderItem(11)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Security Question", None));
        ___qtablewidgetitem28 = self.tableWidget_2.horizontalHeaderItem(12)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Answer", None));
        ___qtablewidgetitem29 = self.tableWidget_2.horizontalHeaderItem(13)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Main Device", None));
        ___qtablewidgetitem30 = self.tableWidget_2.horizontalHeaderItem(14)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Purpose Of Use", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.copyPushButton.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.deletePushButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.updatePushButton.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.visualizeDataPushButton.setText(QCoreApplication.translate("MainWindow", u"Visualize Data", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

