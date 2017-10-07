from PyQt4 import QtGui
import constants
import json


class StellaInput(object):
    def _collect_value(self):
        self.data = dict()
        for widget in self.children():
            if isinstance(widget, QtGui.QLineEdit):
                self.data[
                    str(widget.objectName())
                ] = str(widget.text())

    def _initiate_value(self):
        with open(self.file, 'r') as fp:
            self.data = json.load(fp)
        self._assign_value()

    def _assign_value(self):
        for key, value in self.data.items():
            if not isinstance(value, list):
                getattr(self, key).setText(str(self.data[key]))
            else:
                for sub in range(20):
                    getattr(self, key + '_' + constants.subcatchmentName[sub]
                            ).setText(str(self.data[key][sub]))

    def get_params(self, dict):
        dict = self.data

    def save(self):
        with open(self.file, 'w') as fp:
            json.dump(self.data, fp, indent=3)

    def re_assign(self):
        self._assign_value()

    def run(self):
        with open(self.file, 'w') as fp:
            json.dump(self.data, fp, indent=3)