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
        self.selectDataFile.clicked.connect(self._get_data_file)
        self.selectSimulationFile.clicked.connect(self._get_simulation_file)
        self.selectLandcoverMap.clicked.connect(self._get_landcover_map)
        self.selectSubcatchmentMap.clicked.connect(self._get_subcatchment_map)
        if file_path.isfile(self.file):
            self._initiate_value()
        else:
            self._collect_value()

    def _get_data_file(self):
        data_file = QtGui.QFileDialog.getOpenFileName(
            self,
            'Get data file',
            'c:\\',"Excel files (*.xls)"
        )
        self.inputDataFile.setText(data_file)
        self.data[str(self.inputDataFile.objectName())] = str(data_file)
        self.save()

    def _get_simulation_file(self):
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

    def _get_landcover_map(self):
        landcover_file = str(QtGui.QFileDialog.getOpenFileName(
            self,
            'Get landcover file',
            'c:\\', "Map files (*.tif)"
        ))
        self.inputLandcoverMap.setText(landcover_file)

    def _get_subcatchment_map(self):
        subcatchment_file = str(QtGui.QFileDialog.getOpenFileName(
            self,
            'Get Subcatchment file',
            'c:\\', "Map files (*.tif)"
        ))
        self.inputSubcatchmentMap.setText(subcatchment_file)

    def accept(self):
        self._collect_value()
        self.save()
        super(Input_Run_Specs_Diaglog, self).accept()

    def get_input_data(self):
        if not self.data.get('inputDataFile'):
            self._get_data_file()
        xl_workbook = xlrd.open_workbook(self.data.get('inputDataFile'))
        wksheet = xl_workbook.sheet_by_name("LINKTOSTELLA")
        wksheet2 = xl_workbook.sheet_by_name("LinktoStella9")
        wksheet3 = xl_workbook.sheet_by_name("LinktoStella9(2)")
        # Daily Rain & River Flow & DailyET
        iDailyRain = utils.read_array_data(
            wksheet,
            col_start=1,
            col_end=9,
            row_start=3,
            row_end=1464)
        iRFlowData = utils.read_array_data(
            wksheet,
            col_start=9,
            col_end=17,
            row_start=3,
            row_end=1464)
        iDailyETYear = utils.read_array_data(
            wksheet,
            col_start=18,
            col_end=25,
            row_start=3,
            row_end=1464)
        iDailyEvap = utils.read_array_data(
            wksheet2,
            col_start=17,
            col_end=26,
            row_start=3,
            row_end=1464)
        self.inputData.update(iDailyRain)
        self.inputData.update(iRFlowData)
        self.inputData.update(iDailyETYear)
        self.inputData.update(iDailyEvap)
        self.inputData['I_InputDataYears'] = wksheet.col_values(
            colx=26,
            start_rowx=4,
            end_rowx=8)
        self.inputData['I_InterceptClass'] = wksheet.col_values(
            colx=28,
            start_rowx=4,
            end_rowx=15)
        self.inputData['I_RelDroughtFact'] = wksheet.col_values(
            colx=29,
            start_rowx=4,
            end_rowx=15)
        self.inputData['I_Area'] = wksheet.col_values(
            colx=50,
            start_rowx=4,
            end_rowx=24)
        self.inputData['I_RoutingDistance'] = utils.read_table_to_matrix(
            wksheet,
            col_start=52,
            col_end=58,
            row_start=4,
            row_end=24
        )
        self.inputData['I_RivFlowTime1'] = wksheet.col_values(
            colx=58,
            start_rowx=4,
            end_rowx=24)
        self.inputData['I_MaxDynGWSub1'] = wksheet.col_values(
            colx=59,
            start_rowx=4,
            end_rowx=24)
        self.inputData['I_GWRelFrac1'] = wksheet.col_values(
            colx=60,
            start_rowx=4,
            end_rowx=24)
        self.inputData['I_RivFlowTime2'] = wksheet.col_values(
            colx=61,
            start_rowx=4,
            end_rowx=24)
        self.inputData['I_MaxDynGWSub2'] = wksheet.col_values(
            colx=62,
            start_rowx=4,
            end_rowx=24)
        self.inputData['I_GWRelFrac2'] = wksheet.col_values(
            colx=63,
            start_rowx=4,
            end_rowx=24)
        self.inputData['I_RivFlowTime3'] = wksheet.col_values(
            colx=64,
            start_rowx=4,
            end_rowx=24)
        self.inputData['I_MaxDynGWSub3'] = wksheet.col_values(
            colx=65,
            start_rowx=4,
            end_rowx=24)
        self.inputData['I_GWRelFrac3'] = wksheet.col_values(
            colx=66,
            start_rowx=4,
            end_rowx=24)
        self.inputData['I_RivFlowTime4'] = wksheet.col_values(
            colx=67,
            start_rowx=4,
            end_rowx=24)
        self.inputData['I_MaxDynGWSub4'] = wksheet.col_values(
            colx=68,
            start_rowx=4,
            end_rowx=24)
        self.inputData['I_GWRelFrac4'] = wksheet.col_values(
            colx=69,
            start_rowx=4,
            end_rowx=24)
        self.inputData['I_SoilSatMinFCSub1'] = wksheet.col_values(
            colx=70,
            start_rowx=4,
            end_rowx=24)
        self.inputData['I_PlantAvWatSub1'] = wksheet.col_values(
            colx=71,
            start_rowx=4,
            end_rowx=24)
        self.inputData['I_PWPSub1'] = wksheet.col_values(
            colx=72,
            start_rowx=4,
            end_rowx=24)
        self.inputData['I_SoilSatMinFCSub2'] = wksheet.col_values(
            colx=73,
            start_rowx=4,
            end_rowx=24)
        self.inputData['I_PlantAvWatSub2'] = wksheet.col_values(
            colx=74,
            start_rowx=4,
            end_rowx=24)
        self.inputData['I_PWPSub2'] = wksheet.col_values(
            colx=75,
            start_rowx=4,
            end_rowx=24)
        self.inputData['I_SoilSatMinFCSub3'] = wksheet.col_values(
            colx=76,
            start_rowx=4,
            end_rowx=24)
        self.inputData['I_PlantAvWatSub3'] = wksheet.col_values(
            colx=77,
            start_rowx=4,
            end_rowx=24)
        self.inputData['I_PWPSub3'] = wksheet.col_values(
            colx=78,
            start_rowx=4,
            end_rowx=24)
        self.inputData['I_SoilSatMinFCSub4'] = wksheet.col_values(
            colx=79,
            start_rowx=4,
            end_rowx=24)
        self.inputData['I_PlantAvWatSub4'] = wksheet.col_values(
            colx=80,
            start_rowx=4,
            end_rowx=24)
        self.inputData['I_PWPSub4'] = wksheet.col_values(
            colx=81,
            start_rowx=4,
            end_rowx=24)
        self.inputData['I_TopSoilBD_BDRef1'] = wksheet.col_values(
            colx=82,
            start_rowx=4,
            end_rowx=24)
        self.inputData['I_TopSoilBD_BDRef2'] = wksheet.col_values(
            colx=83,
            start_rowx=4,
            end_rowx=24)
        self.inputData['I_TopSoilBD_BDRef3'] = wksheet.col_values(
            colx=84,
            start_rowx=4,
            end_rowx=24)
        self.inputData['I_TopSoilBD_BDRef4'] = wksheet.col_values(
            colx=85,
            start_rowx=4,
            end_rowx=24)
        self.inputData['I_AvailWatSub1'] = wksheet.col_values(
            colx=86,
            start_rowx=4,
            end_rowx=24)
        self.inputData['I_AvailWatSub2'] = wksheet.col_values(
            colx=87,
            start_rowx=4,
            end_rowx=24)
        self.inputData['I_AvailWatSub3'] = wksheet.col_values(
            colx=88,
            start_rowx=4,
            end_rowx=24)
        self.inputData['I_AvailWatSub4'] = wksheet.col_values(
            colx=89,
            start_rowx=4,
            end_rowx=24)
        self.inputData['I_Evapotrans'] = wksheet.col_values(
            colx=31,
            start_rowx=4,
            end_rowx=16
        )
        self.inputData['I_MultiplierEvapoTrans'] = utils.read_table_to_matrix(
            sheet=wksheet,
            col_start=32,
            col_end=43,
            row_start=4,
            row_end=16
        )

        ifracData = utils.read_array_data(
            wksheet3,
            col_start=0,
            col_end=80,
            row_start=3,
            row_end=24)
        self.inputData.update(ifracData)
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

