import imp
import sys
from os import path as file_path
from PyQt4 import QtCore, QtGui
from functools import partial

from qtdesigners.stella_ui import Ui_MainWindow
import input_grass_and_cattle
import input_lake
import input_subcatchment_balance
import input_lake_hepp
import input_initial_run
import input_rainfall
import input_river
import input_run_specs
import input_soil_and_plant_water
import input_soil_structure_dynamic
import input_landcover_maps
import input_subcatchment_map
import output_map
import output_timeseries
import landcover_info
import copyright_view
import readme


class Stella_Main_Window(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Stella_Main_Window, self).__init__(parent)
        self.setupUi(self)
        self.parameters = dict()
        self.readme_Diaglog = readme.Readme(self)
        self.actionReadme.triggered.connect(self.openReadme)
        self.inputRiver_Diaglog = input_river.Input_River_Diaglog(self)
        self.inputRiver_Diaglog.setObjectName("River")
        self.inputRainfall_Diaglog = input_rainfall.Input_Rainfall_Diaglog(self)
        self.inputRainfall_Diaglog.setObjectName("Rainfall")
        self.inputLake_Diaglog = input_lake.Input_Lake_Diaglog(self)
        self.inputLake_Diaglog.setObjectName("Lake")
        self.inputLake_HEPP_Diaglog = (
            input_lake_hepp.Input_Lake_HEPP_Diaglog(self)
        )
        self.inputLake_HEPP_Diaglog.setObjectName("Lake_HEPP")
        self.inputGrass_and_Cattle_Diaglog = (
            input_grass_and_cattle.Input_Grass_And_Cattle_Diaglog(self)
        )
        self.inputGrass_and_Cattle_Diaglog.setObjectName("Grass_and_Cattle")
        self.inputSubcatchment_Balance_Diaglog = (
            input_subcatchment_balance.Input_Subcatchment_Balance_Diaglog(self)
        )
        self.inputSubcatchment_Balance_Diaglog.setObjectName(
            "Subcatchment_Balance"
        )
        self.inputSoil_Structure_Dynamic_Diaglog = (
            input_soil_structure_dynamic.
                Input_Soil_Structure_Dynamic_Diaglog(self)
        )
        self.inputSoil_Structure_Dynamic_Diaglog.setObjectName(
            "Soil_Structure_Dynamic"
        )
        self.inputInitial_Run_Diaglog = (
            input_initial_run.Input_Initial_Run_Diaglog(self)
        )
        self.inputInitial_Run_Diaglog.setObjectName("Initial_Run")
        self.inputRun_Specs_Diaglog = (
            input_run_specs.Input_Run_Specs_Diaglog(self)
        )
        self.inputRun_Specs_Diaglog.setObjectName("Run_Specs")
        self.inputSoil_and_Plant_Water_Diaglog = (
            input_soil_and_plant_water.Input_Soil_And_Plant_Water_Diaglog(self)
        )
        self.inputSoil_and_Plant_Water_Diaglog.setObjectName("Soil_and_Plant_Water")
        self.inputLandcover_maps_Diaglog = (
            input_landcover_maps.Input_Landcover_Maps_Diaglog(self)
        )
        self.inputLandcover_maps_Diaglog.setObjectName("Landcover_maps")
        self.inputSubcatchment_maps_Diaglog = (
            input_subcatchment_map.Input_Subcatchment_Map_Diaglog(self)
        )
        self.inputSubcatchment_maps_Diaglog.setObjectName("Subcatchment_map")
        self.inputLandcover_colors_Diaglog = landcover_info.LandcoverInfo(self)
        self.inputLandcover_colors_Diaglog.setObjectName("Landcover_info")
        self.inputSubcatchmentColors_Diaglog = landcover_info.LandcoverInfo(self, landcover=False)
        self.inputSubcatchmentColors_Diaglog.setObjectName("Subcatchment_info")
        # self.actionSubcatchmentColors
        # self.landcover
        copyright = copyright_view.Copyright(self)
        copyright.show()
        for diaglog in self.children():
            if isinstance(diaglog, QtGui.QDialog):
                self.get_parameter(diaglog)
                diaglog.data_cb = partial(self.get_parameter_cb, diaglog)

        for action in self.children():
            if isinstance(action, QtGui.QAction):
                actionName = str(action.objectName())
                diaglogName = actionName.replace('action', 'input') + '_Diaglog'
                try:
                    diaglog = getattr(self, diaglogName)
                    self.connect(
                        action,
                        QtCore.SIGNAL("triggered()"),
                        partial(self.actionDiaglog, diaglog)
                    )
                except AttributeError:
                    None
        self.actionRun.triggered.connect(self.onActionRun)
        self.actionMaps.triggered.connect(self.onActionMaps)
        self.actionTimeseries.triggered.connect(self.onActionTimeseries)
        outputMapsSubcatchment = [
            'L_InFlowtoLake',
            'O_EvapoTransAcc',
            'O_PercAcc',
            'O_RainAcc',
            'O_SurfQFlowAcc',
            'O_BaseFlowAcc',
            'O_DeepInfAcc',
            'O_IntercAcc',
            'O_SoilQFlowAcc',
            'O_InfAcc',
            'D_GWaDisch',
            'D_SoilDischarge'
        ]
        ouputTimeSeries = [
            'L_HEPPWatUseFlow',
            'L_HEPP_Kwh',
            'L_LakeVol',
            'L_LakeLevel',
            'L_CumHEPPUse'
        ]
        self.output = dict()
        self.output['maps'] = dict()
        self.output['maps']['subcatchment'] = dict()
        self.output['timeseries'] = dict()
        for map_result in outputMapsSubcatchment:
            self.output['maps']['subcatchment'][map_result] = []
        for time_result in ouputTimeSeries:
            self.output['timeseries'][time_result] = []
        self.actionStop.setEnabled(False)
        self.totalTime.setText(str(self.parameters['Run_Specs']['runto']))
        # self.outputTimeseries = output_timeseries.OutputTimeseries()

    def openReadme(self):
        self.readme_Diaglog.show()

    def actionDiaglog(self, diaglog):
        diaglog.show()
        self.get_parameter(diaglog)

    def onActionTimeseries(self):
        self.outputTimeseries.show()

    def onActionMaps(self):
        self.outputMap.colors = self.inputLandcover_colors_Diaglog.colorResult
        self.outputMap.show()

    def _show_message(self, title, message, func):
        msg = QtGui.QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QtGui.QMessageBox.Ok)
        msg.buttonClicked.connect(func)
        msg.exec_()

    def _check_file(self, file_name, file, func):
        if not file_path.isfile(file):
            message = 'Please recheck {}. It isn\'t file'.format(file_name)
            self._show_message(file_name, message, func)

    def _check_dir(self, dir_name, dir, func):
        if not file_path.isdir(dir):
            message = 'Please recheck {}. It isn\'t folder'.format(dir_name)
            self._show_message(dir_name, message, func)

    def onActionRun(self):
        subcatchment_file = self.parameters['Subcatchment_map']['subcatchmentMap']
        self._check_file(
            'subcatchment file',
            subcatchment_file,
            self.inputSubcatchment_maps_Diaglog.get_subcatchment_map
        )
        landcover_files = [
            self.parameters['Landcover_maps']['landcoverMap_1'],
            self.parameters['Landcover_maps']['landcoverMap_2'],
            self.parameters['Landcover_maps']['landcoverMap_3'],
            self.parameters['Landcover_maps']['landcoverMap_4'],
        ]
        for index, landcover_file in enumerate(landcover_files):
            self._check_file(
                'land cover map period {}'.format(index + 1),
                landcover_file,
                partial(self.inputLandcover_maps_Diaglog.get_landcover_map, index)
            )
        inputdata_file = self.parameters['Run_Specs']['inputDataFile']
        self._check_file(
            'inputdata file',
            inputdata_file,
            self.inputRun_Specs_Diaglog.get_data_file
        )

        self.get_parameter(self.inputRun_Specs_Diaglog)
        self.get_parameter(self.inputLandcover_maps_Diaglog)
        self.get_parameter(self.inputSubcatchment_maps_Diaglog)

        self.inputRun_Specs_Diaglog.get_input_data()
        self.data = self.inputRun_Specs_Diaglog.inputData
        self.simulation_module = imp.load_source(
            'model',
            'model.py')
        self.simulation = self.simulation_module.SimulatingThread(
            parameters=self.parameters,
            data=self.inputRun_Specs_Diaglog.inputData
        )
        self.connect(self.simulation, QtCore.SIGNAL("update"),
                     self.update_result)

        landcover_files = [
            self.parameters['Landcover_maps']['landcoverMap_1'],
            self.parameters['Landcover_maps']['landcoverMap_2'],
            self.parameters['Landcover_maps']['landcoverMap_3'],
            self.parameters['Landcover_maps']['landcoverMap_4'],
        ]
        year_period = [
            int(self.parameters['Initial_Run']['I_StartMYear_1']),
            int(self.parameters['Initial_Run']['I_StartMYear_2']),
            int(self.parameters['Initial_Run']['I_StartMYear_3'])
        ]
        simulationTime = int(self.parameters['Run_Specs']['runto'])
        self.outputMap = output_map.OutputMap(
            subcatchment=self.parameters['Subcatchment_map']['subcatchmentMap'],
            landcover=landcover_files,
            period=year_period,
            simulationTime=simulationTime
        )
        self.outputTimeseries = output_timeseries.OutputTimeseries(
            outputFolder = '',
            simulationTime=simulationTime
        )
        self.actionStop.setEnabled(True)
        self.actionRun.setEnabled(False)
        self.actionStop.triggered.connect(self.onActionStop)
        self.outputMap.connect(self.simulation, QtCore.SIGNAL("updateMap"),
                               self.outputMap.update_display)
        self.outputTimeseries.connect(self.simulation, QtCore.SIGNAL("updateTimeseries"),
                                      self.outputTimeseries.update_display)
        # self.output['timeseries'] = {}
        self.connect(self.simulation, QtCore.SIGNAL("finished()"), self.finish_simulation)
        self.simulation.start()

    def finish_simulation(self):
        delattr(self.simulation, 'output')
        print 'Finished'

    def onActionStop(self):
        self.actionRun.setChecked(False)
        self.actionRun.setEnabled(True)
        delattr(self.outputMap, 'data')
        delattr(self.outputTimeseries, 'timeseriesData')

    def update_result(self, time):
        simulationTime = int(self.parameters['Run_Specs']['runto'])
        self.simulatingTime.setText(str(time))
        self.totalTime.setText(str(simulationTime))
        self.simulatingProgress.setValue(int((time + 1) * 100 / simulationTime))

    def get_parameter_cb(self, diaglog):
        diaglog_name = str(diaglog.objectName())
        self.parameters[diaglog_name] = diaglog.data

    def get_parameter(self, diaglog):
        diaglog_name = str(diaglog.objectName())
        self.parameters[diaglog_name] = diaglog.data


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    form = Stella_Main_Window()
    form.show()
    app.exec_()


