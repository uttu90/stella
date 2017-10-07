# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input_lancover_maps.ui'
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
        Dialog.resize(548, 360)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(190, 320, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 171, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 171, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 181, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 230, 181, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.landcoverMap_1 = QtGui.QLineEdit(Dialog)
        self.landcoverMap_1.setGeometry(QtCore.QRect(20, 50, 371, 20))
        self.landcoverMap_1.setObjectName(_fromUtf8("landcoverMap_1"))
        self.landcoverMap_2 = QtGui.QLineEdit(Dialog)
        self.landcoverMap_2.setGeometry(QtCore.QRect(20, 120, 371, 20))
        self.landcoverMap_2.setObjectName(_fromUtf8("landcoverMap_2"))
        self.landcoverMap_3 = QtGui.QLineEdit(Dialog)
        self.landcoverMap_3.setGeometry(QtCore.QRect(20, 190, 371, 20))
        self.landcoverMap_3.setObjectName(_fromUtf8("landcoverMap_3"))
        self.landcoverMap_4 = QtGui.QLineEdit(Dialog)
        self.landcoverMap_4.setGeometry(QtCore.QRect(20, 260, 371, 20))
        self.landcoverMap_4.setObjectName(_fromUtf8("landcoverMap_4"))
        self.landCoverMap_btn1 = QtGui.QPushButton(Dialog)
        self.landCoverMap_btn1.setGeometry(QtCore.QRect(440, 50, 75, 23))
        self.landCoverMap_btn1.setObjectName(_fromUtf8("landCoverMap_btn1"))
        self.landCoverMap_btn2 = QtGui.QPushButton(Dialog)
        self.landCoverMap_btn2.setGeometry(QtCore.QRect(440, 120, 75, 23))
        self.landCoverMap_btn2.setObjectName(_fromUtf8("landCoverMap_btn2"))
        self.landCoverMap_btn3 = QtGui.QPushButton(Dialog)
        self.landCoverMap_btn3.setGeometry(QtCore.QRect(440, 190, 75, 23))
        self.landCoverMap_btn3.setObjectName(_fromUtf8("landCoverMap_btn3"))
        self.landCoverMap_btn4 = QtGui.QPushButton(Dialog)
        self.landCoverMap_btn4.setGeometry(QtCore.QRect(440, 260, 75, 23))
        self.landCoverMap_btn4.setObjectName(_fromUtf8("landCoverMap_btn4"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Input Landcover maps", None))
        self.label.setText(_translate("Dialog", "Landcover map period 1", None))
        self.label_2.setText(_translate("Dialog", "Landcover map period 2", None))
        self.label_3.setText(_translate("Dialog", "Landcover map period 3", None))
        self.label_4.setText(_translate("Dialog", "Landcover map period 4", None))
        self.landCoverMap_btn1.setText(_translate("Dialog", "Choose File", None))
        self.landCoverMap_btn2.setText(_translate("Dialog", "Choose File", None))
        self.landCoverMap_btn3.setText(_translate("Dialog", "Choose File", None))
        self.landCoverMap_btn4.setText(_translate("Dialog", "Choose File", None))

