import imp
import gdal
from PyQt4 import QtCore, QtGui

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
import output_map
import output_timeseries


class Stella_Main_Window(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Stella_Main_Window, self).__init__(parent)
        self.setupUi(self)
        self.parameters = dict()
        self.connect(
            self.actionRiver,
            QtCore.SIGNAL("triggered()"),
            self.onActionRiver
        )
        self.connect(
            self.actionGrass_and_Cattle,
            QtCore.SIGNAL("triggered()"),
            self.onActionGrass_and_Cattle
        )
        self.connect(
            self.actionLake,
            QtCore.SIGNAL("triggered()"),
            self.onActionLake
        )
        self.connect(
            self.actionLake_HEPP,
            QtCore.SIGNAL("triggered()"),
            self.onActionLake_HEPP
        )
        self.connect(
            self.actionRainfall,
            QtCore.SIGNAL("triggered()"),
            self.onActionRainfall
        )
        self.connect(
            self.actionGrass_and_Cattle,
            QtCore.SIGNAL("triggered()"),
            self.onActionGrass_and_Cattle
        )
        self.connect(
            self.actionSubcatchment_Balance,
            QtCore.SIGNAL("triggered()"),
            self.onActionSubcatchment_Balance
        )
        self.connect(
            self.actionSoil_and_Plant_Water,
            QtCore.SIGNAL("triggered()"),
            self.onActionSoil_and_Plant_Water
        )
        self.connect(
            self.actionSoil_Structure_Dynamic,
            QtCore.SIGNAL("triggered()"),
            self.onActionSoil_Structure_Dynamic
        )
        self.connect(
            self.actionTimeseries,
            QtCore.SIGNAL("triggered()"),
            self.onActionTimeseries
        )
        self.connect(
            self.actionMaps,
            QtCore.SIGNAL("triggered()"),
            self.onActionMaps
        )
        self.connect(
            self.actionInitial_Run,
            QtCore.SIGNAL("triggered()"),
            self.onActionInitial_Run
        )
        self.connect(
            self.actionRun_Specs,
            QtCore.SIGNAL("triggered()"),
            self.onActionRun_Specs
        )
        self.connect(
            self.actionRun,
            QtCore.SIGNAL("triggered()"),
            self.onActionRun
        )
        self.inputRiverDiaglog = input_river.Input_River_Diaglog(self)
        self.inputRiverDiaglog.setObjectName("river")
        self.inputRainfallDiaglog = input_rainfall.Input_Rainfall_Diaglog(self)
        self.inputRainfallDiaglog.setObjectName("rainfall")
        self.inputLakeDiaglog = input_lake.Input_Lake_Diaglog(self)
        self.inputLakeDiaglog.setObjectName("lake")
        self.inputLakeHEPPDiaglog = (
            input_lake_hepp.Input_Lake_HEPP_Diaglog(self)
        )
        self.inputLakeHEPPDiaglog.setObjectName("lake hepp")
        self.inputGrassAndCattle = (
            input_grass_and_cattle.Input_Grass_And_Cattle_Diaglog(self)
        )
        self.inputGrassAndCattle.setObjectName("grass and cattle")
        self.inputSubcatchmentBalanceDiaglog = (
            input_subcatchment_balance.Input_Subcatchment_Balance_Diaglog(self)
        )
        self.inputSubcatchmentBalanceDiaglog.setObjectName(
            "subcatchment balance"
        )
        self.inputSoilStructureDynamicDiaglog = (
            input_soil_structure_dynamic.
                Input_Soil_Structure_Dynamic_Diaglog(self)
        )
        self.inputSoilStructureDynamicDiaglog.setObjectName(
            "soil structure dynamic"
        )
        self.inputInitialRunDiaglog = (
            input_initial_run.Input_Initial_Run_Diaglog(self)
        )
        self.inputInitialRunDiaglog.setObjectName("initial run")
        self.inputRunSpecsDiaglog = (
            input_run_specs.Input_Run_Specs_Diaglog(self)
        )
        self.inputRunSpecsDiaglog.setObjectName("run specs")
        self.inputSoilPlantWaterDiaglog = (
            input_soil_and_plant_water.Input_Soil_And_Plant_Water_Diaglog(self)
        )
        self.inputSoilPlantWaterDiaglog.setObjectName("soil plant water")

        for diaglog in [
            self.inputRiverDiaglog,
            self.inputRunSpecsDiaglog,
            self.inputRainfallDiaglog,
            self.inputLakeHEPPDiaglog,
            self.inputLakeDiaglog,
            self.inputGrassAndCattle,
            self.inputInitialRunDiaglog,
            self.inputSubcatchmentBalanceDiaglog,
            self.inputSoilStructureDynamicDiaglog,
            self.inputSoilPlantWaterDiaglog,
        ]:
            self.get_parameter(diaglog)

        self.inputRunSpecsDiaglog.get_input_data()

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

        self.outputMap = output_map.OutputMap(
            landcover=self.parameters['run specs']['inputLandcoverMap'],
            subcatchment=self.parameters['run specs']['inputSubcatchmentMap']
        )
        filename = self.parameters['run specs']['inputLandcoverMap']
        self.outputTimeseries = output_timeseries.OutputTimeseries()

    def onActionRiver(self):
        self.inputRiverDiaglog.show()
        self.get_parameter(self.inputRiverDiaglog)

    def onActionRainfall(self):
        self.inputRainfallDiaglog.show()
        self.get_parameter(self.inputRainfallDiaglog)

    def onActionLake(self):
        self.inputLakeDiaglog.show()
        self.get_parameter(self.inputLakeDiaglog)

    def onActionLake_HEPP(self):
        self.inputLakeHEPPDiaglog.show()
        self.get_parameter(self.inputLakeHEPPDiaglog)

    def onActionGrass_and_Cattle(self):
        self.inputGrassAndCattle.show()
        self.get_parameter(self.inputGrassAndCattle)

    def onActionSubcatchment_Balance(self):
        self.inputSubcatchmentBalanceDiaglog.show()
        self.get_parameter(self.inputSubcatchmentBalanceDiaglog)

    def onActionSoil_Structure_Dynamic(self):
        self.inputSoilStructureDynamicDiaglog.show()
        self.get_parameter(self.inputSoilStructureDynamicDiaglog)

    def onActionTimeseries(self):
        self.outputTimeseries.show()

    def onActionMaps(self):
        self.outputMap.show()

    def onActionInitial_Run(self):
        self.inputInitialRunDiaglog.show()
        self.get_parameter(self.inputInitialRunDiaglog)

    def onActionRun_Specs(self):
        self.inputRunSpecsDiaglog.show()
        self.get_parameter(self.inputRunSpecsDiaglog)
        self.inputRunSpecsDiaglog.get_input_data()

    def onActionSoil_and_Plant_Water(self):
        self.inputSoilPlantWaterDiaglog.show()
        self.get_parameter(self.inputSoilPlantWaterDiaglog)

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


