# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input_grass_and_cattle.ui'
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
        Dialog.resize(509, 365)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(150, 320, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label_79 = QtGui.QLabel(Dialog)
        self.label_79.setGeometry(QtCore.QRect(30, 140, 91, 16))
        self.label_79.setObjectName(_fromUtf8("label_79"))
        self.G_WUE = QtGui.QLineEdit(Dialog)
        self.G_WUE.setGeometry(QtCore.QRect(170, 260, 61, 20))
        self.G_WUE.setObjectName(_fromUtf8("G_WUE"))
        self.lb = QtGui.QLabel(Dialog)
        self.lb.setGeometry(QtCore.QRect(30, 260, 46, 13))
        self.lb.setObjectName(_fromUtf8("lb"))
        self.C_GrassLitConvlb = QtGui.QLabel(Dialog)
        self.C_GrassLitConvlb.setGeometry(QtCore.QRect(30, 200, 101, 16))
        self.C_GrassLitConvlb.setObjectName(_fromUtf8("C_GrassLitConvlb"))
        self.C_DailyTramFac = QtGui.QLineEdit(Dialog)
        self.C_DailyTramFac.setGeometry(QtCore.QRect(170, 20, 61, 20))
        self.C_DailyTramFac.setObjectName(_fromUtf8("C_DailyTramFac"))
        self.label_77 = QtGui.QLabel(Dialog)
        self.label_77.setGeometry(QtCore.QRect(30, 80, 71, 16))
        self.label_77.setObjectName(_fromUtf8("label_77"))
        self.C_GrassLitConv = QtGui.QLineEdit(Dialog)
        self.C_GrassLitConv.setGeometry(QtCore.QRect(170, 200, 61, 20))
        self.C_GrassLitConv.setObjectName(_fromUtf8("C_GrassLitConv"))
        self.C_DailyIntake = QtGui.QLineEdit(Dialog)
        self.C_DailyIntake.setGeometry(QtCore.QRect(170, 80, 61, 20))
        self.C_DailyIntake.setObjectName(_fromUtf8("C_DailyIntake"))
        self.label_74 = QtGui.QLabel(Dialog)
        self.label_74.setGeometry(QtCore.QRect(30, 20, 91, 16))
        self.label_74.setObjectName(_fromUtf8("label_74"))
        self.C_SurfManureDecFrac = QtGui.QLineEdit(Dialog)
        self.C_SurfManureDecFrac.setGeometry(QtCore.QRect(170, 170, 61, 20))
        self.C_SurfManureDecFrac.setObjectName(_fromUtf8("C_SurfManureDecFrac"))
        self.G_TramplingMultiplier = QtGui.QLineEdit(Dialog)
        self.G_TramplingMultiplier.setGeometry(QtCore.QRect(430, 20, 61, 20))
        self.G_TramplingMultiplier.setObjectName(_fromUtf8("G_TramplingMultiplier"))
        self.C_CattleSale = QtGui.QLineEdit(Dialog)
        self.C_CattleSale.setGeometry(QtCore.QRect(170, 50, 61, 20))
        self.C_CattleSale.setObjectName(_fromUtf8("C_CattleSale"))
        self.label_75 = QtGui.QLabel(Dialog)
        self.label_75.setGeometry(QtCore.QRect(30, 50, 81, 16))
        self.label_75.setObjectName(_fromUtf8("label_75"))
        self.C_SurfLitDecFrac = QtGui.QLineEdit(Dialog)
        self.C_SurfLitDecFrac.setGeometry(QtCore.QRect(170, 140, 61, 20))
        self.C_SurfLitDecFrac.setObjectName(_fromUtf8("C_SurfLitDecFrac"))
        self.label_76 = QtGui.QLabel(Dialog)
        self.label_76.setGeometry(QtCore.QRect(30, 110, 101, 16))
        self.label_76.setObjectName(_fromUtf8("label_76"))
        self.C_GrassLitMortFrac = QtGui.QLineEdit(Dialog)
        self.C_GrassLitMortFrac.setGeometry(QtCore.QRect(170, 230, 61, 20))
        self.C_GrassLitMortFrac.setObjectName(_fromUtf8("C_GrassLitMortFrac"))
        self.C_GrassLitMortFraclb = QtGui.QLabel(Dialog)
        self.C_GrassLitMortFraclb.setGeometry(QtCore.QRect(30, 230, 121, 16))
        self.C_GrassLitMortFraclb.setObjectName(_fromUtf8("C_GrassLitMortFraclb"))
        self.label_83 = QtGui.QLabel(Dialog)
        self.label_83.setGeometry(QtCore.QRect(290, 20, 111, 16))
        self.label_83.setObjectName(_fromUtf8("label_83"))
        self.C_GrazingManConv = QtGui.QLineEdit(Dialog)
        self.C_GrazingManConv.setGeometry(QtCore.QRect(170, 110, 61, 20))
        self.C_GrazingManConv.setObjectName(_fromUtf8("C_GrazingManConv"))
        self.C_SurfManureDecFraclb = QtGui.QLabel(Dialog)
        self.C_SurfManureDecFraclb.setGeometry(QtCore.QRect(30, 170, 121, 16))
        self.C_SurfManureDecFraclb.setObjectName(_fromUtf8("C_SurfManureDecFraclb"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Input Grass and Cattle", None))
        self.label_79.setText(_translate("Dialog", "C_SurfLitDecFrac", None))
        self.G_WUE.setText(_translate("Dialog", "0.04", None))
        self.lb.setText(_translate("Dialog", "G_WUE", None))
        self.C_GrassLitConvlb.setText(_translate("Dialog", "C_GrassLitConv", None))
        self.C_DailyTramFac.setText(_translate("Dialog", "1", None))
        self.label_77.setText(_translate("Dialog", "C_DailyIntake", None))
        self.C_GrassLitConv.setText(_translate("Dialog", "1", None))
        self.C_DailyIntake.setText(_translate("Dialog", "1", None))
        self.label_74.setText(_translate("Dialog", "C_DailyTrampFac", None))
        self.C_SurfManureDecFrac.setText(_translate("Dialog", "0.01", None))
        self.G_TramplingMultiplier.setText(_translate("Dialog", "0", None))
        self.C_CattleSale.setText(_translate("Dialog", "0", None))
        self.label_75.setText(_translate("Dialog", "C_CattleSale", None))
        self.C_SurfLitDecFrac.setText(_translate("Dialog", "0.03", None))
        self.label_76.setText(_translate("Dialog", "C_GrazingManConv", None))
        self.C_GrassLitMortFrac.setText(_translate("Dialog", "0.03", None))
        self.C_GrassLitMortFraclb.setText(_translate("Dialog", "C_GrassLitMortFrac", None))
        self.label_83.setText(_translate("Dialog", "G_TramplingMultiplier", None))
        self.C_GrazingManConv.setText(_translate("Dialog", "0.1", None))
        self.C_SurfManureDecFraclb.setText(_translate("Dialog", "C_SurfManureDecFrac", None))

