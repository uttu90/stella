# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'landcover_info.ui'
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

class Ui_landcover_dlg(object):
    def setupUi(self, landcover_dlg):
        landcover_dlg.setObjectName(_fromUtf8("landcover_dlg"))
        landcover_dlg.resize(752, 372)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/background/GenRiver logo.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        landcover_dlg.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(landcover_dlg)
        self.buttonBox.setGeometry(QtCore.QRect(670, 10, 75, 52))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.lcName_13 = QtGui.QLineEdit(landcover_dlg)
        self.lcName_13.setGeometry(QtCore.QRect(520, 110, 113, 20))
        self.lcName_13.setObjectName(_fromUtf8("lcName_13"))
        self.lcName_7 = QtGui.QLineEdit(landcover_dlg)
        self.lcName_7.setGeometry(QtCore.QRect(200, 230, 113, 20))
        self.lcName_7.setObjectName(_fromUtf8("lcName_7"))
        self.lcName_8 = QtGui.QLineEdit(landcover_dlg)
        self.lcName_8.setGeometry(QtCore.QRect(200, 260, 113, 20))
        self.lcName_8.setObjectName(_fromUtf8("lcName_8"))
        self.lcName_12 = QtGui.QLineEdit(landcover_dlg)
        self.lcName_12.setGeometry(QtCore.QRect(520, 80, 113, 20))
        self.lcName_12.setObjectName(_fromUtf8("lcName_12"))
        self.lcColor_9 = QtGui.QPushButton(landcover_dlg)
        self.lcColor_9.setGeometry(QtCore.QRect(80, 260, 75, 23))
        self.lcColor_9.setText(_fromUtf8(""))
        self.lcColor_9.setObjectName(_fromUtf8("lcColor_9"))
        self.lcName_19 = QtGui.QLineEdit(landcover_dlg)
        self.lcName_19.setGeometry(QtCore.QRect(520, 290, 113, 20))
        self.lcName_19.setObjectName(_fromUtf8("lcName_19"))
        self.lcColor_16 = QtGui.QPushButton(landcover_dlg)
        self.lcColor_16.setGeometry(QtCore.QRect(400, 200, 75, 23))
        self.lcColor_16.setText(_fromUtf8(""))
        self.lcColor_16.setObjectName(_fromUtf8("lcColor_16"))
        self.label_16 = QtGui.QLabel(landcover_dlg)
        self.label_16.setGeometry(QtCore.QRect(340, 320, 46, 13))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.lcName_16 = QtGui.QLineEdit(landcover_dlg)
        self.lcName_16.setGeometry(QtCore.QRect(520, 200, 113, 20))
        self.lcName_16.setObjectName(_fromUtf8("lcName_16"))
        self.lcName_20 = QtGui.QLineEdit(landcover_dlg)
        self.lcName_20.setGeometry(QtCore.QRect(520, 320, 113, 20))
        self.lcName_20.setObjectName(_fromUtf8("lcName_20"))
        self.label_2 = QtGui.QLabel(landcover_dlg)
        self.label_2.setGeometry(QtCore.QRect(100, 20, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lcName_2 = QtGui.QLineEdit(landcover_dlg)
        self.lcName_2.setGeometry(QtCore.QRect(200, 80, 113, 20))
        self.lcName_2.setObjectName(_fromUtf8("lcName_2"))
        self.label_21 = QtGui.QLabel(landcover_dlg)
        self.label_21.setGeometry(QtCore.QRect(340, 170, 46, 13))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.lcColor_10 = QtGui.QPushButton(landcover_dlg)
        self.lcColor_10.setGeometry(QtCore.QRect(80, 320, 75, 23))
        self.lcColor_10.setText(_fromUtf8(""))
        self.lcColor_10.setObjectName(_fromUtf8("lcColor_10"))
        self.lcName_17 = QtGui.QLineEdit(landcover_dlg)
        self.lcName_17.setGeometry(QtCore.QRect(520, 230, 113, 20))
        self.lcName_17.setObjectName(_fromUtf8("lcName_17"))
        self.lcColor_6 = QtGui.QPushButton(landcover_dlg)
        self.lcColor_6.setGeometry(QtCore.QRect(80, 170, 75, 23))
        self.lcColor_6.setText(_fromUtf8(""))
        self.lcColor_6.setObjectName(_fromUtf8("lcColor_6"))
        self.lcName_10 = QtGui.QLineEdit(landcover_dlg)
        self.lcName_10.setGeometry(QtCore.QRect(200, 320, 113, 20))
        self.lcName_10.setObjectName(_fromUtf8("lcName_10"))
        self.label_10 = QtGui.QLabel(landcover_dlg)
        self.label_10.setGeometry(QtCore.QRect(20, 290, 46, 13))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.lcName_9 = QtGui.QLineEdit(landcover_dlg)
        self.lcName_9.setGeometry(QtCore.QRect(200, 290, 113, 20))
        self.lcName_9.setObjectName(_fromUtf8("lcName_9"))
        self.lcName_3 = QtGui.QLineEdit(landcover_dlg)
        self.lcName_3.setGeometry(QtCore.QRect(200, 110, 113, 20))
        self.lcName_3.setObjectName(_fromUtf8("lcName_3"))
        self.label_25 = QtGui.QLabel(landcover_dlg)
        self.label_25.setGeometry(QtCore.QRect(420, 20, 46, 13))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.label_7 = QtGui.QLabel(landcover_dlg)
        self.label_7.setGeometry(QtCore.QRect(20, 200, 46, 13))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lcName_1 = QtGui.QLineEdit(landcover_dlg)
        self.lcName_1.setGeometry(QtCore.QRect(200, 50, 113, 20))
        self.lcName_1.setObjectName(_fromUtf8("lcName_1"))
        self.label_24 = QtGui.QLabel(landcover_dlg)
        self.label_24.setGeometry(QtCore.QRect(340, 20, 46, 13))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.lcColor_14 = QtGui.QPushButton(landcover_dlg)
        self.lcColor_14.setGeometry(QtCore.QRect(400, 140, 75, 23))
        self.lcColor_14.setText(_fromUtf8(""))
        self.lcColor_14.setObjectName(_fromUtf8("lcColor_14"))
        self.label_18 = QtGui.QLabel(landcover_dlg)
        self.label_18.setGeometry(QtCore.QRect(340, 290, 46, 13))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(landcover_dlg)
        self.label_19.setGeometry(QtCore.QRect(340, 80, 46, 13))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.lcColor_13 = QtGui.QPushButton(landcover_dlg)
        self.lcColor_13.setGeometry(QtCore.QRect(400, 110, 75, 23))
        self.lcColor_13.setText(_fromUtf8(""))
        self.lcColor_13.setObjectName(_fromUtf8("lcColor_13"))
        self.label_22 = QtGui.QLabel(landcover_dlg)
        self.label_22.setGeometry(QtCore.QRect(340, 140, 46, 13))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_14 = QtGui.QLabel(landcover_dlg)
        self.label_14.setGeometry(QtCore.QRect(20, 320, 46, 13))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_20 = QtGui.QLabel(landcover_dlg)
        self.label_20.setGeometry(QtCore.QRect(340, 110, 46, 13))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.lcColor_12 = QtGui.QPushButton(landcover_dlg)
        self.lcColor_12.setGeometry(QtCore.QRect(400, 80, 75, 23))
        self.lcColor_12.setText(_fromUtf8(""))
        self.lcColor_12.setObjectName(_fromUtf8("lcColor_12"))
        self.lcName_4 = QtGui.QLineEdit(landcover_dlg)
        self.lcName_4.setGeometry(QtCore.QRect(200, 140, 113, 20))
        self.lcName_4.setObjectName(_fromUtf8("lcName_4"))
        self.label_4 = QtGui.QLabel(landcover_dlg)
        self.label_4.setGeometry(QtCore.QRect(20, 50, 46, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(landcover_dlg)
        self.label_5.setGeometry(QtCore.QRect(20, 80, 46, 13))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lcColor_15 = QtGui.QPushButton(landcover_dlg)
        self.lcColor_15.setGeometry(QtCore.QRect(400, 170, 75, 23))
        self.lcColor_15.setText(_fromUtf8(""))
        self.lcColor_15.setObjectName(_fromUtf8("lcColor_15"))
        self.label_26 = QtGui.QLabel(landcover_dlg)
        self.label_26.setGeometry(QtCore.QRect(540, 20, 46, 13))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.label_23 = QtGui.QLabel(landcover_dlg)
        self.label_23.setGeometry(QtCore.QRect(340, 50, 46, 13))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.label_3 = QtGui.QLabel(landcover_dlg)
        self.label_3.setGeometry(QtCore.QRect(220, 20, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_17 = QtGui.QLabel(landcover_dlg)
        self.label_17.setGeometry(QtCore.QRect(340, 260, 46, 13))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.lcColor_20 = QtGui.QPushButton(landcover_dlg)
        self.lcColor_20.setGeometry(QtCore.QRect(400, 320, 75, 23))
        self.lcColor_20.setText(_fromUtf8(""))
        self.lcColor_20.setObjectName(_fromUtf8("lcColor_20"))
        self.lcName_11 = QtGui.QLineEdit(landcover_dlg)
        self.lcName_11.setGeometry(QtCore.QRect(520, 50, 113, 20))
        self.lcName_11.setObjectName(_fromUtf8("lcName_11"))
        self.lcName_15 = QtGui.QLineEdit(landcover_dlg)
        self.lcName_15.setGeometry(QtCore.QRect(520, 170, 113, 20))
        self.lcName_15.setObjectName(_fromUtf8("lcName_15"))
        self.lcName_5 = QtGui.QLineEdit(landcover_dlg)
        self.lcName_5.setGeometry(QtCore.QRect(200, 170, 113, 20))
        self.lcName_5.setObjectName(_fromUtf8("lcName_5"))
        self.lcColor_8 = QtGui.QPushButton(landcover_dlg)
        self.lcColor_8.setGeometry(QtCore.QRect(80, 290, 75, 23))
        self.lcColor_8.setText(_fromUtf8(""))
        self.lcColor_8.setObjectName(_fromUtf8("lcColor_8"))
        self.label_12 = QtGui.QLabel(landcover_dlg)
        self.label_12.setGeometry(QtCore.QRect(20, 260, 46, 13))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_11 = QtGui.QLabel(landcover_dlg)
        self.label_11.setGeometry(QtCore.QRect(20, 230, 46, 13))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.lcColor_18 = QtGui.QPushButton(landcover_dlg)
        self.lcColor_18.setGeometry(QtCore.QRect(400, 260, 75, 23))
        self.lcColor_18.setText(_fromUtf8(""))
        self.lcColor_18.setObjectName(_fromUtf8("lcColor_18"))
        self.lcColor_11 = QtGui.QPushButton(landcover_dlg)
        self.lcColor_11.setGeometry(QtCore.QRect(400, 50, 75, 23))
        self.lcColor_11.setText(_fromUtf8(""))
        self.lcColor_11.setObjectName(_fromUtf8("lcColor_11"))
        self.label_8 = QtGui.QLabel(landcover_dlg)
        self.label_8.setGeometry(QtCore.QRect(20, 140, 46, 13))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lcColor_3 = QtGui.QPushButton(landcover_dlg)
        self.lcColor_3.setGeometry(QtCore.QRect(80, 110, 75, 23))
        self.lcColor_3.setText(_fromUtf8(""))
        self.lcColor_3.setObjectName(_fromUtf8("lcColor_3"))
        self.label_9 = QtGui.QLabel(landcover_dlg)
        self.label_9.setGeometry(QtCore.QRect(20, 170, 46, 13))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_13 = QtGui.QLabel(landcover_dlg)
        self.label_13.setGeometry(QtCore.QRect(340, 230, 46, 13))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.lcColor_1 = QtGui.QPushButton(landcover_dlg)
        self.lcColor_1.setGeometry(QtCore.QRect(80, 50, 75, 23))
        self.lcColor_1.setText(_fromUtf8(""))
        self.lcColor_1.setObjectName(_fromUtf8("lcColor_1"))
        self.lcName_14 = QtGui.QLineEdit(landcover_dlg)
        self.lcName_14.setGeometry(QtCore.QRect(520, 140, 113, 20))
        self.lcName_14.setObjectName(_fromUtf8("lcName_14"))
        self.lcColor_2 = QtGui.QPushButton(landcover_dlg)
        self.lcColor_2.setGeometry(QtCore.QRect(80, 80, 75, 23))
        self.lcColor_2.setText(_fromUtf8(""))
        self.lcColor_2.setObjectName(_fromUtf8("lcColor_2"))
        self.lcColor_7 = QtGui.QPushButton(landcover_dlg)
        self.lcColor_7.setGeometry(QtCore.QRect(80, 230, 75, 23))
        self.lcColor_7.setText(_fromUtf8(""))
        self.lcColor_7.setObjectName(_fromUtf8("lcColor_7"))
        self.lcColor_4 = QtGui.QPushButton(landcover_dlg)
        self.lcColor_4.setGeometry(QtCore.QRect(80, 140, 75, 23))
        self.lcColor_4.setText(_fromUtf8(""))
        self.lcColor_4.setObjectName(_fromUtf8("lcColor_4"))
        self.label_15 = QtGui.QLabel(landcover_dlg)
        self.label_15.setGeometry(QtCore.QRect(340, 200, 46, 13))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label = QtGui.QLabel(landcover_dlg)
        self.label.setGeometry(QtCore.QRect(20, 20, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_6 = QtGui.QLabel(landcover_dlg)
        self.label_6.setGeometry(QtCore.QRect(20, 110, 46, 13))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lcColor_17 = QtGui.QPushButton(landcover_dlg)
        self.lcColor_17.setGeometry(QtCore.QRect(400, 230, 75, 23))
        self.lcColor_17.setText(_fromUtf8(""))
        self.lcColor_17.setObjectName(_fromUtf8("lcColor_17"))
        self.lcName_6 = QtGui.QLineEdit(landcover_dlg)
        self.lcName_6.setGeometry(QtCore.QRect(200, 200, 113, 20))
        self.lcName_6.setObjectName(_fromUtf8("lcName_6"))
        self.lcName_18 = QtGui.QLineEdit(landcover_dlg)
        self.lcName_18.setGeometry(QtCore.QRect(520, 260, 113, 20))
        self.lcName_18.setObjectName(_fromUtf8("lcName_18"))
        self.lcColor_5 = QtGui.QPushButton(landcover_dlg)
        self.lcColor_5.setGeometry(QtCore.QRect(80, 200, 75, 23))
        self.lcColor_5.setText(_fromUtf8(""))
        self.lcColor_5.setObjectName(_fromUtf8("lcColor_5"))
        self.lcColor_19 = QtGui.QPushButton(landcover_dlg)
        self.lcColor_19.setGeometry(QtCore.QRect(400, 290, 75, 23))
        self.lcColor_19.setText(_fromUtf8(""))
        self.lcColor_19.setObjectName(_fromUtf8("lcColor_19"))

        self.retranslateUi(landcover_dlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), landcover_dlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), landcover_dlg.reject)
        QtCore.QMetaObject.connectSlotsByName(landcover_dlg)

    def retranslateUi(self, landcover_dlg):
        landcover_dlg.setWindowTitle(_translate("landcover_dlg", "Landcover", None))
        self.label_16.setText(_translate("landcover_dlg", "20", None))
        self.label_2.setText(_translate("landcover_dlg", "Color", None))
        self.label_21.setText(_translate("landcover_dlg", "15", None))
        self.label_10.setText(_translate("landcover_dlg", "9", None))
        self.label_25.setText(_translate("landcover_dlg", "Color", None))
        self.label_7.setText(_translate("landcover_dlg", "6", None))
        self.label_24.setText(_translate("landcover_dlg", "ID", None))
        self.label_18.setText(_translate("landcover_dlg", "19", None))
        self.label_19.setText(_translate("landcover_dlg", "12", None))
        self.label_22.setText(_translate("landcover_dlg", "14", None))
        self.label_14.setText(_translate("landcover_dlg", "10", None))
        self.label_20.setText(_translate("landcover_dlg", "13", None))
        self.label_4.setText(_translate("landcover_dlg", "1", None))
        self.label_5.setText(_translate("landcover_dlg", "2", None))
        self.label_26.setText(_translate("landcover_dlg", "Name", None))
        self.label_23.setText(_translate("landcover_dlg", "11", None))
        self.label_3.setText(_translate("landcover_dlg", "Name", None))
        self.label_17.setText(_translate("landcover_dlg", "18", None))
        self.label_12.setText(_translate("landcover_dlg", "8", None))
        self.label_11.setText(_translate("landcover_dlg", "7", None))
        self.label_8.setText(_translate("landcover_dlg", "4", None))
        self.label_9.setText(_translate("landcover_dlg", "5", None))
        self.label_13.setText(_translate("landcover_dlg", "17", None))
        self.label_15.setText(_translate("landcover_dlg", "16", None))
        self.label.setText(_translate("landcover_dlg", "ID", None))
        self.label_6.setText(_translate("landcover_dlg", "3", None))

import images_rc
