# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormalLetter.ui'
#
# Created: Tue Apr 15 18:51:25 2014
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
        Dialog.resize(627, 528)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(270, 490, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.line_7 = QtGui.QFrame(Dialog)
        self.line_7.setGeometry(QtCore.QRect(-10, 430, 651, 16))
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.line_6 = QtGui.QFrame(Dialog)
        self.line_6.setGeometry(QtCore.QRect(-10, 390, 651, 16))
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.dateLineEdit = QtGui.QLineEdit(Dialog)
        self.dateLineEdit.setGeometry(QtCore.QRect(270, 250, 331, 21))
        self.dateLineEdit.setText(_fromUtf8(""))
        self.dateLineEdit.setObjectName(_fromUtf8("dateLineEdit"))
        self.subjectLineEdit = QtGui.QLineEdit(Dialog)
        self.subjectLineEdit.setGeometry(QtCore.QRect(270, 290, 331, 21))
        self.subjectLineEdit.setObjectName(_fromUtf8("subjectLineEdit"))
        self.salutationLineEdit = QtGui.QLineEdit(Dialog)
        self.salutationLineEdit.setGeometry(QtCore.QRect(270, 330, 331, 21))
        self.salutationLineEdit.setObjectName(_fromUtf8("salutationLineEdit"))
        self.contentLineEdit = QtGui.QLineEdit(Dialog)
        self.contentLineEdit.setGeometry(QtCore.QRect(270, 370, 331, 21))
        self.contentLineEdit.setReadOnly(True)
        self.contentLineEdit.setObjectName(_fromUtf8("contentLineEdit"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 131, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(-10, 100, 651, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(20, 370, 111, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.regardsLineEdit = QtGui.QLineEdit(Dialog)
        self.regardsLineEdit.setGeometry(QtCore.QRect(270, 410, 331, 21))
        self.regardsLineEdit.setObjectName(_fromUtf8("regardsLineEdit"))
        self.sendNameLineEdit = QtGui.QLineEdit(Dialog)
        self.sendNameLineEdit.setGeometry(QtCore.QRect(270, 450, 331, 21))
        self.sendNameLineEdit.setObjectName(_fromUtf8("sendNameLineEdit"))
        self.line_5 = QtGui.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(-10, 350, 651, 16))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.sendAddr1LineEdit = QtGui.QLineEdit(Dialog)
        self.sendAddr1LineEdit.setGeometry(QtCore.QRect(270, 20, 331, 21))
        self.sendAddr1LineEdit.setObjectName(_fromUtf8("sendAddr1LineEdit"))
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(-10, 230, 651, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.sendAddr2LineEdit = QtGui.QLineEdit(Dialog)
        self.sendAddr2LineEdit.setGeometry(QtCore.QRect(270, 50, 331, 21))
        self.sendAddr2LineEdit.setText(_fromUtf8(""))
        self.sendAddr2LineEdit.setObjectName(_fromUtf8("sendAddr2LineEdit"))
        self.line_3 = QtGui.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(-10, 270, 651, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.sendAddr3LineEdit = QtGui.QLineEdit(Dialog)
        self.sendAddr3LineEdit.setGeometry(QtCore.QRect(270, 80, 331, 21))
        self.sendAddr3LineEdit.setObjectName(_fromUtf8("sendAddr3LineEdit"))
        self.line_4 = QtGui.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(-10, 310, 651, 16))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.line_8 = QtGui.QFrame(Dialog)
        self.line_8.setGeometry(QtCore.QRect(-20, 470, 651, 16))
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 290, 111, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.recvNameLineEdit = QtGui.QLineEdit(Dialog)
        self.recvNameLineEdit.setGeometry(QtCore.QRect(270, 120, 331, 21))
        self.recvNameLineEdit.setObjectName(_fromUtf8("recvNameLineEdit"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 250, 111, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.recvAddr1LineEdit = QtGui.QLineEdit(Dialog)
        self.recvAddr1LineEdit.setGeometry(QtCore.QRect(270, 150, 331, 21))
        self.recvAddr1LineEdit.setObjectName(_fromUtf8("recvAddr1LineEdit"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 121, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.recvAddr2LineEdit = QtGui.QLineEdit(Dialog)
        self.recvAddr2LineEdit.setGeometry(QtCore.QRect(270, 180, 331, 21))
        self.recvAddr2LineEdit.setText(_fromUtf8(""))
        self.recvAddr2LineEdit.setReadOnly(False)
        self.recvAddr2LineEdit.setObjectName(_fromUtf8("recvAddr2LineEdit"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 330, 111, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.recvAddr3LineEdit = QtGui.QLineEdit(Dialog)
        self.recvAddr3LineEdit.setGeometry(QtCore.QRect(270, 210, 331, 21))
        self.recvAddr3LineEdit.setObjectName(_fromUtf8("recvAddr3LineEdit"))
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(20, 410, 111, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(20, 450, 111, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Formal Letter", None))
        self.contentLineEdit.setText(_translate("Dialog", "-- to be filled late --", None))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Receiver\'s Address</span></p></body></html>", None))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Content</span></p></body></html>", None))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Subject</span></p></body></html>", None))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Date</span></p></body></html>", None))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Sender\'s Address</span></p></body></html>", None))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Salutation</span></p></body></html>", None))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Regards</span></p></body></html>", None))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Sender\'s Name</span></p></body></html>", None))

