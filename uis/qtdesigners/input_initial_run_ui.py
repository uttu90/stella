# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input_initial_run.ui'
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
        Dialog.resize(538, 339)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(180, 290, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label_123 = QtGui.QLabel(Dialog)
        self.label_123.setGeometry(QtCore.QRect(20, 220, 91, 16))
        self.label_123.setObjectName(_fromUtf8("label_123"))
        self.I_CaDOYStart = QtGui.QLineEdit(Dialog)
        self.I_CaDOYStart.setGeometry(QtCore.QRect(460, 90, 61, 20))
        self.I_CaDOYStart.setObjectName(_fromUtf8("I_CaDOYStart"))
        self.I_StartMYear_1 = QtGui.QLineEdit(Dialog)
        self.I_StartMYear_1.setGeometry(QtCore.QRect(130, 60, 61, 20))
        self.I_StartMYear_1.setObjectName(_fromUtf8("I_StartMYear_1"))
        self.label_118 = QtGui.QLabel(Dialog)
        self.label_118.setGeometry(QtCore.QRect(20, 120, 91, 16))
        self.label_118.setObjectName(_fromUtf8("label_118"))
        self.O_MPeriodLength_3 = QtGui.QLineEdit(Dialog)
        self.O_MPeriodLength_3.setGeometry(QtCore.QRect(460, 220, 61, 20))
        self.O_MPeriodLength_3.setObjectName(_fromUtf8("O_MPeriodLength_3"))
        self.I_WarmUpTime = QtGui.QLineEdit(Dialog)
        self.I_WarmUpTime.setGeometry(QtCore.QRect(460, 120, 61, 20))
        self.I_WarmUpTime.setObjectName(_fromUtf8("I_WarmUpTime"))
        self.label_125 = QtGui.QLabel(Dialog)
        self.label_125.setGeometry(QtCore.QRect(320, 220, 111, 16))
        self.label_125.setObjectName(_fromUtf8("label_125"))
        self.label_116 = QtGui.QLabel(Dialog)
        self.label_116.setGeometry(QtCore.QRect(320, 90, 91, 16))
        self.label_116.setObjectName(_fromUtf8("label_116"))
        self.I_RainYearStart = QtGui.QLineEdit(Dialog)
        self.I_RainYearStart.setGeometry(QtCore.QRect(460, 60, 61, 20))
        self.I_RainYearStart.setObjectName(_fromUtf8("I_RainYearStart"))
        self.I_StartMYear_3 = QtGui.QLineEdit(Dialog)
        self.I_StartMYear_3.setGeometry(QtCore.QRect(130, 120, 61, 20))
        self.I_StartMYear_3.setObjectName(_fromUtf8("I_StartMYear_3"))
        self.I_StartDOY_1 = QtGui.QLineEdit(Dialog)
        self.I_StartDOY_1.setGeometry(QtCore.QRect(130, 160, 61, 20))
        self.I_StartDOY_1.setObjectName(_fromUtf8("I_StartDOY_1"))
        self.label_126 = QtGui.QLabel(Dialog)
        self.label_126.setGeometry(QtCore.QRect(320, 190, 111, 16))
        self.label_126.setObjectName(_fromUtf8("label_126"))
        self.O_MPeriodLength_2 = QtGui.QLineEdit(Dialog)
        self.O_MPeriodLength_2.setGeometry(QtCore.QRect(460, 190, 61, 20))
        self.O_MPeriodLength_2.setObjectName(_fromUtf8("O_MPeriodLength_2"))
        self.label_117 = QtGui.QLabel(Dialog)
        self.label_117.setGeometry(QtCore.QRect(320, 120, 91, 16))
        self.label_117.setObjectName(_fromUtf8("label_117"))
        self.label_115 = QtGui.QLabel(Dialog)
        self.label_115.setGeometry(QtCore.QRect(320, 60, 91, 16))
        self.label_115.setObjectName(_fromUtf8("label_115"))
        self.label_119 = QtGui.QLabel(Dialog)
        self.label_119.setGeometry(QtCore.QRect(20, 60, 91, 16))
        self.label_119.setObjectName(_fromUtf8("label_119"))
        self.label_124 = QtGui.QLabel(Dialog)
        self.label_124.setGeometry(QtCore.QRect(320, 160, 101, 16))
        self.label_124.setObjectName(_fromUtf8("label_124"))
        self.O_MPeriodLength_1 = QtGui.QLineEdit(Dialog)
        self.O_MPeriodLength_1.setGeometry(QtCore.QRect(460, 160, 61, 20))
        self.O_MPeriodLength_1.setObjectName(_fromUtf8("O_MPeriodLength_1"))
        self.label_121 = QtGui.QLabel(Dialog)
        self.label_121.setGeometry(QtCore.QRect(20, 160, 91, 16))
        self.label_121.setObjectName(_fromUtf8("label_121"))
        self.label_120 = QtGui.QLabel(Dialog)
        self.label_120.setGeometry(QtCore.QRect(20, 90, 91, 16))
        self.label_120.setObjectName(_fromUtf8("label_120"))
        self.label_122 = QtGui.QLabel(Dialog)
        self.label_122.setGeometry(QtCore.QRect(20, 190, 91, 16))
        self.label_122.setObjectName(_fromUtf8("label_122"))
        self.I_StartMYear_2 = QtGui.QLineEdit(Dialog)
        self.I_StartMYear_2.setGeometry(QtCore.QRect(130, 90, 61, 20))
        self.I_StartMYear_2.setObjectName(_fromUtf8("I_StartMYear_2"))
        self.I_StartDOY_3 = QtGui.QLineEdit(Dialog)
        self.I_StartDOY_3.setGeometry(QtCore.QRect(130, 220, 61, 20))
        self.I_StartDOY_3.setObjectName(_fromUtf8("I_StartDOY_3"))
        self.I_StartDOY_2 = QtGui.QLineEdit(Dialog)
        self.I_StartDOY_2.setGeometry(QtCore.QRect(130, 190, 61, 20))
        self.I_StartDOY_2.setObjectName(_fromUtf8("I_StartDOY_2"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Input initial run", None))
        self.label_123.setText(_translate("Dialog", "I_StartDOY[3]", None))
        self.I_CaDOYStart.setText(_translate("Dialog", "0", None))
        self.I_StartMYear_1.setText(_translate("Dialog", "1", None))
        self.label_118.setText(_translate("Dialog", "I_StartMYear[3]", None))
        self.O_MPeriodLength_3.setText(_translate("Dialog", "365", None))
        self.I_WarmUpTime.setText(_translate("Dialog", "100", None))
        self.label_125.setText(_translate("Dialog", "O_MPeriodLength[3]", None))
        self.label_116.setText(_translate("Dialog", "I_CaDOYStart", None))
        self.I_RainYearStart.setText(_translate("Dialog", "0", None))
        self.I_StartMYear_3.setText(_translate("Dialog", "8", None))
        self.I_StartDOY_1.setText(_translate("Dialog", "1", None))
        self.label_126.setText(_translate("Dialog", "O_MPeriodLength[2]", None))
        self.O_MPeriodLength_2.setText(_translate("Dialog", "365", None))
        self.label_117.setText(_translate("Dialog", "I_WarmUpTime", None))
        self.label_115.setText(_translate("Dialog", "I_RainYearStart", None))
        self.label_119.setText(_translate("Dialog", "I_StartMYear[1]", None))
        self.label_124.setText(_translate("Dialog", "O_MPeriodLength[1]", None))
        self.O_MPeriodLength_1.setText(_translate("Dialog", "365", None))
        self.label_121.setText(_translate("Dialog", "I_StartDOY[1]", None))
        self.label_120.setText(_translate("Dialog", "I_StartMYear[2]", None))
        self.label_122.setText(_translate("Dialog", "I_StartDOY[2]", None))
        self.I_StartMYear_2.setText(_translate("Dialog", "5", None))
        self.I_StartDOY_3.setText(_translate("Dialog", "1", None))
        self.I_StartDOY_2.setText(_translate("Dialog", "1", None))

