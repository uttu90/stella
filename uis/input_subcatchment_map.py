import PyQt4.QtGui as QtGui
import input_subcatchment_map_ui
from os import path as file_path
import stella_input
import excel_utils as utils
import xlrd


class Input_Subcatchment_Map_Diaglog(
    QtGui.QDialog, input_subcatchment_map_ui.Ui_Dialog, stella_input.StellaInput):
    def __init__(self, parent=None):
        super(Input_Subcatchment_Map_Diaglog, self).__init__(parent)
        self.setupUi(self)
        self.inputData = dict()
        self.file = 'input_subcatchment_map.json'
        self.subcatchmentMap_btn.clicked.connect(self.get_subcatchment_map)
        if file_path.isfile(self.file):
            self._initiate_value()
        else:
            self._collect_value()

    def get_subcatchment_map(self):
        subcatchment_file = str(QtGui.QFileDialog.getOpenFileName(
            self,
            'Get Subcatchment file',
            'c:\\', "Map files (*.tif)"
        ))
        self.subcatchmentMap.setText(subcatchment_file)
        self.save()

    def accept(self):
        self._collect_value()
        self.data_cb()
        self.save()
        super(Input_Subcatchment_Map_Diaglog, self).accept()

    def reject(self):
        self.re_assign()
        super(Input_Subcatchment_Map_Diaglog, self).accept()


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    form = Input_Subcatchment_Map_Diaglog()
    form.show()
    app.exec_()

