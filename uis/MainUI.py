import imp

import xlrd
from PyQt4 import QtCore, QtGui

import utils
from stella_model_ol import Ui_MainWindow

from matplotlib import cm as cms
from matplotlib.cbook import MatplotlibDeprecationWarning

from matplotlib.figure import Figure
from matplotlib import colors as colorsmap
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from matplotlib.backends import qt4_compat


class StellaUI(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(StellaUI, self).__init__(parent)
        self.setupUi(self)
        self._prepare_display()
        self.parameters = dict()
        self.data = dict()
        self.output = None
        self.output_specs = [
            'I_RFlowdata_mmday',
            'L_InFlowtoLake',
            'O_RainAcc',
            'O_IntercAcc',
            'O_EvapoTransAcc',
            'O_SoilQFlowAcc',
            'O_InfAcc',
            'O_PercAcc',
            'O_DeepInfAcc',
            'O_BaseFlowAcc',
            'O_SurfQFlowAcc',
            'I_RainDoY',
            'L_RivOutFlow',
            'I_DailyRain',
            'L_HEPPWatUseFlow',
            'L_HEPP_Kwh',
            'L_LakeVol',
            'L_LakeLevel',
            'O_BestYyHEPP',
            'O_WorstYHEPP',
            'L_CumHEPPUse',
            'O_FrBaseFlow',
            'O_FrSoilQuickFlow',
            'I_DailyRainAmount',
            'D_SurfaceFlow',
            'D_SoilDischarge',
            'D_GWaDisch'
        ]
        self.resultBox.addItems(self.output_specs)
        self.resultBox_2.addItems(self.output_specs)
        self.resultBox_3.addItems(self.output_specs)
        self.resultBox_4.addItems(self.output_specs)
        self.output_data = []
        self.selectDataFile.clicked.connect(self._get_data_file)
        self.selectSimulationFile.clicked.connect(self._get_simulation_file)
        self.selectSubcatchmentMap.clicked.connect(self._get_subcatchment_map)
        self.selectLandcoverMap.clicked.connect(self._get_landcover_map)
        self.runbtn.clicked.connect(self._run)
        self.resultBox.currentIndexChanged.connect(self._selectionchange)
        self.resultBox_2.currentIndexChanged.connect(self._selectionchange_2)
        self.resultBox_3.currentIndexChanged.connect(self._selectionchange_3)
        self.resultBox_4.currentIndexChanged.connect(self._selectionchange_4)

    def _selectionchange(self):
        selection = str(self.resultBox.currentText())
        if not self.output_data:
            self.output_data.append(selection)
        else:
            self.output_data[0] = selection
        self._display_timeseries()
        # print self.output_data

    def _selectionchange_2(self):
        selection = str(self.resultBox_2.currentText())
        if len(self.output_data) == 1:
            self.output_data.append(selection)
        elif len(self.output_data) >= 2:
            self.output_data[1] = str(self.resultBox_2.currentText())
        self._display_timeseries()

    def _selectionchange_3(self):
        selection = str(self.resultBox_3.currentText())
        if len(self.output_data) == 2:
            self.output_data.append(selection)
        elif len(self.output_data) >= 3:
            self.output_data[2] = selection
        self._display_timeseries()

    def _selectionchange_4(self):
        selection = str(self.resultBox_4.currentText())
        if len(self.output_data) == 3:
            self.output_data.append(selection)
        elif len(self.output_data) == 4:
            self.output_data[3] = selection
        if self.output:
            self._display_timeseries()

    def _get_data_file(self):
        data_file = QtGui.QFileDialog.getOpenFileName(
            self,
            'Get data file',
            'c:\\',"Excel files (*.xls)"
        )
        self.inputData.setText(data_file)
        if data_file:
            self._get_input_data()

    def _get_simulation_file(self):
        self.simulation_file = str(QtGui.QFileDialog.getOpenFileName(
            self,
            'Get simulation file',
            'c:\\',"Python files (*.py)"
        ))
        self.inputSimulationFile.setText(self.simulation_file)

    def _get_subcatchment_map(self):
        self.subcatchment_file = str(QtGui.QFileDialog.getOpenFileName(
            self,
            'Get subcatchment file',
            'c:\\', "Map files"
        ))
        self.inputSimulationFile.setText(self.subcatchment_file)

    def _get_landcover_map(self):
        self.landcover_file = str(QtGui.QFileDialog.getOpenFileName(
            self,
            'Get landcover file',
            'c:\\', "Map files"
        ))
        self.inputSimulationFile.setText(self.landcover_file)

    def _get_input(self):
        run_specs = dict()
        run_specs['from'] = float(self.runfrom.text())
        run_specs['to'] = float(self.runto.text())
        run_specs['dt'] = float(self.rundt.text())
        self.parameters['run specs'] = run_specs

        initial_run = dict()
        initial_run['Simulation Time'] = float(self.simulationTime.text())
        initial_run['I_StartMYear'] = [
            float(self.I_StartMYear_1.text()),
            float(self.I_StartMYear_2.text()),
            float(self.I_StartMYear_3.text())
        ]
        initial_run['I_StartDOYear'] = [
            float(self.I_StartDOY_1.text()),
            float(self.I_StartDOY_2.text()),
            float(self.I_StartDOY_3.text())]
        initial_run['I_RainYearStar'] = float(self.I_RainYearStart.text())
        initial_run['I_CaDOYearStar'] = float(self.I_CaDOYStart.text())
        initial_run['I_WarmUpTime'] = float(self.I_WarmUpTime.text())
        initial_run['O_MPeriodLength'] = [
            float(self.O_MPeriodLength_1.text()),
            float(self.O_MPeriodLength_2.text()),
            float(self.O_MPeriodLength_3.text())]
        self.parameters['initial run'] = initial_run

        rainfall = dict()
        rainfall['I_UseSpatVarRain?'] = float(self.isI_UseSpatVarRain.text())
        rainfall['I_RainMultiplier'] = float(self.I_RainMultiplier.text())
        rainfall['I_RainCycle?'] = float(self.isI_RainCycle.text())
        rainfall['I_Rain_IntensMean'] = float(self.I_Rain_IntensMean.text())
        rainfall['I_Rain_IntensCoefVar'] = float(
            self.I_Rain_IntensCoefVar.text()
        )
        rainfall['I_Rain_GenSeed'] = float(self.I_Rain_GenSeed.text())
        self.parameters['rainfall'] = rainfall

        river = dict()
        river['I_RoutVeloc_m_per_s'] = float(self.I_RoutVelocm_per_s.text())
        river['I_Tortuosity'] = float(self.I_Tortuosity.text())
        river['I_RiverflowDispersalFactor'] = float(
            self.I_RiverflowDispersalFactor.text()
        )
        river['I_SurfLossFrac'] = float(self.I_SurfLossFrac.text())
        river['I_DaminThisStream'] = [
            float(self.A_is_DamThisStream.text()),
            float(self.B_is_DamThisStream.text()),
            float(self.C_is_DamThisStream.text()),
            float(self.D_is_DamThisStream.text()),
            float(self.E_is_DamThisStream.text()),
            float(self.F_is_DamThisStream.text()),
            float(self.G_is_DamThisStream.text()),
            float(self.H_is_DamThisStream.text()),
            float(self.I_is_DamThisStream.text()),
            float(self.J_is_DamThisStream.text()),
            float(self.K_is_DamThisStream.text()),
            float(self.L_is_DamThisStream.text()),
            float(self.M_is_DamThisStream.text()),
            float(self.N_is_DamThisStream.text()),
            float(self.O_is_DamThisStream.text()),
            float(self.P_is_DamThisStream.text()),
            float(self.Q_is_DamThisStream.text()),
            float(self.R_is_DamThisStream.text()),
            float(self.S_is_DamThisStream.text()),
            float(self.T_is_DamThisStream.text())
        ]
        self.parameters['river'] = river

        soilAndWaterBalance = dict()
        soilAndWaterBalance['I_MaxInf'] = float(self.I_MaxInf.text())
        soilAndWaterBalance['I_MaxInfSoil'] = float(self.I_MaxInfSoil.text())
        soilAndWaterBalance['I_PowerInfiltRed'] = float(
            self.I_PowerInfiltRed.text()
        )
        soilAndWaterBalance['I_SoilPropConst?'] = float(
            self.isI_SoilPropConst.text()
        )
        soilAndWaterBalance['I_AvailWaterClassConst'] = float(
            self.I_AvailQaterClassConst.text()
        )
        soilAndWaterBalance['I_SoilSatMinFCConst'] = float(
            self.I_SoilSatMinFCConst.text()
        )
        soilAndWaterBalance['I_InitRelGW'] = float(self.I_InitRelGW.text())
        soilAndWaterBalance['I_GWRelFracConst?'] = float(
            self.isI_GWRelFracConst.text()
        )
        soilAndWaterBalance['I_MaxDynGWConst'] = float(
            self.I_MaxDynGWConst.text()
        )
        soilAndWaterBalance['I_GWRelFracConst'] = float(
            self.I_GWRelFracConst.text()
        )
        soilAndWaterBalance['I_IntercepEffectionTransp'] = float(
            self.I_IntercepEffectionTransp.text()
        )
        soilAndWaterBalance['I_RainIntercDripRt'] = float(
            self.I_RainIntercDripRt.text()
        )
        soilAndWaterBalance['I_RainMaxIntDripDur'] = float(
            self.I_RainMaxIntDripDur.text()
        )
        soilAndWaterBalance['I_PercFracMultiplier'] = float(
            self.I_PercFracMultiplier.text()
        )
        soilAndWaterBalance['I_InitRelSoil'] = float(
            self.I_InitRelSoil.text()
        )
        soilAndWaterBalance['I_EvapotransMethod'] = float(
            self.I_EvapotransMethod.text()
        )
        soilAndWaterBalance['I_SoilQflowFract'] = float(
            self.I_SoilQflowFract.text()
        )
        self.parameters['soi and water balance'] = soilAndWaterBalance

        lake = dict()
        lake['L_Lake?'] = [
            float(self.A_isL_Lake.text()),
            float(self.B_isL_Lake.text()),
            float(self.C_isL_Lake.text()),
            float(self.D_isL_Lake.text()),
            float(self.E_isL_Lake.text()),
            float(self.F_isL_Lake.text()),
            float(self.G_isL_Lake.text()),
            float(self.H_isL_Lake.text()),
            float(self.I_isL_Lake.text()),
            float(self.J_isL_Lake.text()),
            float(self.K_isL_Lake.text()),
            float(self.L_isL_Lake.text()),
            float(self.M_isL_Lake.text()),
            float(self.N_isL_Lake.text()),
            float(self.O_isL_Lake.text()),
            float(self.P_isL_Lake.text()),
            float(self.Q_isL_Lake.text()),
            float(self.R_isL_Lake.text()),
            float(self.S_isL_Lake.text()),
            float(self.T_isL_Lake.text())
        ]
        lake['L_HEPP_Active?'] = float(self.isL_HEPP_Active.text())
        lake['L_LakeTransMultiplier'] = float(self.L_LakeTransMultiplier.text())
        lake['L_LakeBottomElev'] = float(self.L_LakeBottomElev.text())
        lake['L_LakeElevPreHEPP'] = float(self.L_LakeElevPreHEPP.text())
        lake['L_LakeOverFIPostHEPP'] = float(self.L_LakeOverFIPostHEPP.text())
        lake['L_LakeLevelFullHEPP'] = float(self.L_LakeLevelFullHEPP.text())
        lake['L_LakeLevelHalfHEPP'] = float(self.L_LakeLevelHalfHEPP.text())
        lake['L_LakeLevelNoHEPP'] = float(self.L_LakeLevelNoHEPP.text())
        lake['L_LakeFloodTresh'] = float(self.L_LakeFloodTresh.text())
        lake['L_LakeQmecsHEPP'] = float(self.L_LakeQmecsHEPP.text())
        lake['L_LakeQmecsSanFlow'] = float(self.L_LakeQmecsSanFlow.text())
        lake['L_LakeOverFlowFract'] = float(self.L_LakeOverFlowFract.text())
        lake['L_LakeOverFIFlow'] = float(self.L_LakeOverFIFlow.text())
        lake['L_m3_per_kwh'] = float(self.L_m3_per_kwh.text())
        lake['L_ResrDepth'] = float(self.L_ResrDepth.text())
        self.parameters['lake'] = lake

        lake_hepp = dict()
        lake_hepp['O_CumRivInflowtoLakeMP'] = [
            float(self.O_CumRivInflowtoLakeMP_1.text()),
            float(self.O_CumRivInflowtoLakeMP_2.text()),
            float(self.O_CumRivInflowtoLakeMP_3.text())
        ]
        lake_hepp['O_CumRivOutFlowMP'] = [
            float(self.O_CumRivOutFlowMP_1.text()),
            float(self.O_CumRivOutFlowMP_2.text()),
            float(self.O_CumRivOutFlowMP_3.text())
        ]
        lake_hepp['O_HEPP_Kwh_per_dayMP'] = [
            float(self.O_HEPP_Kwh_per_dayMP_1.text()),
            float(self.O_HEPP_Kwh_per_dayMP_2.text()),
            float(self.O_HEPP_Kwh_per_dayMP_3.text())
        ]
        lake_hepp['O_CumHEPPOutFlowMP'] = [
            float(self.O_CumHEPPOutFlowMP_1.text()),
            float(self.O_CumHEPPOutFlowMP_2.text()),
            float(self.O_CumHEPPOutFlowMP_3.text())
        ]
        lake_hepp['O_RelOPTimeHEPPMP'] = [
            float(self.O_RelOPTimeHEPPMP_1.text()),
            float(self.O_RelOPTimeHEPPMP_2.text()),
            float(self.O_RelOPTimeHEPPMP_3.text()),
        ]
        lake_hepp['O_FrBaseFlow'] = float(self.O_FrBaseFlow.text())
        lake_hepp['O_FrSoilQuickFlow'] = float(self.O_FrSoilQuickFlow.text())
        lake_hepp['O_FrSurfQuickFlow'] = float(self.O_FrSurfQuickflow.text())
        self.parameters['lake hepp'] = lake_hepp

        grassAndCattle = dict()
        grassAndCattle['C_DailyTrampFac'] = float(self.C_DailyTramFac.text())
        grassAndCattle['C_CattleSale'] = float(self.C_CattleSale.text())
        grassAndCattle['C_DailyIntake'] = float(self.C_DailyIntake.text())
        grassAndCattle['C_GrazingManConv'] = float(self.C_GrazingManConv.text())
        grassAndCattle['C_SurfLitDecFrac'] = float(self.C_SurfLitDecFrac.text())
        grassAndCattle['C_SurfManureDecFrac'] = float(
            self.C_SurfManureDecFrac.text()
        )
        grassAndCattle['C_GrassLitConv'] = float(self.C_GrassLitConv.text())
        grassAndCattle['C_GrassLitMortFrac'] = float(
            self.C_GrassLitMortFrac.text())
        grassAndCattle['G_WUE'] = float(self.G_WUE.text())
        grassAndCattle['G_TramplingMultiplier'] = float(
            self.G_TramplingMultiplier.text()
        )
        self.parameters['Grass and Cattle'] = grassAndCattle

        soilStructureDynamic = dict()
        soilStructureDynamic['S_TrampMax'] =float(self.S_TrampMax.text())
        self.parameters['Soil Structure Dynamic'] = soilStructureDynamic

        subcatchmentBalance = dict()
        subcatchmentBalance['O_CumRainMP'] = [
            float(self.O_CumRainMP_1.text()),
            float(self.O_CumRainMP_2.text()),
            float(self.O_CumRainMP_3.text())]
        subcatchmentBalance['O_CumIntercEvapMP'] = [
            float(self.O_CumIntercEvapMP_1.text()),
            float(self.O_CumIntercEvapMP_2.text()),
            float(self.O_CumIntercEvapMP_3.text())]
        subcatchmentBalance['O_CumTranspMP'] = [
            float(self.O_CumTranspMP_1.text()),
            float(self.O_CumTranspMP_2.text()),
            float(self.O_CumTranspMP_3.text()),]
        subcatchmentBalance['O_CumETLandMP'] = [
            float(self.O_CumETLandMP_1.text()),
            float(self.O_CumETLandMP_2.text()),
            float(self.O_CumETLandMP_3.text())]
        subcatchmentBalance['O_CumEvapTransMP'] = [
            float(self.O_CumEvapTranspMP_1.text()),
            float(self.O_CumEvapTranspMP_2.text()),
            float(self.O_CumEvapTranspMP_3.text()),]
        subcatchmentBalance['O_CumSurfQFlow'] = [
            float(self.O_CumSurfQFlow_1.text()),
            float(self.O_CumSurfQFlow_2.text()),
            float(self.O_CumSurfQFlow_3.text())]
        subcatchmentBalance['O_CumInfiltrationMP'] = [
            float(self.O_CumInfiltrationMP_1.text()),
            float(self.O_CumInfiltrationMP_2.text()),
            float(self.O_CumInfiltrationMP_3.text())]
        subcatchmentBalance['O_CumSoilQFlowMP'] = [
            float(self.O_CumSoilQFlowMP_1.text()),
            float(self.O_CumSoilQFlowMP_2.text()),
            float(self.O_CumSoilQFlowMP_3.text())]
        subcatchmentBalance['O_CumDebitPredMP'] = [
            float(self.O_CumDebitPredMP_1.text()),
            float(self.O_CumDebitPredMP_2.text()),
            float(self.O_CumDebitPredMP_3.text())]
        subcatchmentBalance['O_CumBaseFlowMP'] = [
            float(self.O_CumBaseFlowMP_1.text()),
            float(self.O_CumBaseFlowMP_2.text()),
            float(self.O_CumBaseFlowMP_3.text())]
        subcatchmentBalance['O_CumDebitDataMP'] = [
            float(self.O_CumDebitDataMP_1.text()),
            float(self.O_CumDebitDataMP_1.text()),
            float(self.O_CumDebitDataMP_1.text())]
        self.parameters['Subcatchment Balance'] = subcatchmentBalance

    def _get_input_data(self):
        xl_workbook = xlrd.open_workbook(self.inputData.text())
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
        self.data.update(iDailyRain)
        self.data.update(iRFlowData)
        self.data.update(iDailyETYear)
        self.data.update(iDailyEvap)
        self.data['I_InputDataYears'] = wksheet.col_values(
            colx=26,
            start_rowx=4,
            end_rowx=8)
        self.data['I_InterceptClass'] = wksheet.col_values(
            colx=28,
            start_rowx=4,
            end_rowx=15)
        self.data['I_RelDroughtFact'] = wksheet.col_values(
            colx=29,
            start_rowx=4,
            end_rowx=15)
        self.data['I_Area'] = wksheet.col_values(
            colx=50,
            start_rowx=4,
            end_rowx=24)
        self.data['I_RoutingDistance'] = utils.read_table_to_matrix(
            wksheet,
            col_start=52,
            col_end=58,
            row_start=4,
            row_end=24
        )
        self.data['I_RivFlowTime1'] = wksheet.col_values(
            colx=58,
            start_rowx=4,
            end_rowx=24)
        self.data['I_MaxDynGWSub1'] = wksheet.col_values(
            colx=59,
            start_rowx=4,
            end_rowx=24)
        self.data['I_GWRelFrac1'] = wksheet.col_values(
            colx=60,
            start_rowx=4,
            end_rowx=24)
        self.data['I_RivFlowTime2'] = wksheet.col_values(
            colx=61,
            start_rowx=4,
            end_rowx=24)
        self.data['I_MaxDynGWSub2'] = wksheet.col_values(
            colx=62,
            start_rowx=4,
            end_rowx=24)
        self.data['I_GWRelFrac2'] = wksheet.col_values(
            colx=63,
            start_rowx=4,
            end_rowx=24)
        self.data['I_RivFlowTime3'] = wksheet.col_values(
            colx=64,
            start_rowx=4,
            end_rowx=24)
        self.data['I_MaxDynGWSub3'] = wksheet.col_values(
            colx=65,
            start_rowx=4,
            end_rowx=24)
        self.data['I_GWRelFrac3'] = wksheet.col_values(
            colx=66,
            start_rowx=4,
            end_rowx=24)
        self.data['I_RivFlowTime4'] = wksheet.col_values(
            colx=67,
            start_rowx=4,
            end_rowx=24)
        self.data['I_MaxDynGWSub4'] = wksheet.col_values(
            colx=68,
            start_rowx=4,
            end_rowx=24)
        self.data['I_GWRelFrac4'] = wksheet.col_values(
            colx=69,
            start_rowx=4,
            end_rowx=24)
        self.data['I_SoilSatMinFCSub1'] = wksheet.col_values(
            colx=70,
            start_rowx=4,
            end_rowx=24)
        self.data['I_PlantAvWatSub1'] = wksheet.col_values(
            colx=71,
            start_rowx=4,
            end_rowx=24)
        self.data['I_PWPSub1'] = wksheet.col_values(
            colx=72,
            start_rowx=4,
            end_rowx=24)
        self.data['I_SoilSatMinFCSub2'] = wksheet.col_values(
            colx=73,
            start_rowx=4,
            end_rowx=24)
        self.data['I_PlantAvWatSub2'] = wksheet.col_values(
            colx=74,
            start_rowx=4,
            end_rowx=24)
        self.data['I_PWPSub2'] = wksheet.col_values(
            colx=75,
            start_rowx=4,
            end_rowx=24)
        self.data['I_SoilSatMinFCSub3'] = wksheet.col_values(
            colx=76,
            start_rowx=4,
            end_rowx=24)
        self.data['I_PlantAvWatSub3'] = wksheet.col_values(
            colx=77,
            start_rowx=4,
            end_rowx=24)
        self.data['I_PWPSub3'] = wksheet.col_values(
            colx=78,
            start_rowx=4,
            end_rowx=24)
        self.data['I_SoilSatMinFCSub4'] = wksheet.col_values(
            colx=79,
            start_rowx=4,
            end_rowx=24)
        self.data['I_PlantAvWatSub4'] = wksheet.col_values(
            colx=80,
            start_rowx=4,
            end_rowx=24)
        self.data['I_PWPSub4'] = wksheet.col_values(
            colx=81,
            start_rowx=4,
            end_rowx=24)
        self.data['I_TopSoilBD_BDRef1'] = wksheet.col_values(
            colx=82,
            start_rowx=4,
            end_rowx=24)
        self.data['I_TopSoilBD_BDRef2'] = wksheet.col_values(
            colx=83,
            start_rowx=4,
            end_rowx=24)
        self.data['I_TopSoilBD_BDRef3'] = wksheet.col_values(
            colx=84,
            start_rowx=4,
            end_rowx=24)
        self.data['I_TopSoilBD_BDRef4'] = wksheet.col_values(
            colx=85,
            start_rowx=4,
            end_rowx=24)
        self.data['I_AvailWatSub1'] = wksheet.col_values(
            colx=86,
            start_rowx=4,
            end_rowx=24)
        self.data['I_AvailWatSub2'] = wksheet.col_values(
            colx=87,
            start_rowx=4,
            end_rowx=24)
        self.data['I_AvailWatSub3'] = wksheet.col_values(
            colx=88,
            start_rowx=4,
            end_rowx=24)
        self.data['I_AvailWatSub4'] = wksheet.col_values(
            colx=89,
            start_rowx=4,
            end_rowx=24)
        self.data['I_Evapotrans'] = wksheet.col_values(
            colx=31,
            start_rowx=4,
            end_rowx=16
        )
        self.data['I_MultiplierEvapoTrans'] = utils.read_table_to_matrix(
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
        self.data.update(ifracData)
        del xl_workbook

    def _prepare_display(self):
        self.main_frame = self.displayResult
        self.fig = Figure((1.0, 1.0), dpi=60)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.main_frame)
        self.canvas.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.canvas.setFocus()
        self.canvas.setSizePolicy(
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Expanding)
        self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)
        # self.canvas.mpl_connect('key_press_event', self.on_key_press)
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.canvas)
        vbox.addWidget(self.mpl_toolbar)
        self.main_frame.setLayout(vbox)

    def _display_timeseries(self):
        self.fig.clear()
        screen_position = [221, 222, 223, 224]
        for index, array_specs in enumerate(self.output_data):
            if self.output:
                array = self.output[array_specs]
                self.axes = self.fig.add_subplot(screen_position[index])
                # self.axes.set_xlim(0, len(array) - 1)
                self.axes.set_ylim(0, max(array) * 1.1)
                self.axes.set_autoscale_on(True)
                self.axes.plot(array, linestyle='steps-post')
                self.axes.set_xlabel('year')
                self.canvas.draw()

    def _run(self):
        self._get_input()
        # self._get_simulation_file()
        # self._get_data_file()
        self.simulation_module = imp.load_source('model', self.simulation_file)
        self.simulation = self.simulation_module.SimulatingThread(
            parameters=self.parameters,
            data=self.data
        )
        self.connect(self.simulation, QtCore.SIGNAL("update"),
                     self.update_result)
        self.simulation.start()

    def update_result(self, output, time):
        self.output = output
        # self._display_timeseries()
        self.dayProgress.display(time)
        self.yearProgress.display(time/365)
        if time % 100 == 0:
            self._display_timeseries()
        print 'simulating ', time


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    form = StellaUI()
    form.show()
    # form.run()
    app.exec_()