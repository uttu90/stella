import PyQt4.QtGui as QtGui
from PyQt4 import QtCore
from os import path as file_path
from qtdesigners import input_lake_hepp_ui
import stella_input


class Input_Lake_HEPP_Diaglog(
    QtGui.QDialog,
    input_lake_hepp_ui.Ui_Dialog,
    stella_input.StellaInput):
    def __init__(self, parent=None):
        super(Input_Lake_HEPP_Diaglog, self).__init__(parent)
        self.setupUi(self)
        self.file = 'input_lake_hepp.json'
        if file_path.isfile(self.file):
            self._initiate_value()
        else:
            self._collect_value()

    def accept(self):
        self.pre_accept()
        self.emit(QtCore.SIGNAL('update'), self.data)
        super(Input_Lake_HEPP_Diaglog, self).accept()

    def reject(self):
        self.re_assign()
        super(Input_Lake_HEPP_Diaglog, self).accept()

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    form = Input_Lake_HEPP_Diaglog()
    form.show()
    if form.show():
        print form.input_lake
    form.run()
    app.exec_()

