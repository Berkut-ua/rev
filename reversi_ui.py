# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/zzz/workspace/fr/rev.ui'
#
# Created by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Reversi(object):
    def setupUi(self, Reversi):
        Reversi.setObjectName(_fromUtf8("Reversi"))
        Reversi.resize(571, 368)
        self.centralwidget = QtGui.QWidget(Reversi)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 51, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.strEmail = QtGui.QLineEdit(self.centralwidget)
        self.strEmail.setGeometry(QtCore.QRect(90, 10, 151, 25))
        self.strEmail.setObjectName(_fromUtf8("strEmail"))
        self.btnRegister = QtGui.QPushButton(self.centralwidget)
        self.btnRegister.setGeometry(QtCore.QRect(250, 10, 92, 27))
        self.btnRegister.setObjectName(_fromUtf8("btnRegister"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 90, 321, 171))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier"))
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.btnNewGame = QtGui.QPushButton(self.centralwidget)
        self.btnNewGame.setGeometry(QtCore.QRect(350, 10, 92, 27))
        self.btnNewGame.setObjectName(_fromUtf8("btnNewGame"))
        self.lstWidget = QtGui.QListWidget(self.centralwidget)
        self.lstWidget.setGeometry(QtCore.QRect(350, 90, 211, 171))
        self.lstWidget.setObjectName(_fromUtf8("lstWidget"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 60, 59, 15))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lblBoard = QtGui.QLabel(self.centralwidget)
        self.lblBoard.setGeometry(QtCore.QRect(20, 45, 321, 31))
        self.lblBoard.setText(_fromUtf8(""))
        self.lblBoard.setObjectName(_fromUtf8("lblBoard"))
        self.btnMove = QtGui.QPushButton(self.centralwidget)
        self.btnMove.setGeometry(QtCore.QRect(140, 270, 92, 27))
        self.btnMove.setObjectName(_fromUtf8("btnMove"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 270, 113, 25))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        Reversi.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Reversi)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 571, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Reversi.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Reversi)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Reversi.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(Reversi)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        Reversi.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(Reversi)
        QtCore.QMetaObject.connectSlotsByName(Reversi)

    def retranslateUi(self, Reversi):
        Reversi.setWindowTitle(QtGui.QApplication.translate("Reversi", "Reversi", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Reversi", "e-mail", None, QtGui.QApplication.UnicodeUTF8))
        self.strEmail.setText(QtGui.QApplication.translate("Reversi", "z2@z.ua", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRegister.setText(QtGui.QApplication.translate("Reversi", "Register", None, QtGui.QApplication.UnicodeUTF8))
        self.btnNewGame.setText(QtGui.QApplication.translate("Reversi", "New Game", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Reversi", "Games:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnMove.setWhatsThis(QtGui.QApplication.translate("Reversi", "what is it?\n"
"Source", None, QtGui.QApplication.UnicodeUTF8))
        self.btnMove.setText(QtGui.QApplication.translate("Reversi", "Move", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setToolTip(QtGui.QApplication.translate("Reversi", "Something like 3,4", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("Reversi", "toolBar", None, QtGui.QApplication.UnicodeUTF8))

