# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Mainpage.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(507, 298)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.overallbtn = QPushButton(self.centralwidget)
        self.overallbtn.setObjectName(u"overallbtn")
        self.overallbtn.setGeometry(QRect(160, 30, 161, 41))
        self.GRbtn = QPushButton(self.centralwidget)
        self.GRbtn.setObjectName(u"GRbtn")
        self.GRbtn.setGeometry(QRect(160, 190, 161, 41))
        self.herobtn = QPushButton(self.centralwidget)
        self.herobtn.setObjectName(u"herobtn")
        self.herobtn.setGeometry(QRect(160, 110, 161, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 507, 18))
        self.menuWinrate = QMenu(self.menubar)
        self.menuWinrate.setObjectName(u"menuWinrate")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuWinrate.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.overallbtn.setText(QCoreApplication.translate("MainWindow", u"Overall", None))
        self.GRbtn.setText(QCoreApplication.translate("MainWindow", u"Games Required", None))
        self.herobtn.setText(QCoreApplication.translate("MainWindow", u"Hero", None))
        self.menuWinrate.setTitle(QCoreApplication.translate("MainWindow", u"Winrate", None))
    # retranslateUi

