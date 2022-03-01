# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frp.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListView,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QWidget)

class Ui_FrpcConfig(object):
    def setupUi(self, FrpcConfig):
        if not FrpcConfig.objectName():
            FrpcConfig.setObjectName(u"FrpcConfig")
        FrpcConfig.resize(410, 192)
        self.select_url = QListWidget(FrpcConfig)
        QListWidgetItem(self.select_url)
        QListWidgetItem(self.select_url)
        QListWidgetItem(self.select_url)
        QListWidgetItem(self.select_url)
        QListWidgetItem(self.select_url)
        self.select_url.setObjectName(u"select_url")
        self.select_url.setGeometry(QRect(20, 20, 151, 151))
        self.select_url.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.select_url.setViewMode(QListView.ListMode)
        self.accont = QLineEdit(FrpcConfig)
        self.accont.setObjectName(u"accont")
        self.accont.setGeometry(QRect(230, 20, 161, 21))
        self.n1 = QLabel(FrpcConfig)
        self.n1.setObjectName(u"n1")
        self.n1.setGeometry(QRect(190, 20, 41, 21))
        self.n2 = QLabel(FrpcConfig)
        self.n2.setObjectName(u"n2")
        self.n2.setGeometry(QRect(190, 50, 41, 21))
        self.passwd = QLineEdit(FrpcConfig)
        self.passwd.setObjectName(u"passwd")
        self.passwd.setGeometry(QRect(230, 50, 161, 21))
        self.pbtn_start = QPushButton(FrpcConfig)
        self.pbtn_start.setObjectName(u"pbtn_start")
        self.pbtn_start.setGeometry(QRect(190, 80, 51, 22))
        self.port = QLineEdit(FrpcConfig)
        self.port.setObjectName(u"port")
        self.port.setGeometry(QRect(250, 80, 91, 21))
        self.n3 = QLabel(FrpcConfig)
        self.n3.setObjectName(u"n3")
        self.n3.setGeometry(QRect(350, 80, 31, 21))
        self.pbtn_look_gwip = QPushButton(FrpcConfig)
        self.pbtn_look_gwip.setObjectName(u"pbtn_look_gwip")
        self.pbtn_look_gwip.setGeometry(QRect(190, 110, 201, 22))
        self.pbtn_try_update = QPushButton(FrpcConfig)
        self.pbtn_try_update.setObjectName(u"pbtn_try_update")
        self.pbtn_try_update.setGeometry(QRect(190, 150, 91, 22))
        self.pushButton = QPushButton(FrpcConfig)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(290, 150, 101, 21))

        self.retranslateUi(FrpcConfig)

        QMetaObject.connectSlotsByName(FrpcConfig)
    # setupUi

    def retranslateUi(self, FrpcConfig):
        FrpcConfig.setWindowTitle(QCoreApplication.translate("FrpcConfig", u"Form", None))

        __sortingEnabled = self.select_url.isSortingEnabled()
        self.select_url.setSortingEnabled(False)
        ___qlistwidgetitem = self.select_url.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("FrpcConfig", u"[\u514d\u8d39]\u5e7f\u5dde", None));
        ___qlistwidgetitem1 = self.select_url.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("FrpcConfig", u"[\u514d\u8d39]\u4e0a\u6d77", None));
        ___qlistwidgetitem2 = self.select_url.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("FrpcConfig", u"[\u514d\u8d39]\u9999\u6e2f", None));
        ___qlistwidgetitem3 = self.select_url.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("FrpcConfig", u"[\u6b63\u5728\u7ef4\u62a4][\u4ed8\u8d39]\u676d\u5dde  \u4f18\u5148\u4f7f\u7528", None));
        ___qlistwidgetitem4 = self.select_url.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("FrpcConfig", u"[\u6b63\u5728\u7ef4\u62a4][\u4ed8\u8d39]\u5e7f\u5dde  \u676d\u5dde\u4e0d\u884c\u518d\u7528", None));
        self.select_url.setSortingEnabled(__sortingEnabled)

        self.n1.setText(QCoreApplication.translate("FrpcConfig", u"QQ\u53f7\u7801", None))
        self.n2.setText(QCoreApplication.translate("FrpcConfig", u"\u5bc6\u7801", None))
        self.pbtn_start.setText(QCoreApplication.translate("FrpcConfig", u"\u542f\u52a8", None))
        self.n3.setText(QCoreApplication.translate("FrpcConfig", u" \u7aef\u53e3", None))
        self.pbtn_look_gwip.setText(QCoreApplication.translate("FrpcConfig", u"\u67e5\u770b\u516c\u7f51IP", None))
        self.pbtn_try_update.setText(QCoreApplication.translate("FrpcConfig", u"\u5c1d\u8bd5\u66f4\u65b0\u5ba2\u6237\u7aef", None))
        self.pushButton.setText(QCoreApplication.translate("FrpcConfig", u"\u524d\u5f80\u8d5e\u52a9", None))
    # retranslateUi

