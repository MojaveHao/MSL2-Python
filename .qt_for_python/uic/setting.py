# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QPushButton, QSizePolicy, QTextBrowser, QWidget)

class Ui_Setiing(object):
    def setupUi(self, Setiing):
        if not Setiing.objectName():
            Setiing.setObjectName(u"Setiing")
        Setiing.resize(400, 300)
        self.n1 = QLabel(Setiing)
        self.n1.setObjectName(u"n1")
        self.n1.setGeometry(QRect(10, 10, 91, 16))
        self.pbtn_download_auto_backup = QPushButton(Setiing)
        self.pbtn_download_auto_backup.setObjectName(u"pbtn_download_auto_backup")
        self.pbtn_download_auto_backup.setGeometry(QRect(10, 200, 211, 22))
        self.pbtn_download_auto_backup.setCursor(QCursor(Qt.PointingHandCursor))
        self.dl_update = QPushButton(Setiing)
        self.dl_update.setObjectName(u"dl_update")
        self.dl_update.setGeometry(QRect(10, 80, 80, 22))
        self.dl_update.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_update = QComboBox(Setiing)
        self.cbox_update.addItem("")
        self.cbox_update.addItem("")
        self.cbox_update.addItem("")
        self.cbox_update.setObjectName(u"cbox_update")
        self.cbox_update.setGeometry(QRect(150, 80, 65, 22))
        self.cbox_update.setCursor(QCursor(Qt.PointingHandCursor))
        self.n2 = QLabel(Setiing)
        self.n2.setObjectName(u"n2")
        self.n2.setGeometry(QRect(100, 80, 47, 14))
        self.n3 = QTextBrowser(Setiing)
        self.n3.setObjectName(u"n3")
        self.n3.setGeometry(QRect(220, 70, 171, 41))
        self.cbox_goto_website = QComboBox(Setiing)
        self.cbox_goto_website.addItem("")
        self.cbox_goto_website.addItem("")
        self.cbox_goto_website.addItem("")
        self.cbox_goto_website.addItem("")
        self.cbox_goto_website.addItem("")
        self.cbox_goto_website.setObjectName(u"cbox_goto_website")
        self.cbox_goto_website.setGeometry(QRect(70, 110, 81, 22))
        self.cbox_goto_website.setCursor(QCursor(Qt.PointingHandCursor))
        self.pbtn_goto = QPushButton(Setiing)
        self.pbtn_goto.setObjectName(u"pbtn_goto")
        self.pbtn_goto.setGeometry(QRect(20, 110, 51, 22))
        self.update_log = QTextBrowser(Setiing)
        self.update_log.setObjectName(u"update_log")
        self.update_log.setGeometry(QRect(230, 170, 161, 121))
        self.n4 = QLabel(Setiing)
        self.n4.setObjectName(u"n4")
        self.n4.setGeometry(QRect(230, 150, 47, 14))
        self.pbtn_check_configs_for_server = QPushButton(Setiing)
        self.pbtn_check_configs_for_server.setObjectName(u"pbtn_check_configs_for_server")
        self.pbtn_check_configs_for_server.setGeometry(QRect(20, 150, 181, 22))
        self.pbtn_download_website_manage = QPushButton(Setiing)
        self.pbtn_download_website_manage.setObjectName(u"pbtn_download_website_manage")
        self.pbtn_download_website_manage.setGeometry(QRect(10, 230, 211, 22))
        self.pbtn_download_website_manage.setCursor(QCursor(Qt.PointingHandCursor))
        self.label = QLabel(Setiing)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 180, 211, 16))
        self.pbtn_ufl1 = QPushButton(Setiing)
        self.pbtn_ufl1.setObjectName(u"pbtn_ufl1")
        self.pbtn_ufl1.setGeometry(QRect(10, 260, 80, 22))
        self.pbtn_ufl2 = QPushButton(Setiing)
        self.pbtn_ufl2.setObjectName(u"pbtn_ufl2")
        self.pbtn_ufl2.setGeometry(QRect(90, 260, 80, 22))

        self.retranslateUi(Setiing)

        QMetaObject.connectSlotsByName(Setiing)
    # setupUi

    def retranslateUi(self, Setiing):
        Setiing.setWindowTitle(QCoreApplication.translate("Setiing", u"Dialog", None))
        self.n1.setText(QCoreApplication.translate("Setiing", u"MSL2-Python\u8bbe\u7f6e", None))
        self.pbtn_download_auto_backup.setText(QCoreApplication.translate("Setiing", u"\u4e0b\u8f7d\u81ea\u52a8\u5907\u4efd\u63d2\u4ef6\uff08\u9700\u8981\u670d\u52a1\u7aef\u652f\u6301\u63d2\u4ef6\uff09", None))
        self.dl_update.setText(QCoreApplication.translate("Setiing", u"\u68c0\u67e5MSL2\u66f4\u65b0", None))
        self.cbox_update.setItemText(0, QCoreApplication.translate("Setiing", u"Master", None))
        self.cbox_update.setItemText(1, QCoreApplication.translate("Setiing", u"Monthly", None))
        self.cbox_update.setItemText(2, QCoreApplication.translate("Setiing", u"Dev", None))

        self.n2.setText(QCoreApplication.translate("Setiing", u"\u66f4\u65b0\u901a\u9053:", None))
        self.n3.setHtml(QCoreApplication.translate("Setiing", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Master\u7528\u4e8e\u63a5\u6536\u6700\u65b0\u7684\u7a33\u5b9a\u7248\u672c</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Monthly\u7528\u4e8e\u63a5\u6536\u8f83\u7a33\u5b9a\u7684Beta\u66f4\u65b0\uff0c\u65b0\u52a0\u5165\u7684\u529f\u80fd\u53ef\u80fd\u4f1a\u56e0\u4e3abug\u7528\u4e0d\u4e86\uff0c\u5982\u679c\u60a8\u65b0\u53d1\u73b0\u4e86Bug\u8bf7\u524d\u5f80Github\u63d0\u4ea4issues</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-ind"
                        "ent:0; text-indent:0px;\">Dev\u7528\u4e8e\u63a5\u6536\u6700\u65b0\u5f00\u53d1\u7248\uff0c\u4f46Bug\u4e0d\u662f\u4e00\u822c\u7684\u591a\uff0c\u5982\u679c\u60a8\u4e0d\u662f\u60f3\u534f\u52a9\u6211\u4fee\u590dBug\u8bf7\u4e0d\u8981\u9009\u62e9\u6b64\u901a\u9053(\u63a8\u8350\u5148issues\u8ba8\u8bba\u7136\u540e\u518dpull request)</p></body></html>", None))
        self.cbox_goto_website.setItemText(0, QCoreApplication.translate("Setiing", u"Forge\u5b98\u7f51", None))
        self.cbox_goto_website.setItemText(1, QCoreApplication.translate("Setiing", u"Fabric\u5b98\u7f51", None))
        self.cbox_goto_website.setItemText(2, QCoreApplication.translate("Setiing", u"Cbukkit\u5b98\u7f51(\u4e0b\u8f7d)", None))
        self.cbox_goto_website.setItemText(3, QCoreApplication.translate("Setiing", u"Spigot\u5b98\u7f51(\u4e0b\u8f7d)", None))
        self.cbox_goto_website.setItemText(4, QCoreApplication.translate("Setiing", u"Vanilla\u5b98\u7f51(\u4e0b\u8f7d)", None))

        self.pbtn_goto.setText(QCoreApplication.translate("Setiing", u"\u524d\u5f80", None))
        self.n4.setText(QCoreApplication.translate("Setiing", u"\u66f4\u65b0\u65e5\u5fd7", None))
        self.pbtn_check_configs_for_server.setText(QCoreApplication.translate("Setiing", u"\u68c0\u67e5\u670d\u52a1\u7aef\u8def\u5f84\u4e0b\u6240\u6709\u914d\u7f6e\u6587\u4ef6", None))
        self.pbtn_download_website_manage.setText(QCoreApplication.translate("Setiing", u"\u4e0b\u8f7d\u7f51\u9875\u7ba1\u7406\u63d2\u4ef6\uff08\u9700\u8981\u670d\u52a1\u7aef\u652f\u6301\u63d2\u4ef6\uff09", None))
        self.label.setText(QCoreApplication.translate("Setiing", u"\u4ee5\u4e0b\u63d2\u4ef6\u6211\u89c9\u5f97\u7279\u522b\u6709\u7528\u4f46\u90fd\u4e0d\u662f\u6211\u5199\u7684:", None))
        self.pbtn_ufl1.setText(QCoreApplication.translate("Setiing", u"\u5e38\u7528\u63d2\u4ef6\u5217\u88681", None))
        self.pbtn_ufl2.setText(QCoreApplication.translate("Setiing", u"\u5e38\u7528\u63d2\u4ef6\u5217\u88682", None))
    # retranslateUi

