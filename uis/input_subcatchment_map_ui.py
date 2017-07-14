# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\input_subcatchment_map.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        Dialog.resize(468, 177)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(100, 130, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 40, 121, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.subcatchmentMap = QtGui.QLineEdit(Dialog)
        self.subcatchmentMap.setGeometry(QtCore.QRect(50, 70, 311, 20))
        self.subcatchmentMap.setObjectName(_fromUtf8("subcatchmentMap"))
        self.subcatchmentMap_btn = QtGui.QPushButton(Dialog)
        self.subcatchmentMap_btn.setGeometry(QtCore.QRect(380, 70, 75, 23))
        self.subcatchmentMap_btn.setObjectName(_fromUtf8("subcatchmentMap_btn"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Input Subcatchment map", None))
        self.label.setText(_translate("Dialog", "Subcatchment Map", None))
        self.subcatchmentMap_btn.setText(_translate("Dialog", "Choose File", None))

