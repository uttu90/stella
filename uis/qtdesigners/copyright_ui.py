# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'copyright.ui'
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

class Ui_genRiver(object):
    def setupUi(self, genRiver):
        genRiver.setObjectName(_fromUtf8("genRiver"))
        genRiver.resize(766, 518)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/background/GenRiver logo.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        genRiver.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(genRiver)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.webView = QtWebKit.QWebView(genRiver)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("qrc:/webview/genriver.html")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.gridLayout.addWidget(self.webView, 0, 0, 1, 1)

        self.retranslateUi(genRiver)
        QtCore.QMetaObject.connectSlotsByName(genRiver)

    def retranslateUi(self, genRiver):
        genRiver.setWindowTitle(_translate("genRiver", "GenRiver version 2.0", None))

from PyQt4 import QtWebKit
import copyright_rc
import images_rc
