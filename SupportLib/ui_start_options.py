# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start_options.ui'
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
from PySide6.QtWidgets import (QApplication, QPlainTextEdit, QPushButton, QSizePolicy,
    QTextBrowser, QWidget)

class Ui_ServerStartOptionsSetting(object):
    def setupUi(self, ServerStartOptionsSetting):
        if not ServerStartOptionsSetting.objectName():
            ServerStartOptionsSetting.setObjectName(u"ServerStartOptionsSetting")
        ServerStartOptionsSetting.resize(619, 343)
        self.n1 = QTextBrowser(ServerStartOptionsSetting)
        self.n1.setObjectName(u"n1")
        self.n1.setGeometry(QRect(280, 10, 331, 321))
        self.options = QPlainTextEdit(ServerStartOptionsSetting)
        self.options.setObjectName(u"options")
        self.options.setGeometry(QRect(10, 10, 261, 321))
        self.pbtn_verify_and_exit = QPushButton(ServerStartOptionsSetting)
        self.pbtn_verify_and_exit.setObjectName(u"pbtn_verify_and_exit")
        self.pbtn_verify_and_exit.setGeometry(QRect(129, 310, 141, 20))

        self.retranslateUi(ServerStartOptionsSetting)

        QMetaObject.connectSlotsByName(ServerStartOptionsSetting)
    # setupUi

    def retranslateUi(self, ServerStartOptionsSetting):
        ServerStartOptionsSetting.setWindowTitle(QCoreApplication.translate("ServerStartOptionsSetting", u"Form", None))
        self.n1.setHtml(QCoreApplication.translate("ServerStartOptionsSetting", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u8bf4\u660e</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-XX:+AggressiveOpts \u5c3d\u53ef\u80fd\u4f7f\u7528\u66f4\u591a\u5bf9\u6027\u80fd\u6709\u5e2e\u52a9\u7684\u4f18\u5316\u529f\u80fd</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-XX:+UseCo"
                        "mpressedOops \u6307\u9488\u538b\u7f29\uff0c\u53ea\u652f\u630164Bit\uff0c\u5982\u60a8\u662f32bit\u8bf7\u52ff\u5f00\u542f</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-XX:+UseG1GC \u60a8\u5206\u914d\u7ed9\u670d\u52a1\u5668\u7684\u5185\u5b58\u5fc5\u987b\u5927\u4e8e\u7b49\u4e8e4GB\u4e14\u6700\u5927\u5185\u5b58\u548c\u6700\u5c0f\u5185\u5b58\u76f8\u7b49</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5982\u6709\u5176\u4ed6\u6ce8\u610f\u4e8b\u9879\u8fd8\u8bf7\u8865\u5145\ud83d\ude4f</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u542f\u52a8\u53c2\u6570\u6765\u6e90\uff1a</p>\n"
"<p style=\" margin-top:0px; margin-b"
                        "ottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://logo.gitbook.io/server/5/5-2\"><span style=\" text-decoration: underline; color:#0000ff;\">5-2\uff1a\u8c03\u6574JVM\u542f\u52a8\u53c2\u6570 - \u8fbe\u8fbe\u7684\u5f00\u670d\u6559\u7a0b (gitbook.io)</span></a></p></body></html>", None))
        self.options.setPlainText(QCoreApplication.translate("ServerStartOptionsSetting", u"-XX:+UseG1GC -XX:+UnlockExperimentalVMOptions -XX:MaxGCPauseMillis=100 -XX:+DisableExplicitGC -XX:TargetSurvivorRatio=90 -XX:G1NewSizePercent=50 -XX:G1MaxNewSizePercent=80 -XX:G1MixedGCLiveThresholdPercent=35 -XX:+AlwaysPreTouch -XX:+ParallelRefProcEnabled -Dusing.aikars.flags=mcflags.emc.gs", None))
        self.pbtn_verify_and_exit.setText(QCoreApplication.translate("ServerStartOptionsSetting", u"\u63d0\u4ea4\u5e76\u5173\u95ed\u6b64\u7a97\u53e3", None))
    # retranslateUi

