import PyQt4.QtGui as QtGui
import input_initial_run_ui
import os.path as file_path
import stella_input

class Input_Initial_Run_Diaglog(
    QtGui.QDialog,
    input_initial_run_ui.Ui_Dialog,
    stella_input.StellaInput):

    def __init__(self, parent=None):
        super(Input_Initial_Run_Diaglog, self).__init__(parent)
        self.setupUi(self)
        self.file = 'input_initial_run.json'
        if file_path.isfile(self.file):
            self._initiate_value()
        else:
            self._collect_value()

    def accept(self):
        self._collect_value()
        self.save()
        super(Input_Initial_Run_Diaglog, self).accept()

    def reject(self):
        self.re_assign()
        super(Input_Initial_Run_Diaglog, self).accept()


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    form = Input_Initial_Run_Diaglog()
    form.show()
    if form.show():
        print form.input_initial_run
    form.run()
    app.exec_()

