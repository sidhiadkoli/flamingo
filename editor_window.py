# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Editor_window.ui'
#
# Created: Mon Apr  7 09:08:25 2014
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
        MainWindow.resize(882, 571)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 0, 881, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 520, 891, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(530, 10, 20, 521))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.commentsListWidget = QtGui.QListWidget(self.centralwidget)
        self.commentsListWidget.setGeometry(QtCore.QRect(550, 20, 321, 291))
        self.commentsListWidget.setProperty("isWrapping", False)
        self.commentsListWidget.setWordWrap(True)
        self.commentsListWidget.setObjectName(_fromUtf8("commentsListWidget"))
        item = QtGui.QListWidgetItem()
        self.commentsListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.commentsListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.commentsListWidget.addItem(item)
        self.editorTextEdit = QtGui.QTextEdit(self.centralwidget)
        self.editorTextEdit.setGeometry(QtCore.QRect(10, 20, 521, 501))
        self.editorTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.editorTextEdit.setReadOnly(False)
        self.editorTextEdit.setObjectName(_fromUtf8("editorTextEdit"))
        self.readabilityTextEdit = QtGui.QTextEdit(self.centralwidget)
        self.readabilityTextEdit.setGeometry(QtCore.QRect(550, 320, 321, 191))
        self.readabilityTextEdit.setReadOnly(True)
        self.readabilityTextEdit.setObjectName(_fromUtf8("readabilityTextEdit"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 882, 22))
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
        __sortingEnabled = self.commentsListWidget.isSortingEnabled()
        self.commentsListWidget.setSortingEnabled(False)
        item = self.commentsListWidget.item(0)
        item.setText(_translate("MainWindow", "Comment 1", None))
        item = self.commentsListWidget.item(1)
        item.setText(_translate("MainWindow", "Comment 2", None))
        item = self.commentsListWidget.item(2)
        item.setText(_translate("MainWindow", "Comment 3", None))
        self.commentsListWidget.setSortingEnabled(__sortingEnabled)
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuTools.setTitle(_translate("MainWindow", "Tools", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))

