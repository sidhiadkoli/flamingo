# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Create_file.ui'
#
# Created: Tue Mar 18 13:12:58 2014
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
        MainWindow.resize(636, 486)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 60, 161, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.pathTextEdit = QtGui.QTextEdit(self.centralwidget)
        self.pathTextEdit.setGeometry(QtCore.QRect(30, 90, 331, 31))
        self.pathTextEdit.setFrameShadow(QtGui.QFrame.Sunken)
        self.pathTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pathTextEdit.setReadOnly(False)
        self.pathTextEdit.setAcceptRichText(False)
        self.pathTextEdit.setObjectName(_fromUtf8("pathTextEdit"))
        self.browsePushButton = QtGui.QPushButton(self.centralwidget)
        self.browsePushButton.setGeometry(QtCore.QRect(390, 90, 91, 31))
        self.browsePushButton.setObjectName(_fromUtf8("browsePushButton"))
        self.openPushButton = QtGui.QPushButton(self.centralwidget)
        self.openPushButton.setGeometry(QtCore.QRect(30, 130, 81, 31))
        self.openPushButton.setObjectName(_fromUtf8("openPushButton"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 193, 161, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.nameTextEdit = QtGui.QTextEdit(self.centralwidget)
        self.nameTextEdit.setGeometry(QtCore.QRect(210, 220, 331, 31))
        self.nameTextEdit.setObjectName(_fromUtf8("nameTextEdit"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 230, 61, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 270, 51, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 310, 131, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.createPushButton = QtGui.QPushButton(self.centralwidget)
        self.createPushButton.setGeometry(QtCore.QRect(360, 400, 75, 23))
        self.createPushButton.setObjectName(_fromUtf8("createPushButton"))
        self.cancelPushButton = QtGui.QPushButton(self.centralwidget)
        self.cancelPushButton.setGeometry(QtCore.QRect(460, 400, 75, 23))
        self.cancelPushButton.setObjectName(_fromUtf8("cancelPushButton"))
        self.themeComboBox = QtGui.QComboBox(self.centralwidget)
        self.themeComboBox.setGeometry(QtCore.QRect(210, 260, 291, 31))
        self.themeComboBox.setObjectName(_fromUtf8("themeComboBox"))
        self.readabilityComboBox = QtGui.QComboBox(self.centralwidget)
        self.readabilityComboBox.setGeometry(QtCore.QRect(210, 300, 291, 31))
        self.readabilityComboBox.setObjectName(_fromUtf8("readabilityComboBox"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 170, 281, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(310, 170, 321, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(290, 170, 21, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 30, 631, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 636, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFLAMINGO = QtGui.QMenu(self.menubar)
        self.menuFLAMINGO.setObjectName(_fromUtf8("menuFLAMINGO"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFLAMINGO.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Open Existing File:</span></p></body></html>", None))
        self.browsePushButton.setText(_translate("MainWindow", "Browse", None))
        self.openPushButton.setText(_translate("MainWindow", "Open", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Create a new file:</span></p></body></html>", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Name</span></p></body></html>", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Theme</span></p></body></html>", None))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Target Readability</span></p></body></html>", None))
        self.createPushButton.setText(_translate("MainWindow", "Create", None))
        self.cancelPushButton.setText(_translate("MainWindow", "Cancel", None))
        self.label_6.setText(_translate("MainWindow", "OR", None))
        self.menuFLAMINGO.setTitle(_translate("MainWindow", "FLAMINGO", None))

