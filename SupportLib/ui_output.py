# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'output.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QGridLayout, QTextBrowser)


class Ui_Output(object):
    def setupUi(self, Output):
        if not Output.objectName():
            Output.setObjectName(u"Output")
        Output.resize(640, 480)
        self.gridLayout = QGridLayout(Output)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.show_logs = QTextBrowser(Output)
        self.show_logs.setObjectName(u"show_logs")
        self.show_logs.setStyleSheet(u"border:none;")
        
        self.gridLayout.addWidget(self.show_logs, 0, 0, 1, 1)
        
        self.retranslateUi(Output)
        
        QMetaObject.connectSlotsByName(Output)
    
    # setupUi
    
    def retranslateUi(self, Output):
        Output.setWindowTitle(QCoreApplication.translate("Output", u"Dialog", None))
    # retranslateUi
