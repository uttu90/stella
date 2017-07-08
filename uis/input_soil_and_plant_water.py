import PyQt4.QtGui as QtGui
from os import path as file_path
import input_soil_and_plant_water_ui
import stella_input


class Input_Soil_And_Plant_Water_Diaglog(
    QtGui.QDialog,
    input_soil_and_plant_water_ui.Ui_Dialog,
    stella_input.StellaInput):
    def __init__(self, parent=None):
        super(Input_Soil_And_Plant_Water_Diaglog, self).__init__(parent)
        self.setupUi(self)
        self.file = 'input_soil_and_plant_water.json'
        if file_path.isfile(self.file):
            self._initiate_value()
        else:
            self._collect_value()

    def accept(self):
        self._collect_value()
        self.save()
        super(Input_Soil_And_Plant_Water_Diaglog, self).accept()

    def reject(self):
        self.re_assign()
        super(Input_Soil_And_Plant_Water_Diaglog, self).accept()

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    form = Input_Soil_And_Plant_Water_Diaglog()
    form.show()
    if form.show():
        print form.input_soil_and_plant_water
    form.run()
    app.exec_()

