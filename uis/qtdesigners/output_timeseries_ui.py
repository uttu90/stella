# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\output_timeseries.ui'
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
        Dialog.resize(825, 573)
        self.label_168 = QtGui.QLabel(Dialog)
        self.label_168.setGeometry(QtCore.QRect(10, 10, 93, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_168.sizePolicy().hasHeightForWidth())
        self.label_168.setSizePolicy(sizePolicy)
        self.label_168.setMaximumSize(QtCore.QSize(200, 100))
        self.label_168.setObjectName(_fromUtf8("label_168"))
        self.yearProgress = QtGui.QLCDNumber(Dialog)
        self.yearProgress.setGeometry(QtCore.QRect(150, 40, 64, 23))
        self.yearProgress.setMaximumSize(QtCore.QSize(100, 50))
        self.yearProgress.setObjectName(_fromUtf8("yearProgress"))
        self.label_169 = QtGui.QLabel(Dialog)
        self.label_169.setGeometry(QtCore.QRect(10, 40, 19, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_169.sizePolicy().hasHeightForWidth())
        self.label_169.setSizePolicy(sizePolicy)
        self.label_169.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_169.setObjectName(_fromUtf8("label_169"))
        self.displayResult = QtGui.QWidget(Dialog)
        self.displayResult.setGeometry(QtCore.QRect(230, 10, 581, 556))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.displayResult.sizePolicy().hasHeightForWidth())
        self.displayResult.setSizePolicy(sizePolicy)
        self.displayResult.setObjectName(_fromUtf8("displayResult"))
        self.label_170 = QtGui.QLabel(Dialog)
        self.label_170.setGeometry(QtCore.QRect(120, 40, 21, 16))
        self.label_170.setMaximumSize(QtCore.QSize(200, 50))
        self.label_170.setObjectName(_fromUtf8("label_170"))
        self.dayProgress = QtGui.QLCDNumber(Dialog)
        self.dayProgress.setGeometry(QtCore.QRect(40, 40, 64, 23))
        self.dayProgress.setMaximumSize(QtCore.QSize(100, 50))
        self.dayProgress.setObjectName(_fromUtf8("dayProgress"))
        self.exportData = QtGui.QPushButton(Dialog)
        self.exportData.setGeometry(QtCore.QRect(134, 10, 81, 23))
        self.exportData.setObjectName(_fromUtf8("exportData"))
        self.checkBox = QtGui.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(10, 70, 70, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.backBtn = QtGui.QPushButton(Dialog)
        self.backBtn.setGeometry(QtCore.QRect(10, 100, 75, 23))
        self.backBtn.setObjectName(_fromUtf8("backBtn"))
        self.nextBtn = QtGui.QPushButton(Dialog)
        self.nextBtn.setGeometry(QtCore.QRect(140, 100, 75, 23))
        self.nextBtn.setObjectName(_fromUtf8("nextBtn"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(19, 150, 201, 101))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 30, 131, 17))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_3 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 60, 111, 17))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 280, 201, 141))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.checkBox_4 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 20, 131, 17))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.checkBox_5 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_5.setGeometry(QtCore.QRect(10, 50, 91, 17))
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.checkBox_6 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_6.setGeometry(QtCore.QRect(10, 80, 70, 17))
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.checkBox_7 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_7.setGeometry(QtCore.QRect(10, 110, 101, 17))
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Output Timeseries", None))
        self.label_168.setText(_translate("Dialog", "Simulation progress", None))
        self.label_169.setText(_translate("Dialog", "Day", None))
        self.label_170.setText(_translate("Dialog", "Year", None))
        self.exportData.setText(_translate("Dialog", "Export to Excel", None))
        self.checkBox.setText(_translate("Dialog", "Auto", None))
        self.backBtn.setText(_translate("Dialog", "< Back", None))
        self.nextBtn.setText(_translate("Dialog", "Next >", None))
        self.groupBox.setTitle(_translate("Dialog", "Water Balance", None))
        self.checkBox_2.setText(_translate("Dialog", "I_RFlowdata_mmday", None))
        self.checkBox_3.setText(_translate("Dialog", "L_InFlowtoLake", None))
        self.groupBox_2.setTitle(_translate("Dialog", "HEPP", None))
        self.checkBox_4.setText(_translate("Dialog", "L_HEPPWatUseFlow", None))
        self.checkBox_5.setText(_translate("Dialog", "L_HEPP_Kwh", None))
        self.checkBox_6.setText(_translate("Dialog", "L_LakeVol", None))
        self.checkBox_7.setText(_translate("Dialog", "L_LakeLevel", None))

