# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kfq.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(815, 321)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 0))
        self.widget.setMaximumSize(QSize(90, 16777215))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pbtn_output = QPushButton(self.widget)
        self.pbtn_output.setObjectName(u"pbtn_output")
        self.pbtn_output.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.pbtn_output)

        self.pbtn_frp = QPushButton(self.widget)
        self.pbtn_frp.setObjectName(u"pbtn_frp")
        self.pbtn_frp.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.pbtn_frp)

        self.pbtn_about = QPushButton(self.widget)
        self.pbtn_about.setObjectName(u"pbtn_about")
        self.pbtn_about.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.pbtn_about)

        self.pbtn_visit_help = QPushButton(self.widget)
        self.pbtn_visit_help.setObjectName(u"pbtn_visit_help")
        self.pbtn_visit_help.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.pbtn_visit_help)

        self.pbtn_upd_set = QPushButton(self.widget)
        self.pbtn_upd_set.setObjectName(u"pbtn_upd_set")
        self.pbtn_upd_set.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.pbtn_upd_set)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pbtn_start_server = QPushButton(self.widget_2)
        self.pbtn_start_server.setObjectName(u"pbtn_start_server")
        self.pbtn_start_server.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.pbtn_start_server, 0, 0, 1, 9)

        self.pbtn_select_path = QPushButton(self.widget_2)
        self.pbtn_select_path.setObjectName(u"pbtn_select_path")
        self.pbtn_select_path.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.pbtn_select_path, 3, 8, 1, 1)

        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout_4 = QGridLayout(self.widget_6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.max_ram = QSpinBox(self.widget_6)
        self.max_ram.setObjectName(u"max_ram")
        self.max_ram.setMinimum(1)
        self.max_ram.setMaximum(256)

        self.gridLayout_4.addWidget(self.max_ram, 0, 3, 1, 1)

        self.n_5 = QLabel(self.widget_6)
        self.n_5.setObjectName(u"n_5")

        self.gridLayout_4.addWidget(self.n_5, 0, 4, 1, 1)

        self.n_11 = QLabel(self.widget_6)
        self.n_11.setObjectName(u"n_11")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.n_11.sizePolicy().hasHeightForWidth())
        self.n_11.setSizePolicy(sizePolicy)
        self.n_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.n_11, 3, 0, 2, 3)

        self.n_6 = QLabel(self.widget_6)
        self.n_6.setObjectName(u"n_6")
        sizePolicy.setHeightForWidth(self.n_6.sizePolicy().hasHeightForWidth())
        self.n_6.setSizePolicy(sizePolicy)
        self.n_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.n_6, 1, 0, 2, 3)

        self.max_player = QLineEdit(self.widget_6)
        self.max_player.setObjectName(u"max_player")

        self.gridLayout_4.addWidget(self.max_player, 1, 3, 2, 2)

        self.cbox_command_block = QComboBox(self.widget_6)
        self.cbox_command_block.addItem("")
        self.cbox_command_block.addItem("")
        self.cbox_command_block.setObjectName(u"cbox_command_block")
        self.cbox_command_block.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.cbox_command_block, 3, 3, 2, 2)

        self.n_4 = QLabel(self.widget_6)
        self.n_4.setObjectName(u"n_4")
        sizePolicy.setHeightForWidth(self.n_4.sizePolicy().hasHeightForWidth())
        self.n_4.setSizePolicy(sizePolicy)
        self.n_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.n_4, 0, 0, 1, 3)


        self.gridLayout_2.addWidget(self.widget_6, 6, 3, 2, 1)

        self.n_8 = QLabel(self.widget_2)
        self.n_8.setObjectName(u"n_8")

        self.gridLayout_2.addWidget(self.n_8, 1, 0, 2, 1)

        self.widget_7 = QWidget(self.widget_2)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout_5 = QGridLayout(self.widget_7)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pbtn_dis_log4j2 = QPushButton(self.widget_7)
        self.pbtn_dis_log4j2.setObjectName(u"pbtn_dis_log4j2")
        self.pbtn_dis_log4j2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_5.addWidget(self.pbtn_dis_log4j2, 0, 0, 1, 3)

        self.motd = QLineEdit(self.widget_7)
        self.motd.setObjectName(u"motd")

        self.gridLayout_5.addWidget(self.motd, 3, 2, 2, 1)

        self.server_port = QLineEdit(self.widget_7)
        self.server_port.setObjectName(u"server_port")

        self.gridLayout_5.addWidget(self.server_port, 2, 2, 1, 1)

        self.n_9 = QLabel(self.widget_7)
        self.n_9.setObjectName(u"n_9")
        sizePolicy.setHeightForWidth(self.n_9.sizePolicy().hasHeightForWidth())
        self.n_9.setSizePolicy(sizePolicy)
        self.n_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.n_9, 1, 0, 2, 1)

        self.n_12 = QLabel(self.widget_7)
        self.n_12.setObjectName(u"n_12")
        sizePolicy.setHeightForWidth(self.n_12.sizePolicy().hasHeightForWidth())
        self.n_12.setSizePolicy(sizePolicy)
        self.n_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.n_12, 3, 0, 1, 2)


        self.gridLayout_2.addWidget(self.widget_7, 6, 4, 2, 5)

        self.pbtn_download_server = QPushButton(self.widget_2)
        self.pbtn_download_server.setObjectName(u"pbtn_download_server")
        self.pbtn_download_server.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.pbtn_download_server, 1, 5, 2, 4)

        self.n_1 = QLabel(self.widget_2)
        self.n_1.setObjectName(u"n_1")

        self.gridLayout_2.addWidget(self.n_1, 3, 0, 1, 1)

        self.cbox_using_java = QComboBox(self.widget_2)
        self.cbox_using_java.addItem("")
        self.cbox_using_java.addItem("")
        self.cbox_using_java.addItem("")
        self.cbox_using_java.addItem("")
        self.cbox_using_java.setObjectName(u"cbox_using_java")
        self.cbox_using_java.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.cbox_using_java, 1, 1, 2, 2)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"Line{background-color: rgb(66, 66, 66);border:none;}")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.line_2 = QFrame(self.widget_4)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.n_13 = QLabel(self.widget_4)
        self.n_13.setObjectName(u"n_13")
        sizePolicy.setHeightForWidth(self.n_13.sizePolicy().hasHeightForWidth())
        self.n_13.setSizePolicy(sizePolicy)
        self.n_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.n_13)

        self.line = QFrame(self.widget_4)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line)


        self.gridLayout_2.addWidget(self.widget_4, 4, 0, 1, 9)

        self.lb_path = QLabel(self.widget_2)
        self.lb_path.setObjectName(u"lb_path")
        self.lb_path.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_path, 3, 1, 1, 7)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_3 = QGridLayout(self.widget_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.n_10 = QLabel(self.widget_5)
        self.n_10.setObjectName(u"n_10")
        sizePolicy.setHeightForWidth(self.n_10.sizePolicy().hasHeightForWidth())
        self.n_10.setSizePolicy(sizePolicy)
        self.n_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.n_10, 2, 0, 1, 1)

        self.n_3 = QLabel(self.widget_5)
        self.n_3.setObjectName(u"n_3")
        sizePolicy.setHeightForWidth(self.n_3.sizePolicy().hasHeightForWidth())
        self.n_3.setSizePolicy(sizePolicy)
        self.n_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.n_3, 0, 0, 1, 1)

        self.cbox_pvp = QComboBox(self.widget_5)
        self.cbox_pvp.addItem("")
        self.cbox_pvp.addItem("")
        self.cbox_pvp.setObjectName(u"cbox_pvp")
        self.cbox_pvp.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.cbox_pvp, 2, 1, 1, 2)

        self.n_7 = QLabel(self.widget_5)
        self.n_7.setObjectName(u"n_7")
        sizePolicy.setHeightForWidth(self.n_7.sizePolicy().hasHeightForWidth())
        self.n_7.setSizePolicy(sizePolicy)
        self.n_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.n_7, 1, 0, 1, 1)

        self.min_ram = QSpinBox(self.widget_5)
        self.min_ram.setObjectName(u"min_ram")
        self.min_ram.setMinimum(1)
        self.min_ram.setMaximum(256)

        self.gridLayout_3.addWidget(self.min_ram, 0, 1, 1, 1)

        self.label = QLabel(self.widget_5)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.label, 0, 2, 1, 1)

        self.cbox_mojang = QComboBox(self.widget_5)
        self.cbox_mojang.addItem("")
        self.cbox_mojang.addItem("")
        self.cbox_mojang.setObjectName(u"cbox_mojang")
        self.cbox_mojang.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.cbox_mojang, 1, 1, 1, 2)


        self.gridLayout_2.addWidget(self.widget_5, 6, 0, 2, 3)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"Line{background-color: rgb(66, 66, 66);border:none;}")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.line_3 = QFrame(self.widget_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_3)

        self.pbtn_ok_adv_set = QPushButton(self.widget_3)
        self.pbtn_ok_adv_set.setObjectName(u"pbtn_ok_adv_set")
        self.pbtn_ok_adv_set.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.pbtn_ok_adv_set)

        self.line_4 = QFrame(self.widget_3)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_4)


        self.gridLayout_2.addWidget(self.widget_3, 8, 0, 1, 9)

        self.pbtn_show_java_path = QPushButton(self.widget_2)
        self.pbtn_show_java_path.setObjectName(u"pbtn_show_java_path")
        self.pbtn_show_java_path.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.pbtn_show_java_path, 1, 3, 2, 2)


        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pbtn_output.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa", None))
        self.pbtn_frp.setText(QCoreApplication.translate("MainWindow", u"\u6620\u5c04", None))
        self.pbtn_about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.pbtn_visit_help.setText(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.pbtn_upd_set.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.pbtn_start_server.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f\u670d\u52a1\u5668", None))
        self.pbtn_select_path.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8def\u5f84", None))
        self.n_5.setText(QCoreApplication.translate("MainWindow", u"GB", None))
        self.n_11.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u542f\u7528\u547d\u4ee4\u65b9\u5757\uff1a", None))
        self.n_6.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5927\u73a9\u5bb6\u6570\u91cf\uff1a", None))
        self.max_player.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.cbox_command_block.setItemText(0, QCoreApplication.translate("MainWindow", u"True", None))
        self.cbox_command_block.setItemText(1, QCoreApplication.translate("MainWindow", u"False", None))

        self.n_4.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5927\u5185\u5b58\uff1a", None))
        self.n_8.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528Java:", None))
        self.pbtn_dis_log4j2.setText(QCoreApplication.translate("MainWindow", u"\u901a\u8fc7\u542f\u52a8\u53c2\u6570\u7981\u7528Log4j2", None))
        self.server_port.setText(QCoreApplication.translate("MainWindow", u"19132", None))
        self.n_9.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u5668\u7aef\u53e3\uff1a", None))
        self.n_12.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u5668\u5217\u8868\u754c\u9762\u63d0\u793a\uff1a", None))
        self.pbtn_download_server.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d", None))
        self.n_1.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u7aef\u8def\u5f84\uff1a", None))
        self.cbox_using_java.setItemText(0, QCoreApplication.translate("MainWindow", u"Java17", None))
        self.cbox_using_java.setItemText(1, QCoreApplication.translate("MainWindow", u"Java16", None))
        self.cbox_using_java.setItemText(2, QCoreApplication.translate("MainWindow", u"Java8", None))
        self.cbox_using_java.setItemText(3, QCoreApplication.translate("MainWindow", u"\u7cfb\u7edf\u53d8\u91cf", None))

        self.n_13.setText(QCoreApplication.translate("MainWindow", u"\u4ee5\u4e0b\u8bbe\u7f6e\u5c06\u5728\u670d\u52a1\u5668\u91cd\u542f\u540e\u751f\u6548", None))
        self.lb_path.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.n_10.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f PVP\uff1a", None))
        self.n_3.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5c0f\u5185\u5b58\uff1a", None))
        self.cbox_pvp.setItemText(0, QCoreApplication.translate("MainWindow", u"True", None))
        self.cbox_pvp.setItemText(1, QCoreApplication.translate("MainWindow", u"False", None))

        self.n_7.setText(QCoreApplication.translate("MainWindow", u"\u6b63\u7248\u9a8c\u8bc1\uff1a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"GB", None))
        self.cbox_mojang.setItemText(0, QCoreApplication.translate("MainWindow", u"True", None))
        self.cbox_mojang.setItemText(1, QCoreApplication.translate("MainWindow", u"False", None))

        self.pbtn_ok_adv_set.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4", None))
        self.pbtn_show_java_path.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u663e\u793a\u5f53\u524d\u8def\u5f84", None))
    # retranslateUi

