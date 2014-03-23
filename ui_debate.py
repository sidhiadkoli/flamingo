# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Debate.ui'
#
# Created: Sun Mar 23 15:10:30 2014
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(644, 460)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(290, 410, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 240, 121, 41))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.introTextEdit = QtGui.QTextEdit(Dialog)
        self.introTextEdit.setGeometry(QtCore.QRect(170, 20, 461, 81))
        self.introTextEdit.setObjectName(_fromUtf8("introTextEdit"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 320, 131, 41))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.line_4 = QtGui.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(0, 290, 651, 20))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 141, 41))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.line_3 = QtGui.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(0, 200, 651, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 111, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.arg3TextEdit = QtGui.QTextEdit(Dialog)
        self.arg3TextEdit.setGeometry(QtCore.QRect(170, 320, 461, 51))
        self.arg3TextEdit.setObjectName(_fromUtf8("arg3TextEdit"))
        self.arg2TextEdit = QtGui.QTextEdit(Dialog)
        self.arg2TextEdit.setGeometry(QtCore.QRect(170, 230, 461, 51))
        self.arg2TextEdit.setObjectName(_fromUtf8("arg2TextEdit"))
        self.line_5 = QtGui.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(0, 380, 651, 20))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(0, 110, 651, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.arg1TextEdit = QtGui.QTextEdit(Dialog)
        self.arg1TextEdit.setGeometry(QtCore.QRect(170, 140, 461, 51))
        self.arg1TextEdit.setObjectName(_fromUtf8("arg1TextEdit"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_4.setText(_translate("Dialog", "Argument 2", None))
        self.label_5.setText(_translate("Dialog", "Argument 3", None))
        self.label_3.setText(_translate("Dialog", "Argument 1", None))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p>Introduction</p></body></html>", None))

