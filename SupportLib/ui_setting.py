# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QPushButton, QSizePolicy, QTabWidget, QTextBrowser,
    QWidget)

class Ui_Setting(object):
    def setupUi(self, Setiing):
        if not Setiing.objectName():
            Setiing.setObjectName(u"Setiing")
        Setiing.resize(503, 338)
        self.tabWidget = QTabWidget(Setiing)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 481, 321))
        self.tab_update = QWidget()
        self.tab_update.setObjectName(u"tab_update")
        self.n3 = QTextBrowser(self.tab_update)
        self.n3.setObjectName(u"n3")
        self.n3.setGeometry(QRect(10, 60, 191, 221))
        self.cbox_update = QComboBox(self.tab_update)
        self.cbox_update.addItem("")
        self.cbox_update.addItem("")
        self.cbox_update.addItem("")
        self.cbox_update.setObjectName(u"cbox_update")
        self.cbox_update.setGeometry(QRect(200, 20, 91, 22))
        self.cbox_update.setCursor(QCursor(Qt.PointingHandCursor))
        self.n2 = QLabel(self.tab_update)
        self.n2.setObjectName(u"n2")
        self.n2.setGeometry(QRect(130, 20, 71, 16))
        self.dl_update = QPushButton(self.tab_update)
        self.dl_update.setObjectName(u"dl_update")
        self.dl_update.setGeometry(QRect(0, 20, 131, 22))
        self.dl_update.setCursor(QCursor(Qt.PointingHandCursor))
        self.n5 = QLabel(self.tab_update)
        self.n5.setObjectName(u"n5")
        self.n5.setGeometry(QRect(10, 40, 41, 16))
        self.n4 = QLabel(self.tab_update)
        self.n4.setObjectName(u"n4")
        self.n4.setGeometry(QRect(210, 50, 71, 16))
        self.update_log = QTextBrowser(self.tab_update)
        self.update_log.setObjectName(u"update_log")
        self.update_log.setGeometry(QRect(210, 70, 271, 211))
        self.n1 = QLabel(self.tab_update)
        self.n1.setObjectName(u"n1")
        self.n1.setGeometry(QRect(10, 0, 69, 20))
        self.tabWidget.addTab(self.tab_update, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.pbtn_ufl2 = QPushButton(self.tab_2)
        self.pbtn_ufl2.setObjectName(u"pbtn_ufl2")
        self.pbtn_ufl2.setGeometry(QRect(130, 120, 121, 31))
        self.pbtn_download_website_manage = QPushButton(self.tab_2)
        self.pbtn_download_website_manage.setObjectName(u"pbtn_download_website_manage")
        self.pbtn_download_website_manage.setGeometry(QRect(10, 90, 291, 22))
        self.pbtn_download_website_manage.setCursor(QCursor(Qt.PointingHandCursor))
        self.pbtn_ufl1 = QPushButton(self.tab_2)
        self.pbtn_ufl1.setObjectName(u"pbtn_ufl1")
        self.pbtn_ufl1.setGeometry(QRect(10, 120, 121, 31))
        self.pbtn_download_auto_backup = QPushButton(self.tab_2)
        self.pbtn_download_auto_backup.setObjectName(u"pbtn_download_auto_backup")
        self.pbtn_download_auto_backup.setGeometry(QRect(10, 60, 291, 22))
        self.pbtn_download_auto_backup.setCursor(QCursor(Qt.PointingHandCursor))
        self.n9 = QLabel(self.tab_2)
        self.n9.setObjectName(u"n9")
        self.n9.setGeometry(QRect(10, 40, 281, 16))
        self.pbtn_goto = QPushButton(self.tab_2)
        self.pbtn_goto.setObjectName(u"pbtn_goto")
        self.pbtn_goto.setGeometry(QRect(10, 170, 51, 22))
        self.cbox_goto_website = QComboBox(self.tab_2)
        self.cbox_goto_website.addItem("")
        self.cbox_goto_website.addItem("")
        self.cbox_goto_website.addItem("")
        self.cbox_goto_website.addItem("")
        self.cbox_goto_website.addItem("")
        self.cbox_goto_website.setObjectName(u"cbox_goto_website")
        self.cbox_goto_website.setGeometry(QRect(60, 170, 191, 22))
        self.cbox_goto_website.setCursor(QCursor(Qt.PointingHandCursor))
        self.n7 = QLabel(self.tab_2)
        self.n7.setObjectName(u"n7")
        self.n7.setGeometry(QRect(10, 10, 69, 20))
        self.pbtn_view_at_docment = QPushButton(self.tab_2)
        self.pbtn_view_at_docment.setObjectName(u"pbtn_view_at_docment")
        self.pbtn_view_at_docment.setGeometry(QRect(10, 200, 211, 29))
        self.pbtn_how_to_choice = QPushButton(self.tab_2)
        self.pbtn_how_to_choice.setObjectName(u"pbtn_how_to_choice")
        self.pbtn_how_to_choice.setGeometry(QRect(110, 260, 93, 29))
        self.pbtn_how_to_choice.setCursor(QCursor(Qt.PointingHandCursor))
        self.pbtn_download = QPushButton(self.tab_2)
        self.pbtn_download.setObjectName(u"pbtn_download")
        self.pbtn_download.setGeometry(QRect(210, 260, 93, 29))
        self.pbtn_download.setCursor(QCursor(Qt.PointingHandCursor))
        self.n6 = QLabel(self.tab_2)
        self.n6.setObjectName(u"n6")
        self.n6.setGeometry(QRect(20, 230, 301, 20))
        self.cbox_want_to_download = QComboBox(self.tab_2)
        self.cbox_want_to_download.addItem("")
        self.cbox_want_to_download.addItem("")
        self.cbox_want_to_download.addItem("")
        self.cbox_want_to_download.addItem("")
        self.cbox_want_to_download.setObjectName(u"cbox_want_to_download")
        self.cbox_want_to_download.setGeometry(QRect(20, 260, 87, 26))
        self.cbox_want_to_download.setCursor(QCursor(Qt.PointingHandCursor))
        self.pbtn_goto_mosl = QPushButton(self.tab_2)
        self.pbtn_goto_mosl.setObjectName(u"pbtn_goto_mosl")
        self.pbtn_goto_mosl.setGeometry(QRect(310, 270, 151, 20))
        self.n8 = QLabel(self.tab_2)
        self.n8.setObjectName(u"n8")
        self.n8.setGeometry(QRect(310, 250, 121, 16))
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Setiing)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Setiing)
    # setupUi

    def retranslateUi(self, Setiing):
        Setiing.setWindowTitle(QCoreApplication.translate("Setiing", u"Dialog", None))
        self.n3.setHtml(QCoreApplication.translate("Setiing", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\">Main\u7528\u4e8e\u63a5\u6536\u6700\u65b0\u7684\u7a33\u5b9a\u7248\u672c                    </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\">Monthly\u7528\u4e8e\u63a5\u6536\u8f83\u7a33\u5b9a\u7684Beta\u66f4\u65b0\uff0c\u65b0\u52a0\u5165\u7684\u529f\u80fd\u53ef\u80fd\u4f1a\u56e0\u4e3abug\u7528\u4e0d\u4e86\uff0c\u5982\u679c\u60a8\u65b0\u53d1\u73b0\u4e86Bug\u8bf7"
                        "\u524d\u5f80Github\u63d0\u4ea4issues                    </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\">Dev\u7528\u4e8e\u63a5\u6536\u6700\u65b0\u5f00\u53d1\u7248\uff0c\u4f46Bug\u4e0d\u662f\u4e00\u822c\u7684\u591a\uff0c\u5982\u679c\u60a8\u4e0d\u662f\u60f3\u534f\u52a9\u6211\u4fee\u590dBug\u8bf7\u4e0d\u8981\u9009\u62e9\u6b64\u901a\u9053(\u63a8\u8350\u5148issues\u8ba8\u8bba\u7136\u540e\u518dpull request)</span><span style=\" font-family:'Microsoft YaHei UI';\">                </span></p></body></html>", None))
        self.cbox_update.setItemText(0, QCoreApplication.translate("Setiing", u"Main", None))
        self.cbox_update.setItemText(1, QCoreApplication.translate("Setiing", u"Monthly", None))
        self.cbox_update.setItemText(2, QCoreApplication.translate("Setiing", u"Dev", None))

        self.n2.setText(QCoreApplication.translate("Setiing", u"\u66f4\u65b0\u901a\u9053:", None))
        self.dl_update.setText(QCoreApplication.translate("Setiing", u"\u68c0\u67e5MSL2\u66f4\u65b0", None))
        self.n5.setText(QCoreApplication.translate("Setiing", u"\u8bf4\u660e\uff1a", None))
        self.n4.setText(QCoreApplication.translate("Setiing", u"\u66f4\u65b0\u65e5\u5fd7", None))
        self.n1.setText(QCoreApplication.translate("Setiing", u"\u66f4\u65b0\u8bbe\u7f6e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_update), QCoreApplication.translate("Setiing", u"Tab 1", None))
        self.pbtn_ufl2.setText(QCoreApplication.translate("Setiing", u"\u5e38\u7528\u63d2\u4ef6\u5217\u88682", None))
        self.pbtn_download_website_manage.setText(QCoreApplication.translate("Setiing", u"\u4e0b\u8f7d\u7f51\u9875\u7ba1\u7406\u63d2\u4ef6\uff08\u9700\u8981\u670d\u52a1\u7aef\u652f\u6301\u63d2\u4ef6\uff09", None))
        self.pbtn_ufl1.setText(QCoreApplication.translate("Setiing", u"\u5e38\u7528\u63d2\u4ef6\u5217\u88681", None))
        self.pbtn_download_auto_backup.setText(QCoreApplication.translate("Setiing", u"\u4e0b\u8f7d\u81ea\u52a8\u5907\u4efd\u63d2\u4ef6\uff08\u9700\u8981\u670d\u52a1\u7aef\u652f\u6301\u63d2\u4ef6\uff09", None))
        self.n9.setText(QCoreApplication.translate("Setiing", u"\u4ee5\u4e0b\u63d2\u4ef6\u6211\u89c9\u5f97\u7279\u522b\u6709\u7528\u4f46\u90fd\u4e0d\u662f\u6211\u5199\u7684:", None))
        self.pbtn_goto.setText(QCoreApplication.translate("Setiing", u"\u524d\u5f80", None))
        self.cbox_goto_website.setItemText(0, QCoreApplication.translate("Setiing", u"Forge\u5b98\u7f51", None))
        self.cbox_goto_website.setItemText(1, QCoreApplication.translate("Setiing", u"Fabric\u5b98\u7f51", None))
        self.cbox_goto_website.setItemText(2, QCoreApplication.translate("Setiing", u"Cbukkit\u5b98\u7f51(\u4e0b\u8f7d)", None))
        self.cbox_goto_website.setItemText(3, QCoreApplication.translate("Setiing", u"Spigot\u5b98\u7f51(\u4e0b\u8f7d)", None))
        self.cbox_goto_website.setItemText(4, QCoreApplication.translate("Setiing", u"Vanilla\u5b98\u7f51(\u4e0b\u8f7d)", None))

        self.n7.setText(QCoreApplication.translate("Setiing", u"\u4e0b\u8f7d", None))
        self.pbtn_view_at_docment.setText(QCoreApplication.translate("Setiing", u"\u67e5\u770b\u6587\u6863\u4e2d\u7684Java\u5b89\u88c5\u65b9\u6cd5", None))
        self.pbtn_how_to_choice.setText(QCoreApplication.translate("Setiing", u"\u5982\u4f55\u9009\u62e9", None))
        self.pbtn_download.setText(QCoreApplication.translate("Setiing", u"\u4e0b\u8f7d", None))
        self.n6.setText(QCoreApplication.translate("Setiing", u"\u901a\u8fc7apt\u4e0b\u8f7dJava\uff08\u4e0d\u63a8\u8350\uff0c\u4ec5Ubuntu\u7b49\u5c11\u6570\u7cfb\u7edf\u53ef\u7528\uff09:", None))
        self.cbox_want_to_download.setItemText(0, QCoreApplication.translate("Setiing", u"Java17", None))
        self.cbox_want_to_download.setItemText(1, QCoreApplication.translate("Setiing", u"Java16", None))
        self.cbox_want_to_download.setItemText(2, QCoreApplication.translate("Setiing", u"Java8", None))
        self.cbox_want_to_download.setItemText(3, QCoreApplication.translate("Setiing", u"Java7", None))

        self.pbtn_goto_mosl.setText(QCoreApplication.translate("Setiing", u"\u524d\u5f80moslauncher.tk\u4e0b\u8f7d", None))
        self.n8.setText(QCoreApplication.translate("Setiing", u"Win/macOS\u53ef\u4ee5\u9009\u62e9\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Setiing", u"Tab 2", None))
    # retranslateUi

