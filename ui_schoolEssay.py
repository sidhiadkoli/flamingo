# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'School_essay.ui'
#
# Created: Fri Mar 21 12:12:39 2014
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
        Dialog.resize(652, 588)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(290, 540, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.line_4 = QtGui.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(0, 420, 651, 20))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 111, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.introTextEdit = QtGui.QTextEdit(Dialog)
        self.introTextEdit.setGeometry(QtCore.QRect(170, 100, 461, 131))
        self.introTextEdit.setTabChangesFocus(True)
        self.introTextEdit.setAcceptRichText(False)
        self.introTextEdit.setObjectName(_fromUtf8("introTextEdit"))
        self.point1TextEdit = QtGui.QTextEdit(Dialog)
        self.point1TextEdit.setGeometry(QtCore.QRect(170, 270, 461, 51))
        self.point1TextEdit.setTabChangesFocus(True)
        self.point1TextEdit.setAcceptRichText(False)
        self.point1TextEdit.setObjectName(_fromUtf8("point1TextEdit"))
        self.point2TextEdit = QtGui.QTextEdit(Dialog)
        self.point2TextEdit.setGeometry(QtCore.QRect(170, 360, 461, 51))
        self.point2TextEdit.setTabChangesFocus(True)
        self.point2TextEdit.setAcceptRichText(False)
        self.point2TextEdit.setObjectName(_fromUtf8("point2TextEdit"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 270, 141, 51))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(0, 240, 651, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.point3TextEdit = QtGui.QTextEdit(Dialog)
        self.point3TextEdit.setGeometry(QtCore.QRect(170, 450, 461, 51))
        self.point3TextEdit.setTabChangesFocus(True)
        self.point3TextEdit.setAcceptRichText(False)
        self.point3TextEdit.setObjectName(_fromUtf8("point3TextEdit"))
        self.line_5 = QtGui.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(0, 510, 651, 20))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 360, 131, 51))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.line_3 = QtGui.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(0, 330, 651, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 450, 131, 51))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.line_6 = QtGui.QFrame(Dialog)
        self.line_6.setGeometry(QtCore.QRect(0, 70, 651, 20))
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.titleTextEdit = QtGui.QTextEdit(Dialog)
        self.titleTextEdit.setGeometry(QtCore.QRect(170, 20, 461, 41))
        self.titleTextEdit.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.titleTextEdit.setTabChangesFocus(True)
        self.titleTextEdit.setAcceptRichText(False)
        self.titleTextEdit.setObjectName(_fromUtf8("titleTextEdit"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "School Essay", None))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p>Introduction</p></body></html>", None))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p>Point Considered for </p><p>Paragraph 1</p></body></html>", None))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p>Point Considered for </p><p>Paragraph 2</p></body></html>", None))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p>Point Considered for </p><p>Paragraph 3</p></body></html>", None))
        self.label.setText(_translate("Dialog", "Essay title", None))

