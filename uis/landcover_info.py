import os
from PyQt4 import QtGui, QtCore
from functools import partial
import json

from qtdesigners import landcover_info_ui


class LandcoverInfo(QtGui.QDialog, landcover_info_ui.Ui_landcover_dlg):
    def __init__(self, parent=None, landcover=True):
        super(LandcoverInfo, self).__init__(parent)
        self.setupUi(self)
        if landcover:
            self.file = 'landcover_info.json'
            self.setWindowTitle('Landcover')
        else:
            self.file = 'subcatchment_info.json'
            self.setWindowTitle('Subcatchment')
        self.data = {}
        self.colorResult = [None for _ in range(1, 21)]
        if os.path.isfile(self.file):
            self._initiate_value()
        else:
            self._collect_value()
        for widget in self.children():
            if isinstance(widget, QtGui.QPushButton):
                widget.clicked.connect(partial(self.set_color_button, widget))
                # cl = widget.palette().color(QtGui.QPalette.Background)
                # print cl.red(), cl.green(), cl.blue()

    def set_color_button(self, button):
        color = QtGui.QColorDialog.getColor()
        button.setStyleSheet("QWidget { background-color: %s}" % color.name())

    def _initiate_value(self):
        with open(self.file, 'r') as fp:
            self.data = json.load(fp)
        self._assign_value()
        self._assign_result()

    def _assign_result(self):
        for i in range(1, 21):
            btn_name = "lcColor_%s" % i
            color = self.data[btn_name][28: 35] if self.data[btn_name] else "#ffffff"
            self.colorResult[i-1] = color

    def _collect_value(self):
        for widget in self.children():
            if isinstance(widget, QtGui.QLineEdit):
                self.data[str(widget.objectName())] = str(widget.text())
            if isinstance(widget, QtGui.QPushButton):
                self.data[str(widget.objectName())] = str(widget.styleSheet())
        self._assign_result()

    def save(self):
        with open(self.file, 'w') as fp:
            json.dump(self.data, fp, indent=3)

    def _assign_value(self):
        for key, value in self.data.items():
            widget = getattr(self, key)
            if isinstance(widget, QtGui.QLineEdit):
                widget.setText(value)
            if isinstance(widget, QtGui.QPushButton):
                widget.setStyleSheet(value)

    def re_assign(self):
        self._assign_value()

    def accept(self):
        self._collect_value()
        self.save()
        self._assign_result()
        super(LandcoverInfo, self).accept()

    def reject(self):
        self.re_assign()
        self._assign_result()
        super(LandcoverInfo, self).reject()

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    form = LandcoverInfo()
    form.exec_()
    form.close()
    app.exec_()
