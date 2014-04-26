# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Editor_window.ui'
#
# Created: Fri Apr 25 19:23:29 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(880, 674)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 0, 881, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.commentsListWidget = QtGui.QListWidget(self.centralwidget)
        self.commentsListWidget.setGeometry(QtCore.QRect(540, 30, 331, 281))
        self.commentsListWidget.setProperty("isWrapping", False)
        self.commentsListWidget.setWordWrap(True)
        self.commentsListWidget.setObjectName(_fromUtf8("commentsListWidget"))
        self.readabilityTextEdit = QtGui.QTextEdit(self.centralwidget)
        self.readabilityTextEdit.setGeometry(QtCore.QRect(540, 380, 331, 251))
        self.readabilityTextEdit.setReadOnly(True)
        self.readabilityTextEdit.setObjectName(_fromUtf8("readabilityTextEdit"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(550, 0, 331, 31))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lowrb = QtGui.QRadioButton(self.groupBox)
        self.lowrb.setGeometry(QtCore.QRect(10, 10, 102, 20))
        self.lowrb.setObjectName(_fromUtf8("lowrb"))
        self.highrb = QtGui.QRadioButton(self.groupBox)
        self.highrb.setGeometry(QtCore.QRect(110, 10, 102, 20))
        self.highrb.setChecked(False)
        self.highrb.setObjectName(_fromUtf8("highrb"))
        self.bothrb = QtGui.QRadioButton(self.groupBox)
        self.bothrb.setGeometry(QtCore.QRect(220, 10, 102, 20))
        self.bothrb.setChecked(True)
        self.bothrb.setObjectName(_fromUtf8("bothrb"))
        self.flowerTextEdit = QtGui.QTextEdit(self.centralwidget)
        self.flowerTextEdit.setGeometry(QtCore.QRect(640, 320, 131, 51))
        self.flowerTextEdit.setReadOnly(True)
        self.flowerTextEdit.setObjectName(_fromUtf8("flowerTextEdit"))
        self.editorTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.editorTextEdit.setGeometry(QtCore.QRect(13, 17, 521, 611))
        self.editorTextEdit.setTabStopWidth(42)
        self.editorTextEdit.setObjectName(_fromUtf8("editorTextEdit"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 880, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.lowrb.setText(_translate("MainWindow", "Blue", None))
        self.highrb.setText(_translate("MainWindow", "Red", None))
        self.bothrb.setText(_translate("MainWindow", "Both", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuTools.setTitle(_translate("MainWindow", "Tools", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))

