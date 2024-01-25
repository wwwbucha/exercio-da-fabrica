# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)
import codigos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(619, 611)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_grande = QFrame(self.centralwidget)
        self.frame_grande.setObjectName(u"frame_grande")
        self.frame_grande.setStyleSheet(u"\n"
"background-color: rgb(0, 0, 255);")
        self.frame_grande.setFrameShape(QFrame.StyledPanel)
        self.frame_grande.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_grande)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.frame_grande)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.usuario = QLabel(self.frame_2)
        self.usuario.setObjectName(u"usuario")
        self.usuario.setScaledContents(False)

        self.verticalLayout_2.addWidget(self.usuario)

        self.usuario_2 = QLineEdit(self.frame_2)
        self.usuario_2.setObjectName(u"usuario_2")

        self.verticalLayout_2.addWidget(self.usuario_2)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame = QFrame(self.frame_grande)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.desenho = QLabel(self.frame)
        self.desenho.setObjectName(u"desenho")
        self.desenho.setEnabled(True)
        self.desenho.setPixmap(QPixmap(u":/codigos/icons/acorn.png"))
        self.desenho.setScaledContents(True)

        self.verticalLayout.addWidget(self.desenho)

        self.senha_2 = QLabel(self.frame)
        self.senha_2.setObjectName(u"senha_2")

        self.verticalLayout.addWidget(self.senha_2)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.lineEdit)


        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout_4.addWidget(self.frame_grande)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 619, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.usuario.setText(QCoreApplication.translate("MainWindow", u"usuario", None))
        self.usuario_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"digite seu usuario:", None))
        self.desenho.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/codigos/icons/animal-penguin.png\"/></p></body></html>", None))
        self.senha_2.setText(QCoreApplication.translate("MainWindow", u"senha", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"digite sua senha:", None))
    # retranslateUi

