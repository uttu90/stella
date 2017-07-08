# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'output_timeseries.ui'
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
        Dialog.resize(822, 574)
        self.resultBox_2 = QtGui.QComboBox(Dialog)
        self.resultBox_2.setGeometry(QtCore.QRect(-30, 370, 201, 20))
        self.resultBox_2.setObjectName(_fromUtf8("resultBox_2"))
        self.label_168 = QtGui.QLabel(Dialog)
        self.label_168.setGeometry(QtCore.QRect(-30, 180, 93, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_168.sizePolicy().hasHeightForWidth())
        self.label_168.setSizePolicy(sizePolicy)
        self.label_168.setMaximumSize(QtCore.QSize(200, 100))
        self.label_168.setObjectName(_fromUtf8("label_168"))
        self.resultBox_4 = QtGui.QComboBox(Dialog)
        self.resultBox_4.setGeometry(QtCore.QRect(-30, 620, 201, 20))
        self.resultBox_4.setObjectName(_fromUtf8("resultBox_4"))
        self.yearProgress = QtGui.QLCDNumber(Dialog)
        self.yearProgress.setGeometry(QtCore.QRect(110, 210, 64, 23))
        self.yearProgress.setMaximumSize(QtCore.QSize(100, 50))
        self.yearProgress.setObjectName(_fromUtf8("yearProgress"))
        self.label_170 = QtGui.QLabel(Dialog)
        self.label_170.setGeometry(QtCore.QRect(80, 210, 21, 16))
        self.label_170.setMaximumSize(QtCore.QSize(200, 50))
        self.label_170.setObjectName(_fromUtf8("label_170"))
        self.dayProgress = QtGui.QLCDNumber(Dialog)
        self.dayProgress.setGeometry(QtCore.QRect(0, 210, 64, 23))
        self.dayProgress.setMaximumSize(QtCore.QSize(100, 50))
        self.dayProgress.setObjectName(_fromUtf8("dayProgress"))
        self.resultBox_3 = QtGui.QComboBox(Dialog)
        self.resultBox_3.setGeometry(QtCore.QRect(-30, 490, 201, 20))
        self.resultBox_3.setObjectName(_fromUtf8("resultBox_3"))
        self.displayResult = QtGui.QWidget(Dialog)
        self.displayResult.setGeometry(QtCore.QRect(190, 180, 581, 556))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.displayResult.sizePolicy().hasHeightForWidth())
        self.displayResult.setSizePolicy(sizePolicy)
        self.displayResult.setObjectName(_fromUtf8("displayResult"))
        self.resultBox = QtGui.QComboBox(Dialog)
        self.resultBox.setGeometry(QtCore.QRect(-29, 251, 201, 20))
        self.resultBox.setObjectName(_fromUtf8("resultBox"))
        self.label_169 = QtGui.QLabel(Dialog)
        self.label_169.setGeometry(QtCore.QRect(-30, 210, 19, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_169.sizePolicy().hasHeightForWidth())
        self.label_169.setSizePolicy(sizePolicy)
        self.label_169.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_169.setObjectName(_fromUtf8("label_169"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Output Timeseries", None))
        self.label_168.setText(_translate("Dialog", "Simulation progress", None))
        self.label_170.setText(_translate("Dialog", "Year", None))
        self.label_169.setText(_translate("Dialog", "Day", None))

