import PyQt4.QtGui as QtGui
from os import path as file_path
from qtdesigners import input_river_ui
import stella_input


class Input_River_Diaglog(
    QtGui.QDialog,
    input_river_ui.Ui_Dialog,
    stella_input.StellaInput):
    def __init__(self, parent=None):
        super(Input_River_Diaglog, self).__init__(parent)
        self.setupUi(self)
        self.file = 'input_river.json'
        if file_path.isfile(self.file):
            self._initiate_value()
        else:
            self._collect_value()

    def accept(self):
        self._collect_value()
        self.data_cb()
        self.save()
        super(Input_River_Diaglog, self).accept()

    def reject(self):
        self.re_assign()
        super(Input_River_Diaglog, self).accept()

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    form = Input_River_Diaglog()
    form.show()
    if form.show():
        print form.data
    form.run()
    app.exec_()

