# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input_rainfall.ui'
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
        Dialog.resize(399, 300)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.I_RainMultiplier = QtGui.QLineEdit(Dialog)
        self.I_RainMultiplier.setGeometry(QtCore.QRect(200, 60, 113, 20))
        self.I_RainMultiplier.setObjectName(_fromUtf8("I_RainMultiplier"))
        self.I_Rain_IntensMeanlabel = QtGui.QLabel(Dialog)
        self.I_Rain_IntensMeanlabel.setGeometry(QtCore.QRect(80, 120, 101, 16))
        self.I_Rain_IntensMeanlabel.setObjectName(_fromUtf8("I_Rain_IntensMeanlabel"))
        self.I_RainMultiplierlabel = QtGui.QLabel(Dialog)
        self.I_RainMultiplierlabel.setGeometry(QtCore.QRect(80, 60, 91, 16))
        self.I_RainMultiplierlabel.setObjectName(_fromUtf8("I_RainMultiplierlabel"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(80, 180, 91, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 30, 91, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.I_Rain_GenSeed = QtGui.QLineEdit(Dialog)
        self.I_Rain_GenSeed.setGeometry(QtCore.QRect(200, 180, 113, 20))
        self.I_Rain_GenSeed.setObjectName(_fromUtf8("I_Rain_GenSeed"))
        self.I_Rain_IntensCoefVar = QtGui.QLineEdit(Dialog)
        self.I_Rain_IntensCoefVar.setGeometry(QtCore.QRect(200, 150, 113, 20))
        self.I_Rain_IntensCoefVar.setObjectName(_fromUtf8("I_Rain_IntensCoefVar"))
        self.isI_UseSpatVarRain = QtGui.QLineEdit(Dialog)
        self.isI_UseSpatVarRain.setGeometry(QtCore.QRect(200, 30, 113, 20))
        self.isI_UseSpatVarRain.setObjectName(_fromUtf8("isI_UseSpatVarRain"))
        self.isI_RainCyclelabel = QtGui.QLabel(Dialog)
        self.isI_RainCyclelabel.setGeometry(QtCore.QRect(80, 90, 91, 16))
        self.isI_RainCyclelabel.setObjectName(_fromUtf8("isI_RainCyclelabel"))
        self.isI_RainCycle = QtGui.QLineEdit(Dialog)
        self.isI_RainCycle.setGeometry(QtCore.QRect(200, 90, 113, 20))
        self.isI_RainCycle.setObjectName(_fromUtf8("isI_RainCycle"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 150, 111, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.I_Rain_IntensMean = QtGui.QLineEdit(Dialog)
        self.I_Rain_IntensMean.setGeometry(QtCore.QRect(200, 120, 113, 20))
        self.I_Rain_IntensMean.setObjectName(_fromUtf8("I_Rain_IntensMean"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Input RainFall Parameters", None))
        self.I_RainMultiplier.setText(_translate("Dialog", "1", None))
        self.I_Rain_IntensMeanlabel.setText(_translate("Dialog", "I_Rain_IntensMean", None))
        self.I_RainMultiplierlabel.setText(_translate("Dialog", "I_RainMultiplier", None))
        self.label_5.setText(_translate("Dialog", "I_Rain_GenSeed", None))
        self.label.setText(_translate("Dialog", "I_UseSpatVarRain?", None))
        self.I_Rain_GenSeed.setText(_translate("Dialog", "200", None))
        self.I_Rain_IntensCoefVar.setText(_translate("Dialog", "0.3", None))
        self.isI_UseSpatVarRain.setText(_translate("Dialog", "0", None))
        self.isI_RainCyclelabel.setText(_translate("Dialog", "I_RainCycle?", None))
        self.isI_RainCycle.setText(_translate("Dialog", "0", None))
        self.label_4.setText(_translate("Dialog", "I_Rain_IntensCoefVar", None))
        self.I_Rain_IntensMean.setText(_translate("Dialog", "10", None))

