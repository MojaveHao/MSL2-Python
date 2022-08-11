# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'help.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QLabel, QLineEdit,
                               QPushButton, QTextBrowser)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(481, 298)
        self.n1 = QLabel(Dialog)
        self.n1.setObjectName(u"n1")
        self.n1.setGeometry(QRect(180, 0, 111, 41))
        font = QFont()
        font.setPointSize(16)
        self.n1.setFont(font)
        self.n2 = QLabel(Dialog)
        self.n2.setObjectName(u"n2")
        self.n2.setGeometry(QRect(10, 40, 451, 20))
        self.n3 = QLabel(Dialog)
        self.n3.setObjectName(u"n3")
        self.n3.setGeometry(QRect(210, 60, 61, 16))
        self.help_list = QTextBrowser(Dialog)
        self.help_list.setObjectName(u"help_list")
        self.help_list.setGeometry(QRect(20, 90, 361, 192))
        self.pbtn_visit = QPushButton(Dialog)
        self.pbtn_visit.setObjectName(u"pbtn_visit")
        self.pbtn_visit.setGeometry(QRect(390, 150, 80, 22))
        self.n4 = QLabel(Dialog)
        self.n4.setObjectName(u"n4")
        self.n4.setGeometry(QRect(390, 100, 81, 16))
        self.ledit_no = QLineEdit(Dialog)
        self.ledit_no.setObjectName(u"ledit_no")
        self.ledit_no.setGeometry(QRect(390, 125, 81, 21))
        self.pbtn_exit = QPushButton(Dialog)
        self.pbtn_exit.setObjectName(u"pbtn_exit")
        self.pbtn_exit.setGeometry(QRect(390, 180, 80, 22))
        
        self.retranslateUi(Dialog)
        
        QMetaObject.connectSlotsByName(Dialog)
    
    # setupUi
    
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.n1.setText(QCoreApplication.translate("Dialog", u"\u5e2e\u52a9\u4e0e\u652f\u6301", None))
        self.n2.setText(QCoreApplication.translate("Dialog",
                                                   u"\u6b22\u8fce\u6765\u5230Msl2-Python\u7684\u5e2e\u52a9\u4e0e\u652f\u6301\u9875\u9762\uff01\u5f00\u670d\u8fc7\u7a0b\u4e2d\u4e00\u4e9b\u57fa\u672c\u95ee\u9898\u90fd\u53ef\u4ee5\u5728\u8fd9\u91cc\u627e\u5230\u7b54\u6848\uff01",
                                                   None))
        self.n3.setText(QCoreApplication.translate("Dialog", u"\u5f00\u670d\u6109\u5feb:)", None))
        self.help_list.setHtml(QCoreApplication.translate("Dialog",
                                                          u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                          "                    <html><head><meta name=\"qrichtext\" content=\"1\" /><style\n"
                                                          "                    type=\"text/css\">\n"
                                                          "                    p, li { white-space: pre-wrap; }\n"
                                                          "                    </style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\n"
                                                          "                    font-weight:400; font-style:normal;\">\n"
                                                          "                    <p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px;\n"
                                                          "                    margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.<span style=\"\n"
                                                          "                    font-family:'Consolas','Courier New','monospace'; font-size:14px; color:#008000;\">server.properties\u5982\u4f55\u914d\u7f6e</span></p>\n"
                                                          "                    <p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px;\n"
                                                          "                    margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\"\n"
                                                          "            "
                                                          "        font-family:'Consolas','Courier New','monospace'; font-size:14px; color:#008000;\">2.\u670d\u52a1\u7aef\u7684\u6587\u4ef6\u7ed3\u6784</span></p>\n"
                                                          "                    <p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px;\n"
                                                          "                    margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\"\n"
                                                          "                    font-family:'Consolas','Courier New','monospace'; font-size:14px; color:#008000;\">3.\u7b2c\u4e00\u6b21\u5f00\u670d\u524d\u7684\u51c6\u5907\u5de5\u4f5c</span></p>\n"
                                                          "                    <p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px;\n"
                                                          "                    margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\"\n"
                                                          "                    font-family:'Consolas','Courier New','monospace'; font-size:14px; color:#008000;\">4.\u5e38\u7528\u6307\u4ee4</span></p>\n"
                                                          "                    <p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px;\n"
                                                          "                    margin-ri"
                                                          "ght:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\"\n"
                                                          "                    font-family:'Consolas','Courier New','monospace'; font-size:14px; color:#008000;\">5.\u5e38\u7528\u63d2\u4ef6</span></p>\n"
                                                          "                    <p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px;\n"
                                                          "                    margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\"\n"
                                                          "                    font-family:'Consolas','Courier New','monospace'; font-size:14px; color:#008000;\">6.\u5173\u4e8eLog4j2\u6f0f\u6d1e</span></p></body></html>\n"
                                                          "                ", None))
        self.pbtn_visit.setText(QCoreApplication.translate("Dialog", u"\u67e5\u770b", None))
        self.n4.setText(QCoreApplication.translate("Dialog", u"\u8bf7\u8f93\u5165\u60a8\u7684\u7f16\u53f7\uff1a", None))
        self.pbtn_exit.setText(QCoreApplication.translate("Dialog", u"\u9000\u51fa", None))
    # retranslateUi
