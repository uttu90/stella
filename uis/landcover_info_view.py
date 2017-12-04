import os
from PyQt4 import QtGui, QtCore
from functools import partial
import json

import landcover_info_view_ui


class LandcoverInfo(QtGui.QDialog, landcover_info_view_ui.Ui_landcover_dlg):
    def __init__(self, parent=None):
        super(LandcoverInfo, self).__init__(parent)
        self.setupUi(self)
        self.file = 'landcover_info.json'
        self.data = {}
        self.colorResult = [None for _ in range(1, 21)]
        if os.path.isfile(self.file):
            self._initiate_value()
        else:
            self._collect_value()

    def _initiate_value(self):
        with open(self.file, 'r') as fp:
            self.data = json.load(fp)
        self._assign_value()
        self._assign_result()

    def _collect_value(self):
        for widget in self.children():
            if isinstance(widget, QtGui.QLineEdit):
                self.data[str(widget.objectName())] = str(widget.text())
            if isinstance(widget, QtGui.QPushButton):
                self.data[str(widget.objectName())] = str(widget.styleSheet())
        self._assign_result()

    def _assign_value(self):
        for key, value in self.data.items():
            widget = getattr(self, key)
            if isinstance(widget, QtGui.QLineEdit):
                widget.setText(value)
            if isinstance(widget, QtGui.QPushButton):
                widget.setStyleSheet(value)

    def _assign_result(self):
        for i in range(1, 21):
            btn_name = "lcColor_%s" % i
            color = self.data[btn_name][28: 35] if self.data[btn_name] else "#ffffff"
            self.colorResult[i-1] = color
