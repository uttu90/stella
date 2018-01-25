from PyQt4 import QtCore
import numpy as np
from utils import np_utils
from utils import excel_utils
import spatrain
import calculate
import constants
import xlwt


class SimulatingThread(QtCore.QThread):
    def __init__(self, parameters, data):
        super(SimulatingThread, self).__init__()
        self.stopped = False
        self.parameters = parameters
        self.data = data
        self.output = dict()
        self.output['map'] = {}
        self.output['timeseries'] = {}

        self.outputWb = xlwt.Workbook()
        self.waterBalanceSheet = self.outputWb.add_sheet('Water Balance')
        self.heppSheet = self.outputWb.add_sheet('HEPP')
        # self.sheet = self.outputWb.add_sheet('outputData')
        # simulationTime = 10000
        self.simulationTime = int(self.parameters['Run_Specs']['runto'])
        for mapName in constants.outputMap:
            self.output['map'][mapName] = np.empty(self.simulationTime, dtype=object)
        for timeseries in constants.outputTimeseries:
            self.output['timeseries'][timeseries] = np.empty(self.simulationTime)

    def __del__(self):
        print 'end'
        self.wait()

    def stop(self):
        self.stopped = True
        print "stop triggered"


    def run(self):
        run_specs = self.parameters['Run_Specs']
        begin = int(run_specs['runfrom'])
        # simulationTime = int(run_specs['runto'])
        dt = int(run_specs['rundt'])
        obsPoint = 8
        vegClass = 20
        measurePeriod = 3
        subcatchment = 20
        # print self.stopped
        self.stopped = False
        initial_run = self.parameters['Initial_Run']
        # simulationTime = int(initial_run['simulationTime'])
        I_StartMYear = [
            int(initial_run['I_StartMYear_1']),
            int(initial_run['I_StartMYear_2']),
            int(initial_run['I_StartMYear_3']),
        ]
        I_StartDOYear = [
            int(initial_run['I_StartDOY_1']),
            int(initial_run['I_StartDOY_2']),
            int(initial_run['I_StartDOY_3']),
        ]
        I_RainYearStar = int(initial_run['I_RainYearStart'])
        I_CaDOYearStar = int(initial_run['I_CaDOYStart'])
        I_WarmUpTime = int(initial_run['I_WarmUpTime'])
        O_MPeriodLength_ = [
            int(initial_run['O_MPeriodLength_1']),
            int(initial_run['O_MPeriodLength_2']),
            int(initial_run['O_MPeriodLength_3']),
        ]
        O_MPeriodLength = np.array(O_MPeriodLength_).reshape(measurePeriod, 1)
        rainfall = self.parameters['Rainfall']
        isI_UseSpatVarRain = int(rainfall['isI_UseSpatVarRain'])
        I_RainMultiplier = int(rainfall['I_RainMultiplier'])
        isI_RainCycle = int(rainfall['isI_RainCycle'])
        I_Rain_IntensMean = int(rainfall['I_Rain_IntensMean'])
        I_Rain_IntensCoefVar = float(rainfall['I_Rain_IntensCoefVar'])
        I_Rain_GenSeed = int(rainfall['I_Rain_GenSeed'])

        river = self.parameters['River']
        I_RoutVeloc_m_per_s = float(river['I_RoutVelocm_per_s'])
        I_Tortuosity = float(river['I_Tortuosity'])
        I_RiverflowDispersalFactor = float(river['I_RiverflowDispersalFactor'])
        I_SurfLossFrac = float(river['I_SurfLossFrac'])
        isI_DaminThisStream = np.array(
            [
                int(river['isDamThisStream_A']),
                int(river['isDamThisStream_B']),
                int(river['isDamThisStream_C']),
                int(river['isDamThisStream_D']),
                int(river['isDamThisStream_E']),
                int(river['isDamThisStream_F']),
                int(river['isDamThisStream_G']),
                int(river['isDamThisStream_H']),
                int(river['isDamThisStream_I']),
                int(river['isDamThisStream_J']),
                int(river['isDamThisStream_K']),
                int(river['isDamThisStream_L']),
                int(river['isDamThisStream_M']),
                int(river['isDamThisStream_N']),
                int(river['isDamThisStream_O']),
                int(river['isDamThisStream_P']),
                int(river['isDamThisStream_Q']),
                int(river['isDamThisStream_R']),
                int(river['isDamThisStream_S']),
                int(river['isDamThisStream_T']),
            ]
        ).reshape(subcatchment, 1)

        soilAndWaterBalance = self.parameters['Soil_and_Plant_Water']
        I_MaxInf = float(soilAndWaterBalance['I_MaxInf'])
        I_MaxInfSoil = float(soilAndWaterBalance['I_MaxInfSoil'])
        I_PowerInfiltRed = float(soilAndWaterBalance['I_PowerInfiltRed'])
        isI_SoilPropConst = float(soilAndWaterBalance['isI_SoilPropConst'])
        I_AvailWaterClassConst = float(
            soilAndWaterBalance['I_AvailQaterClassConst']
        )
        I_SoilSatMinFCConst = float(soilAndWaterBalance['I_SoilSatMinFCConst'])
        I_InitRelGW = float(soilAndWaterBalance['I_InitRelGW'])
        isI_GWRelFracConst = float(soilAndWaterBalance['isI_GWRelFracConst'])
        I_MaxDynGWConst = float(soilAndWaterBalance['I_MaxDynGWConst'])
        I_GWRelFracConst = float(soilAndWaterBalance['I_GWRelFracConst'])
        I_IntercepEffectionTransp = float(
            soilAndWaterBalance['I_IntercepEffectionTransp']
        )
        I_RainIntercDripRt = float(soilAndWaterBalance['I_RainIntercDripRt'])
        I_RainMaxIntDripDur = float(soilAndWaterBalance['I_RainMaxIntDripDur'])
        I_PercFracMultiplier = float(
            soilAndWaterBalance['I_PercFracMultiplier']
        )
        I_InitRelSoil = float(soilAndWaterBalance['I_InitRelSoil'])
        I_EvapotransMethod = float(soilAndWaterBalance['I_EvapotransMethod'])
        I_SoilQflowFract = float(soilAndWaterBalance['I_SoilQflowFract'])

        lake = self.parameters['Lake']
        isL_Lake = np.array(
            [
                float(lake['isL_Lake_A']),
                float(lake['isL_Lake_B']),
                float(lake['isL_Lake_C']),
                float(lake['isL_Lake_D']),
                float(lake['isL_Lake_E']),
                float(lake['isL_Lake_F']),
                float(lake['isL_Lake_G']),
                float(lake['isL_Lake_H']),
                float(lake['isL_Lake_I']),
                float(lake['isL_Lake_J']),
                float(lake['isL_Lake_K']),
                float(lake['isL_Lake_L']),
                float(lake['isL_Lake_M']),
                float(lake['isL_Lake_N']),
                float(lake['isL_Lake_O']),
                float(lake['isL_Lake_P']),
                float(lake['isL_Lake_Q']),
                float(lake['isL_Lake_R']),
                float(lake['isL_Lake_S']),
                float(lake['isL_Lake_T']),
            ]
        ).reshape(subcatchment, 1)
        isL_HEPP_Active = float(lake['isL_HEPP_Active'])
        l_LakeTransMultiplier = float(lake['L_LakeTransMultiplier'])
        l_LakeBottomElev = float(lake['L_LakeBottomElev'])
        l_LakeElevPreHEPP = float(lake['L_LakeElevPreHEPP'])
        l_LakeOverFIPostHEPP = float(lake['L_LakeOverFIPostHEPP'])
        l_LakeLevelFullHEPP = float(lake['L_LakeLevelFullHEPP'])
        l_LakeLevelHalfHEPP = float(lake['L_LakeLevelHalfHEPP'])
        l_LakeLevelNoHEPP = float(lake['L_LakeLevelNoHEPP'])
        l_LakeFloodTresh = float(lake['L_LakeFloodTresh'])
        l_LakeQmecsHEPP = float(lake['L_LakeQmecsHEPP'])
        l_LakeQmecsSanFlow = float(lake['L_LakeQmecsSanFlow'])
        l_LakeOverFlowFract = float(lake['L_LakeOverFlowFract'])
        l_LakeOverFIFlow = float(lake['L_LakeOverFIFlow'])
        l_m3_per_kwh = float(lake['L_m3_per_kwh'])
        l_ResrDepth = float(lake['L_ResrDepth'])

        lake_hepp = self.parameters['Lake_HEPP']
        o_CumRivInflowtoLakeMP = [
            float(lake_hepp['O_CumRivInflowtoLakeMP_1']),
            float(lake_hepp['O_CumRivInflowtoLakeMP_2']),
            float(lake_hepp['O_CumRivInflowtoLakeMP_3']),
        ]
        o_CumRivOutFlowMP = [
            float(lake_hepp['O_CumRivOutFlowMP_1']),
            float(lake_hepp['O_CumRivOutFlowMP_2']),
            float(lake_hepp['O_CumRivOutFlowMP_3']),
        ]
        o_HEPP_Kwh_per_dayMP = [
            float(lake_hepp['O_HEPP_Kwh_per_dayMP_1']),
            float(lake_hepp['O_HEPP_Kwh_per_dayMP_2']),
            float(lake_hepp['O_HEPP_Kwh_per_dayMP_3']),
        ]
        o_CumHEPPOutFlowMP = [
            float(lake_hepp['O_CumHEPPOutFlowMP_1']),
            float(lake_hepp['O_CumHEPPOutFlowMP_2']),
            float(lake_hepp['O_CumHEPPOutFlowMP_3']),
        ]
        o_RelOPTimeHEPPMP = [
            float(lake_hepp['O_RelOPTimeHEPPMP_1']),
            float(lake_hepp['O_RelOPTimeHEPPMP_2']),
            float(lake_hepp['O_RelOPTimeHEPPMP_3']),
        ]
        o_FrBaseFlow = float(lake_hepp['O_FrBaseFlow'])
        o_FrSoilQuickFlow = float(lake_hepp['O_FrSoilQuickFlow'])
        o_FrSurfQuickFlow = float(lake_hepp['O_FrSurfQuickflow'])

        grassAndCattle = self.parameters['Grass_and_Cattle']
        c_DailyTrampFac = float(grassAndCattle['C_DailyTramFac'])
        c_CattleSale = float(grassAndCattle['C_CattleSale'])
        c_DailyIntake = float(grassAndCattle['C_DailyIntake'])
        c_GrazingManConv = float(grassAndCattle['C_GrazingManConv'])
        c_SurfLitDecFrac = float(grassAndCattle['C_SurfLitDecFrac'])
        c_SurfManureDecFrac = float(grassAndCattle['C_SurfManureDecFrac'])
        c_GrassLitConv = float(grassAndCattle['C_GrassLitConv'])
        c_GrassLitMortFrac = float(grassAndCattle['C_GrassLitMortFrac'])
        g_WUE = float(grassAndCattle['G_WUE'])
        g_TramplingMultiplier = float(grassAndCattle['G_TramplingMultiplier'])

        soilStructureDynamic = self.parameters['Soil_Structure_Dynamic']
        s_TrampMax = float(soilStructureDynamic['S_TrampMax'])

        subcatchmentBalance = self.parameters['Subcatchment_Balance']
        o_CumRainMP = [
            float(subcatchmentBalance['O_CumRainMP_1']),
            float(subcatchmentBalance['O_CumRainMP_2']),
            float(subcatchmentBalance['O_CumRainMP_3']),
        ]
        o_CumIntercEvapMP = [
            float(subcatchmentBalance['O_CumIntercEvapMP_1']),
            float(subcatchmentBalance['O_CumIntercEvapMP_2']),
            float(subcatchmentBalance['O_CumIntercEvapMP_3']),
        ]
        o_CumTranspMP = [
            float(subcatchmentBalance['O_CumTranspMP_1']),
            float(subcatchmentBalance['O_CumTranspMP_2']),
            float(subcatchmentBalance['O_CumTranspMP_3']),
        ]
        o_CumETLandMP = [
            float(subcatchmentBalance['O_CumETLandMP_1']),
            float(subcatchmentBalance['O_CumETLandMP_2']),
            float(subcatchmentBalance['O_CumETLandMP_3']),
        ]
        o_CumEvapTransMP = [
            float(subcatchmentBalance['O_CumEvapTranspMP_1']),
            float(subcatchmentBalance['O_CumEvapTranspMP_2']),
            float(subcatchmentBalance['O_CumEvapTranspMP_3']),
        ]
        o_CumSurfQFlow = [
            float(subcatchmentBalance['O_CumSurfQFlow_1']),
            float(subcatchmentBalance['O_CumSurfQFlow_2']),
            float(subcatchmentBalance['O_CumSurfQFlow_3']),
        ]
        o_CumInfiltrationMP = [
            float(subcatchmentBalance['O_CumInfiltrationMP_1']),
            float(subcatchmentBalance['O_CumInfiltrationMP_2']),
            float(subcatchmentBalance['O_CumInfiltrationMP_3'])
        ]
        o_CumSoilQFlowMP = [
            float(subcatchmentBalance['O_CumSoilQFlowMP_1']),
            float(subcatchmentBalance['O_CumSoilQFlowMP_2']),
            float(subcatchmentBalance['O_CumSoilQFlowMP_3'])
        ]
        o_CumDebitPredMP = [
            float(subcatchmentBalance['O_CumDebitPredMP_1']),
            float(subcatchmentBalance['O_CumDebitPredMP_2']),
            float(subcatchmentBalance['O_CumDebitPredMP_3']),
        ]
        o_CumBaseFlowMP = [
            float(subcatchmentBalance['O_CumBaseFlowMP_1']),
            float(subcatchmentBalance['O_CumBaseFlowMP_2']),
            float(subcatchmentBalance['O_CumBaseFlowMP_3']),
        ]
        o_CumDebitDataMP = [
            float(subcatchmentBalance['O_CumDebitDataMP_1']),
            float(subcatchmentBalance['O_CumDebitDataMP_2']),
            float(subcatchmentBalance['O_CumDebitDataMP_3']),
        ]

        # Loading data

        I_Evapotrans = [0] + self.data['I_Evapotrans']
        # print I_Evapotrans
        insert_value = [0 for _ in range(12)]
        I_MultiplierEvapoTrans = np.array(self.data['I_MultiplierEvapoTrans'])

        I_MultiplierEvapoTrans = [np.zeros(shape=(1, vegClass))] + [
            I_MultiplierEvapoTrans[_].reshape(1, vegClass)
            for _ in range(12)
        ]
        I_Frac_1_1 = np.array(
            self.data['I_Frac1_1']
        ).reshape(subcatchment, 1)
        I_Frac_2_1 = np.array(
            self.data['I_Frac2_1']
        ).reshape(subcatchment, 1)
        I_Frac_3_1 = np.array(
            self.data['I_Frac3_1']
        ).reshape(subcatchment, 1)
        I_Frac_4_1 = np.array(
            self.data['I_Frac4_1']
        ).reshape(subcatchment, 1)
        I_Frac_5_1 = np.array(
            self.data['I_Frac5_1']
        ).reshape(subcatchment, 1)
        I_Frac_6_1 = np.array(
            self.data['I_Frac6_1']
        ).reshape(subcatchment, 1)
        I_Frac_7_1 = np.array(
            self.data['I_Frac7_1']
        ).reshape(subcatchment, 1)
        I_Frac_8_1 = np.array(
            self.data['I_Frac8_1']
        ).reshape(subcatchment, 1)
        I_Frac_9_1 = np.array(
            self.data['I_Frac9_1']
        ).reshape(subcatchment, 1)
        I_Frac_10_1 = np.array(
            self.data['I_Frac10_1']
        ).reshape(subcatchment, 1)
        I_Frac_11_1 = np.array(
            self.data['I_Frac11_1']
        ).reshape(subcatchment, 1)
        I_Frac_12_1 = np.array(
            self.data['I_Frac12_1']
        ).reshape(subcatchment, 1)
        I_Frac_13_1 = np.array(
            self.data['I_Frac13_1']
        ).reshape(subcatchment, 1)
        I_Frac_14_1 = np.array(
            self.data['I_Frac14_1']
        ).reshape(subcatchment, 1)
        I_Frac_15_1 = np.array(
            self.data['I_Frac15_1']
        ).reshape(subcatchment, 1)
        I_Frac_16_1 = np.array(
            self.data['I_Frac16_1']
        ).reshape(subcatchment, 1)
        I_Frac_17_1 = np.array(
            self.data['I_Frac17_1']
        ).reshape(subcatchment, 1)
        I_Frac_18_1 = np.array(
            self.data['I_Frac18_1']
        ).reshape(subcatchment, 1)
        I_Frac_19_1 = np.array(
            self.data['I_Frac19_1']
        ).reshape(subcatchment, 1)
        I_Frac_20_1 = np.array(
            self.data['I_Frac20_1']
        ).reshape(subcatchment, 1)
        I_FracVegClass_1 = np.column_stack((
            I_Frac_1_1,
            I_Frac_2_1,
            I_Frac_3_1,
            I_Frac_4_1,
            I_Frac_5_1,
            I_Frac_6_1,
            I_Frac_7_1,
            I_Frac_8_1,
            I_Frac_9_1,
            I_Frac_10_1,
            I_Frac_11_1,
            I_Frac_12_1,
            I_Frac_13_1,
            I_Frac_14_1,
            I_Frac_15_1,
            I_Frac_16_1,
            I_Frac_17_1,
            I_Frac_18_1,
            I_Frac_19_1,
            I_Frac_20_1
        ))
        # print I_FracVegClass_1
        I_Frac_1_2 = np.array(
            self.data['I_Frac1_2']
        ).reshape(subcatchment, 1)
        I_Frac_2_2 = np.array(
            self.data['I_Frac2_2']
        ).reshape(subcatchment, 1)
        I_Frac_3_2 = np.array(
            self.data['I_Frac3_2']
        ).reshape(subcatchment, 1)
        I_Frac_4_2 = np.array(
            self.data['I_Frac4_2']
        ).reshape(subcatchment, 1)
        I_Frac_5_2 = np.array(
            self.data['I_Frac5_2']
        ).reshape(subcatchment, 1)
        I_Frac_6_2 = np.array(
            self.data['I_Frac6_2']
        ).reshape(subcatchment, 1)
        I_Frac_7_2 = np.array(
            self.data['I_Frac7_2']
        ).reshape(subcatchment, 1)
        I_Frac_8_2 = np.array(
            self.data['I_Frac8_2']
        ).reshape(subcatchment, 1)
        I_Frac_9_2 = np.array(
            self.data['I_Frac9_2']
        ).reshape(subcatchment, 1)
        I_Frac_10_2 = np.array(
            self.data['I_Frac10_2']
        ).reshape(subcatchment, 1)
        I_Frac_11_2 = np.array(
            self.data['I_Frac11_2']
        ).reshape(subcatchment, 1)
        I_Frac_12_2 = np.array(
            self.data['I_Frac12_2']
        ).reshape(subcatchment, 1)
        I_Frac_13_2 = np.array(
            self.data['I_Frac13_2']
        ).reshape(subcatchment, 1)
        I_Frac_14_2 = np.array(
            self.data['I_Frac14_2']
        ).reshape(subcatchment, 1)
        I_Frac_15_2 = np.array(
            self.data['I_Frac15_2']
        ).reshape(subcatchment, 1)
        I_Frac_16_2 = np.array(
            self.data['I_Frac16_2']
        ).reshape(subcatchment, 1)
        I_Frac_17_2 = np.array(
            self.data['I_Frac17_2']
        ).reshape(subcatchment, 1)
        I_Frac_18_2 = np.array(
            self.data['I_Frac18_2']
        ).reshape(subcatchment, 1)
        I_Frac_19_2 = np.array(
            self.data['I_Frac19_2']
        ).reshape(subcatchment, 1)
        I_Frac_20_2 = np.array(
            self.data['I_Frac20_2']
        ).reshape(subcatchment, 1)
        I_FracVegClass_2 = np.column_stack((
            I_Frac_1_2,
            I_Frac_2_2,
            I_Frac_3_2,
            I_Frac_4_2,
            I_Frac_5_2,
            I_Frac_6_2,
            I_Frac_7_2,
            I_Frac_8_2,
            I_Frac_9_2,
            I_Frac_10_2,
            I_Frac_11_2,
            I_Frac_12_2,
            I_Frac_13_2,
            I_Frac_14_2,
            I_Frac_15_2,
            I_Frac_16_2,
            I_Frac_17_2,
            I_Frac_18_2,
            I_Frac_19_2,
            I_Frac_20_2
        ))

        I_Frac_1_3 = np.array(
            self.data['I_Frac1_3']
        ).reshape(subcatchment, 1)
        I_Frac_2_3 = np.array(
            self.data['I_Frac2_3']
        ).reshape(subcatchment, 1)
        I_Frac_3_3 = np.array(
            self.data['I_Frac3_3']
        ).reshape(subcatchment, 1)
        I_Frac_4_3 = np.array(
            self.data['I_Frac4_3']
        ).reshape(subcatchment, 1)
        I_Frac_5_3 = np.array(
            self.data['I_Frac5_3']
        ).reshape(subcatchment, 1)
        I_Frac_6_3 = np.array(
            self.data['I_Frac6_3']
        ).reshape(subcatchment, 1)
        I_Frac_7_3 = np.array(
            self.data['I_Frac7_3']
        ).reshape(subcatchment, 1)
        I_Frac_8_3 = np.array(
            self.data['I_Frac8_3']
        ).reshape(subcatchment, 1)
        I_Frac_9_3 = np.array(
            self.data['I_Frac9_3']
        ).reshape(subcatchment, 1)
        I_Frac_10_3 = np.array(
            self.data['I_Frac10_3']
        ).reshape(subcatchment, 1)
        I_Frac_11_3 = np.array(
            self.data['I_Frac11_3']
        ).reshape(subcatchment, 1)
        I_Frac_12_3 = np.array(
            self.data['I_Frac12_3']
        ).reshape(subcatchment, 1)
        I_Frac_13_3 = np.array(
            self.data['I_Frac13_3']
        ).reshape(subcatchment, 1)
        I_Frac_14_3 = np.array(
            self.data['I_Frac14_3']
        ).reshape(subcatchment, 1)
        I_Frac_15_3 = np.array(
            self.data['I_Frac15_3']
        ).reshape(subcatchment, 1)
        I_Frac_16_3 = np.array(
            self.data['I_Frac16_3']
        ).reshape(subcatchment, 1)
        I_Frac_17_3 = np.array(
            self.data['I_Frac17_3']
        ).reshape(subcatchment, 1)
        I_Frac_18_3 = np.array(
            self.data['I_Frac18_3']
        ).reshape(subcatchment, 1)
        I_Frac_19_3 = np.array(
            self.data['I_Frac19_3']
        ).reshape(subcatchment, 1)
        I_Frac_20_3 = np.array(
            self.data['I_Frac20_3']
        ).reshape(subcatchment, 1)
        I_FracVegClass_3 = np.column_stack((
            I_Frac_1_3,
            I_Frac_2_3,
            I_Frac_3_3,
            I_Frac_4_3,
            I_Frac_5_3,
            I_Frac_6_3,
            I_Frac_7_3,
            I_Frac_8_3,
            I_Frac_9_3,
            I_Frac_10_3,
            I_Frac_11_3,
            I_Frac_12_3,
            I_Frac_13_3,
            I_Frac_14_3,
            I_Frac_15_3,
            I_Frac_16_3,
            I_Frac_17_3,
            I_Frac_18_3,
            I_Frac_19_3,
            I_Frac_20_3
        ))

        I_Frac_1_4 = np.array(
            self.data['I_Frac1_4']
        ).reshape(subcatchment, 1)
        I_Frac_2_4 = np.array(
            self.data['I_Frac2_4']
        ).reshape(subcatchment, 1)
        I_Frac_3_4 = np.array(
            self.data['I_Frac3_4']
        ).reshape(subcatchment, 1)
        I_Frac_4_4 = np.array(
            self.data['I_Frac4_4']
        ).reshape(subcatchment, 1)
        I_Frac_5_4 = np.array(
            self.data['I_Frac5_4']
        ).reshape(subcatchment, 1)
        I_Frac_6_4 = np.array(
            self.data['I_Frac6_4']
        ).reshape(subcatchment, 1)
        I_Frac_7_4 = np.array(
            self.data['I_Frac7_4']
        ).reshape(subcatchment, 1)
        I_Frac_8_4 = np.array(
            self.data['I_Frac8_4']
        ).reshape(subcatchment, 1)
        I_Frac_9_4 = np.array(
            self.data['I_Frac9_4']
        ).reshape(subcatchment, 1)
        I_Frac_10_4 = np.array(
            self.data['I_Frac10_4']
        ).reshape(subcatchment, 1)
        I_Frac_11_4 = np.array(
            self.data['I_Frac11_4']
        ).reshape(subcatchment, 1)
        I_Frac_12_4 = np.array(
            self.data['I_Frac12_4']
        ).reshape(subcatchment, 1)
        I_Frac_13_4 = np.array(
            self.data['I_Frac13_4']
        ).reshape(subcatchment, 1)
        I_Frac_14_4 = np.array(
            self.data['I_Frac14_4']
        ).reshape(subcatchment, 1)
        I_Frac_15_4 = np.array(
            self.data['I_Frac15_4']
        ).reshape(subcatchment, 1)
        I_Frac_16_4 = np.array(
            self.data['I_Frac16_4']
        ).reshape(subcatchment, 1)
        I_Frac_17_4 = np.array(
            self.data['I_Frac17_4']
        ).reshape(subcatchment, 1)
        I_Frac_18_4 = np.array(
            self.data['I_Frac18_4']
        ).reshape(subcatchment, 1)
        I_Frac_19_4 = np.array(
            self.data['I_Frac19_4']
        ).reshape(subcatchment, 1)
        I_Frac_20_4 = np.array(
            self.data['I_Frac20_4']
        ).reshape(subcatchment, 1)
        I_FracVegClass_4 = np.column_stack((
            I_Frac_1_4,
            I_Frac_2_4,
            I_Frac_3_4,
            I_Frac_4_4,
            I_Frac_5_4,
            I_Frac_6_4,
            I_Frac_7_4,
            I_Frac_8_4,
            I_Frac_9_4,
            I_Frac_10_4,
            I_Frac_11_4,
            I_Frac_12_4,
            I_Frac_13_4,
            I_Frac_14_4,
            I_Frac_15_4,
            I_Frac_16_4,
            I_Frac_17_4,
            I_Frac_18_4,
            I_Frac_19_4,
            I_Frac_20_4
        ))

        I_FracVegClasses = [
            I_FracVegClass_1,
            I_FracVegClass_2,
            I_FracVegClass_3,
            I_FracVegClass_4
        ]

        I_GWRelFrac1 = np.array(
            self.data['I_GWRelFrac1']
        ).reshape(subcatchment, 1)
        I_GWRelFrac2 = np.array(
            self.data['I_GWRelFrac2']
        ).reshape(subcatchment, 1)
        I_GWRelFrac3 = np.array(
            self.data['I_GWRelFrac3']
        ).reshape(subcatchment, 1)
        I_GWRelFrac4 = np.array(
            self.data['I_GWRelFrac4']
        ).reshape(subcatchment, 1)

        I_GWRelFracs = [
            I_GWRelFrac1,
            I_GWRelFrac2,
            I_GWRelFrac3,
            I_GWRelFrac4
        ]

        I_MaxDynGWSub1 = np.array(
            self.data['I_MaxDynGWSub1']
        ).reshape(subcatchment, 1)
        I_MaxDynGWSub2 = np.array(
            self.data['I_MaxDynGWSub2']
        ).reshape(subcatchment, 1)
        I_MaxDynGWSub3 = np.array(
            self.data['I_MaxDynGWSub3']
        ).reshape(subcatchment, 1)
        I_MaxDynGWSub4 = np.array(
            self.data['I_MaxDynGWSub4']
        ).reshape(subcatchment, 1)

        I_MaxDynGWSubs = [
            I_MaxDynGWSub1,
            I_MaxDynGWSub2,
            I_MaxDynGWSub3,
            I_MaxDynGWSub4
        ]

        I_PWPSub1 = np.array(
            self.data['I_PWPSub1']
        ).reshape(subcatchment, 1)
        I_PWPSub2 = np.array(
            self.data['I_PWPSub2']
        ).reshape(subcatchment, 1)
        I_PWPSub3 = np.array(
            self.data['I_PWPSub3']
        ).reshape(subcatchment, 1)
        I_PWPSub4 = np.array(
            self.data['I_PWPSub4']
        ).reshape(subcatchment, 1)
        I_PWPSubs = [I_PWPSub1, I_PWPSub2, I_PWPSub3, I_PWPSub4]

        I_PlantAvWatSub1 = np.array(
            self.data['I_PlantAvWatSub1']
        ).reshape(subcatchment, 1)
        I_PlantAvWatSub2 = np.array(
            self.data['I_PlantAvWatSub2']
        ).reshape(subcatchment, 1)
        I_PlantAvWatSub3 = np.array(
            self.data['I_PlantAvWatSub3']
        ).reshape(subcatchment, 1)
        I_PlantAvWatSub4 = np.array(
            self.data['I_PlantAvWatSub4']
        ).reshape(subcatchment, 1)
        I_PlantAvWatSubs = [
            I_PlantAvWatSub1,
            I_PlantAvWatSub2,
            I_PlantAvWatSub3,
            I_PlantAvWatSub4]

        I_SoilSatminFCSub1 = np.array(
            self.data['I_SoilSatMinFCSub1']
        ).reshape(subcatchment, 1)
        I_SoilSatminFCSub2 = np.array(
            self.data['I_SoilSatMinFCSub2']
        ).reshape(subcatchment, 1)
        I_SoilSatminFCSub3 = np.array(
            self.data['I_SoilSatMinFCSub3']
        ).reshape(subcatchment, 1)
        I_SoilSatminFCSub4 = np.array(
            self.data['I_SoilSatMinFCSub4']
        ).reshape(subcatchment, 1)
        I_SoilSatminFCSubs = [
            I_SoilSatminFCSub1,
            I_SoilSatminFCSub2,
            I_SoilSatminFCSub3,
            I_SoilSatminFCSub4,
        ]

        I_RivFlowTime1 = np.array(
            self.data['I_RivFlowTime1']
        ).reshape(subcatchment, 1)
        I_RivFlowTime2 = np.array(
            self.data['I_RivFlowTime2']
        ).reshape(subcatchment, 1)
        I_RivFlowTime3 = np.array(
            self.data['I_RivFlowTime3']
        ).reshape(subcatchment, 1)
        I_RivFlowTime4 = np.array(
            self.data['I_RivFlowTime4']
        ).reshape(subcatchment, 1)
        I_RivFlowTimes = [
            I_RivFlowTime1,
            I_RivFlowTime2,
            I_RivFlowTime3,
            I_RivFlowTime4
        ]

        # I_AvailWatSub1 = np.array(
        #     self.data['I_AvailWatSub1']
        # ).reshape(subcatchment, 1)
        # I_AvailWatSub2 = np.array(
        #     self.data['I_AvailWatSub2']
        # ).reshape(subcatchment, 1)
        # I_AvailWatSub3 = np.array(
        #     self.data['I_AvailWatSub3']
        # ).reshape(subcatchment, 1)
        # I_AvailWatSub4 = np.array(
        #     self.data['I_AvailWatSub4']
        # ).reshape(subcatchment, 1)
        # I_AvailWatSubs = [
        #     I_AvailWatSub1,
        #     I_AvailWatSub2,
        #     I_AvailWatSub3,
        #     I_AvailWatSub4
        # ]

        I_TopSoilBD_BDRef1 = np.array(
            self.data['I_TopSoilBD_BDRef1']
        ).reshape(subcatchment, 1)
        I_TopSoilBD_BDRef2 = np.array(
            self.data['I_TopSoilBD_BDRef2']
        ).reshape(subcatchment, 1)
        I_TopSoilBD_BDRef3 = np.array(
            self.data['I_TopSoilBD_BDRef3']
        ).reshape(subcatchment, 1)
        I_TopSoilBD_BDRef4 = np.array(
            self.data['I_TopSoilBD_BDRef4']
        ).reshape(subcatchment, 1)
        I_TopSoilBD_BDRefs = [
            I_TopSoilBD_BDRef1,
            I_TopSoilBD_BDRef2,
            I_TopSoilBD_BDRef3,
            I_TopSoilBD_BDRef4
        ]

        I_DailyRainYear_1_to_4 = self.data['I_DailyRainYear_1_to_4']
        I_DailyRainYear_5_to_8 = self.data['I_DailyRainYear_5_to_8']
        I_DailyRainYear_9_to_12 = self.data['I_DailyRainYear_9_to_12']
        I_DailyRainYear_13_to_16 = self.data['I_DailyRainYear_13_to_16']
        I_DailyRainYear_17_to_20 = self.data['I_DailyRainYear_17_to_20']
        I_DailyRainYear_21_to_24 = self.data['I_DailyRainYear_21_to_24']
        I_DailyRainYear_25_to_28 = self.data['I_DailyRainYear_25_to_28']
        I_DailyRainYear = (
            [0] +
            I_DailyRainYear_1_to_4 +
            I_DailyRainYear_5_to_8 +
            I_DailyRainYear_9_to_12 +
            I_DailyRainYear_13_to_16 +
            I_DailyRainYear_17_to_20 +
            I_DailyRainYear_21_to_24 +
            I_DailyRainYear_25_to_28
        )

        I_Daily_Evap_1_to_4 = self.data['I_Daily_Evap_1_to_4']
        I_Daily_Evap_5_to_8 = self.data['I_Daily_Evap_5_to_8']
        I_Daily_Evap_9_to_12 = self.data['I_Daily_Evap_9_to_12']
        I_Daily_Evap_13_to_16 = self.data['I_Daily_Evap_13_to_16']
        I_Daily_Evap_17_to_20 = self.data['I_Daily_Evap_17_to_20']
        I_Daily_Evap_21_to_24 = self.data['I_Daily_Evap_21_to_24']
        I_Daily_Evap_25_to_28 = self.data['I_Daily_Evap_25_to_28']
        I_Daily_Evap_29_to_32 = self.data['I_Daily_Evap_29_to_32']
        I_Daily_Evap = (
            [0] +
            I_Daily_Evap_1_to_4 +
            I_Daily_Evap_5_to_8 +
            I_Daily_Evap_9_to_12 +
            I_Daily_Evap_13_to_16 +
            I_Daily_Evap_17_to_20 +
            I_Daily_Evap_21_to_24 +
            I_Daily_Evap_25_to_28 +
            I_Daily_Evap_29_to_32
                        )

        I_RFlowData_Year_1_to_4 = self.data['I_RFlowData Year_1_to_4']
        I_RFlowData_Year_5_to_8 = self.data['I_RFlowData Year_5_to_8']
        I_RFlowData_Year_9_to_12 = self.data['I_RFlowData Year_9_to_12']
        I_RFlowData_Year_13_to_16 = self.data['I_RFlowData Year_13_to_16']
        I_RFlowData_Year_17_to_20 = self.data['I_RFlowData Year_17_to_20']
        I_RFlowData_Year_21_to_24 = self.data['I_RFlowData Year_21_to_24']
        I_RFlowData_Year_25_to_28 = self.data['I_RFlowData Year_25_to_28']
        I_RFlowData_Year_29_to_32 = self.data['I_RFlowDataYear_29_to_32']

        I_RFlowData = ([0] +
            I_RFlowData_Year_1_to_4 +
            I_RFlowData_Year_5_to_8 +
            I_RFlowData_Year_9_to_12 +
            I_RFlowData_Year_13_to_16 +
            I_RFlowData_Year_17_to_20 +
            I_RFlowData_Year_21_to_24 +
            I_RFlowData_Year_25_to_28 +
            I_RFlowData_Year_29_to_32
                       )
        # RainNormal = self.data['RainNormal']

        I_InputDataYears = self.data['I_InputDataYears']
        I_InterceptClass = np.array(
            self.data['I_InterceptClass']
        ).reshape(vegClass, 1)
        I_RelDroughtFact = np.array(
            self.data['I_RelDroughtFact']
        ).reshape(vegClass, 1)
        I_Area = np.array(
            self.data['I_Area']
        ).reshape(subcatchment, 1)
        # print I_Area
        I_RoutingDistanceLoad = np.array(
            self.data['I_RoutingDistance']
        )
        insert_value = [-1 for _ in range(20)]
        I_RoutingDistance = np.column_stack((
            I_RoutingDistanceLoad,
            insert_value,
        ))

        # Initial stock value

        time = begin
        C_StockingRate = 1
        D_InitLakeVol = 0
        D_InitRivVol = 0
        O_CumBaseFlow = 0
        O_CumDeepInfilt = 0
        O_CumEvapotrans = 0
        O_CumInfiltration = 0
        O_CumIntercE = 0
        O_CumIntercepEvap = 0
        O_CumPercolation = 0
        O_CumRain = 0
        O_CumSoilQFlow = 0
        O_CumSoilQFlow_Subca_1 = np.zeros(shape=(subcatchment, obsPoint))
        O_CumSurfQFlow = 0
        O_CumTransp = 0
        O_RainYest = np.zeros(shape=(subcatchment, 1))
        G_GrassStandingBiomass = np.ones(shape=(subcatchment, vegClass))
        G_SurfaceLitter = np.zeros(shape=(subcatchment, vegClass))
        G_SurfManure = np.zeros(shape=(subcatchment, vegClass))
        isI_WarmEdUp = 0
        O_CumDebitData = 0
        L_CumEvapLake = 0
        L_CumHEPPUse = 0
        L_CumRivOutFlow = 0
        I_TotalArea = np.sum(I_Area)
        I_RelArea = I_Area / I_TotalArea
        L_LakeArea = np.multiply(isL_Lake == 1, I_RelArea)
        L_LakeElevPreHEPP = 362.3
        L_LakeBottomElev = 160
        L_OutflTrVolPreHEPP = (1000 *
                               (L_LakeElevPreHEPP - L_LakeBottomElev) *
                               np_utils.array_sum(L_LakeArea))
        L_LakeVol = (L_OutflTrVolPreHEPP * isL_HEPP_Active +
                     (1 - isL_HEPP_Active) * L_OutflTrVolPreHEPP)
        O_BestYyHEPP = 0
        O_Ch_inGWStock = np.zeros(shape=(1, measurePeriod))
        O_Ch_inWStock = np.zeros(shape=(1, measurePeriod))
        O_CumBaseFlowMP = np.zeros(shape=(1, measurePeriod))
        O_CumDebitDataMP = np.zeros(shape=(1, measurePeriod))
        O_CumDebitPredMP = np.zeros(shape=(1, measurePeriod))
        O_CumEvapLakeMP = np.zeros(shape=(1, measurePeriod))
        O_CumEvapTransMP = np.zeros(shape=(1, measurePeriod))
        O_CumGWMP = np.zeros(shape=(1, measurePeriod))
        O_CumHEPPOutFlowMP = np.zeros(shape=(1, measurePeriod))
        O_CumInfiltrationMP = np.zeros(shape=(1, measurePeriod))
        O_CumIntercEvapMP = np.zeros(shape=(1, measurePeriod))
        O_CumRainMP = np.zeros(shape=(1, measurePeriod))
        O_CumRivInflowtoLakeMP = np.zeros(shape=(1, measurePeriod))
        O_CumRivOutFlowMP = np.zeros(shape=(1, measurePeriod))
        O_CumSoilQFlowMP = np.zeros(shape=(1, measurePeriod))
        O_CumSoilWMP = np.zeros(shape=(1, measurePeriod))
        O_CumSurfQFlowMP = np.zeros(shape=(1, measurePeriod))
        O_CumTranspMP = np.zeros(shape=(1, measurePeriod))
        O_DeltaCatchmStMP = np.zeros(shape=(1, measurePeriod))
        O_Hepp_Kwh_per_dayMP = np.zeros(shape=(1, measurePeriod))
        O_InitEvapoMP = np.zeros(shape=(1, measurePeriod))
        O_InitGWStockMP = np.zeros(shape=(1, measurePeriod))
        O_InitSWMP = np.zeros(shape=(1, measurePeriod))
        O_LastYHepp = 0
        O_ThisYHepp = 0
        O_WorstYHEPP = 1
        O_YearSim = 1
        D_CumEvapTranspClass = np.zeros(shape=(subcatchment, vegClass))
        D_CumNegRain = np.zeros(shape=(subcatchment, 1))
        D_EvapTranspClass = np.zeros(shape=(subcatchment, vegClass))
        I_InitMaxDynGWSub = I_MaxDynGWSub1
        I_MaxDynGWact = (np.multiply(isI_GWRelFracConst, I_MaxDynGWConst) +
                         np.multiply(1 - isI_GWRelFracConst, I_InitMaxDynGWSub))
        I_MaxDynGWArea = np.multiply(I_MaxDynGWact, I_RelArea)
        D_GWArea = I_MaxDynGWArea * I_InitRelGW
        O_InitGWStock = np_utils.array_sum(I_MaxDynGWArea) * I_InitRelGW
        I_InitPlantAvWat = I_PlantAvWatSub1
        I_InitFracVegClass = np.multiply(I_RelArea > 0, I_FracVegClass_1)
        I_AvailWaterConst = 300
        I_InitAvailWaterClass = (
            I_AvailWaterConst *
            np.multiply(I_InitFracVegClass, I_RelArea)
            if isI_SoilPropConst == 1
            else np.multiply(
                np.multiply(I_InitPlantAvWat,
                            I_InitFracVegClass),
                I_RelArea))
        O_InitSoilW = np_utils.array_sum(I_InitAvailWaterClass) * I_InitRelSoil
        D_SoilWater = I_InitAvailWaterClass * I_InitRelSoil
        I_InitBD_BDRefVeg = I_TopSoilBD_BDRef1
        S_RelBulkDensity = I_InitBD_BDRefVeg * np.ones(shape=(subcatchment, vegClass))
        D_CumInflowtoLake = 0
        D_CumTotRiverFlow = np.zeros(shape=(subcatchment, obsPoint))
        D_StreamsSurfQ = np.zeros(shape=(subcatchment, obsPoint))
        D_TotRiverFlowNoDelay = np.zeros(shape=(subcatchment, obsPoint))
        D_CumResvEvap = 0
        L_ResrDepth = 10000
        D_ReservoirVol = L_ResrDepth * np.multiply(isL_Lake, I_RelArea)
        D_SubcResVol = np.multiply(D_ReservoirVol, isI_DaminThisStream)
        # print 'D_SubcResVol' + str(D_SubcResVol[0].shape)

        # const
        I_MaxInf = 700
        I_CaDOYStart = 0
        I_RainYearStart = 0
        Start = 0
        Trans1 = 1
        Trans2 = 2
        End = 3
        I_RainMultiplier = 1
        I_RainDoY_Stage = [0, 1460, 2920, 4380, 5840, 7300, 8760, 10200]
        # simulationTime = 10000
        I_Rain_GenSeed = 200
        I_Rain_IntensCoefVar = 0.3
        I_Rain_IntensMean = 10
        isD_FeedingIntoLake = np.ones(shape=(subcatchment, 1))
        I_EvapotransMethod = 1
        I_MaxInfSSoil = 200
        I_PowerInfiltRed = 3.5
        isD_GWUseFacility = np.ones(shape=(subcatchment, vegClass))
        D_GW_Utilization_fraction = 0.2 * np.ones(shape=(subcatchment, 1))
        D_IrrigEfficiency = np.zeros(shape=(subcatchment, 1))
        I_InterceptEffectonTransp = 0.1
        I_SoilQflowFrac = 0.1
        C_DailyIntake = 1
        C_DailyTrampFac = 1
        C_CattleSale = 0
        G_GrassLitConv = 1
        G_GrassMortFrac = 0.03
        G_GrazingManConv = 0.1
        G_SurfLitDecFrac = 0.03
        G_SurfManureDecFrac = 0.01
        G_TramplingMultiplier = 0
        G_WUE = 0.04
        S_TrampMax = 100
        S_RippingSurface = np.zeros(shape=(subcatchment, vegClass))
        D_SubCResUseFrac = [0.01, 0.005, 0.02, 0.03, 0.205, 0.325, 0.36, 0.335, 0.315, 0.195,  0.02,  0.01,  0.015,  0.015,  0.015,  0.015,  0.015,  0.015,  0.015,  0.015]
        D_FracGWtoLake = np.zeros(shape=(subcatchment, 1))
        L_LakeLevelFullHEPP = 362.3
        L_LakeLevelHalfHEPP = 361.8
        L_LakeLevelNoHEPP = 359.5
        L_LakeOverFlowFrac = 0.1
        L_LakeOverFlPostHEPP = 362.6
        L_LakeOverFlPow = 4
        L_QmecsHEPP = 47.1
        L_QmecsSanFlow = 3
        L_m3_per_kwh = 1.584
        L_LakeTranspMultiplier = 1
        isI_SubcContr = np.ones(shape=(subcatchment, 1))
        np.random.seed(I_Rain_GenSeed)
        RainNormal = np.random.normal(I_Rain_IntensMean, I_Rain_IntensCoefVar, size=self.simulationTime)

        G_GrassFract_Biomass = np.array([0.2, 0.1, 0.05, 0.001, 0.4, 0.2, 0.1, 0.01, 0.3, 0.1, 0.2, 1, 1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]).reshape(vegClass, 1)

        D_SurfFlowRiver = [0]
        while time < self.simulationTime and not self.stopped:
            I_Warmedup = 1 if time > int(I_WarmUpTime) else 0
            I_Simulation_Time = (
                time +
                I_CaDOYStart +
                365 * I_RainYearStart -
                I_Warmedup * (I_WarmUpTime + 1))
            Simulation_Time = time % 1460
            # I_Warmedup = 1 if time >= int(I_WarmUpTime) else 0
            I_RainDoY = (I_Simulation_Time
                         if (isI_RainCycle == 0)
                         else 1 + I_Simulation_Time % 365)
            I_SpatRainTime = I_RainMultiplier * spatrain.I_SpatRain[I_RainDoY/1460][Simulation_Time]
            I_Daily_Evapotrans = I_Daily_Evap[I_RainDoY]
            I_DailyRain = (
                I_DailyRainYear[I_Simulation_Time] *
                np.ones(shape=(subcatchment, 1)) *
                I_RainMultiplier
            )
            # print I_DailyRain

            I_RainPerDay = I_SpatRainTime if isI_UseSpatVarRain else I_DailyRain

            I_RainDuration = ((I_RainPerDay / I_Rain_IntensMean) *
                                min(max(0,
                                      1 - 3 * I_Rain_IntensCoefVar,
                                    RainNormal[time]),
                                  1 + 3 * I_Rain_IntensCoefVar))
            # I_RainDuration=1
            # print np.around(I_RainDuration, decimals=2)
            # print I_Simulation_Time
            year_stage = np_utils.get_year_stage(I_Simulation_Time/365, I_InputDataYears)
            # print year_stage
            # year_stage = I_Simulation_Time / 1460
            I_FracVegClassSum = np.sum(I_FracVegClasses[year_stage], axis=1).reshape(subcatchment, 1)
            I_FracVegClassNow = np.multiply(I_RelArea > 0, np.divide(
                I_FracVegClasses[year_stage] +
                (I_FracVegClasses[year_stage + 1] - I_FracVegClasses[year_stage]) *
                (int(I_Simulation_Time/365) - I_InputDataYears[year_stage]) /
                (I_InputDataYears[year_stage + 1] - I_InputDataYears[year_stage]),
                I_FracVegClassSum,
                # np_utils.array_sum(I_FracVegClasses[year_stage], shape=(subcatchment, 1)),
                out=np.zeros_like(I_FracVegClasses[year_stage]),
                where=I_FracVegClassSum > 0
            ))
            # print np.sum(I_FracVegClasses[1])
            # print(np.sum(I_FracVegClasses[1]) - np.sum(I_FracVegClasses[0]))
            # print I_FracVegClasses[1].transpose()
            # print I_FracVegClassNow
            # print I_FracVegClassNow
            I_GWRelFracNow = (
                I_GWRelFracs[year_stage] +
                (I_GWRelFracs[year_stage + 1] - I_GWRelFracs[year_stage]) *
                (int(I_Simulation_Time/365) - I_InputDataYears[year_stage]) /
                (I_InputDataYears[year_stage + 1] - I_InputDataYears[year_stage])
            )
            # print I_GWRelFracNow
            I_MaxDynGwSubNow = (
                I_MaxDynGWSubs[year_stage] +
                (I_MaxDynGWSubs[year_stage + 1] - I_MaxDynGWSubs[year_stage]) *
                (int(I_Simulation_Time/365) - I_InputDataYears[year_stage]) /
                (I_InputDataYears[year_stage + 1] - I_InputDataYears[year_stage])
            )
            # print I_MaxDynGwSubNow
            I_PWPSubNow = (
                I_PWPSubs[year_stage] +
                (I_PWPSubs[year_stage + 1] - I_PWPSubs[year_stage]) *
                (int(I_Simulation_Time/365) - I_InputDataYears[year_stage]) /
                (I_InputDataYears[year_stage + 1] - I_InputDataYears[year_stage])
            )

            I_SoilSatminFCSubNow = (
                I_SoilSatminFCSubs[year_stage] +
                (I_SoilSatminFCSubs[year_stage + 1] - I_SoilSatminFCSubs[year_stage]) *
                (int(I_Simulation_Time/365) - I_InputDataYears[year_stage]) /
                (I_InputDataYears[year_stage + 1] - I_InputDataYears[year_stage])
            )
            # print I_SoilSatminFCSubNow
            I_RivFlowTimeNow = (
                I_RivFlowTimes[year_stage] +
                (I_RivFlowTimes[year_stage + 1] - I_RivFlowTimes[year_stage]) *
                (int(I_Simulation_Time/365) - I_InputDataYears[year_stage]) /
                (I_InputDataYears[year_stage + 1] - I_InputDataYears[year_stage])
            )
            # print I_RivFlowTimeNow
            I_BD_BDRefVegNow = (
                I_TopSoilBD_BDRefs[year_stage] +
                (I_TopSoilBD_BDRefs[year_stage + 1] - I_TopSoilBD_BDRefs[year_stage]) *
                (int(I_Simulation_Time/365) - I_InputDataYears[year_stage]) /
                (I_InputDataYears[year_stage + 1] - I_InputDataYears[year_stage])
            )
            # print np.sum(I_TopSoilBD_BDRefs[year_stage + 1] - I_TopSoilBD_BDRefs[year_stage])
            # print ( (int(I_Simulation_Time/365) - I_InputDataYears[year_stage]) /
            #     (I_InputDataYears[year_stage + 1] - I_InputDataYears[year_stage]))
            # print np.sum(I_BD_BDRefVegNow)
            #
            I_AvailWatClassNow = (
                I_PlantAvWatSubs[year_stage] +
                (I_PlantAvWatSubs[year_stage + 1] - I_PlantAvWatSubs[year_stage]) *
                (int(I_Simulation_Time/365) - I_InputDataYears[year_stage]) /
                (I_InputDataYears[year_stage + 1] - I_InputDataYears[year_stage])
            )
            # print I_AvailWatClassNow
            # I_FracVegClassSum1 = np_utils.array_sum(I_FracVegClass_1)
            # I_FracVegClassSum2 = np_utils.array_sum(I_FracVegClass_2)
            # I_FracVegClassSum3 = np_utils.array_sum(I_FracVegClass_3)
            # I_FracVegClassSum4 = np_utils.array_sum(I_FracVegClass_4)
            # I_FracVegClassSumNow = np_utils.array_sum(I_FracVegClassNow)
            I_DailyRainAmount = np.multiply(
                I_RainPerDay,
                np.multiply(I_FracVegClassNow, I_RelArea)
            )

            isI_StillWarmUp = time <= I_WarmUpTime
            I_WUcorrection = time == int(I_WarmUpTime + 1)
            # I_WarmedUp = time == int(I_WarmUpTime)
            isO_Reset = I_Warmedup == 1 or I_WUcorrection == 1
            I_FracArea = np.multiply(I_FracVegClassNow, I_RelArea)
            I_TimeEvap = (
                0 if I_RainDoY == 0 else 365 if I_RainDoY % 365 == 0
                else I_RainDoY % 365
            )
            I_MoY = 0 if I_RainDoY == 0 else int(I_TimeEvap / 30.5) + 1
            # print 'adfadf', I_MoY
            # I_PotEvapTransp = None
            if I_EvapotransMethod == 1:
                I_PotEvapTransp = np.multiply(
                    I_Evapotrans[I_MoY],
                    np.multiply(I_MultiplierEvapoTrans[I_MoY], I_FracArea)
                )
            else:
                I_PotEvapTransp = np.multiply(
                    I_Daily_Evapotrans[I_MoY],
                    np.multiply(I_MultiplierEvapoTrans[I_MoY], I_FracArea)
                )
            # print I_MoY, I_PotEvapTransp.transpose()
            # print I_PotEvapTransp.shape == (20, 20)
            # print I_RelArea
            # print I_FracVegClassNow.transpose()
            I_MaxInfSubSAreaClass = I_MaxInfSSoil * np.multiply(I_RelArea, I_FracVegClassNow)
            # print np.around(I_MaxInfSubSAreaClass.transpose(), decimals=2)
            # print I_MaxInfSubSAreaClass.shape == (20, 20)
            I_MaxInfArea = I_MaxInf * np.multiply(np.multiply(
                I_FracArea,
                # np.ones(shape=(subcatchment, vegClass)),
                np.power(np.divide(0.7,
                                   I_BD_BDRefVegNow,
                                   out=np.zeros_like(I_BD_BDRefVegNow),
                                   where=I_BD_BDRefVegNow > 0),
                         I_PowerInfiltRed
                         )
            ), I_BD_BDRefVegNow > 0)
            # print np.sum(I_MaxInfArea)
            # print np.sum(I_MaxInfArea)
            # print np.around(I_MaxInfArea, decimals=2).transpose()
            # print I_MaxInfArea.shape == (20, 20)
            I_CanIntercAreaClass = np.multiply(I_InterceptClass, I_FracArea.transpose()).transpose()
            # print np.around(I_CanIntercAreaClass, decimals=2).transpose()
            I_AvailWaterClass = (I_AvailWaterConst * I_FracArea
                                 if isI_SoilPropConst
                                 else np.multiply(I_AvailWatClassNow,
                                                  I_FracArea))
            # print np.around(I_AvailWaterClass, decimals=2).transpose()
            I_SoilSatClass = (I_AvailWaterConst + I_SoilSatMinFCConst) * I_FracArea if isI_SoilPropConst else np.multiply(np.add(I_SoilSatminFCSubNow, I_AvailWatClassNow), I_FracArea)

            # print np.around(I_SoilSatClass, decimals=2).transpose()
            I_GWRelFrac = I_GWRelFracConst if isI_SoilPropConst else I_GWRelFracNow
            I_MaxDynGWact = I_MaxDynGWConst if I_GWRelFracConst else I_MaxDynGwSubNow
            I_MaxDynGWArea = np.multiply(I_MaxDynGWact, I_RelArea)
            # print np.around(I_GWRelFrac, decimals=2)
            # print I_MaxDynGWArea.shape == (20, 1)
            I_InitTotGW = np.add(I_MaxDynGWArea, I_InitRelGW)
            D_InterceptEvap = np.multiply(
                I_CanIntercAreaClass,
                (1 - np.exp(-np.divide(
                    I_DailyRainAmount,
                    I_CanIntercAreaClass,
                    out=np.zeros_like(
                        I_CanIntercAreaClass),
                    where=I_CanIntercAreaClass > 0))))
            # print np.around(D_InterceptEvap, decimals=2).transpose()
            D_RainInterc = np.divide(
                D_InterceptEvap,
                I_FracArea,
                out=np.zeros_like(D_InterceptEvap),
                where=I_FracArea > 0)
            # print np.around(D_RainInterc, decimals=2).transpose()
            D_RainIntercDelay = (
                np.minimum(
                    I_RainMaxIntDripDur,
                    np.sum(D_RainInterc, axis=1).reshape(subcatchment, 1) / I_RainIntercDripRt
                ) )
            # print np.around(D_RainIntercDelay, decimals=2)
            # print I_RainMaxIntDripDur, I_RainIntercDripRt
            I_RainTimeAvForInf = np.minimum(
                24,
                I_RainDuration + D_RainIntercDelay
            )
            # print np.around(I_RainTimeAvForInf, decimals=2)
            D_Infiltration = np.multiply(
                isL_Lake == 0,
                np.minimum(
                    np.minimum(I_SoilSatClass - D_SoilWater,
                               np.multiply(I_MaxInfArea,
                                           I_RainTimeAvForInf) / 24),
                    I_DailyRainAmount - D_InterceptEvap))
            D_Infiltration = calculate.inflow_constrain(D_Infiltration)
            # print D_Infiltration.transpose()
            # print (np.sum(np.around(D_Infiltration, decimals=2)))
            # print np.around(D_Infiltration, decimals=2).transpose()
            I_RelDroughtFact_AvailWaterClass = np.multiply(
                I_RelDroughtFact,
                I_AvailWaterClass)

            D_RelWaterAv = np.minimum(
                1,
                np.divide(
                    D_SoilWater,
                    I_RelDroughtFact_AvailWaterClass,
                    out=np.ones_like(D_SoilWater),
                    where=I_RelDroughtFact_AvailWaterClass > 0
                )
            )

            # print np.around(D_RelWaterAv, decimals=2).transpose()

            D_Irrigation = np.minimum(
                np.divide(
                    np.multiply(D_GWArea,
                                np.multiply(isD_GWUseFacility,
                                            np.multiply(
                                                D_GW_Utilization_fraction,
                                                np.subtract(1, D_RelWaterAv)))),
                    D_IrrigEfficiency,
                    out=np.zeros(shape=(subcatchment, vegClass)),
                    where=D_IrrigEfficiency > 0),
                I_PotEvapTransp)
            # print np.around(D_Irrigation, decimals=2).transpose()
            D_Percolation = np.multiply(
                I_AvailWaterClass > 0,
                np.minimum(
                    I_MaxInfSubSAreaClass,
                    np.minimum(
                        np.multiply(
                            D_SoilWater,
                            np.multiply(I_PercFracMultiplier, I_GWRelFrac)),
                        I_MaxDynGWArea - D_GWArea)) -
                np.multiply(D_IrrigEfficiency, D_Irrigation)) - np.multiply(
                    I_AvailWaterClass <= 0,
                    np.multiply(D_IrrigEfficiency, D_Irrigation))
            # print np.around(D_Percolation, decimals=2).transpose()
            D_Percolation = calculate.outflow_constrain(D_Percolation, D_SoilWater, D_Infiltration, True, 1)

            D_DeepInfiltration = np.multiply(
                isL_Lake == 0,
                np.minimum(
                    np.minimum(
                        np.minimum(
                            np.multiply(
                                np.sum(I_MaxInfArea, axis=1).reshape(subcatchment, 1),
                                I_RainTimeAvForInf
                            ) / 24 - np.sum(
                                I_SoilSatClass,
                                axis=1).reshape(subcatchment, 1) +
                            np.sum(D_SoilWater,
                                   axis=1).reshape(subcatchment, 1),
                            np.sum(I_MaxInfSubSAreaClass,
                                   axis=1).reshape(subcatchment, 1)
                        ),
                        np.sum(I_DailyRainAmount,
                               axis=1).reshape(subcatchment, 1) -
                        np.sum(D_InterceptEvap,
                               axis=1).reshape(subcatchment, 1) -
                        np.sum(D_Infiltration,
                               axis=1).reshape(subcatchment, 1)),
                    I_MaxDynGWArea - D_GWArea))
            D_DeepInfiltration = calculate.inflow_constrain(D_DeepInfiltration)
            # print D_DeepInfiltration

            D_GWaDisch = np.multiply(D_GWArea, I_GWRelFrac)
            D_GWaDisch = calculate.outflow_constrain(D_GWaDisch, D_GWArea,
                                                     D_DeepInfiltration + np.sum(D_Percolation, axis=1).reshape(
                                                         subcatchment, 1),
                                                     True, 1)

            D_WaterEvapIrrigation = np.multiply(
                D_IrrigEfficiency > 0,
                D_Irrigation * (1 - D_IrrigEfficiency))
            D_WaterEvapIrrigation = calculate.outflow_constrain(D_WaterEvapIrrigation, D_GWArea, D_DeepInfiltration + np.sum(D_Percolation, axis=1).reshape(subcatchment, 1) - D_GWaDisch)

            # print np.around(D_GWArea[time], decimals=2)

            D_SoilQflowRelFrac = np.ones(
                shape=(subcatchment, 1)
            ) * I_SoilQflowFrac
            D_SoilDischarge = np.multiply(
                D_SoilQflowRelFrac,
                (D_SoilWater - I_AvailWaterClass)
            )
            D_SoilDischarge = calculate.outflow_constrain(D_SoilDischarge, D_SoilWater,
                                                          D_Infiltration - D_Percolation)
            # print D_DeepInfiltration
            # print 'D_DeepInfiltration', D_DeepInfiltration.shape, D_GWArea[time].shape
            D_ActEvapTransp = np.multiply(
                isL_Lake != 1,
                np.multiply(
                    I_PotEvapTransp -
                    np.multiply(I_InterceptEffectonTransp, D_InterceptEvap),
                    D_RelWaterAv))

            D_ActEvapTransp = calculate.outflow_constrain(D_ActEvapTransp, D_SoilWater, D_Infiltration - D_Percolation - D_SoilDischarge, True, 1)

            D_SurfaceFlow = (
                np.multiply(isL_Lake == 1, np.sum(
                                I_DailyRainAmount,
                                axis=1).reshape(subcatchment, 1)
                            ) +
                np.multiply(isL_Lake != 1, (np.sum(
                                     I_DailyRainAmount,
                                     axis=1
                                 ).reshape(subcatchment, 1) -
                                  np.sum(
                                      D_InterceptEvap,
                                      axis=1
                                  ).reshape(subcatchment, 1) -
                                  np.sum(
                                      D_Infiltration,
                                      axis=1
                                  ).reshape(subcatchment, 1) -
                                  D_DeepInfiltration))
            )

            # D_SoilDischarge = np.multiply(D_SoilDischarge_ > 0, D_SoilDischarge_)
            # print np.round(D_SoilWater[time], decimals=2).transpose()
            # print np.around(D_SoilDischarge, decimals=2).transpose()
            G_GrassAll = np_utils.array_sum(G_GrassStandingBiomass)
            G_GrowthRate = G_WUE * np.multiply(D_ActEvapTransp.transpose(),
                                               G_GrassFract_Biomass).transpose()
            G_Grazing = (0
                         if G_GrassAll == 0
                         else (C_StockingRate *
                               C_DailyIntake *
                               G_GrassStandingBiomass /
                               G_GrassAll))

            G_Grazing = calculate.outflow_constrain(G_Grazing, G_GrassStandingBiomass, G_GrowthRate)
            # print np.around(C_StockingRate[time], decimals=2)
            # print np.around(G_GrassStandingBiomass, decimals=2)
            C_TrampComp = C_DailyTrampFac * G_Grazing / C_DailyIntake
            C_DeathRate = C_StockingRate * C_DailyIntake - G_GrassAll
            C_DeathRate = (C_DeathRate > 0) * C_DeathRate
            C_Destocking = min(C_StockingRate, C_CattleSale + C_DeathRate)
            C_Stocking = 0 * C_StockingRate
            C_Destocking = calculate.outflow_constrain(C_Destocking, C_StockingRate, C_Stocking, True, 1)
            # print C_Stocking, C_Destocking
            # G_GrassFract_Biomass = np.zeros(vegClass)

            # print np.around(G_GrowthRate, decimals=2)
            # G_GrassAll = np_utils.array_sum(G_GrassStandingBiomass[time])
            G_LeafMortality = (G_GrassStandingBiomass * G_GrassMortFrac +
                               G_Grazing * G_TramplingMultiplier)
            G_LeafMortality = calculate.outflow_constrain(G_LeafMortality, G_GrassStandingBiomass, G_GrowthRate - G_Grazing)
            G_LitterDeposition = G_LeafMortality * G_GrassLitConv

            G_Incorporation_DecaySurfLit = (G_SurfaceLitter *
                                            G_SurfLitDecFrac)
            G_Incorporation_DecaySurfLit = calculate.outflow_constrain(G_Incorporation_DecaySurfLit, G_SurfaceLitter, G_LitterDeposition)
            # print G_SurfaceLitter[time]
            G_FaecesProd = G_Grazing * G_GrazingManConv
            G_Incorporation_DecayManure = (G_SurfManure *
                                           G_SurfManureDecFrac)
            G_Incorporation_DecayManure = calculate.outflow_constrain(G_Incorporation_DecayManure, G_SurfManure, G_FaecesProd)
            G_SurfaceCover = (G_GrassStandingBiomass +
                              G_SurfaceLitter +
                              G_SurfManure)
            S_RainAtSoilSurface = I_DailyRainAmount - D_InterceptEvap
            # print np.around(S_RainAtSoilSurface, decimals=2)
            # print np.around(S_RelBulkDensity[time], decimals=2)
            S_SplashErosion = (0 * np.divide(
                np.multiply(G_SurfaceCover,
                            S_RainAtSoilSurface),
                I_RainDuration,
                out=np.zeros_like(G_SurfaceCover),
                where=I_RainDuration > 0))

            S_StructureFormation = 0 * np.multiply(S_RelBulkDensity,
                                                   G_SurfaceCover)

            S_Compaction = (
                np.multiply((1.3 - S_RelBulkDensity), C_TrampComp) /
                S_TrampMax)
            S_Compaction = calculate.outflow_constrain(S_Compaction, S_RelBulkDensity, S_SplashErosion + S_RippingSurface + S_StructureFormation)

            D_ReservoirVol = L_ResrDepth * np.multiply(isL_Lake, I_RelArea)
            # print D_SubcResVol[time].shape
            # print np.around(D_SubcResVol[time], decimals=2)
            D_SubCResUseFrac_ = D_SubCResUseFrac[I_RainDoY] if I_RainDoY < len(D_SubCResUseFrac) else D_SubCResUseFrac[-1]

            D_RoutingTime = np.divide(
                I_RoutingDistance,
                (I_RivFlowTimeNow * I_RoutVeloc_m_per_s) * 3.6 * 24 * I_Tortuosity)
            # print np.around(D_RoutingTime, decimals=2)
            I_ReleaseFrac = np.minimum(
                1,
                np.divide(I_RiverflowDispersalFactor,
                          D_RoutingTime,
                          out=np.ones(shape=(subcatchment, obsPoint)),
                          where=D_RoutingTime > 0))
            # print np.around(I_ReleaseFrac, decimals=2)
            # print D_SurfaceFlow.shape, D_GWaDisch.shape, D_FracGWtoLake.shape, D_SoilDischarge.shape, D_SubCResOutflow.shape, isI_DaminThisStream.shape
            D_Influx_to_Resr = np.multiply(
                isI_DaminThisStream == 1,
                (D_GWaDisch +
                 np.sum(D_SoilDischarge, axis=1).reshape(subcatchment, 1)
                 + D_SurfaceFlow)
            )
            # print D_GWaDisch
            D_Influx_to_Resr = calculate.inflow_constrain(D_Influx_to_Resr)

            D_EvaporReservoir = I_Evapotrans[I_MoY % 12] * np.sum(isL_Lake)
            D_EvaporReservoir = calculate.outflow_constrain(D_EvaporReservoir, D_SubcResVol, D_Influx_to_Resr,
                                                            True, 1)

            D_SubCResOutflow = np.add(
                np.multiply(
                    D_SubcResVol > D_ReservoirVol,
                    np.subtract(D_SubcResVol, D_ReservoirVol)),
                np.multiply(D_SubcResVol < D_ReservoirVol,
                            D_SubCResUseFrac_ * D_SubcResVol))
            # print np.around(D_SubCResOutflow, decimals=2)
            # print D_SubCResOutflow
            # print D_SubcResVol[time]
            # print D_Influx_to_Resr
            # print D_EvaporReservoir
            D_SubCResOutflow = calculate.outflow_constrain(D_SubCResOutflow, D_SubcResVol,
                                                           D_Influx_to_Resr - D_EvaporReservoir, True, 1)

            D_TotalStreamInflow = (
                D_SurfaceFlow +
                np.multiply(
                    D_GWaDisch,
                    (1 - D_FracGWtoLake)) +
                np.sum(D_SoilDischarge, axis=1).reshape(subcatchment, 1) +
                np.multiply(D_SubCResOutflow,
                            (1 - isI_DaminThisStream)))
            D_RivLakeSameDay = np.multiply(
                np.multiply(D_RoutingTime >= 0, D_RoutingTime < 1),
                np.multiply(isD_FeedingIntoLake,
                            np.multiply(D_TotalStreamInflow,
                                        I_ReleaseFrac)))

            # print D_RivLakeSameDay
            D_RivInflLake = np.multiply(
                np.multiply(
                    I_ReleaseFrac[:, constants.Inflowlake].reshape(subcatchment, 1),
                    D_TotRiverFlowNoDelay[:, constants.Inflowlake].reshape(subcatchment, 1)),
                isD_FeedingIntoLake)
            D_RivInflLake = np.multiply(np.ones(shape=(subcatchment, obsPoint)), D_RivInflLake)

            D_DirectSurfFkowObsPoint = np.multiply(
                np.multiply(D_RoutingTime >= 0, D_RoutingTime < 1),
                np.multiply(D_TotalStreamInflow, (1 - I_ReleaseFrac)))
            D_DirectSurfFkowObsPoint = calculate.inflow_constrain(D_DirectSurfFkowObsPoint)

            D_RiverDelay = np.multiply(
                I_ReleaseFrac,
                np.multiply(D_TotRiverFlowNoDelay,
                            (1 - isD_FeedingIntoLake))
            )
            D_RiverDelay = calculate.outflow_constrain(D_RiverDelay, D_TotRiverFlowNoDelay,
                                                       D_SurfFlowRiver[time] + D_DirectSurfFkowObsPoint, True, 1)

            D_RivInflLake = calculate.outflow_constrain(D_RivInflLake, D_TotRiverFlowNoDelay,
                                                        D_DirectSurfFkowObsPoint + D_SurfFlowRiver[time] - D_RiverDelay)

            D_RiverFlowtoLake = (
                np.sum(
                    D_RivLakeSameDay,
                    axis=0)[constants.Inflowlake] +
                np.sum(
                    D_RivInflLake,
                    axis=0)[constants.Inflowlake]
            )
            D_RiverFlowtoLake = calculate.inflow_constrain(D_RiverFlowtoLake)

            O_RivInflLake = (
                D_RivInflLake[:, constants.Inflowlake].reshape(
                    subcatchment,
                    1
                )
            )


            O_RivLakeSameDay = (
                D_RivLakeSameDay[:, constants.Inflowlake].reshape(
                    subcatchment,
                    1
                )
            )
            O_RiverFlowtoLake = O_RivInflLake + O_RivLakeSameDay
            D_GWLakeSub = np.multiply(D_FracGWtoLake, D_GWaDisch)

            D_GWtoLake = np_utils.array_sum(D_GWLakeSub)
            D_GWtoLake = calculate.inflow_constrain(D_GWtoLake)

            D_RestartL = isO_Reset * D_CumInflowtoLake / dt
            D_RestartL = calculate.biflow_constrain(D_RestartL, D_CumInflowtoLake + D_RiverFlowtoLake + D_GWtoLake, True)

            # D_TotalStreamInflow = (
            #     (D_SurfaceFlow +
            #      np.multiply(D_GWaDisch, (1 - D_FracGWtoLake)) +
            #      np_utils.array_sum(D_SoilDischarge, shape=(subcatchment, 1))) +
            #     np.multiply(D_SubCResOutflow, (1 - isI_DaminThisStream)))


            D_RiverDirect = np.multiply(
                np.multiply(D_RoutingTime > 0, D_RoutingTime < 1),
                np.multiply((1 - isD_FeedingIntoLake),
                            np.multiply(D_TotalStreamInflow, I_ReleaseFrac)))
            D_RiverDirect = calculate.inflow_constrain(D_RiverDirect)

            # D_RivInfLake = np.multiply(
            #     np.multiply(I_ReleaseFrac, D_TotRiverFlowNoDelay[time]),
            #     isD_FeedingIntoLake)
            SurFlowRiverTransitTime = np.around(np.add(np.multiply(D_RoutingTime >= 1, D_RoutingTime), np.multiply(D_RoutingTime <1, 1)))

            D_CurrRivVol = (
            np.sum(
                D_StreamsSurfQ,
                axis=0
            )[0] +
            np.sum(
                D_TotRiverFlowNoDelay,
                axis=0)[0]
            )
            D_RestartR = np.multiply(isO_Reset, D_CumTotRiverFlow) / dt
            D_RestartR = calculate.biflow_constrain(D_RestartR, D_CumTotRiverFlow + D_RiverDelay + D_RiverDirect,
                                                    True)

            D_SurfFlowObsPoint = np.multiply(D_RoutingTime >= 1,
                                             D_TotalStreamInflow)
            D_SurfFlowObsPoint = calculate.inflow_constrain(D_SurfFlowObsPoint)

            L_LakeTransDef = np.multiply(isL_Lake, I_PotEvapTransp[constants.AF_Kelapa] - D_ActEvapTransp[constants.AF_Kelapa])
            L_LakeArea = np.multiply(isL_Lake,
                                     I_RelArea,
                                     out=np.zeros_like(isL_Lake),
                                     where=isL_Lake != 1)
            L_LakeLevel =  (
                L_LakeVol /
                (1000 * np.sum(L_LakeArea)) + L_LakeBottomElev
            ) if (np.sum(L_LakeArea) > 0) else 0

            L_Lakelevelexcess = (
                L_LakeLevel -
                (1 - isL_HEPP_Active) * L_LakeElevPreHEPP -
                isL_HEPP_Active * L_LakeOverFlPostHEPP)

            L_HEPP_Daily_Dem = L_QmecsHEPP * 3600 * 24 / I_TotalArea * 10 ** -3

            L_HEPP_Outflow = (
                L_HEPP_Daily_Dem
                if L_LakeLevel > L_LakeLevelFullHEPP
                else L_HEPP_Daily_Dem * 0.5 * (
                    1 +
                    max(0,
                        (L_LakeLevel - L_LakeLevelHalfHEPP) /
                        (L_LakeLevelFullHEPP - L_LakeLevelHalfHEPP)))
                if L_LakeLevel > L_LakeLevelNoHEPP else 0)
            L_HEPPWatUseFlow = L_HEPP_Outflow if isL_HEPP_Active == 1 else 0
            L_HEPP_Kwh = 1000 * I_TotalArea * L_HEPPWatUseFlow / L_m3_per_kwh

            # L_HEPP_OpTimeRel = (
            # (L_CumHEPPUse[time] / L_HEPP_Daily_Dem) / I_Simulation_Time
            # if I_Simulation_Time > 0 and isI_WarmEdUp[time] == 1
            # else 0)

            L_InFlowtoLake = D_RiverFlowtoLake + D_GWtoLake
            # print D_GWtoLake

            L_EvapLake = min(np.sum(L_LakeTransDef),
                             L_LakeVol) * L_LakeTranspMultiplier
            L_EvapLake = calculate.outflow_constrain(L_EvapLake, L_LakeVol, L_InFlowtoLake, True, 1)
            L_SanitaryFlow = L_QmecsSanFlow * 3600 * 24 / I_TotalArea * 10 ** -3
            L_OutflTrVolPreHEPP = 1000 * (
                L_LakeElevPreHEPP -
                L_LakeBottomElev) * np.sum(L_LakeArea)
            L_OutflTrVoPostHEPP = 1000 * (
                L_LakeOverFlPostHEPP -
                L_LakeBottomElev) * np.sum(L_LakeArea)
            L_RivOutFlow = max(isL_HEPP_Active * L_SanitaryFlow,
                               (L_LakeVol -
                                L_OutflTrVoPostHEPP * isL_HEPP_Active -
                                L_OutflTrVolPreHEPP * (1 - isL_HEPP_Active)) * (
                               L_LakeOverFlowFrac) * (
                                   1 + L_Lakelevelexcess ** L_LakeOverFlPow))
            L_RivOutFlow = calculate.outflow_constrain(L_RivOutFlow, L_LakeVol, L_InFlowtoLake - L_EvapLake)
            O_InFlowtoLake = O_RiverFlowtoLake + D_GWLakeSub
            L_RestartR = isO_Reset * L_CumRivOutFlow / dt
            L_RestartH = isO_Reset * L_CumHEPPUse
            L_RestartE = isO_Reset * L_CumEvapLake / dt
            O_TotStreamFlow = (O_CumBaseFlow +
                               O_CumSoilQFlow +
                               O_CumSurfQFlow)
            D_DeltaStockRiver = D_InitRivVol - D_CurrRivVol
            # D_SurfaceFlowAcc = np.sum(D_SurfaceFlow)
            O_DeltaGWStock = O_InitGWStock - np.sum(D_GWArea)
            # print O_DeltaGWStock
            O_DeltaSoilWStock = O_InitSoilW - np.sum(D_SoilWater)
            # print O_InitSoilW[time]
            # O_ChkAllCatchmAccFor = (-O_CumRain[time] +
            #                         O_CumIntercE[time] +
            #                         O_CumTransp[time] +
            #                         O_TotStreamFlow -
            #                         O_DeltaGWStock -
            #                         O_DeltaSoilWStock)
            O_DeltaStockLake = D_InitLakeVol - L_LakeVol
            # O_ChkAllLakeAccFor = (D_CumInflowtoLake[time] -
            #                       L_CumEvapLake[time] -
            #                       L_CumRivOutFlow[time] -
            #                       L_CumHEPPUse[time] +
            #                       O_DeltaStockLake)
            D_CumTotRiverFlowAll = np.sum(D_CumTotRiverFlow, axis=1)[0]
            # O_ChkAllRiverAccFor = (O_TotStreamFlow -
            #                        D_CumTotRiverFlowAll -
            #                        D_CumInflowtoLake[time] +
            #                        D_DeltaStockRiver)
            # O_DailyRainSubCtm = np_utils.array_sum(I_DailyRainAmount, shape=(subcatchment, 1))
            O_FrBaseFlow = (O_CumBaseFlow / O_TotStreamFlow
                            if O_TotStreamFlow > 0
                            else 0)
            # O_FrSoilQuickFlow = (O_CumSoilQFlow[time] / O_TotStreamFlow
            #                      if O_TotStreamFlow > 0
            #                      else 0)
            # O_FrSurfQuickFlow = (O_CumSurfQFlow[time] / O_TotStreamFlow
            #                      if O_TotStreamFlow else 0)
            O_RainYesterday = O_RainYest * I_Warmedup
            # O_RainHalfDelayed = (np_utils.array_sum(O_RainYesterday) +
            #                      np_utils.array_sum(I_DailyRainAmount)) / 2
            O_RelWatAvVegSubc = np.multiply(D_RelWaterAv, I_FracVegClassNow)
            O_RelWatAv_Subc = np.divide(
                np.mean(O_RelWatAvVegSubc, axis=1).reshape(subcatchment, 1),
                np.sum(I_FracVegClassNow, axis=1).reshape(subcatchment, 1),
                out=np.ones(shape=(subcatchment, 1)),
                where=np.sum(I_FracVegClassNow, axis=1).reshape(subcatchment, 1) > 0)
            # O_RelWatAv_Overall = np_utils.array_mean(O_RelWatAv_Subc)
            # O_Rel_ET_Subc = np.divide(
            #     D_InterceptEvap +
            #     D_ActEvapTransp,
            #     I_PotEvapTransp,
            #     out=np.zeros_like(I_PotEvapTransp),
            #     where=I_PotEvapTransp != 0)
            # O_Reset = 1 if I_WarmedUp == 1 or I_WUcorrection == 1 else 0
            # S_RainAtSoilSurface = I_DailyRainAmount - D_InterceptEvap

            O_InitLake = isO_Reset * (L_LakeVol - D_InitLakeVol)
            O_InitLake = calculate.biflow_constrain(O_InitLake, D_InitLakeVol, True)
            O_InitRiv = isO_Reset * (D_CurrRivVol - D_InitLakeVol)
            O_InitRiv = calculate.biflow_constrain(O_InitRiv, D_InitRivVol, True)
            O_BaseFlowAcc = np.sum(D_GWaDisch) * I_Warmedup
            O_BaseFlowAcc = calculate.inflow_constrain(O_BaseFlowAcc)
            # O_CumDeepInfAcc = np_utils.array_sum(D_DeepInfiltration) * I_WarmedUp
            O_EvapoTransAcc = (np.sum(I_PotEvapTransp) > 0) * (np.sum(D_ActEvapTransp) + np.sum(D_InterceptEvap)) * I_Warmedup
            # O_InfAcc = np_utils.array_sum(D_Infiltration) * I_WarmedUp
            O_AccET = np.sum(D_InterceptEvap) * I_Warmedup
            O_PercAcc = np.sum(D_Percolation) * I_Warmedup

            O_RainAcc = np.sum(I_DailyRainAmount) * I_Warmedup
            # O_CumSoilQFlowAcc = np.sum(D_SoilDischarge) * I_Warmedup
            O_SurfQFlowAcc = np.sum(D_SurfaceFlow) * I_Warmedup

            O_TranspAcc = np.sum(D_ActEvapTransp) * I_Warmedup
            O_InitGW = isO_Reset * (
                np.sum(D_GWArea) -
                O_InitGWStock
            )
            O_InitSW = isO_Reset * (
                np.sum(D_SoilWater) -
                O_InitSoilW
            )
            O_RainToday = np.sum(
                I_DailyRainAmount,
                axis=1
            ).reshape(subcatchment, 1) * I_Warmedup
            O_LastYearHEPP = (O_LastYHepp > 0) * (O_ThisYHepp - O_LastYHepp)/(365 * L_HEPP_Daily_Dem)
            O_BYP = (O_LastYearHEPP > 0 and O_LastYearHEPP > O_BestYyHEPP) * (-O_BestYyHEPP + O_LastYearHEPP)

            O_StarMYear = np.array([4, 6, 8]).reshape(measurePeriod, 1)
            O_StartDOY = np.array([1, 1, 1]).reshape(measurePeriod, 1)
            O_StartMDay = (O_StarMYear - 1) * 365 + 1 + (O_StartDOY - 1)
            O_EndMDay = O_StartMDay + O_MPeriodLength
            # print O_StartMDay, O_EndMDay
            Yearly_Tick = 1 if I_Warmedup == 1 and time % 365 == 0 else 0
            # time_stage = I_Simulation_Time / 1460
            # I_DebitTime = I_RFlowData[time_stage]
            # for index, stage in enumerate(I_RainDoY_Stage):
            #     I_DebitTime = (I_RFlowData[index]
            #                    if I_Simulation_Time <= stage
            #                     else I_RFlowData[6] if I_Simulation_Time <= 10220
            #                     else I_RFlowData[7])
            I_RFlowDataQmecs = I_RFlowData[I_Simulation_Time]
            I_ContrSubcArea = np.multiply(I_RelArea, isI_SubcContr)
            I_RFlowdata_mmday = 0 if np.sum(I_ContrSubcArea) == 0 else (I_RFlowDataQmecs*24*3600*10**3)/(np.sum(I_ContrSubcArea) * I_TotalArea * 10**6)
            # print 'O_Ch_in_GWStockMP', O_InitGWStockMP[time].shape, O_Ch_inGWStock[time].shape
            O_Ch_in_GWStockMP = np.multiply(
                np.multiply(O_StartMDay < time, O_EndMDay + 1 > time),
                (np.sum(D_GWArea) -
                O_InitGWStockMP -
                O_Ch_inGWStock)
            )
            O_Ch_in_WStockMP = np.multiply(
                np.multiply(O_StartMDay < time, O_EndMDay + 1 > time),
                (np.sum(D_SoilWater) -
                 O_InitSWMP -
                 O_Ch_inWStock)
            )

            inMDay = np.multiply(I_Simulation_Time >= O_StartMDay, I_Simulation_Time < O_EndMDay)
            inMDayStillWarmUp = np.multiply(I_Simulation_Time >= O_StartMDay, np.multiply(I_Simulation_Time < O_EndMDay, isI_StillWarmUp == 0))
            # print inMDayStillWarmUp

            O_BaseFlowAccMP = inMDayStillWarmUp * np.sum(D_GWaDisch)

            O_DebitDataAccMP = inMDayStillWarmUp * I_RFlowdata_mmday        # print 'D_RiverFlowtoLake', D_RiverFlowtoLake
            O_DebitPredAccMP = inMDayStillWarmUp * D_RiverFlowtoLake

            O_EvapLakeMP = inMDayStillWarmUp * L_EvapLake

            O_Ch_in_EvapoTrans = inMDayStillWarmUp * (np.sum(D_CumEvapTranspClass) - O_InitEvapoMP - O_CumEvapTransMP)

            O_GWAccMP = inMDay * np.sum(D_GWArea)

            O_HEPPOutFlowMP = inMDay * L_HEPPWatUseFlow

            O_InfAccMP = inMDayStillWarmUp * np.sum(D_Infiltration)

            O_IntercAccMP = inMDayStillWarmUp * np.sum(D_InterceptEvap)

            O_RainAccMP = inMDayStillWarmUp * np.sum(I_DailyRainAmount)
            O_RivInflowtoLakeMP = inMDayStillWarmUp * L_InFlowtoLake
            O_RivOutFlowMP = inMDayStillWarmUp * L_RivOutFlow
            O_SoilQFlowAccMP = inMDayStillWarmUp * np.sum(D_SoilDischarge)
            O_SoilWAccMP = inMDayStillWarmUp * np.sum(D_SoilWater)
            O_SurfQFlowAccMP = inMDayStillWarmUp * np.sum(D_SurfaceFlow)
            O_TranspAccMP = inMDayStillWarmUp * np_utils.array_sum(D_ActEvapTransp)
            O_Ch_in_CatchmStMP = inMDay * (
                O_Ch_inGWStock +
                O_Ch_in_GWStockMP +
                O_Ch_inWStock +
                O_Ch_in_WStockMP -
                O_DeltaCatchmStMP)

            O_Hepp_ElctrProd = inMDayStillWarmUp * (
                L_HEPP_Kwh / (O_EndMDay - O_StartMDay))
            # print 'O_Hepp_ElctrProd', O_Hepp_ElctrProd.shape
            O_Ch_EvapoTran = np.sum(D_CumEvapTranspClass) * (time == O_StartMDay)
            O_ChGWMP = np.sum(D_GWArea) *(time == O_StartMDay)
            # O_ChSoilWMP = np.sum(D_SoilWater[time]) * (time == O_StartMDay)
            O_ChSoilWMP = np.sum(D_SoilWater) * (time == O_StartMDay)
            # O_HeppUseF1 = Yearly_Tick * O_ThisYHepp[time]
            O_HeppUseF2 = Yearly_Tick * O_LastYHepp
            O_HeppUseF0 = Yearly_Tick * L_CumHEPPUse
            O_HeppUseF1 = Yearly_Tick * O_ThisYHepp
            # O_CumET_LandMP = O_CumIntercEvapMP + O_CumTranspMP
            # O_CurrentETall = np.sum(D_ActEvapTransp)
            O_WYP = (- O_WorstYHEPP + O_LastYearHEPP
                     if 0 < O_LastYearHEPP < O_WorstYHEPP
                     else 0)
            # O_CumET_LandMP = O_CumIntercEvapMP + O_CumTranspMP
            # O_CurrentETall = np_utils.array_sum(D_ActEvapTransp)
            # O_RelOpTimeHEPPMP = ((O_CumHEPPOutFlowMP[time] /
            #                       L_HEPP_Daily_Dem) /
            #                      (O_EndMDay - O_StartMDay))
            # O_SoilWaterTot = np.sum(D_SoilWater[time])
            O_DeepInfAcc = np.sum(
                D_DeepInfiltration
            ) * I_Warmedup
            O_DeepInfAcc = calculate.inflow_constrain(O_DeepInfAcc)

            O_InfAcc = (
                np.sum(D_Infiltration) * I_Warmedup
            )
            O_InfAcc = calculate.inflow_constrain(O_InfAcc)

            O_IntercAcc = (
                np.sum(D_InterceptEvap) * I_Warmedup
            )

            O_SoilQFlowAcc = (
                np.sum(D_SoilDischarge) * I_Warmedup
            )

            # print O_SoilQFlowAcc

            O_SoilQflow_Subca = np.sum(
                D_SoilDischarge,
                axis=1
            ).reshape(subcatchment, 1)

            C_StockingRate = calculate.update(
                C_StockingRate,
                inflow=C_Stocking,
                outflow=C_Destocking,
                dt=dt
            )
            D_InitLakeVol = calculate.update(
                D_InitLakeVol,
                inflow=O_InitLake,
                dt=dt
            )
            D_InitRivVol = calculate.update(
                D_InitRivVol,
                inflow=O_InitRiv,
                dt=dt
            )
            O_CumBaseFlow = calculate.update(
                O_CumBaseFlow,
                inflow=O_BaseFlowAcc,
                dt=dt
            )
            O_CumDeepInfilt = calculate.update(
                O_CumDeepInfilt,
                inflow=O_DeepInfAcc,
                dt=dt
            )
            O_CumEvapotrans = calculate.update(
                O_CumEvapotrans,
                inflow=O_EvapoTransAcc,
                dt=dt
            )
            O_CumInfiltration = calculate.update(
                O_CumInfiltration,
                inflow=O_InfAcc,
                dt=dt
            )
            O_CumIntercE = calculate.update(
                O_CumIntercE,
                inflow=O_AccET,
                dt=dt
            )
            O_CumIntercepEvap = calculate.update(
                O_CumIntercepEvap,
                inflow=O_IntercAcc,
                dt=dt
            )
            O_CumPercolation = calculate.update(
                O_CumPercolation,
                inflow=O_PercAcc,
                dt=dt
            )
            O_CumRain = calculate.update(
                O_CumRain,
                inflow=O_RainAcc,
                dt=dt
            )
            O_CumSoilQFlow = calculate.update(
                O_CumSoilQFlow,
                inflow=O_SoilQFlowAcc,
                dt=dt
            )
            O_CumSoilQFlow_Subca_1 = calculate.update(
                O_CumSoilQFlow_Subca_1,
                inflow=O_SoilQflow_Subca,
                dt=dt
            )
            O_CumSurfQFlow = calculate.update(
                O_CumSurfQFlow,
                inflow=O_SurfQFlowAcc,
                dt=dt
            )
            O_CumTransp = calculate.update(
                O_CumTransp,
                inflow=O_TranspAcc,
                dt=dt
            )
            O_InitGWStock = calculate.update(
                O_InitGWStock,
                inflow=O_InitGW,
                dt=dt
            )
            O_InitSoilW = calculate.update(
                O_InitSoilW,
                inflow=O_InitSW,
                dt=dt
            )
            O_RainYest = calculate.update(
                O_RainYest,
                inflow=O_RainToday,
                outflow=O_RainYesterday,
                dt=dt
            )
            G_GrassStandingBiomass = calculate.update(
                G_GrassStandingBiomass,
                inflow=G_GrowthRate,
                outflow=G_Grazing+G_LeafMortality,
                dt=dt
            )
            G_SurfaceLitter = calculate.update(
                G_SurfaceLitter,
                inflow=G_LitterDeposition,
                outflow=G_Incorporation_DecaySurfLit,
                dt=dt
            )
            G_SurfManure = calculate.update(
                G_SurfManure,
                inflow=G_FaecesProd,
                outflow=G_Incorporation_DecayManure,
                dt=dt
            )
            isI_WarmEdUp = calculate.update(
                isI_WarmEdUp,
                inflow=I_Warmedup,
                dt=dt
            )
            O_CumDebitData = calculate.update(
                O_CumDebitData,
                inflow=I_RFlowdata_mmday,
                dt=dt
            )
            L_CumEvapLake = calculate.update(
                L_CumEvapLake,
                inflow=L_EvapLake,
                outflow=L_RestartE,
                dt=dt
            )
            L_CumHEPPUse = calculate.update(
                L_CumHEPPUse,
                inflow=L_HEPPWatUseFlow,
                outflow=L_RestartH,
                dt=dt
            )
            L_CumRivOutFlow = calculate.update(
                L_CumRivOutFlow,
                inflow=L_RivOutFlow,
                outflow=L_RestartR,
                dt=dt
            )
            L_LakeVol = calculate.update(
                L_LakeVol,
                inflow=L_InFlowtoLake,
                outflow=L_EvapLake + L_RivOutFlow + L_HEPPWatUseFlow,
                dt=dt
            )
            O_BestYyHEPP = calculate.update(
                O_BestYyHEPP,
                inflow=O_BYP,
                dt=dt
            )
            O_Ch_inGWStock = calculate.update(
                O_Ch_inGWStock,
                inflow=O_Ch_in_GWStockMP,
                dt=dt
            )
            O_Ch_inWStock = calculate.update(
                O_Ch_inWStock,
                inflow=O_Ch_in_WStockMP,
                dt=dt
            )
            O_CumBaseFlowMP = calculate.update(
                O_CumBaseFlowMP,
                inflow=O_BaseFlowAccMP,
                dt=dt
            )
            O_CumDebitDataMP = calculate.update(
                O_CumDebitDataMP,
                inflow=O_DebitDataAccMP,
                dt=dt
            )
            O_CumDebitPredMP = calculate.update(
                O_CumDebitPredMP,
                inflow=O_DebitPredAccMP,
                dt=dt
            )
            O_CumEvapLakeMP = calculate.update(
                O_CumEvapLakeMP,
                inflow=O_EvapLakeMP,
                dt=dt
            )
            O_CumEvapTransMP = calculate.update(
                O_CumEvapTransMP,
                inflow=O_Ch_in_EvapoTrans,
                dt=dt
            )
            O_CumGWMP = calculate.update(
                O_CumGWMP,
                inflow=O_GWAccMP,
                dt=dt
            )
            O_CumHEPPOutFlowMP = calculate.update(
                O_CumHEPPOutFlowMP,
                inflow=O_HEPPOutFlowMP,
                dt=dt
            )
            O_CumInfiltrationMP = calculate.update(
                O_CumInfiltrationMP,
                inflow=O_InfAccMP,
                dt=dt
            )
            O_CumIntercEvapMP = calculate.update(
                O_CumIntercEvapMP,
                inflow=O_IntercAccMP,
                dt=dt
            )
            O_CumRainMP = calculate.update(
                O_CumRainMP,
                inflow=O_RainAccMP,
                dt=dt
            )
            O_CumRivInflowtoLakeMP = calculate.update(
                O_CumRivInflowtoLakeMP,
                inflow=O_RivInflowtoLakeMP,
                dt=dt
            )
            O_CumRivOutFlowMP = calculate.update(
                O_CumRivOutFlowMP,
                inflow=O_RivOutFlowMP,
                dt=dt
            )
            O_CumSoilQFlowMP = calculate.update(
                O_CumSoilQFlowMP,
                inflow=O_SoilQFlowAccMP,
                dt=dt
            )
            O_CumSoilWMP = calculate.update(
                O_CumSoilWMP,
                inflow=O_SoilWAccMP,
                dt=dt
            )
            O_CumSurfQFlowMP = calculate.update(
                O_CumSurfQFlowMP,
                inflow=O_SurfQFlowAccMP,
                dt=dt
            )
            O_CumTranspMP = calculate.update(
                O_CumTranspMP,
                inflow=O_TranspAccMP,
                dt=dt
            )
            O_DeltaCatchmStMP = calculate.update(
                O_DeltaCatchmStMP,
                inflow=O_Ch_in_CatchmStMP,
                dt=dt
            )
            O_Hepp_Kwh_per_dayMP = calculate.update(
                O_Hepp_Kwh_per_dayMP,
                inflow=O_Hepp_ElctrProd,
                dt=dt
            )
            O_InitEvapoMP = calculate.update(
                O_InitEvapoMP,
                inflow=O_Ch_EvapoTran,
                dt=dt
            )
            O_InitGWStockMP = calculate.update(
                O_InitGWStockMP,
                inflow=O_ChGWMP,
                dt=dt
            )
            O_InitSWMP = calculate.update(
                O_InitSWMP,
                inflow=O_ChSoilWMP,
                dt=dt
            )
            O_LastYHepp = calculate.update(
                O_LastYHepp,
                inflow=O_HeppUseF1,
                outflow=O_HeppUseF2,
                dt=dt
            )
            O_ThisYHepp = calculate.update(
                O_ThisYHepp,
                inflow=O_HeppUseF0,
                outflow=O_HeppUseF1,
                dt=dt
            )
            O_WorstYHEPP = calculate.update(
                O_WorstYHEPP,
                inflow=O_WYP,
                dt=dt
            )
            O_YearSim = calculate.update(
                O_YearSim,
                inflow=Yearly_Tick,
                dt=dt
            )
            D_CumEvapTranspClass = calculate.update(
                D_CumEvapTranspClass,
                inflow=D_ActEvapTransp + D_InterceptEvap,
                dt=dt
            )
            D_CumNegRain = calculate.update(
                D_CumNegRain,
                outflow=(
                    D_InterceptEvap +
                    D_Infiltration +
                    D_DeepInfiltration +
                    D_SurfaceFlow
                ),
                dt=dt,
                non_negative=True
            )
            # print 'D_EvapTranspClass', D_EvapTranspClass[time].shape, D_EvapTranspClass[time]
            D_EvapTranspClass = calculate.update(
                D_EvapTranspClass,
                inflow=D_WaterEvapIrrigation,
                dt=dt
            )
            D_GWArea = calculate.update(
                D_GWArea,
                inflow=np.add(np.sum(D_Percolation, axis=1).reshape(subcatchment, 1), D_DeepInfiltration),
                outflow=np.add(
                    D_GWaDisch,
                    np.sum(D_WaterEvapIrrigation, axis=1).reshape(subcatchment, 1)
                ),
                dt=dt
            )
            D_SoilWater = calculate.update(
                D_SoilWater,
                inflow=D_Infiltration,
                outflow=(
                    D_ActEvapTransp +
                    D_Percolation +
                    D_SoilDischarge
                ),
                dt=dt
            )
            S_RelBulkDensity = calculate.update(
                S_RelBulkDensity,
                inflow=(
                    S_StructureFormation +
                    S_RippingSurface +
                    S_SplashErosion
                ),
                outflow=S_Compaction,
                dt=dt
            )
            D_CumInflowtoLake = calculate.update(
                D_CumInflowtoLake,
                inflow=D_RiverFlowtoLake + D_GWtoLake,
                outflow=D_RestartL,
                dt=dt
            )
            D_CumTotRiverFlow = calculate.update(
                D_CumTotRiverFlow,
                inflow=D_RiverDelay + D_RiverDirect,
                outflow=D_RestartR,
                dt=dt
            )
            D_StreamsSurfQ = calculate.update_conveyor(
                stock=D_StreamsSurfQ,
                inflow=D_SurfFlowObsPoint,
                outflow=D_SurfFlowRiver,
                transitTime=SurFlowRiverTransitTime,
                time=time,
                dt=dt
            )
            D_TotRiverFlowNoDelay = calculate.update(
                D_TotRiverFlowNoDelay,
                inflow=D_SurfFlowRiver[time] + D_DirectSurfFkowObsPoint,
                outflow=D_RiverDelay + D_RivInflLake,
                dt=dt
            )
            D_CumResvEvap = calculate.update(
                D_CumResvEvap,
                inflow=D_EvaporReservoir,
                dt=dt
            )
            D_SubcResVol = calculate.update(
                D_SubcResVol,
                inflow=D_SubcResVol + D_Influx_to_Resr,
                outflow=D_EvaporReservoir + D_SubCResOutflow,
                dt=dt
            )
            # self.output['map']['O_EvapoTransAcc'].append(
            #     np.sum(D_ActEvapTransp +
            #     D_InterceptEvap, axis=1).reshape(subcatchment, 1)
            # )

            # self.output['timeseries'] = {
            self.output['timeseries']['I_RFlowdata_mmday'][time] =  I_RFlowdata_mmday
            self.output['timeseries']['L_InFlowtoLake'][time] =  L_InFlowtoLake
            self.output['timeseries']['O_RainAcc'][time] =  O_RainAcc
            self.output['timeseries']['O_IntercAcc'][time] =  O_IntercAcc
            self.output['timeseries']['O_EvapoTransAcc'][time] =  O_EvapoTransAcc
            self.output['timeseries']['O_SurfQFlowAcc'][time] =  O_SurfQFlowAcc
            self.output['timeseries']['O_InfAcc'][time] =  O_InfAcc
            # self.output['timeseries'][]# 'O_RainAcc'][time: = O_RainAcc
            self.output['timeseries']['O_DeepInfAcc'][time] =  O_DeepInfAcc
            self.output['timeseries']['O_PercAcc'][time] =  O_PercAcc
            self.output['timeseries']['O_BaseFlowAcc'][time] =  O_BaseFlowAcc
            self.output['timeseries']['O_SoilQFlowAcc'][time] =  O_SoilQFlowAcc
            self.output['timeseries']['O_CumRain'][time] =  O_CumRain
            self.output['timeseries']['O_CumIntercepEvap'][time] =  O_CumIntercepEvap
            self.output['timeseries']['O_CumEvapotrans'][time] =  O_CumEvapotrans
            self.output['timeseries']['O_CumSurfQFlow'][time] =  O_CumSurfQFlow
            self.output['timeseries']['O_CumInfiltration'][time] =  O_CumInfiltration
            # self.output['timeseries'][]# 'O_CumRain'][time: = O_CumRain
            self.output['timeseries']['O_CumPercolation'][time] =  O_CumPercolation
            self.output['timeseries']['O_CumDeepInfilt'][time] =  O_CumDeepInfilt
            self.output['timeseries']['O_CumBaseFlow'][time] =  O_CumBaseFlow
            self.output['timeseries']['O_CumSoilQFlow'][time] =  O_CumSoilQFlow
            self.output['timeseries']['L_HEPPWatUseFlow'][time] =  L_HEPPWatUseFlow
            self.output['timeseries']['L_LakeVol'][time] =  L_LakeVol
            self.output['timeseries']['L_HEPP_Kwh'][time] =  L_HEPP_Kwh
            self.output['timeseries']['L_LakeLevel'][time] =  L_LakeLevel
            # }

            # self.output['map'] = {
            self.output['map']['O_EvapoTransAcc'][time] = np.sum(D_ActEvapTransp +
            D_InterceptEvap, axis=1).reshape(subcatchment, 1)
            self.output['map']['L_InFlowtoLake'][time] = (O_InFlowtoLake)
            self.output['map']['O_PercAcc'][time] = (np.sum(D_Percolation, axis=1).reshape(subcatchment, 1))
            self.output['map']['O_RainAcc'][time] = (np.sum(I_DailyRainAmount, axis=1).reshape(subcatchment, 1))
            self.output['map']['O_SurfQFlowAcc'][time] = (D_SurfaceFlow)
            self.output['map']['O_BaseFlowAcc'][time] = (
                np.sum(np.multiply(
                    D_GWaDisch,
                    np.multiply(I_Simulation_Time >= O_StartMDay,
                                np.multiply(I_Simulation_Time < O_EndMDay,
                                            isI_StillWarmUp == 0)).transpose()
                ), axis=1).reshape(subcatchment, 1)
            )
            self.output['map']['O_DeepInfAcc'][time] = ( D_DeepInfiltration )
            self.output['map']['O_IntercAcc'][time] = (np.sum(D_InterceptEvap, axis=1).reshape(subcatchment, 1))
            self.output['map']['O_SoilQFlowAcc'][time] = (np.sum(D_SoilDischarge, axis=1).reshape(subcatchment, 1))
            self.output['map']['O_InfAcc'][time] = (np.sum(D_Infiltration, axis=1).reshape(subcatchment, 1))
            self.output['map']['D_GWaDisch'][time] = (D_GWaDisch)
            self.output['map']['D_SoilDischarge'][time] = (np.sum(D_SoilDischarge, axis=1).reshape(subcatchment, 1))
            # }

            # self.output['map']['L_InFlowtoLake'].append(O_InFlowtoLake)
            # self.output['map']['O_PercAcc'].append(np.sum(D_Percolation, axis=1).reshape(subcatchment, 1))
            # self.output['map']['O_RainAcc'].append(np.sum(I_DailyRainAmount, axis=1).reshape(subcatchment, 1))
            # self.output['map']['O_SurfQFlowAcc'].append(D_SurfaceFlow)
            # self.output['map']['O_BaseFlowAcc'].append(
            #     np.sum(np.multiply(
            #         D_GWaDisch,
            #         np.multiply(I_Simulation_Time >= O_StartMDay,
            #                     np.multiply(I_Simulation_Time < O_EndMDay,
            #                                 isI_StillWarmUp == 0)).transpose()
            #     ), axis=1).reshape(subcatchment, 1)
            # )
            # self.output['map']['O_DeepInfAcc'].append(
            #     D_DeepInfiltration
            # )
            # self.output['map']['O_IntercAcc'].append(np.sum(D_InterceptEvap, axis=1).reshape(subcatchment, 1))
            # self.output['map']['O_SoilQFlowAcc'].append(np.sum(D_SoilDischarge, axis=1).reshape(subcatchment, 1))
            # self.output['map']['O_InfAcc'].append(np.sum(D_Infiltration, axis=1).reshape(subcatchment, 1))
            # self.output['map']['D_GWaDisch'].append(D_GWaDisch)
            # self.output['map']['D_SoilDischarge'].append(np.sum(D_SoilDischarge, axis=1).reshape(subcatchment, 1))


            # Display Water Balance
            # self.output['timeseries']['display']['Water Balance']['Page 1']['I_RFlowdata_mmday'].append(I_RFlowdata_mmday)
            # self.output['timeseries']['display']['Water Balance']['Page 1']['L_InFlowtoLake'].append(L_InFlowtoLake)
            #
            # self.output['timeseries']['display']['Water Balance']['Page 2']['O_RainAcc'].append(O_RainAcc)
            # self.output['timeseries']['display']['Water Balance']['Page 2']['O_IntercAcc'].append(O_IntercAcc)
            # self.output['timeseries']['display']['Water Balance']['Page 2']['O_EvapoTransAcc'].append(O_EvapoTransAcc)
            # self.output['timeseries']['display']['Water Balance']['Page 2']['O_SurfQFlowAcc'].append(O_SurfQFlowAcc)
            # self.output['timeseries']['display']['Water Balance']['Page 2']['O_InfAcc'].append(O_InfAcc)
            #
            # self.output['timeseries']['display']['Water Balance']['Page 3']['O_RainAcc'].append(O_RainAcc)
            # self.output['timeseries']['display']['Water Balance']['Page 3']['O_DeepInfAcc'].append(O_DeepInfAcc)
            # self.output['timeseries']['display']['Water Balance']['Page 3']['O_PercAcc'].append(O_PercAcc)
            # self.output['timeseries']['display']['Water Balance']['Page 3']['O_BaseFlowAcc'].append(O_BaseFlowAcc)
            # self.output['timeseries']['display']['Water Balance']['Page 3']['O_SoilQFlowAcc'].append(O_SoilQFlowAcc)
            #
            # self.output['timeseries']['display']['Water Balance']['Page 4']['O_CumRain'].append(O_CumRain)
            # self.output['timeseries']['display']['Water Balance']['Page 4']['O_CumIntercepEvap'].append(O_CumIntercepEvap)
            # self.output['timeseries']['display']['Water Balance']['Page 4']['O_CumEvapotrans'].append(O_CumEvapotrans)
            # self.output['timeseries']['display']['Water Balance']['Page 4']['O_CumSurfQFlow'].append(O_CumSurfQFlow)
            # self.output['timeseries']['display']['Water Balance']['Page 4']['O_CumInfiltration'].append(O_CumInfiltration)
            #
            # self.output['timeseries']['display']['Water Balance']['Page 5']['O_CumRain'].append(O_CumRain)
            # self.output['timeseries']['display']['Water Balance']['Page 5']['O_CumPercolation'].append(O_CumPercolation)
            # self.output['timeseries']['display']['Water Balance']['Page 5']['O_CumDeepInfilt'].append(O_CumDeepInfilt)
            # self.output['timeseries']['display']['Water Balance']['Page 5']['O_CumBaseFlow'].append(O_CumBaseFlow)
            # self.output['timeseries']['display']['Water Balance']['Page 5']['O_CumSoilQFlow'].append(O_CumSoilQFlow)
            # print O_CumPercolation
            # Display HEPP
            # self.output['timeseries']['display']['HEPP']['L_HEPPWatUseFlow'].append(L_HEPPWatUseFlow)
            # self.output['timeseries']['display']['HEPP']['L_LakeVol'].append(L_LakeVol)
            # self.output['timeseries']['display']['HEPP']['L_HEPP_Kwh'].append(L_HEPP_Kwh)
            # self.output['timeseries']['display']['HEPP']['L_LakeLevel'].append(L_LakeLevel)

            # Data Water Balance:
            # self.output['timeseries']['data']['Water Balance']['I_RFlowdata_mmday'].append(I_RFlowdata_mmday)
            # self.output['timeseries']['data']['Water Balance']['L_InFlowtoLake'].append(L_InFlowtoLake)
            # self.output['timeseries']['data']['Water Balance']['O_RainAcc'].append(O_RainAcc)
            # self.output['timeseries']['data']['Water Balance']['O_IntercAcc'].append(O_IntercAcc)
            # self.output['timeseries']['data']['Water Balance']['O_EvapoTransAcc'].append(O_EvapoTransAcc)
            # self.output['timeseries']['data']['Water Balance']['O_SoilQFlowAcc'].append(O_SoilQFlowAcc)
            # self.output['timeseries']['data']['Water Balance']['O_InfAcc'].append(O_InfAcc)
            # self.output['timeseries']['data']['Water Balance']['O_PercAcc'].append(O_PercAcc)
            # self.output['timeseries']['data']['Water Balance']['O_DeepInfAcc'].append(O_DeepInfAcc)
            # self.output['timeseries']['data']['Water Balance']['O_BaseFlowAcc'].append(O_BaseFlowAcc)
            # self.output['timeseries']['data']['Water Balance']['O_SurfQFlowAcc'].append(O_SurfQFlowAcc)

            # Data Watershed Indicator
            # self.output['timeseries']['data']['Watershed Indicator']['I_RainDoY'].append(I_RainDoY)
            # self.output['timeseries']['data']['Watershed Indicator']['L_InFlowtoLake'].append(L_InFlowtoLake)
            # self.output['timeseries']['data']['Watershed Indicator']['O_RainAcc'].append(O_RainAcc)
            # self.output['timeseries']['data']['Watershed Indicator']['O_IntercAcc'].append(O_IntercAcc)
            # self.output['timeseries']['data']['Watershed Indicator']['O_EvapoTransAcc'].append(O_EvapoTransAcc)
            # self.output['timeseries']['data']['Watershed Indicator']['O_SoilQFlowAcc'].append(O_SoilQFlowAcc)
            # self.output['timeseries']['data']['Watershed Indicator']['O_InfAcc'].append(O_InfAcc)
            # self.output['timeseries']['data']['Watershed Indicator']['O_PercAcc'].append(O_PercAcc)
            # self.output['timeseries']['data']['Watershed Indicator']['I_RFlowdata_mmday'].append(I_RFlowdata_mmday)
            # self.output['timeseries']['data']['Watershed Indicator']['O_SurfQFlowAcc'].append(O_SurfQFlowAcc)

            # Data HEPP
            # self.output['timeseries']['data']['HEPP']['O_BestYyHEPP'].append(O_BestYyHEPP[time])
            # self.output['timeseries']['data']['HEPP']['O_WorstYHEPP'].append(O_WorstYHEPP[time])
            # self.output['timeseries']['data']['HEPP']['L_CumHEPPUse'].append(L_CumHEPPUse[time])
            # self.output['timeseries']['data']['HEPP']['O_FrBaseFlow'].append(O_FrBaseFlow)
            # self.output['timeseries']['data']['HEPP']['O_FrSoilQuickFlow'].append(O_SoilQFlowAcc)
            # self.output['timeseries']['data']['HEPP']['O_FrSurfQuickFlow'].append(O_SurfQFlowAcc)

            # self.output['timeseries']['I_RFlowdata_mmday'].append(I_RFlowdata_mmday)
            #
            # self.output['timeseries']['L_InFlowtoLake'].append(L_InFlowtoLake)
            # self.output['timeseries']['O_EvapoTransAcc'].append(O_EvapoTransAcc)
            #
            #
            # self.output['timeseries']['O_PercAcc'].append(O_PercAcc)
            #
            # self.output['timeseries']['O_RainAcc'].append(O_RainAcc)
            #
            # self.output['timeseries']['O_SurfQFlowAcc'].append(O_SurfQFlowAcc)
            #
            # self.output['timeseries']['O_BaseFlowAcc'].append(O_BaseFlowAcc)
            #
            # self.output['timeseries']['O_DeepInfAcc'].append(O_DeepInfAcc)
            #
            # self.output['timeseries']['O_IntercAcc'].append(O_IntercAcc)
            #
            # self.output['timeseries']['O_SoilQFlowAcc'].append(O_SoilQFlowAcc)
            #
            # self.output['timeseries']['O_InfAcc'].append(O_InfAcc)
            #
            # self.output['timeseries']['I_RainDoY'].append(I_RainDoY)
            # self.output['timeseries']['L_RivOutFlow'].append(L_RivOutFlow)
            # self.output['timeseries']['I_DailyRain'].append(I_DailyRain[0])
            # self.output['timeseries']['L_HEPPWatUseFlow'].append(L_HEPPWatUseFlow)
            # self.output['timeseries']['L_HEPP_Kwh'].append(L_HEPP_Kwh)
            # self.output['timeseries']['L_LakeVol'].append(L_LakeVol[time])
            # self.output['timeseries']['L_LakeLevel'].append(L_LakeLevel)
            # self.output['timeseries']['O_BestYyHEPP'].append(O_BestYyHEPP[time])
            # self.output['timeseries']['O_WorstYHEPP'].append(O_WorstYHEPP[time])
            # self.output['timeseries']['L_CumHEPPUse'].append(L_CumHEPPUse[time])
            # self.output['timeseries']['O_FrBaseFlow'].append(O_FrBaseFlow)
            # self.output['timeseries']['O_FrSoilQuickFlow'].append(O_FrSoilQuickFlow)
            # self.output['timeseries']['I_DailyRainAmount'].append(np_utils.array_sum(I_DailyRainAmount))
            # self.output['timeseries']['D_SurfaceFlow'].append(np_utils.array_sum(D_SurfaceFlow))

            excel_utils.write_params(self.waterBalanceSheet, time + 1,
                                     'Days', time,
                                     'L_InFlowtoLake', L_InFlowtoLake,
                                     'I_RFlowdata_mmday', I_RFlowdata_mmday,
                                     'O_RainAcc', O_RainAcc,
                                     'O_IntercAcc', O_IntercAcc,
                                     'O_EvapoTransAcc', O_EvapoTransAcc,
                                     'O_SurfQFlowAcc', O_SurfQFlowAcc,
                                     'O_InfAcc', O_InfAcc,
                                     'O_PercAcc' ,O_PercAcc,
                                     'O_DeepInfAcc', O_DeepInfAcc,
                                     'O_BaseFlowAcc', O_BaseFlowAcc,
                                     'O_SoilQFlowAcc', O_SoilQFlowAcc,
                                     'O_CumRain', O_CumRain,
                                     'O_CumSurfQFlow', O_CumSurfQFlow,
                                     'O_CumEvapotrans', O_CumEvapotrans,
                                     'O_CumInfiltration', O_CumInfiltration,
                                     'O_CumIntercepEvap', O_CumIntercepEvap,
                                     'O_CumBaseFlow', O_CumBaseFlow,
                                     'O_CumPercolation', O_CumPercolation,
                                     'O_CumSoilQFlow', O_CumSoilQFlow,
                                     'O_CumDeepInInflt', O_CumDeepInfilt,
                                     )
            excel_utils.write_params(self.heppSheet, time + 1,
                                     'Days', time,
                                     'L_HEPPWatUseFlow', L_HEPPWatUseFlow,
                                     'L_LakeVol', L_LakeVol,
                                     'L_LakeLevel', L_LakeLevel,
                                     'L_HEPP_Kwh', L_HEPP_Kwh
                                     )

            # self.emit(QtCore.SIGNAL('update'), self.output, time)
            self.emit(QtCore.SIGNAL('update'), time)
            self.emit(QtCore.SIGNAL('updateTimeseries'), self.output['timeseries'], time)
            self.emit(QtCore.SIGNAL('updateMap'), self.output['map'], time)
            time = time + dt

            if time >= self.simulationTime:
                self.outputWb.save('Output Timeseries.xls')
