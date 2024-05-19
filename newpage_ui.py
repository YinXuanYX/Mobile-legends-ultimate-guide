# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newpage.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1138, 711)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 161, 711))
        self.widget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(117, 58, 175);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(71, 142, 213);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/mlbb.jpg"))
        self.label.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.assa = QPushButton(self.widget)
        self.assa.setObjectName(u"assa")
        icon = QIcon()
        icon.addFile(u":/Assassin_Icon.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.assa.setIcon(icon)
        self.assa.setCheckable(True)

        self.verticalLayout.addWidget(self.assa)

        self.tank = QPushButton(self.widget)
        self.tank.setObjectName(u"tank")
        icon1 = QIcon()
        icon1.addFile(u":/Tank_Icon.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.tank.setIcon(icon1)
        self.tank.setCheckable(True)

        self.verticalLayout.addWidget(self.tank)

        self.fighter = QPushButton(self.widget)
        self.fighter.setObjectName(u"fighter")
        icon2 = QIcon()
        icon2.addFile(u":/Fighter_Icon.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.fighter.setIcon(icon2)
        self.fighter.setCheckable(True)

        self.verticalLayout.addWidget(self.fighter)

        self.mage = QPushButton(self.widget)
        self.mage.setObjectName(u"mage")
        icon3 = QIcon()
        icon3.addFile(u":/Mage_Icon.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.mage.setIcon(icon3)
        self.mage.setCheckable(True)

        self.verticalLayout.addWidget(self.mage)

        self.mm = QPushButton(self.widget)
        self.mm.setObjectName(u"mm")
        icon4 = QIcon()
        icon4.addFile(u":/Marksman_Icon.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.mm.setIcon(icon4)
        self.mm.setCheckable(True)

        self.verticalLayout.addWidget(self.mm)

        self.sup = QPushButton(self.widget)
        self.sup.setObjectName(u"sup")
        icon5 = QIcon()
        icon5.addFile(u":/Support_Icon.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.sup.setIcon(icon5)
        self.sup.setCheckable(True)

        self.verticalLayout.addWidget(self.sup)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 325, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.cls = QPushButton(self.widget)
        self.cls.setObjectName(u"cls")
        self.cls.setCheckable(True)

        self.verticalLayout_2.addWidget(self.cls)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(160, -20, 981, 731))
        self.widget_2.setStyleSheet(u"QWidget{\n"
"background-color: rgb(0, 0, 255);\n"
"}")
        self.stackedWidget = QStackedWidget(self.widget_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(30, 30, 941, 681))
        self.stackedWidget.setFocusPolicy(Qt.StrongFocus)
        self.stackedWidget.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.assaspage = QWidget()
        self.assaspage.setObjectName(u"assaspage")
        self.label_3 = QLabel(self.assaspage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(210, 10, 341, 41))
        font = QFont()
        font.setFamilies([u"Sitka Banner Semibold"])
        font.setPointSize(19)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.Saber = QPushButton(self.assaspage)
        self.Saber.setObjectName(u"Saber")
        self.Saber.setGeometry(QRect(40, 130, 75, 23))
        self.Saber.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.Saber.setCheckable(True)
        self.pushButton_2 = QPushButton(self.assaspage)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(170, 130, 75, 23))
        self.pushButton_3 = QPushButton(self.assaspage)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(290, 130, 75, 23))
        self.pushButton_4 = QPushButton(self.assaspage)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(410, 130, 75, 23))
        self.pushButton_5 = QPushButton(self.assaspage)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(530, 130, 75, 23))
        self.pushButton_6 = QPushButton(self.assaspage)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(650, 130, 75, 23))
        self.label_8 = QLabel(self.assaspage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 70, 71, 51))
        self.label_8.setPixmap(QPixmap(u":/Saber.png"))
        self.label_8.setScaledContents(True)
        self.stackedWidget.addWidget(self.assaspage)
        self.tankspage = QWidget()
        self.tankspage.setObjectName(u"tankspage")
        self.label_4 = QLabel(self.tankspage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(200, 70, 341, 41))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.tankspage)
        self.fighterspage = QWidget()
        self.fighterspage.setObjectName(u"fighterspage")
        self.label_5 = QLabel(self.fighterspage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(190, 40, 341, 41))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.fighterspage)
        self.magepage = QWidget()
        self.magepage.setObjectName(u"magepage")
        self.label_6 = QLabel(self.magepage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(190, 30, 341, 41))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.magepage)
        self.mmpage = QWidget()
        self.mmpage.setObjectName(u"mmpage")
        self.label_7 = QLabel(self.mmpage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(200, 30, 341, 41))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.mmpage)
        self.supportpage = QWidget()
        self.supportpage.setObjectName(u"supportpage")
        self.label_2 = QLabel(self.supportpage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 30, 341, 41))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.supportpage)
        self.saberpage = QWidget()
        self.saberpage.setObjectName(u"saberpage")
        self.widget_3 = QWidget(self.saberpage)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(10, 10, 921, 661))
        self.widget_3.setStyleSheet(u"background-color: rgb(149, 0, 149);")
        self.heropic = QLabel(self.widget_3)
        self.heropic.setObjectName(u"heropic")
        self.heropic.setGeometry(QRect(30, 10, 381, 181))
        self.heropic.setPixmap(QPixmap(u":/Saber.png"))
        self.heropic.setScaledContents(True)
        self.heropic.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.Passive_name_label = QLabel(self.widget_3)
        self.Passive_name_label.setObjectName(u"Passive_name_label")
        self.Passive_name_label.setGeometry(QRect(80, 220, 111, 21))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setUnderline(True)
        self.Passive_name_label.setFont(font1)
        self.Passive_name_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Passive_name_label.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.Passivelabel = QLabel(self.widget_3)
        self.Passivelabel.setObjectName(u"Passivelabel")
        self.Passivelabel.setGeometry(QRect(20, 200, 81, 21))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.Passivelabel.setFont(font2)
        self.Passivelabel.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.Passivelabel.setOpenExternalLinks(False)
        self.Passivelabel.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.passivepic = QLabel(self.widget_3)
        self.passivepic.setObjectName(u"passivepic")
        self.passivepic.setGeometry(QRect(20, 220, 47, 51))
        self.passivepic.setPixmap(QPixmap(u":/EnemyBane.png"))
        self.passivepic.setScaledContents(True)
        self.passivepic.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.passivedesc = QLabel(self.widget_3)
        self.passivedesc.setObjectName(u"passivedesc")
        self.passivedesc.setGeometry(QRect(80, 240, 591, 21))
        self.passivedesc.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.passivedesc.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.passivedesc.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.skill1text = QLabel(self.widget_3)
        self.skill1text.setObjectName(u"skill1text")
        self.skill1text.setGeometry(QRect(20, 280, 51, 16))
        self.skill1text.setFont(font2)
        self.skill1text.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.skill1pic = QLabel(self.widget_3)
        self.skill1pic.setObjectName(u"skill1pic")
        self.skill1pic.setGeometry(QRect(20, 300, 51, 51))
        self.skill1pic.setPixmap(QPixmap(u":/Orbiting_Swords.png"))
        self.skill1pic.setScaledContents(True)
        self.skill1pic.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.skill1_name = QLabel(self.widget_3)
        self.skill1_name.setObjectName(u"skill1_name")
        self.skill1_name.setGeometry(QRect(90, 290, 111, 16))
        self.skill1_name.setFont(font1)
        self.skill1_name.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.skill1_name.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.skill1desc = QLabel(self.widget_3)
        self.skill1desc.setObjectName(u"skill1desc")
        self.skill1desc.setGeometry(QRect(90, 310, 631, 81))
        self.skill1desc.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.skill1desc.setWordWrap(True)
        self.skill1desc.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.skill2text = QLabel(self.widget_3)
        self.skill2text.setObjectName(u"skill2text")
        self.skill2text.setGeometry(QRect(20, 390, 51, 16))
        self.skill2text.setFont(font2)
        self.skill2text.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.skill2text.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.skill2pic = QLabel(self.widget_3)
        self.skill2pic.setObjectName(u"skill2pic")
        self.skill2pic.setGeometry(QRect(20, 410, 51, 51))
        self.skill2pic.setPixmap(QPixmap(u":/Charge.png"))
        self.skill2pic.setScaledContents(True)
        self.skill2pic.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.skill2_name = QLabel(self.widget_3)
        self.skill2_name.setObjectName(u"skill2_name")
        self.skill2_name.setGeometry(QRect(90, 400, 51, 16))
        self.skill2_name.setFont(font1)
        self.skill2_name.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.skill2_name.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.skill2desc = QLabel(self.widget_3)
        self.skill2desc.setObjectName(u"skill2desc")
        self.skill2desc.setGeometry(QRect(90, 420, 641, 51))
        self.skill2desc.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.skill2desc.setWordWrap(True)
        self.skill2desc.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.ultimatetext = QLabel(self.widget_3)
        self.ultimatetext.setObjectName(u"ultimatetext")
        self.ultimatetext.setGeometry(QRect(20, 550, 71, 16))
        self.ultimatetext.setFont(font2)
        self.ultimatetext.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.ultimatetext.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.ultipic = QLabel(self.widget_3)
        self.ultipic.setObjectName(u"ultipic")
        self.ultipic.setGeometry(QRect(30, 580, 51, 51))
        self.ultipic.setPixmap(QPixmap(u":/Triple_Sweep.png"))
        self.ultipic.setScaledContents(True)
        self.ultipic.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.Ultimatename = QLabel(self.widget_3)
        self.Ultimatename.setObjectName(u"Ultimatename")
        self.Ultimatename.setGeometry(QRect(100, 560, 91, 16))
        self.Ultimatename.setFont(font1)
        self.Ultimatename.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Ultimatename.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.ultimatedesc = QLabel(self.widget_3)
        self.ultimatedesc.setObjectName(u"ultimatedesc")
        self.ultimatedesc.setGeometry(QRect(100, 580, 641, 51))
        self.ultimatedesc.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.ultimatedesc.setWordWrap(True)
        self.ultimatedesc.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.specialskilltext = QLabel(self.widget_3)
        self.specialskilltext.setObjectName(u"specialskilltext")
        self.specialskilltext.setGeometry(QRect(10, 470, 111, 16))
        self.specialskilltext.setFont(font2)
        self.specialskilltext.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.specialskilldesc = QLabel(self.widget_3)
        self.specialskilldesc.setObjectName(u"specialskilldesc")
        self.specialskilldesc.setGeometry(QRect(110, 500, 641, 51))
        self.specialskilldesc.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.specialskilldesc.setWordWrap(True)
        self.specialskilldesc.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.specialskillpic = QLabel(self.widget_3)
        self.specialskillpic.setObjectName(u"specialskillpic")
        self.specialskillpic.setGeometry(QRect(30, 510, 47, 14))
        self.specialskillpic.setStyleSheet(u"background-color: rgb(255, 170, 255);")
        self.specialskillpic.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.Specialskillname = QLabel(self.widget_3)
        self.Specialskillname.setObjectName(u"Specialskillname")
        self.Specialskillname.setGeometry(QRect(110, 480, 91, 16))
        self.Specialskillname.setFont(font1)
        self.Specialskillname.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Specialskillname.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.stackedWidget.addWidget(self.saberpage)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.cls.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.assa.setText(QCoreApplication.translate("MainWindow", u"Assassins", None))
        self.tank.setText(QCoreApplication.translate("MainWindow", u"Tank", None))
        self.fighter.setText(QCoreApplication.translate("MainWindow", u"Fighter", None))
        self.mage.setText(QCoreApplication.translate("MainWindow", u"Mage", None))
        self.mm.setText(QCoreApplication.translate("MainWindow", u"Marksman", None))
        self.sup.setText(QCoreApplication.translate("MainWindow", u"Support", None))
        self.cls.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Assassins", None))
        self.Saber.setText(QCoreApplication.translate("MainWindow", u"Saber", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_8.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Tanks", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Fighters", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Mage", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Marksman", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Supports", None))
        self.heropic.setText("")
        self.Passive_name_label.setText(QCoreApplication.translate("MainWindow", u"Lesbians", None))
        self.Passivelabel.setText(QCoreApplication.translate("MainWindow", u"Passive", None))
        self.passivepic.setText("")
        self.passivedesc.setText(QCoreApplication.translate("MainWindow", u"wtf", None))
        self.skill1text.setText(QCoreApplication.translate("MainWindow", u"Skill 1", None))
        self.skill1pic.setText("")
        self.skill1_name.setText(QCoreApplication.translate("MainWindow", u"Orbiting Swords", None))
        self.skill1desc.setText(QCoreApplication.translate("MainWindow", u"Saber releases 5 swords that orbit around him and deal 80\u2013105 (+30% Extra Physical Attack) Physical Damage to nearby enemies on hit. The swords will retract back to him after a while.\n"
"When the swords are present, Saber sends a sword toward his target on each attack, dealing 210\u2013260 (+60% Extra Physical Attack) Physical Damage to the target and 50% of the damage to other enemies it passes through (damage against minions is reduced to 50%). Each attack also reduces the cooldown of Charge by 1 second.", None))
        self.skill2text.setText(QCoreApplication.translate("MainWindow", u"Skill 2", None))
        self.skill2pic.setText("")
        self.skill2_name.setText(QCoreApplication.translate("MainWindow", u"Charge", None))
        self.skill2desc.setText(QCoreApplication.translate("MainWindow", u"Saber dashes in the target direction, dealing 75\u2013150 (+50% Extra Physical Attack) Physical Damage to enemies along the way while enhancing his next Basic Attack. The enhanced Basic Attack deals 75\u2013150 (+120% Total Physical Attack) Physical Damage and slows the target by 60% for 1 second.", None))
        self.ultimatetext.setText(QCoreApplication.translate("MainWindow", u"Ultimate", None))
        self.ultipic.setText("")
        self.Ultimatename.setText(QCoreApplication.translate("MainWindow", u"Triple Sweep", None))
        self.ultimatedesc.setText(QCoreApplication.translate("MainWindow", u"Saber charges at the target enemy hero, knocking them airborne for 1.2 seconds and striking them 3 times over the duration. The first two strikes deal 120\u2013180 (+100% Extra Physical Attack) Physical Damage each, while the third strike deals 240\u2013360 (+200% Extra Physical Attack) Physical Damage.", None))
        self.specialskilltext.setText(QCoreApplication.translate("MainWindow", u"Special Skill", None))
        self.specialskilldesc.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.specialskillpic.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.Specialskillname.setText(QCoreApplication.translate("MainWindow", u"None", None))
    # retranslateUi
