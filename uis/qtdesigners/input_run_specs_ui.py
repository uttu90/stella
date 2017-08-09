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
        Dialog.resize(573, 276)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(200, 210, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label_129 = QtGui.QLabel(Dialog)
        self.label_129.setGeometry(QtCore.QRect(20, 120, 46, 13))
        self.label_129.setObjectName(_fromUtf8("label_129"))
        self.inputSimulationFile = QtGui.QLineEdit(Dialog)
        self.inputSimulationFile.setGeometry(QtCore.QRect(200, 110, 251, 20))
        self.inputSimulationFile.setObjectName(_fromUtf8("inputSimulationFile"))
        self.selectSimulationFile = QtGui.QPushButton(Dialog)
        self.selectSimulationFile.setGeometry(QtCore.QRect(470, 110, 75, 23))
        self.selectSimulationFile.setObjectName(_fromUtf8("selectSimulationFile"))
        self.label_131 = QtGui.QLabel(Dialog)
        self.label_131.setGeometry(QtCore.QRect(260, 80, 161, 16))
        self.label_131.setObjectName(_fromUtf8("label_131"))
        self.runfrom = QtGui.QLineEdit(Dialog)
        self.runfrom.setGeometry(QtCore.QRect(120, 40, 51, 20))
        self.runfrom.setObjectName(_fromUtf8("runfrom"))
        self.label_130 = QtGui.QLabel(Dialog)
        self.label_130.setGeometry(QtCore.QRect(260, 20, 131, 16))
        self.label_130.setObjectName(_fromUtf8("label_130"))
        self.selectDataFile = QtGui.QPushButton(Dialog)
        self.selectDataFile.setGeometry(QtCore.QRect(470, 50, 75, 23))
        self.selectDataFile.setObjectName(_fromUtf8("selectDataFile"))
        self.rundt = QtGui.QLineEdit(Dialog)
        self.rundt.setGeometry(QtCore.QRect(120, 120, 51, 20))
        self.rundt.setObjectName(_fromUtf8("rundt"))
        self.label_128 = QtGui.QLabel(Dialog)
        self.label_128.setGeometry(QtCore.QRect(20, 80, 46, 13))
        self.label_128.setObjectName(_fromUtf8("label_128"))
        self.label_127 = QtGui.QLabel(Dialog)
        self.label_127.setGeometry(QtCore.QRect(20, 40, 46, 13))
        self.label_127.setObjectName(_fromUtf8("label_127"))
        self.inputDataFile = QtGui.QLineEdit(Dialog)
        self.inputDataFile.setGeometry(QtCore.QRect(200, 50, 251, 20))
        self.inputDataFile.setObjectName(_fromUtf8("inputDataFile"))
        self.runto = QtGui.QLineEdit(Dialog)
        self.runto.setGeometry(QtCore.QRect(120, 80, 51, 20))
        self.runto.setObjectName(_fromUtf8("runto"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 160, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.outputUpdate = QtGui.QLineEdit(Dialog)
        self.outputUpdate.setGeometry(QtCore.QRect(120, 160, 51, 20))
        self.outputUpdate.setObjectName(_fromUtf8("outputUpdate"))
        self.label_132 = QtGui.QLabel(Dialog)
        self.label_132.setGeometry(QtCore.QRect(260, 140, 161, 16))
        self.label_132.setObjectName(_fromUtf8("label_132"))
        self.outputFolder = QtGui.QLineEdit(Dialog)
        self.outputFolder.setGeometry(QtCore.QRect(200, 160, 251, 20))
        self.outputFolder.setObjectName(_fromUtf8("outputFolder"))
        self.selectOuputFolder = QtGui.QPushButton(Dialog)
        self.selectOuputFolder.setGeometry(QtCore.QRect(470, 160, 75, 23))
        self.selectOuputFolder.setObjectName(_fromUtf8("selectOuputFolder"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Run Specs", None))
        self.label_129.setText(_translate("Dialog", "DT", None))
        self.selectSimulationFile.setText(_translate("Dialog", "Select", None))
        self.label_131.setText(_translate("Dialog", "Choose Python simulation file", None))
        self.runfrom.setText(_translate("Dialog", "0", None))
        self.label_130.setText(_translate("Dialog", "Choose excel data file", None))
        self.selectDataFile.setText(_translate("Dialog", "Select", None))
        self.rundt.setText(_translate("Dialog", "1", None))
        self.label_128.setText(_translate("Dialog", "To", None))
        self.label_127.setText(_translate("Dialog", "From", None))
        self.runto.setText(_translate("Dialog", "2", None))
        self.label.setText(_translate("Dialog", "Output update", None))
        self.outputUpdate.setText(_translate("Dialog", "100", None))
        self.label_132.setText(_translate("Dialog", "Choose output folder", None))
        self.selectOuputFolder.setText(_translate("Dialog", "Select", None))

