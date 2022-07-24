# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'output.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QSizePolicy, QTextBrowser,
    QWidget)

class Ui_Output(object):
    def setupUi(self, Output):
        if not Output.objectName():
            Output.setObjectName(u"Output")
        Output.resize(640, 480)
        self.show_logs = QTextBrowser(Output)
        self.show_logs.setObjectName(u"show_logs")
        self.show_logs.setGeometry(QRect(10, 10, 621, 461))

        self.retranslateUi(Output)

        QMetaObject.connectSlotsByName(Output)
    # setupUi

    def retranslateUi(self, Output):
        Output.setWindowTitle(QCoreApplication.translate("Output", u"Dialog", None))
    # retranslateUi

