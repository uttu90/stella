# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'readme.ui'
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

class Ui_readme(object):
    def setupUi(self, readme):
        readme.setObjectName(_fromUtf8("readme"))
        readme.resize(964, 532)
        self.gridLayout = QtGui.QGridLayout(readme)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.webView = QtWebKit.QWebView(readme)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("qrc:/webview/readme.html")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.gridLayout.addWidget(self.webView, 0, 0, 1, 1)

        self.retranslateUi(readme)
        QtCore.QMetaObject.connectSlotsByName(readme)

    def retranslateUi(self, readme):
        readme.setWindowTitle(_translate("readme", "Readme", None))

from PyQt4 import QtWebKit
import readme_rc
