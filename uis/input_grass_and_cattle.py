import PyQt4.QtGui as QtGui
import os.path as file_path
import input_grass_and_cattle_ui
import stella_input


class Input_Grass_And_Cattle_Diaglog(
    QtGui.QDialog,
    input_grass_and_cattle_ui.Ui_Dialog,
    stella_input.StellaInput):

    def __init__(self, parent=None):
        super(Input_Grass_And_Cattle_Diaglog, self).__init__(parent)
        self.setupUi(self)
        self.file = 'input_grass_and_cattle.json'
        if file_path.isfile(self.file):
            self._initiate_value()
        else:
            self._collect_value()

    def accept(self):
        self._collect_value()
        self.save()
        super(Input_Grass_And_Cattle_Diaglog, self).accept()

    def reject(self):
        self.re_assign()
        super(Input_Grass_And_Cattle_Diaglog, self).accept()

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    form = Input_Grass_And_Cattle_Diaglog()
    form.show()
    if form.show():
        print form.input_grass_and_cattle
    form.run()
    app.exec_()

