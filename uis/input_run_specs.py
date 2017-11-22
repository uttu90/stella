import PyQt4.QtGui as QtGui
import input_run_specs_ui
from os import path as file_path
import stella_input
import excel_utils as utils
import xlrd


class Input_Run_Specs_Diaglog(
    QtGui.QDialog, input_run_specs_ui.Ui_Dialog, stella_input.StellaInput):
    def __init__(self, parent=None):
        super(Input_Run_Specs_Diaglog, self).__init__(parent)
        self.setupUi(self)
        self.inputData = dict()
        self.file = 'input_run_specs.json'
        self.selectDataFile.clicked.connect(self.get_data_file)
        self.selectSimulationFile.clicked.connect(self.get_simulation_file)
        self.selectOuputFolder.clicked.connect(self.get_output_folder)
        if file_path.isfile(self.file):
            self._initiate_value()
        else:
            self._collect_value()

    def get_data_file(self):
        data_file = QtGui.QFileDialog.getOpenFileName(
            self,
            'Get data file',
            'c:\\',"Excel files (*.xls)"
        )
        self.inputDataFile.setText(data_file)
        self.data[str(self.inputDataFile.objectName())] = str(data_file)
        self.save()

    def get_simulation_file(self):
        simulation_file = str(QtGui.QFileDialog.getOpenFileName(
            self,
            'Get simulation file',
            'c:\\',"Python files (*.py)"
        ))
        self.inputSimulationFile.setText(simulation_file)
        self.data[str(self.inputSimulationFile.objectName())] = str(
            simulation_file
        )
        self.save()

    def get_output_folder(self):
        output_folder = str(QtGui.QFileDialog.getExistingDirectory(
            self,
            'Get output folder'
        ))
        self.outputFolder.setText(output_folder)
        self.data[str(self.outputFolder.objectName())] = output_folder
        self.save()

    def accept(self):
        self._collect_value()
        self.data_cb()
        self.save()
        super(Input_Run_Specs_Diaglog, self).accept()

    def get_input_data(self):
        xl_workbook = xlrd.open_workbook(self.data.get('inputDataFile'))
        # wksheet2 = xl_workbook.sheet_by_name("LINKTOSTELLA")
        wksheet = xl_workbook.sheet_by_name("LinktoStella9")
        wksheet3 = xl_workbook.sheet_by_name("LinktoStella9(2)")
        utils.read_array_data(self.inputData, wksheet, col_start=1, col_end=30, row_start=3)
        utils.read_array_data(self.inputData, wksheet, col_start=51, col_end=80, row_start=3)
        utils.read_array_data(self.inputData, wksheet3, col_start=0, col_end=80, row_start=3)
        self.inputData['I_MultiplierEvapoTrans'] = utils.read_table_to_matrix(wksheet, col_start=30, col_end=50, row_start=4, row_end=16)
        a = self.inputData['I_MultiplierEvapoTrans']
        for ia in a:
            print len(ia)
        self.inputData['I_RoutingDistance'] = utils.read_table_to_matrix(wksheet, col_start=80, col_end=87, row_start=4, row_end=24)
        del xl_workbook

    def reject(self):
        self.re_assign()
        super(Input_Run_Specs_Diaglog, self).accept()


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    form = Input_Run_Specs_Diaglog()
    form.show()
    app.exec_()

