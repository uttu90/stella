from PyQt4 import QtGui
from qtdesigners import copyright_ui

class Copyright(QtGui.QDialog, copyright_ui.Ui_genRiver):
    def __init__(self, parent=None):
        super(Copyright, self).__init__(parent)
        self.setupUi(self)
        self.data=None
