import PyQt4.QtGui as QtGui
from os import path as file_path
from qtdesigners import input_lake_ui
import stella_input

class Input_Lake_Diaglog(
    QtGui.QDialog,
    input_lake_ui.Ui_Dialog,
    stella_input.StellaInput):

    def __init__(self, parent=None):
        super(Input_Lake_Diaglog, self).__init__(parent)
        self.setupUi(self)
        self.file = 'input_lake.json'
        if file_path.isfile(self.file):
            self._initiate_value()
        else:
            self._collect_value()

    def accept(self):
        self._collect_value()
        self.data_cb()
        self.save()
        super(Input_Lake_Diaglog, self).accept()

    def reject(self):
        self.re_assign()
        super(Input_Lake_Diaglog, self).accept()


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    form = Input_Lake_Diaglog()
    form.show()
    if form.show():
        print form.input_lake
    form.run()
    app.exec_()

