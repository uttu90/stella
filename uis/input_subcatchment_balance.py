import PyQt4.QtGui as QtGui
from os import path as file_path
import input_subcatchment_balance_ui
import stella_input


class Input_Subcatchment_Balance_Diaglog(
    QtGui.QDialog,
    input_subcatchment_balance_ui.Ui_Dialog,
    stella_input.StellaInput):
    def __init__(self, parent=None):
        super(Input_Subcatchment_Balance_Diaglog, self).__init__(parent)
        self.setupUi(self)
        self.file = 'input_subcatchment_balance.json'
        if file_path.isfile(self.file):
            self._initiate_value()
        else:
            self._collect_value()

    def accept(self):
        self._collect_value()
        self.data_cb()
        self.save()
        super(Input_Subcatchment_Balance_Diaglog, self).accept()

    def reject(self):
        self.re_assign()
        super(Input_Subcatchment_Balance_Diaglog, self).accept()


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    form = Input_Subcatchment_Balance_Diaglog()
    form.show()
    if form.show():
        print form.data
    x = form.run()
    app.exec_()

