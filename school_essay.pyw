# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'School_essay.ui'
#
# Created: Tue Mar 18 15:57:04 2014
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
        MainWindow.resize(651, 567)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.introTextEdit = QtGui.QTextEdit(self.centralwidget)
        self.introTextEdit.setGeometry(QtCore.QRect(170, 10, 461, 131))
        self.introTextEdit.setObjectName(_fromUtf8("introTextEdit"))
        self.point1TextEdit = QtGui.QTextEdit(self.centralwidget)
        self.point1TextEdit.setGeometry(QtCore.QRect(170, 180, 461, 51))
        self.point1TextEdit.setObjectName(_fromUtf8("point1TextEdit"))
        self.point2TextEdit = QtGui.QTextEdit(self.centralwidget)
        self.point2TextEdit.setGeometry(QtCore.QRect(170, 270, 461, 51))
        self.point2TextEdit.setObjectName(_fromUtf8("point2TextEdit"))
        self.point3TextEdit = QtGui.QTextEdit(self.centralwidget)
        self.point3TextEdit.setGeometry(QtCore.QRect(170, 360, 461, 51))
        self.point3TextEdit.setObjectName(_fromUtf8("point3TextEdit"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 460, 111, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 111, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 180, 141, 51))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 270, 131, 51))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 360, 131, 51))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.proceedPushButton = QtGui.QPushButton(self.centralwidget)
        self.proceedPushButton.setGeometry(QtCore.QRect(450, 460, 141, 31))
        self.proceedPushButton.setObjectName(_fromUtf8("proceedPushButton"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 150, 651, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 240, 651, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(0, 330, 651, 20))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(0, 420, 651, 20))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 651, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>School Essay</p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Introduction</p></body></html>", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>Point Considered for </p><p>Paragraph 1</p></body></html>", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>Point Considered for </p><p>Paragraph 2</p></body></html>", None))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>Point Considered for </p><p>Paragraph 3</p></body></html>", None))
        self.proceedPushButton.setText(_translate("MainWindow", "Proceed", None))

