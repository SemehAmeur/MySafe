# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'history.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_History(object):
    def setupUi(self, History):
        if not History.objectName():
            History.setObjectName(u"History")
        History.resize(643, 300)
        self.gridLayout = QGridLayout(History)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget = QTableWidget(History)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)


        self.retranslateUi(History)

        QMetaObject.connectSlotsByName(History)
    # setupUi

    def retranslateUi(self, History):
        History.setWindowTitle(QCoreApplication.translate("History", u"History", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("History", u"Action", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("History", u"Date", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("History", u"Hour", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("History", u"Activity", None));
    # retranslateUi

