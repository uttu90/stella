# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input_run_specs.ui'
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
        Dialog.resize(573, 371)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(210, 320, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.selectSubcatchmentMap = QtGui.QPushButton(Dialog)
        self.selectSubcatchmentMap.setGeometry(QtCore.QRect(470, 200, 75, 23))
        self.selectSubcatchmentMap.setObjectName(_fromUtf8("selectSubcatchmentMap"))
        self.label_129 = QtGui.QLabel(Dialog)
        self.label_129.setGeometry(QtCore.QRect(20, 120, 46, 13))
        self.label_129.setObjectName(_fromUtf8("label_129"))
        self.inputSimulationFile = QtGui.QLineEdit(Dialog)
        self.inputSimulationFile.setGeometry(QtCore.QRect(200, 120, 251, 20))
        self.inputSimulationFile.setObjectName(_fromUtf8("inputSimulationFile"))
        self.selectSimulationFile = QtGui.QPushButton(Dialog)
        self.selectSimulationFile.setGeometry(QtCore.QRect(470, 120, 75, 23))
        self.selectSimulationFile.setObjectName(_fromUtf8("selectSimulationFile"))
        self.label_131 = QtGui.QLabel(Dialog)
        self.label_131.setGeometry(QtCore.QRect(260, 90, 161, 16))
        self.label_131.setObjectName(_fromUtf8("label_131"))
        self.runfrom = QtGui.QLineEdit(Dialog)
        self.runfrom.setGeometry(QtCore.QRect(120, 40, 51, 20))
        self.runfrom.setObjectName(_fromUtf8("runfrom"))
        self.label_130 = QtGui.QLabel(Dialog)
        self.label_130.setGeometry(QtCore.QRect(260, 10, 131, 16))
        self.label_130.setObjectName(_fromUtf8("label_130"))
        self.selectDataFile = QtGui.QPushButton(Dialog)
        self.selectDataFile.setGeometry(QtCore.QRect(470, 40, 75, 23))
        self.selectDataFile.setObjectName(_fromUtf8("selectDataFile"))
        self.label_166 = QtGui.QLabel(Dialog)
        self.label_166.setGeometry(QtCore.QRect(260, 170, 161, 16))
        self.label_166.setObjectName(_fromUtf8("label_166"))
        self.rundt = QtGui.QLineEdit(Dialog)
        self.rundt.setGeometry(QtCore.QRect(120, 120, 51, 20))
        self.rundt.setObjectName(_fromUtf8("rundt"))
        self.label_128 = QtGui.QLabel(Dialog)
        self.label_128.setGeometry(QtCore.QRect(20, 80, 46, 13))
        self.label_128.setObjectName(_fromUtf8("label_128"))
        self.selectLandcoverMap = QtGui.QPushButton(Dialog)
        self.selectLandcoverMap.setGeometry(QtCore.QRect(470, 270, 75, 23))
        self.selectLandcoverMap.setObjectName(_fromUtf8("selectLandcoverMap"))
        self.inputSubcatchmentMap = QtGui.QLineEdit(Dialog)
        self.inputSubcatchmentMap.setGeometry(QtCore.QRect(200, 200, 251, 20))
        self.inputSubcatchmentMap.setObjectName(_fromUtf8("inputSubcatchmentMap"))
        self.label_167 = QtGui.QLabel(Dialog)
        self.label_167.setGeometry(QtCore.QRect(260, 240, 161, 16))
        self.label_167.setObjectName(_fromUtf8("label_167"))
        self.label_127 = QtGui.QLabel(Dialog)
        self.label_127.setGeometry(QtCore.QRect(20, 40, 46, 13))
        self.label_127.setObjectName(_fromUtf8("label_127"))
        self.inputDataFile = QtGui.QLineEdit(Dialog)
        self.inputDataFile.setGeometry(QtCore.QRect(200, 40, 251, 20))
        self.inputDataFile.setObjectName(_fromUtf8("inputDataFile"))
        self.runto = QtGui.QLineEdit(Dialog)
        self.runto.setGeometry(QtCore.QRect(120, 80, 51, 20))
        self.runto.setObjectName(_fromUtf8("runto"))
        self.inputLandcoverMap = QtGui.QLineEdit(Dialog)
        self.inputLandcoverMap.setGeometry(QtCore.QRect(200, 270, 251, 20))
        self.inputLandcoverMap.setObjectName(_fromUtf8("inputLandcoverMap"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 160, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.outputUpdate = QtGui.QLineEdit(Dialog)
        self.outputUpdate.setGeometry(QtCore.QRect(120, 160, 51, 20))
        self.outputUpdate.setObjectName(_fromUtf8("outputUpdate"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Run Specs", None))
        self.selectSubcatchmentMap.setText(_translate("Dialog", "Select", None))
        self.label_129.setText(_translate("Dialog", "DT", None))
        self.selectSimulationFile.setText(_translate("Dialog", "Select", None))
        self.label_131.setText(_translate("Dialog", "Choose Python simulation file", None))
        self.runfrom.setText(_translate("Dialog", "0", None))
        self.label_130.setText(_translate("Dialog", "Choose excel data file", None))
        self.selectDataFile.setText(_translate("Dialog", "Select", None))
        self.label_166.setText(_translate("Dialog", "Choose subcatchment map", None))
        self.rundt.setText(_translate("Dialog", "1", None))
        self.label_128.setText(_translate("Dialog", "To", None))
        self.selectLandcoverMap.setText(_translate("Dialog", "Select", None))
        self.label_167.setText(_translate("Dialog", "Choose landcover map", None))
        self.label_127.setText(_translate("Dialog", "From", None))
        self.runto.setText(_translate("Dialog", "2", None))
        self.label.setText(_translate("Dialog", "Output update", None))
        self.outputUpdate.setText(_translate("Dialog", "100", None))

