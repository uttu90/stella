import imp
import gdal
from PyQt4 import QtCore, QtGui
from functools import partial

from stella_ui import Ui_MainWindow
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


class Stella_Main_Window(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Stella_Main_Window, self).__init__(parent)
        self.setupUi(self)
        self.parameters = dict()
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
        self.inputSubcatchment_map_Diaglog = (
            input_subcatchment_map.Input_Subcatchment_Map_Diaglog(self)
        )
        self.inputSubcatchment_map_Diaglog.setObjectName("Subcatchment_map")

        for diaglog in self.children():
            if isinstance(diaglog, QtGui.QDialog):
                self.get_parameter(diaglog)

        for action in self.children():
            if isinstance(action, QtGui.QAction):
                actionName = str(action.objectName())
                diaglogName = actionName.replace('action', 'input') + '_Diaglog'
                try:
                    diaglog = getattr(self, diaglogName)
                    print diaglog, action
                    self.connect(
                        action,
                        QtCore.SIGNAL("triggered()"),
                        partial(self.actionDiaglog, diaglog)
                    )
                except AttributeError:
                    None

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

        self.periodUpdate = int(self.parameters['Run_Specs']['outputUpdate'])
        self.outputTimeseries = output_timeseries.OutputTimeseries()

    def actionDiaglog(self, diaglog):
        print diaglog
        diaglog.show()
        self.get_parameter(diaglog)

    def onActionTimeseries(self):
        self.outputTimeseries.show()

    def onActionMaps(self):
        self.outputMap.show()

    def onActionRun(self):
        self.outputTimeseries.show()
        self.simulation_module = imp.load_source(
            'model',
            self.parameters['run specs']['inputSimulationFile'])
        self.simulation = self.simulation_module.SimulatingThread(
            parameters=self.parameters,
            data=self.inputRunSpecsDiaglog.inputData
        )
        self.connect(self.simulation, QtCore.SIGNAL("update"),
                     self.update_result)
        self.simulation.start()

    def update_result(self, output, time):
        if time % self.periodUpdate == 0:
            self.outputMap.update_display(output, time)
            self.outputTimeseries.update_display(output, time)

    def get_parameter(self, diaglog):
        diaglog_name = str(diaglog.objectName())
        self.parameters[diaglog_name] = diaglog.data


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    form = Stella_Main_Window()
    form.show()
    app.exec_()


