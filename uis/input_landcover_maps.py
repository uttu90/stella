import PyQt4.QtGui as QtGui
from PyQt4 import QtCore
from qtdesigners import input_lancover_maps_ui
from os import path as file_path
import stella_input
from functools import partial
import excel_utils as utils
import xlrd


class Input_Landcover_Maps_Diaglog(
    QtGui.QDialog, input_lancover_maps_ui.Ui_Dialog, stella_input.StellaInput):
    def __init__(self, parent=None):
        super(Input_Landcover_Maps_Diaglog, self).__init__(parent)
        self.setupUi(self)
        self.inputData = dict()
        self.file = 'input_landcover_maps.json'
        for btnIndex, btn in enumerate([
            self.landCoverMap_btn1,
            self.landCoverMap_btn2,
            self.landCoverMap_btn3,
            self.landCoverMap_btn4
        ]):
            btn.clicked.connect(partial(self.get_landcover_map, btnIndex))

        if file_path.isfile(self.file):
            self._initiate_value()
        else:
            self._collect_value()

    def get_landcover_map(self, index):
        landcover_file = str(QtGui.QFileDialog.getOpenFileName(
            self,
            'Get landcover file',
            'c:\\', "Map files (*.tif)"
        ))
        landcover_edit = 'landcoverMap_{}'.format(index + 1)
        getattr(self, landcover_edit).setText(landcover_file)
        self.save()

    def accept(self):
        self.pre_accept()
        self.emit(QtCore.SIGNAL('update'), self.data)
        super(Input_Landcover_Maps_Diaglog, self).accept()

    def reject(self):
        self.re_assign()
        super(Input_Landcover_Maps_Diaglog, self).accept()


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    form = Input_Landcover_Maps_Diaglog()
    form.show()
    app.exec_()

