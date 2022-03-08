# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'download.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QPushButton,
    QSizePolicy, QTextBrowser, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(419, 253)
        self.pbtn_start_download = QPushButton(Dialog)
        self.pbtn_start_download.setObjectName(u"pbtn_start_download")
        self.pbtn_start_download.setGeometry(QRect(330, 10, 80, 22))
        self.pbtn_start_download.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_type = QComboBox(Dialog)
        self.cbox_type.addItem("")
        self.cbox_type.addItem("")
        self.cbox_type.addItem("")
        self.cbox_type.addItem("")
        self.cbox_type.addItem("")
        self.cbox_type.addItem("")
        self.cbox_type.addItem("")
        self.cbox_type.addItem("")
        self.cbox_type.addItem("")
        self.cbox_type.addItem("")
        self.cbox_type.addItem("")
        self.cbox_type.addItem("")
        self.cbox_type.addItem("")
        self.cbox_type.addItem("")
        self.cbox_type.addItem("")
        self.cbox_type.addItem("")
        self.cbox_type.setObjectName(u"cbox_type")
        self.cbox_type.setGeometry(QRect(10, 10, 181, 22))
        self.cbox_type.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox = QComboBox(Dialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(200, 10, 121, 22))
        self.comboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.tb_about = QTextBrowser(Dialog)
        self.tb_about.setObjectName(u"tb_about")
        self.tb_about.setGeometry(QRect(10, 40, 401, 201))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pbtn_start_download.setText(QCoreApplication.translate("Dialog", u"\u5f00\u59cb\u4e0b\u8f7d", None))
        self.cbox_type.setItemText(0, QCoreApplication.translate("Dialog", u"Paper", None))
        self.cbox_type.setItemText(1, QCoreApplication.translate("Dialog", u"Forge", None))
        self.cbox_type.setItemText(2, QCoreApplication.translate("Dialog", u"Vanilla", None))
        self.cbox_type.setItemText(3, QCoreApplication.translate("Dialog", u"Bukkit", None))
        self.cbox_type.setItemText(4, QCoreApplication.translate("Dialog", u"Spigot", None))
        self.cbox_type.setItemText(5, QCoreApplication.translate("Dialog", u"Mojang", None))
        self.cbox_type.setItemText(6, QCoreApplication.translate("Dialog", u"Nukkit", None))
        self.cbox_type.setItemText(7, QCoreApplication.translate("Dialog", u"CubeRite", None))
        self.cbox_type.setItemText(8, QCoreApplication.translate("Dialog", u"GlowStone", None))
        self.cbox_type.setItemText(9, QCoreApplication.translate("Dialog", u"Akarin", None))
        self.cbox_type.setItemText(10, QCoreApplication.translate("Dialog", u"BunggeeCord", None))
        self.cbox_type.setItemText(11, QCoreApplication.translate("Dialog", u"BukkitPlugins", None))
        self.cbox_type.setItemText(12, QCoreApplication.translate("Dialog", u"TacoSpigot", None))
        self.cbox_type.setItemText(13, QCoreApplication.translate("Dialog", u"Cauldron", None))
        self.cbox_type.setItemText(14, QCoreApplication.translate("Dialog", u"Thermos", None))
        self.cbox_type.setItemText(15, QCoreApplication.translate("Dialog", u"WaterFall", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"1.18.1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"1.18", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"1.17.1", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"1.17", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"1.16.5", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Dialog", u"1.16.4", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Dialog", u"1.16.3", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("Dialog", u"1.16.2", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("Dialog", u"1.16.1", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("Dialog", u"1.16", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("Dialog", u"1.15.2", None))
        self.comboBox.setItemText(11, QCoreApplication.translate("Dialog", u"1.15.1", None))
        self.comboBox.setItemText(12, QCoreApplication.translate("Dialog", u"1.15", None))
        self.comboBox.setItemText(13, QCoreApplication.translate("Dialog", u"1.14.4", None))
        self.comboBox.setItemText(14, QCoreApplication.translate("Dialog", u"1.14.3", None))
        self.comboBox.setItemText(15, QCoreApplication.translate("Dialog", u"1.14.2", None))
        self.comboBox.setItemText(16, QCoreApplication.translate("Dialog", u"1.14.1", None))
        self.comboBox.setItemText(17, QCoreApplication.translate("Dialog", u"1.14", None))
        self.comboBox.setItemText(18, QCoreApplication.translate("Dialog", u"1.13.2", None))
        self.comboBox.setItemText(19, QCoreApplication.translate("Dialog", u"1.13.1", None))
        self.comboBox.setItemText(20, QCoreApplication.translate("Dialog", u"1.13", None))
        self.comboBox.setItemText(21, QCoreApplication.translate("Dialog", u"1.12.2", None))
        self.comboBox.setItemText(22, QCoreApplication.translate("Dialog", u"1.12.1", None))
        self.comboBox.setItemText(23, QCoreApplication.translate("Dialog", u"1.12", None))
        self.comboBox.setItemText(24, QCoreApplication.translate("Dialog", u"1.11.2", None))
        self.comboBox.setItemText(25, QCoreApplication.translate("Dialog", u"1.11.1", None))
        self.comboBox.setItemText(26, QCoreApplication.translate("Dialog", u"1.11", None))
        self.comboBox.setItemText(27, QCoreApplication.translate("Dialog", u"1.10.2", None))
        self.comboBox.setItemText(28, QCoreApplication.translate("Dialog", u"1.10.1", None))
        self.comboBox.setItemText(29, QCoreApplication.translate("Dialog", u"1.10", None))
        self.comboBox.setItemText(30, QCoreApplication.translate("Dialog", u"1.9.4", None))
        self.comboBox.setItemText(31, QCoreApplication.translate("Dialog", u"1.9.3", None))
        self.comboBox.setItemText(32, QCoreApplication.translate("Dialog", u"1.9.2", None))
        self.comboBox.setItemText(33, QCoreApplication.translate("Dialog", u"1.9.1", None))
        self.comboBox.setItemText(34, QCoreApplication.translate("Dialog", u"1.9", None))
        self.comboBox.setItemText(35, QCoreApplication.translate("Dialog", u"1.8.9", None))
        self.comboBox.setItemText(36, QCoreApplication.translate("Dialog", u"1.8.8", None))
        self.comboBox.setItemText(37, QCoreApplication.translate("Dialog", u"1.8.7", None))
        self.comboBox.setItemText(38, QCoreApplication.translate("Dialog", u"1.8.6", None))
        self.comboBox.setItemText(39, QCoreApplication.translate("Dialog", u"1.8.5", None))
        self.comboBox.setItemText(40, QCoreApplication.translate("Dialog", u"1.8.4", None))
        self.comboBox.setItemText(41, QCoreApplication.translate("Dialog", u"1.8.3", None))
        self.comboBox.setItemText(42, QCoreApplication.translate("Dialog", u"1.8.2", None))
        self.comboBox.setItemText(43, QCoreApplication.translate("Dialog", u"1.8.1", None))
        self.comboBox.setItemText(44, QCoreApplication.translate("Dialog", u"1.8", None))
        self.comboBox.setItemText(45, QCoreApplication.translate("Dialog", u"1.7.9", None))
        self.comboBox.setItemText(46, QCoreApplication.translate("Dialog", u"1.7.8", None))
        self.comboBox.setItemText(47, QCoreApplication.translate("Dialog", u"1.7.7", None))
        self.comboBox.setItemText(48, QCoreApplication.translate("Dialog", u"1.7.6", None))
        self.comboBox.setItemText(49, QCoreApplication.translate("Dialog", u"1.7.5", None))
        self.comboBox.setItemText(50, QCoreApplication.translate("Dialog", u"1.7.4", None))
        self.comboBox.setItemText(51, QCoreApplication.translate("Dialog", u"1.7.3", None))
        self.comboBox.setItemText(52, QCoreApplication.translate("Dialog", u"1.7.2", None))
        self.comboBox.setItemText(53, QCoreApplication.translate("Dialog", u"1.7.1", None))
        self.comboBox.setItemText(54, QCoreApplication.translate("Dialog", u"1.7", None))

        self.tb_about.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">###############################################</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">         \u672c\u5217\u8868\u53d6\u81eaSakuraMirror,\u5e76\u975eMSL2(C#)\u6240\u4f7f\u7528\u7684\u521d\u68a6\u8d44\u6e90\u7ad9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">     \u6b64\u5217\u8868\u5305\u542b\u4ee5\u4e0b\u79cd\u7c7b\u670d\u52a1\u7aef\uff1a\u4f7f\u7528Java\u7684JE\u670d\u52a1\u7aef     "
                        "     				\u975eJava\u7684JE\u670d\u52a1\u7aef             				\u4f7f\u7528C++\u7684BE\u670d\u52a1\u7aef</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                         	\u4f7f\u7528Java\u7684BE\u670d\u52a1\u7aef</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                         	\u5e26\u53cd\u5411\u4ee3\u7406\u7684\u670d\u52a1\u7aef</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">		\u4e92\u901a\u670d\u670d\u52a1\u7aef</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                      \u6ce8\u610f\uff1a\u6709\u90e8\u5206\u670d\u52a1\u7aef\u53ea\u6709\u8001\u7248\u672c\uff08\u5927\u90e8\u5206\u65f6\u5019\u662f1.12.2\u7248\u672c\uff09</p>\n"
"<p "
                        "style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">             \u90e8\u5206\u670d\u52a1\u7aef\u7684\u7248\u672c\u4e0e\u6e38\u620f\u7248\u672c\u4e0d\u4e00\u6837\uff0c\u6b64\u7c7b\u670d\u52a1\u7aef\u6ca1\u6709\u6807\u6ce8\u662f\u5426\u505c\u66f4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">						\u4f7f\u7528[B]\u8868\u793aBE\u7248\u670d\u52a1\u7aef\uff0c\u9664\u6b64\u4e4b\u5916\u57fa\u672c\u90fd\u662fJE\u7248\u670d\u52a1\u7aef</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">						\u4f7f\u7528[P]\u8868\u793a\u5e26\u53cd\u5411\u4ee3\u7406\u7684\u670d\u52a1\u7aef\uff0c\u9664\u6b64\u4e4b\u5916\u57fa\u672c\u90fd\u4e0d\u5e26\u53cd\u5411\u4ee3\u7406</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">						\u4f7f\u7528"
                        "[J]\u8868\u793a\u4f7f\u7528Java\u7684BE\u670d\u52a1\u7aef</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">						\u4f7f\u7528[C]\u8868\u793a\u4f7f\u7528C++\u7684JE\u670d\u52a1\u7aef</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">						\u4f7f\u7528[\u7248\u672c\u53f7]\u8868\u793a\u76ee\u524d\u53ea\u6709\u8001\u7248\u672c\u7684\u670d\u52a1\u7aef</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">						\u4f7f\u7528[H]\u8868\u793a\u6bd4\u8f83\u786c\u6838\uff0c\u65b0\u624b\u4e0d\u5efa\u8bae\u4f7f\u7528\u7684\u670d\u52a1\u7aef\uff0c\u901a\u5e38\u60c5\u51b5\u4e0b\u4f1a\u4e0e[P]\u4e00\u8d77\u51fa\u73b0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">						\u4f7f\u7528[M]\u8868\u793a\u6027\u80fd\u8f83\u5f3a"
                        "\u7684\u670d\u52a1\u7aef</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">								</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">							\u6574\u7406\u4e0d\u6613\uff0c\u671b\u91c7\u7eb3\uff01</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">###############################################</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[1.12.2]Akarin</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Akarin \u662f\u4e00\u6b3e\u652f\u6301\u591a\u7ebf\u7a0b\u7684 Minecraft \u670d\u52a1\u7aef\uff0c\u6765\u81ea \u201c\u65b0\u7ef4\u5ea6\u201d\uff0c\u524d\u8eab\u662f TorchSpigot \u670d\u52a1\u7aef\u3002</p>\n"
"<p style=\"-"
                        "qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[P][H][M]BungeeCord</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">BungeeCord \u662f\u4e00\u4e2a\u9ad8\u6027\u80fd\u7684\u53cd\u5411\u4ee3\u7406\u670d\u52a1\u7aef\uff0c\u5b83\u53ef\u4ee5\u5c06\u591a\u4e2a Minecraft \u670d\u52a1\u5668\u53d8\u6210\u4e00\u4e2a \u201c\u7fa4\u7ec4\u670d\u52a1\u5668\u201d\u3002</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u4f7f\u7528\u4ecb\u7ecd\uff1ahttp://www.mcbbs.net/thread-424117-1-1.html</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p"
                        ">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[1.7.10]Contigo</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Contigo \u662f Thermos \u7684\u4e00\u4e2a\u5206\u652f\u7248\u672c\uff0c\u652f\u6301 Mod \u548c\u63d2\u4ef6\u3002</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[1.12.2]Craft Bukkit</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Craft Bukkit \u662f\u4e00\u4e2a\u8001\u724c\u7684 Minecraft \u670d\u52a1\u7aef\uff0c\u652f\u6301\u5927\u90e8\u5206\u63d2\u4ef6\uff0c\u529f\u80fd\u6bd4\u8f83\u5b8c\u5584\uff0c\u76ee\u524d\u662f\u66f4\u65b0"
                        "\u6bd4\u8f83\u5feb\u7684\u51e0\u4e2a\u670d\u52a1\u7aef\u4e4b\u4e00\u3002</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u8fd9\u4e2a\u670d\u52a1\u7aef\u5bb9\u6613\u51fa\u73b0\u4e00\u4e9b\u6027\u80fd\u95ee\u9898\uff0c\u5982\u679c\u4f60\u7684\u670d\u52a1\u5668\u7ecf\u5e38\u5728\u65e5\u5fd7\u4e2d\u51fa\u73b0\u201cCan't keep up\u201d\u4e4b\u7c7b\u7684\u62a5\u9519\uff0c\u53ef\u4ee5\u8003\u8651\u4f7f\u7528 Spigot\u3001PaperSpigot \u7b49\u670d\u52a1\u7aef\u3002</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[C][M]CubeRite \u662f\u4e00\u4e2a\u57fa\u4e8e C++ \u7f16\u5199\u7684\u5f00\u6e90\u9ad8\u6027\u80fd Minecraft \u670d\u52a1\u7aef</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left"
                        ":0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u76ee\u524d Cuberite \u5df2\u7ecf\u53ef\u4ee5\u505a\u5230\u5927\u90e8\u5206\u7684\u57fa\u4e8e Bukkit \u67b6\u6784\u7684 Minecraft \u670d\u52a1\u7aef\uff08\u4f8b\u5982 Spigot\uff09\u7684\u529f\u80fd\uff0c\u5e76\u4e14\u5728\u6027\u80fd\u65b9\u9762\u5177\u6709\u66f4\u5927\u7684\u4f18\u52bf\u3002</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[P][H][M]DragonProxy</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">DragonProxy \u9f99\u4ee3\u7406\u662f\u4e00\u4e2a\u9ad8\u6027\u80fd\u7684\u53cd\u5411\u4ee3\u7406\u670d\u52a1\u7aef\uff0c\u5176\u529f\u80fd\u7c7b\u4f3c\u4e8e BungeeCord\uff0c\u4f46\u662f\u5b83\u7684\u4f5c\u7528\u662f\u8ba9\u7535"
                        "\u8111\u548c\u624b\u673a\u4e00\u8d77\u8054\u673a</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[1.12.2][P][H]GlowStone</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">GlowStone \u8424\u77f3\u662f\u4e00\u6b3e\u5f00\u6e90\u7684 Bukkit \u670d\u52a1\u7aef\uff0c\u5f00\u53d1\u8005\u53ef\u4ee5\u6839\u636e\u81ea\u5df1\u9700\u6c42\u4fee\u6539\u6216\u5236\u4f5c\u4e00\u4e2a\u670d\u52a1\u7aef\uff0c\u5185\u7f6e\u4e86 Sponge \u652f\u6301\u7684\u63d2\u4ef6\u3002</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0p"
                        "x; -qt-block-indent:0; text-indent:0px;\">[P][H][M]HexaCord</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">HexaCord \u662f\u4e00\u4e2a fork \u81ea BungeeCord \u7684\u53cd\u5411\u4ee3\u7406\u670d\u52a1\u7aef\uff0c\u57fa\u4e8e\u539f\u57fa\u7840\u505a\u4e86\u4e00\u4e9b\u4f18\u5316\uff0c\u5305\u62ec\u6027\u80fd\u7684\u63d0\u5347\u3002</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[1.11.2][M]Hose</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hose \u662f\u4e00\u6b3e\u5f00\u6e90\u7684\u591a\u7ebf\u7a0b Minecraft \u670d\u52a1\u7aef\uff0c\u6027\u80fd\u66f4\u5f3a\u3002</p>\n"
"<p style=\"-qt-paragraph-type:empty; margi"
                        "n-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[B]MiNET</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">MiNET \u662f\u4e00\u4e2a\u7528 C \u8bed\u8a00\u7f16\u5199\u7684 Minecraft PE \u57fa\u5ca9\u7248\u670d\u52a1\u7aef\u3002</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">MiNET \u9762\u5411\u7684\u662f\u5927\u578b\u7684 Minecraft \u6e38\u620f\u670d\u52a1\u5668\uff0c\u62e5\u6709\u4f01\u4e1a\u7ea7\u7684\u7a33\u5b9a\u6027\u3002</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u670d\u52a1\u7aef\u7684\u6bcf\u4e2a\u5b9e\u4f8b\u53ef\u4ee5\u540c\u65f6\u5728\u7ebf 10-100 \u4e2a\u73a9\u5bb6\uff0c"
                        "MiNET \u7684\u76ee\u6807\u662f\u5343\u4eba\u5728\u7ebf\uff08\u5f88\u5f3a\uff09\u3002</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">MiNET \u5728\u672a\u6765\u53ef\u80fd\u4f1a\u6210\u4e3a\u5fae\u8f6f\u4e91\u4ea7\u54c1\uff08\u5b98\u65b9\u539f\u8bdd\u7ffb\u8bd1\uff09</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Bugjump</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u61c2\u5f97\u90fd\u61c2\uff0c\u5b98\u65b9\u670d\u52a1\u7aef\uff0c\u5565\u90fd\u52a0\u4e0d\u4e86</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
                        "<br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[B][J]Nukkit</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Nukkit \u662f\u4e00\u6b3e\u7531 Java \u9a71\u52a8\u7684 Minecraft PE \u643a\u5e26\u7248\u670d\u52a1\u7aef\uff0c\u9002\u5408\u5f00\u4e00\u4e2a\u591a\u4eba\u8054\u673a\u7684 PE \u7248\u672c\u670d\u52a1\u5668\u3002</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[J]NukkitX</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">NukkitX \u5e94\u8be5\u662f Nukkit \u7684\u5f3a\u5316 / \u540e\u7eed\u7248\u672c\uff0c\u8fd9\u662f\u4e00\u4e2a"
                        "\u9ad8\u6027\u80fd\u7684 Minecraft PE \u57fa\u5ca9\u7248\u670d\u52a1\u5668\uff0c\u7531 Java \u5f3a\u529b\u9a71\u52a8\u3002</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[1.12.2]PaperSpigot</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Spigot \u7684\u8fdb\u4e00\u6b65\u4f18\u5316\u7248\u672c\uff0c\u5728\u76f8\u5173\u7b97\u6cd5\u65b9\u9762\uff0c\u8f83 Spigot \u6709\u6240\u63d0\u9ad8\uff0c\u4f18\u5316 TPS \u7b49\uff0c\u652f\u6301 CraftBukkit \u548c Spigot \u63d2\u4ef6\uff0cAPI \u6ca1\u6709\u592a\u5927\u4fee\u6539\u3002</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5728 1.9 \u7248\u672c\u4e4b\u524d\u90fd\u5e26\u6709"
                        "\u53cd\u4f5c\u5f0a\u529f\u80fd\uff0c1.9 \u4e4b\u540e\u7684\u7248\u672c\u9700\u8981\u81ea\u884c\u5b89\u88c5\u5176\u4ed6\u53cd\u4f5c\u5f0a\u63d2\u4ef6\u3002</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PocketMine-MP</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PocketMine-MP \u662f\u4e00\u4e2a\u7528 PHP \u5f00\u53d1\u7684 Minecraft Bedrock \u57fa\u5ca9\u7248\u670d\u52a1\u7aef\uff0c\u4e5f\u662f\u76ee\u524d\u4f7f\u7528\u6700\u4e3a\u5e7f\u6cdb\u7684\u670d\u52a1\u7aef\u4e4b\u4e00\u3002</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u56e0\u4e3a\u9ad8\u53ef\u6269\u5c55\u6027\u548c\u63d2\u4ef6\u7f16\u5199\u8d77\u6765"
                        "\u76f8\u5bf9\u7b80\u6613\uff0c\u6df1\u53d7\u5e7f\u5927\u624b\u673a\u7248\u670d\u4e3b\u559c\u7231\u3002</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[1.13.2]Spigot</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Spigot \u662f CraftBukkit \u670d\u52a1\u7aef\u4e4b\u540e\u7684\u5ef6\u7eed\u7248\u672c\uff0c\u6bd4 CraftBukkit \u4f18\u5316\u4e86\u4e0d\u5c11\u5730\u65b9\uff0c\u652f\u6301 CraftBukkit \u7684\u63d2\u4ef6\uff0c\u6027\u80fd\u6bd4 CraftBukkit \u597d\u5f88\u591a\uff0c\u5e76\u4e14\u81ea\u5e26\u53cd\u4f5c\u5f0a\u529f\u80fd</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<"
                        "p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[1.11.2]Sponge Forge</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sponge \u662f\u4e00\u4e2a\u5168\u65b0\u7684\u670d\u52a1\u7aef\uff0c\u652f\u6301 Sponge \u7684\u4e13\u7528\u63d2\u4ef6\uff0c\u53ef\u88c5 Mod\uff0c\u517c\u5bb9\u6027\u6bd4 Cauldron \u76f8\u6bd4\u63d0\u9ad8\u4e86\u4e0d\u5c11\uff0c\u9002\u5408\u5f00 MOD \u670d\uff0c\u652f\u6301\u7684\u7248\u672c\u975e\u5e38\u9ad8\uff0c\u662f\u76ee\u524d\u652f\u6301 MOD \u7684\u670d\u52a1\u7aef\u91cc\u517c\u5bb9\u7248\u672c\u6700\u9ad8\u7684\u670d\u52a1\u7aef\u3002</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sponge \u672c\u8eab\u4e0d\u652f\u6301 Bukkit \u63d2\u4ef6\uff08\u5373\u4f7f\u6709\u517c\u5bb9\u5c42\uff0c\u6548\u679c\u4e5f\u4e0d\u662f\u5f88\u597d\uff0c\u53ea\u80fd\u652f\u6301\u4e00"
                        "\u822c\u7684\u63d2\u4ef6\uff09\uff0c\u9700\u8981\u670d\u52a1\u5668\u7684\u914d\u7f6e\u6bd4\u8f83\u9ad8\uff0c\u542f\u52a8\u901f\u5ea6\u4e0d\u4f73\u3002</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[1.12.2]Sponge Vanilla</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">SpongeVanilla \u662f SpongeForge \u7684\u7eaf\u51c0\u7248\u672c\uff0c\u540c\u6837\u652f\u6301 SpongeForge \u7684\u63d2\u4ef6\u3002</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u6027\u80fd\u76f8\u5bf9\u8f83\u597d\uff0c\u5360\u7528\u7684\u5185\u5b58\u8f83\u5c11\uff0c\u9002\u5408\u4f4e\u914d\u673a\u5668\u5f00\u670d\uff0c\u5bf9 Bukkit \u63d2\u4ef6\u7684"
                        "\u652f\u6301\u4e0d\u4f73\uff0c\u63d2\u4ef6\u975e\u5e38\u5c11\uff0c\u914d\u7f6e\u4e0d\u65b9\u4fbf\uff0c\u4e0d\u80fd\u5b89\u88c5Mod\u3002</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[1.12.2]TacoSpigot</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">TacoSpigot \u662f Spigot \u7684\u4f18\u5316\u7248\u672c\uff0c\u652f\u6301 CraftBukkit \u548c Spigot \u7684\u63d2\u4ef6\uff0cAPI \u57fa\u672c\u65e0\u53d8\u5316\uff0c\u81ea\u5e26\u53cd\u4f5c\u5f0a\u3002</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;"
                        " -qt-block-indent:0; text-indent:0px;\">[1.12.2]Torch</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Torch \u662f\u4e00\u6b3e\u7531\u56fd\u4eba\u5236\u4f5c\u7684\u670d\u52a1\u7aef\uff0c\u662f Spigot \u7684\u4f18\u5316\u7248\u672c\uff0c\u652f\u6301\u975e\u5e38\u591a\u63d2\u4ef6\uff0c\u6027\u80fd\u5f3a\u608d\uff0c\u652f\u6301\u591a\u6838\u5fc3 CPU \u8fd0\u7b97\uff0c\u81ea\u5e26\u53cd\u4f5c\u5f0a\u529f\u80fd\u3002</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Vefland \u662f\u7531\u683c\u5170\u8482\u534f\u4f1a\u521b\u59cb\u4eba\u4e50\u4e50\u63a5\u624b TorchSpigot \u5f00\u53d1\u540e\u7684\u65b0\u9879\u76ee\uff0c\u540c\u6837\u662f\u4e00\u4e2a\u591a\u7ebf\u7a0b\u7684\u670d\u52a1\u7aef\uff0c\u6027\u80fd"
                        "\u4f18\u5316\u6781\u4f73\uff0c\u542f\u52a8\u901f\u5ea6\u6bd4\u9999\u6e2f\u8bb0\u8005\u8fd8\u5feb\u3002</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[1.12.2]Velocity</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Velocity \u662f\u4e00\u4e2a Minecraft \u53cd\u5411\u4ee3\u7406\u670d\u52a1\u7aef\uff0c\u62e5\u6709\u975e\u5e38\u5f3a\u5927\u7684\u670d\u52a1\u5668\u652f\u6301\uff0c\u53ef\u6269\u5c55\u6027\u548c\u7075\u6d3b\u6027\u3002</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5bf9\u4e8e\u5927\u578b\u7fa4\u7ec4\u670d\u52a1\u5668\uff0cVelocity \u662f\u4e00\u4e2a\u5f88\u597d\u7684\u9009\u62e9\u3002</p>\n"
"<p sty"
                        "le=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">WaterFall</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">WaterFall \u662f BungeeCord \u7684\u4e00\u4e2a\u5206\u652f\u3002</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Waterfall \u81f4\u529b\u4e8e\u4f18\u5316 Bungeecord \u5728\u4ee3\u7406\u670d\u52a1\u7aef\u6570\u636e\u8fc7\u7a0b\u4e2d\u4ea7\u751f\u7684\u4e0d\u5fc5\u8981\u5783\u573e\uff0c\u4f7f\u4f60\u7684 BungeeCord \u6027\u80fd\u66f4\u9ad8\uff0c\u66f4\u5145\u5206\u53d1\u6325\u5728\u5f88\u9ad8\u73a9\u5bb6\u5728\u7ebf\u6570\u65f6 CPU \u7684\u6027\u80fd\u3002</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px"
                        "; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5927\u5bb6\u90fd\u77e5\u9053\uff0c\u4e00\u65e6 MCPC\uff0c\u6216\u8005 KCauldron \u7b49 mod \u670d\u52a1\u7aef\u5728 BC \u8fdb\u884c\u8de8\u670d\u7684\u65f6\u5019\uff0c\u8fd9\u5c06\u4f1a\u4f7f\u5c1d\u8bd5\u8de8\u670d\u7684\u73a9\u5bb6\u7684\u5ba2\u6237\u7aef\u5d29\u6e83\uff0c\u800c WaterFall \u4e0d\u4f1a,\u5b83\u53ca\u65f6\u4fee\u590d\u4e86\u8fd9\u4e2a Bug\u3002</p></body></html>", None))
    # retranslateUi

