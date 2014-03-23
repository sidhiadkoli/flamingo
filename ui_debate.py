# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Debate.ui'
#
# Created: Tue Mar 18 15:02:23 2014
#      by: PyQt4 UI code generator 4.10.4
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
        Dialog.resize(649, 587)
        self.arg1TextEdit = QtGui.QTextEdit(Dialog)
        self.arg1TextEdit.setGeometry(QtCore.QRect(170, 220, 461, 51))
        self.arg1TextEdit.setObjectName(_fromUtf8("arg1TextEdit"))
        self.introTextEdit = QtGui.QTextEdit(Dialog)
        self.introTextEdit.setGeometry(QtCore.QRect(170, 90, 461, 81))
        self.introTextEdit.setObjectName(_fromUtf8("introTextEdit"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 400, 131, 41))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 70, 651, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 320, 121, 41))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 111, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(270, 20, 111, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.arg1TextEdit_2 = QtGui.QTextEdit(Dialog)
        self.arg1TextEdit_2.setGeometry(QtCore.QRect(170, 400, 461, 51))
        self.arg1TextEdit_2.setObjectName(_fromUtf8("arg1TextEdit_2"))
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(0, 180, 651, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.proceedPushButton = QtGui.QPushButton(Dialog)
        self.proceedPushButton.setGeometry(QtCore.QRect(450, 520, 141, 31))
        self.proceedPushButton.setObjectName(_fromUtf8("proceedPushButton"))
        self.line_5 = QtGui.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(0, 460, 651, 20))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.line_4 = QtGui.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(0, 370, 651, 20))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 220, 141, 41))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.arg2TextEdit = QtGui.QTextEdit(Dialog)
        self.arg2TextEdit.setGeometry(QtCore.QRect(170, 310, 461, 51))
        self.arg2TextEdit.setObjectName(_fromUtf8("arg2TextEdit"))
        self.line_3 = QtGui.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(0, 280, 651, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.arg1TextEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p>Arguement 3</p></body></html>", None))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p>Arguement 2</p></body></html>", None))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p>Introduction</p></body></html>", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Debate</span></p></body></html>", None))
        self.proceedPushButton.setText(_translate("Dialog", "Proceed", None))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p>Arguement 1</p></body></html>", None))

