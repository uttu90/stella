from PyQt4 import QtCore
import numpy as np
from utils import np_utils
import spatrain
import calculate
import constants


class SimulatingThread(QtCore.QThread):
    def __init__(self, parameters, data):
        super(SimulatingThread, self).__init__()
        self.stopped = False
        self.parameters = parameters
        self.data = data
        self.output = {}
        self.output['map'] = {}
        self.output['timeseries'] = {}

        self.output['map']['L_InFlowtoLake'] = []
        self.output['map']['O_RainAcc'] = []
        self.output['map']['O_IntercAcc'] = []
        self.output['map']['O_EvapoTransAcc'] = []
        self.output['map']['O_SoilQFlowAcc'] = []
        self.output['map']['O_InfAcc'] = []
        self.output['map']['O_PercAcc'] = []
        self.output['map']['O_DeepInfAcc'] = []
        self.output['map']['O_BaseFlowAcc'] = []
        self.output['map']['O_SurfQFlowAcc'] = []
        self.output['map']['D_SoilDischarge'] = []
        self.output['map']['D_GWaDisch'] = []

        # Display Water Balance
        self.output['timeseries']['display'] = {}
        self.output['timeseries']['display']['Water Balance'] = {}
        self.output['timeseries']['display']['Water Balance']['I_RFlowdata_mmday'] = []
        self.output['timeseries']['display']['Water Balance']['L_InFlowtoLake'] = []

        # Display HEPP
        self.output['timeseries']['display']['HEPP'] = {}
        self.output['timeseries']['display']['HEPP']['L_HEPPWatUseFlow'] = []
        self.output['timeseries']['display']['HEPP']['L_LakeVol'] = []
        self.output['timeseries']['display']['HEPP']['L_HEPP_Kwh'] = []
        self.output['timeseries']['display']['HEPP']['L_LakeLevel'] = []

        # Data Water Balance:
        self.output['timeseries']['data'] = {}
        self.output['timeseries']['data']['Water Balance'] = {}
        self.output['timeseries']['data']['Water Balance']['I_RFlowdata_mmday'] = []
        self.output['timeseries']['data']['Water Balance']['L_InFlowtoLake'] = []
        self.output['timeseries']['data']['Water Balance']['O_RainAcc'] = []
        self.output['timeseries']['data']['Water Balance']['O_IntercAcc'] = []
        self.output['timeseries']['data']['Water Balance']['O_EvapoTransAcc'] = []
        self.output['timeseries']['data']['Water Balance']['O_SoilQFlowAcc'] = []
        self.output['timeseries']['data']['Water Balance']['O_InfAcc'] = []
        self.output['timeseries']['data']['Water Balance']['O_PercAcc'] = []
        self.output['timeseries']['data']['Water Balance']['O_DeepInfAcc'] = []
        self.output['timeseries']['data']['Water Balance']['O_BaseFlowAcc'] = []
        self.output['timeseries']['data']['Water Balance']['O_SurfQFlowAcc'] = []

        # Data Watershed Indicator
        self.output['timeseries']['data']['Watershed Indicator'] = {}
        self.output['timeseries']['data']['Watershed Indicator']['I_RainDoY'] = []
        self.output['timeseries']['data']['Watershed Indicator']['L_InFlowtoLake'] = []
        self.output['timeseries']['data']['Watershed Indicator']['O_RainAcc'] = []
        self.output['timeseries']['data']['Watershed Indicator']['O_IntercAcc'] = []
        self.output['timeseries']['data']['Watershed Indicator']['O_EvapoTransAcc'] = []
        self.output['timeseries']['data']['Watershed Indicator']['O_SoilQFlowAcc'] = []
        self.output['timeseries']['data']['Watershed Indicator']['O_InfAcc'] = []
        self.output['timeseries']['data']['Watershed Indicator']['O_PercAcc'] = []
        self.output['timeseries']['data']['Watershed Indicator']['I_RFlowdata_mmday'] = []
        self.output['timeseries']['data']['Watershed Indicator']['O_SurfQFlowAcc'] = []

        # Data HEPP
        self.output['timeseries']['data']['HEPP'] = {}
        self.output['timeseries']['data']['HEPP']['O_BestYyHEPP'] = []
        self.output['timeseries']['data']['HEPP']['O_WorstYHEPP'] = []
        self.output['timeseries']['data']['HEPP']['L_CumHEPPUse'] = []
        self.output['timeseries']['data']['HEPP']['O_FrBaseFlow'] = []
        self.output['timeseries']['data']['HEPP']['O_FrSoilQuickFlow'] = []
        self.output['timeseries']['data']['HEPP']['O_FrSurfQuickFlow'] = []

        # self.output['timeseries']['O_RainAcc'] = []
        # self.output['timeseries']['O_IntercAcc'] = []
        # self.output['timeseries']['O_EvapoTransAcc'] = []
        # self.output['timeseries']['O_SoilQFlowAcc'] = []
        # self.output['timeseries']['O_InfAcc'] = []
        # self.output['timeseries']['O_PercAcc'] = []
        # self.output['timeseries']['O_DeepInfAcc'] = []
        # self.output['timeseries']['O_BaseFlowAcc'] = []
        # self.output['timeseries']['O_SurfQFlowAcc'] = []
        # self.output['timeseries']['I_RainDoY'] = []
        # self.output['timeseries']['L_RivOutFlow'] = []
        # self.output['timeseries']['I_DailyRain'] = []
        # self.output['timeseries']['L_HEPPWatUseFlow'] = []
        # self.output['timeseries']['L_HEPP_Kwh'] = []
        # self.output['timeseries']['L_LakeVol'] = []
        # self.output['timeseries']['L_LakeLevel'] = []
        # self.output['timeseries']['O_BestYyHEPP'] = []
        # self.output['timeseries']['O_WorstYHEPP'] = []
        # self.output['timeseries']['L_CumHEPPUse'] = []
        # self.output['timeseries']['O_FrBaseFlow'] = []
        # self.output['timeseries']['O_FrSoilQuickFlow'] = []
        # self.output['timeseries']['I_DailyRainAmount'] = []
        # self.output['timeseries']['D_SurfaceFlow'] = []

    def __del__(self):
        self.wait()

    def stop(self):
        self.stopped = True
        print "stop triggered"

    def run(self):
        run_specs = self.parameters['Run_Specs']
        begin = int(run_specs['runfrom'])
        end = int(run_specs['runto'])
        dt = int(run_specs['rundt'])
        obsPoint = 8
        vegClass = 20
        measurePeriod = 3
        subcatchment = 20
        print self.stopped
        self.stopped = False
        initial_run = self.parameters['Initial_Run']
        simulationTime = int(initial_run['simulationTime'])
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

        I_Evapotrans = self.data['I_Evapotrans']
        insert_value = [0 for _ in range(12)]
        I_MultiplierEvapoTrans = np.column_stack(
            (np.array(self.data['I_MultiplierEvapoTrans']),
             insert_value, insert_value, insert_value,
             insert_value, insert_value, insert_value,
             insert_value, insert_value, insert_value,)
        )
        I_MultiplierEvapoTrans = [
            I_MultiplierEvapoTrans[i].reshape(1, vegClass)
            for i in range(12)
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
        I_DailyRainYear = [
            I_DailyRainYear_1_to_4,
            I_DailyRainYear_5_to_8,
            I_DailyRainYear_9_to_12,
            I_DailyRainYear_13_to_16,
            I_DailyRainYear_17_to_20,
            I_DailyRainYear_21_to_24,
            I_DailyRainYear_25_to_28,
        ]

        I_Daily_Evap_1_to_4 = self.data['I_Daily_Evap_1_to_4']
        I_Daily_Evap_5_to_8 = self.data['I_Daily_Evap_5_to_8']
        I_Daily_Evap_9_to_12 = self.data['I_Daily_Evap_9_to_12']
        I_Daily_Evap_13_to_16 = self.data['I_Daily_Evap_13_to_16']
        I_Daily_Evap_17_to_20 = self.data['I_Daily_Evap_17_to_20']
        I_Daily_Evap_21_to_24 = self.data['I_Daily_Evap_21_to_24']
        I_Daily_Evap_25_to_28 = self.data['I_Daily_Evap_25_to_28']
        I_Daily_Evap_29_to_32 = self.data['I_Daily_Evap_29_to_32']
        I_Daily_Evap = [
            I_Daily_Evap_1_to_4,
            I_Daily_Evap_5_to_8,
            I_Daily_Evap_9_to_12,
            I_Daily_Evap_13_to_16,
            I_Daily_Evap_17_to_20,
            I_Daily_Evap_21_to_24,
            I_Daily_Evap_25_to_28,
            I_Daily_Evap_29_to_32,
        ]

        I_RFlowData_Year_1_to_4 = self.data['I_RFlowData Year_1_to_4']
        I_RFlowData_Year_5_to_8 = self.data['I_RFlowData Year_5_to_8']
        I_RFlowData_Year_9_to_12 = self.data['I_RFlowData Year_9_to_12']
        I_RFlowData_Year_13_to_16 = self.data['I_RFlowData Year_13_to_16']
        I_RFlowData_Year_17_to_20 = self.data['I_RFlowData Year_17_to_20']
        I_RFlowData_Year_21_to_24 = self.data['I_RFlowData Year_21_to_24']
        I_RFlowData_Year_25_to_28 = self.data['I_RFlowData Year_25_to_28']
        I_RFlowData_Year_29_to_32 = self.data['I_RFlowData Year_29_to_32']

        I_RFlowData = [
            I_RFlowData_Year_1_to_4,
            I_RFlowData_Year_5_to_8,
            I_RFlowData_Year_9_to_12,
            I_RFlowData_Year_13_to_16,
            I_RFlowData_Year_17_to_20,
            I_RFlowData_Year_21_to_24,
            I_RFlowData_Year_25_to_28,
            I_RFlowData_Year_29_to_32,
        ]
        I_InputDataYears = self.data['I_InputDataYears']
        I_InterceptClass = np.array(
            self.data['I_InterceptClass'] + [0 for _ in range(0,9)]
        ).reshape(vegClass, 1)
        I_RelDroughtFact = np.array(
            self.data['I_RelDroughtFact'] +
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ).reshape(vegClass, 1)
        I_Area = np.array(
            self.data['I_Area']
        ).reshape(subcatchment, 1)
        I_RoutingDistanceLoad = np.array(
            self.data['I_RoutingDistance']
        )
        insert_value = [-1 for _ in range(20)]
        I_RoutingDistance = np.column_stack((
            I_RoutingDistanceLoad,
            insert_value,
        ))

        # Initial stock value

        time = 0
        C_StockingRate = [1]
        D_InitLakeVol = [0]
        D_InitRivVol = [0]
        O_CumBaseFlow = [0]
        O_CumDeepInfilt = [0]
        O_CumEvapotrans = [0]
        O_CumInfiltration = [0]
        O_CumIntercE = [0]
        O_CumIntercepEvap = [0]
        O_CumPercolation = [0]
        O_CumRain = [0]
        O_CumSoilQFlow = [0]
        O_CumSoilQFlow_Subca_1 = [np.zeros(shape=(subcatchment, obsPoint))]
        O_CumSurfQFlow = [0]
        O_CumTransp = [0]
        O_RainYest = [np.zeros(shape=(subcatchment, 1))]
        G_GrassStandingBiomass = [np.ones(shape=(subcatchment, vegClass))]
        G_SurfaceLitter = [np.zeros(shape=(subcatchment, vegClass))]
        G_SurfManure = [np.zeros(shape=(subcatchment, vegClass))]
        isI_WarmEdUp = [0]
        O_CumDebitData = [0]
        L_CumEvapLake = [0]
        L_CumHEPPUse = [0]
        L_CumRivOutFlow = [0]
        I_TotalArea = np_utils.array_sum(I_Area)
        I_RelArea = I_Area / I_TotalArea
        L_LakeArea = np.multiply(isL_Lake == 1, I_RelArea)
        L_LakeElevPreHEPP = 362.3
        L_LakeBottomElev = 160
        L_OutflTrVolPreHEPP = (1000 *
                               (L_LakeElevPreHEPP - L_LakeBottomElev) *
                               np_utils.array_sum(L_LakeArea))
        L_LakeVol = [L_OutflTrVolPreHEPP * isL_HEPP_Active +
                     (1 - isL_HEPP_Active) * L_OutflTrVolPreHEPP]
        O_BestYyHEPP = [0]
        O_Ch_inGWStock = [np.zeros(shape=(1, measurePeriod))]
        O_Ch_inWStock = [np.zeros(shape=(1, measurePeriod))]
        O_CumBaseFlowMP = [np.zeros(shape=(1, measurePeriod))]
        O_CumDebitDataMP = [np.zeros(shape=(1, measurePeriod))]
        O_CumDebitPredMP = [np.zeros(shape=(1, measurePeriod))]
        O_CumEvapLakeMP = [np.zeros(shape=(1, measurePeriod))]
        O_CumEvapTransMP = [np.zeros(shape=(1, measurePeriod))]
        O_CumGWMP = [np.zeros(shape=(1, measurePeriod))]
        O_CumHEPPOutFlowMP = [np.zeros(shape=(1, measurePeriod))]
        O_CumInfiltrationMP = [np.zeros(shape=(1, measurePeriod))]
        O_CumIntercEvapMP = [np.zeros(shape=(1, measurePeriod))]
        O_CumRainMP = [np.zeros(shape=(1, measurePeriod))]
        O_CumRivInflowtoLakeMP = [np.zeros(shape=(1, measurePeriod))]
        O_CumRivOutFlowMP = [np.zeros(shape=(1, measurePeriod))]
        O_CumSoilQFlowMP = [np.zeros(shape=(1, measurePeriod))]
        O_CumSoilWMP = [np.zeros(shape=(1, measurePeriod))]
        O_CumSurfQFlowMP = [np.zeros(shape=(1, measurePeriod))]
        O_CumTranspMP = [np.zeros(shape=(1, measurePeriod))]
        O_DeltaCatchmStMP = [np.zeros(shape=(1, measurePeriod))]
        O_Hepp_Kwh_per_dayMP = [np.zeros(shape=(1, measurePeriod))]
        O_InitEvapoMP = [np.zeros(shape=(1, measurePeriod))]
        O_InitGWStockMP = [np.zeros(shape=(1, measurePeriod))]
        O_InitSWMP = [np.zeros(shape=(1, measurePeriod))]
        O_LastYHepp = [0]
        O_ThisYHepp = [0]
        O_WorstYHEPP = [1]
        O_YearSim = [1]
        D_CumEvapTranspClass = [np.zeros(shape=(subcatchment, vegClass))]
        D_CumNegRain = [np.zeros(shape=(subcatchment, 1))]
        D_EvapTranspClass = [np.zeros(shape=(subcatchment, vegClass))]
        I_InitMaxDynGWSub = I_MaxDynGWSub1
        I_MaxDynGWact = (np.multiply(isI_GWRelFracConst, I_MaxDynGWConst) +
                         np.multiply(1 - isI_GWRelFracConst, I_InitMaxDynGWSub))
        I_MaxDynGWArea = np.multiply(I_MaxDynGWact, I_RelArea)
        D_GWArea = [I_MaxDynGWArea * I_InitRelGW]
        O_InitGWStock = [np_utils.array_sum(I_MaxDynGWArea) * I_InitRelGW]
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
        O_InitSoilW = [np_utils.array_sum(I_InitAvailWaterClass) *
                       I_InitRelSoil]
        D_SoilWater = [I_InitAvailWaterClass * I_InitRelSoil]
        I_InitBD_BDRefVeg = I_TopSoilBD_BDRef1
        S_RelBulkDensity = [I_InitBD_BDRefVeg * np.ones(shape=(subcatchment, vegClass))]
        D_CumInflowtoLake = [0]
        D_CumTotRiverFlow = [np.zeros(shape=(subcatchment, obsPoint))]
        D_StreamsSurfQ = [np.zeros(shape=(subcatchment, obsPoint))]
        D_TotRiverFlowNoDelay = [np.zeros(shape=(subcatchment, obsPoint))]
        D_CumResvEvap = [0]
        L_ResrDepth = 10000
        D_ReservoirVol = L_ResrDepth * np.multiply(isL_Lake, I_RelArea)
        D_SubcResVol = [np.multiply(D_ReservoirVol, isI_DaminThisStream)]
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
        simulationTime = 100
        RainNormal = np.random.normal(1, I_Rain_IntensCoefVar, simulationTime)
        G_GrassFract_Biomass = np.array([0.2, 0.1, 0.05, 0.001, 0.4, 0.2, 0.1, 0.01, 0.3, 0.1, 0.2, 1, 1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]).reshape(vegClass, 1)

        # Init other params
        # D_RoutingTimeInit = I_RivFlowTimes[0]
        # D_SurfFlowTransitTime = np.Round()
        D_SurfFlowRiver = [0]
        while time < int(simulationTime) and not self.stopped:
            RainNormal[time]
            print time
            I_Simulation_Time = int(
                time +
                I_CaDOYStart +
                365 * I_RainYearStart -
                isI_WarmEdUp[time] * (I_WarmUpTime + 1))
            Simulation_Time = time % 1460
            I_Warmedup = 1 if time == int(I_WarmUpTime) else 0
            I_RainDoY = (I_Simulation_Time
                         if (isI_RainCycle == 0)
                         else 1 + I_Simulation_Time % 365)
            # I_Flag1 = 1 if I_Simulation_Time < I_InputDataYears[Trans1] else 0
            # I_Flag2 = (1
            #            if I_Simulation_Time < I_InputDataYears[Trans2]
            #               and I_Flag1 == 0
            #            else 0)
            # rain_time_stage = np_utils.get_stage(I_RainDoY, I_RainDoY_Stage)
            I_SpatRainTime = I_RainMultiplier * spatrain.I_SpatRain[I_RainDoY/1460][Simulation_Time]
            I_Daily_Evapotrans = I_Daily_Evap[I_RainDoY/1460][Simulation_Time]
            I_DailyRain = (
                I_DailyRainYear[I_RainDoY/1460][Simulation_Time] *
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

            year_stage = np_utils.get_year_stage(I_Simulation_Time/365, I_InputDataYears)
            I_FracVegClassNow = np.divide(
                I_FracVegClasses[year_stage] +
                (I_FracVegClasses[year_stage + 1] - I_FracVegClasses[year_stage]) *
                (int(I_Simulation_Time/365) - I_InputDataYears[year_stage]) /
                (I_InputDataYears[year_stage + 1] - I_InputDataYears[year_stage]),
                np.sum(I_FracVegClasses[year_stage], axis=1).reshape(20, 1),
                # np_utils.array_sum(I_FracVegClasses[year_stage], shape=(subcatchment, 1)),
                out=np.zeros_like(I_FracVegClasses[year_stage]),
                where=I_RelArea != 0
            )
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

            # print I_BD_BDRefVegNow
            #
            I_AvailWatClassNow = (
                I_PlantAvWatSubs[year_stage] +
                (I_PlantAvWatSubs[year_stage + 1] - I_PlantAvWatSubs[year_stage]) *
                (int(I_Simulation_Time/365) - I_InputDataYears[year_stage]) /
                (I_InputDataYears[year_stage + 1] - I_InputDataYears[year_stage])
            )
            # print I_AvailWatClassNow
            I_FracVegClassSum1 = np_utils.array_sum(I_FracVegClass_1)
            I_FracVegClassSum2 = np_utils.array_sum(I_FracVegClass_2)
            I_FracVegClassSum3 = np_utils.array_sum(I_FracVegClass_3)
            I_FracVegClassSum4 = np_utils.array_sum(I_FracVegClass_4)
            I_FracVegClassSumNow = np_utils.array_sum(I_FracVegClassNow)
            I_DailyRainAmount = np.multiply(
                I_RainPerDay,
                np.multiply(I_FracVegClassNow, I_RelArea)
            )

            isI_StillWarmUp = time <= I_WarmUpTime
            I_WUcorrection = time == int(I_WarmUpTime + 1)
            I_WarmedUp = time == int(I_WarmUpTime)
            isO_Reset = I_WarmedUp == 1 or I_WUcorrection == 1
            I_FracArea = np.multiply(I_FracVegClassNow, I_RelArea)
            I_TimeEvap = (
                365 if I_RainDoY % 365 == 0
                else I_RainDoY % 365
            )
            I_MoY = 0 if I_RainDoY == 0 else int(I_TimeEvap / 30.5)
            I_PotEvapTransp = None
            if I_EvapotransMethod == 1:
                I_PotEvapTransp = np.multiply(
                    I_Evapotrans[I_MoY],
                    np.multiply(I_MultiplierEvapoTrans[I_MoY % 12], I_FracArea)
                )
            else:
                I_PotEvapTransp = np.multiply(
                    I_Daily_Evapotrans[I_MoY],
                    np.multiply(I_MultiplierEvapoTrans, I_FracArea)
                )
            # print I_MoY, I_PotEvapTransp.transpose()
            # print I_PotEvapTransp.shape == (20, 20)
            # print I_RelArea
            # print I_FracVegClassNow.transpose()
            I_MaxInfSubSAreaClass = I_MaxInfSSoil * np.multiply(I_RelArea, I_FracVegClassNow)
            # print np.around(I_MaxInfSubSAreaClass.transpose(), decimals=2)
            # print I_MaxInfSubSAreaClass.shape == (20, 20)
            I_MaxInfArea = I_MaxInf * np.multiply(
                I_FracArea,
                np.power(np.divide(0.7,
                                   I_BD_BDRefVegNow,
                                   out=np.zeros_like(I_BD_BDRefVegNow),
                                   where=I_BD_BDRefVegNow > 0),
                         I_PowerInfiltRed
                         )
            )

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
                (1 - isL_Lake),
                np.minimum(
                    np.minimum(I_SoilSatClass - D_SoilWater[time],
                               np.multiply(I_MaxInfArea,
                                           I_RainTimeAvForInf) / 24),
                    I_DailyRainAmount - D_InterceptEvap))
            # print np.around(D_Infiltration, decimals=2).transpose()
            I_RelDroughtFact_AvailWaterClass = np.multiply(
                I_RelDroughtFact,
                I_AvailWaterClass)

            D_RelWaterAv = np.minimum(
                1,
                np.divide(
                    D_SoilWater[time],
                    I_RelDroughtFact_AvailWaterClass,
                    out=np.ones_like(D_SoilWater[time]),
                    where=I_RelDroughtFact_AvailWaterClass > 0
                )
            )

            # print np.around(D_RelWaterAv, decimals=2).transpose()

            D_Irrigation = np.minimum(
                np.divide(
                    np.multiply(D_GWArea[time],
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
                            D_SoilWater[time],
                            np.multiply(I_PercFracMultiplier, I_GWRelFrac)),
                        I_MaxDynGWArea - D_GWArea[time])) -
                np.multiply(D_IrrigEfficiency, D_Irrigation) -
                np.multiply(
                    I_AvailWaterClass <= 0,
                    np.multiply(D_IrrigEfficiency, D_Irrigation)))
            # print np.around(D_Percolation, decimals=2).transpose()
            D_WaterEvapIrrigation = np.multiply(
                D_IrrigEfficiency > 0,
                D_Irrigation * (1 - D_IrrigEfficiency))

            D_GWaDisch = np.multiply(D_GWArea[time], I_GWRelFrac)
            # print np.around(D_GWArea[time], decimals=2)
            D_DeepInfiltration = np.multiply(
                isL_Lake == 1,
                np.minimum(
                    np.minimum(
                        np.minimum(
                            np.multiply(
                                np.sum(I_MaxInfArea, axis=1).reshape(subcatchment,1),
                                I_RainTimeAvForInf
                            ) / 24 - np.sum(
                                I_SoilSatClass,
                                axis=1).reshape(subcatchment,1) +
                            np.sum(D_SoilWater[time],
                                      axis=1).reshape(subcatchment,1),
                            np.sum(I_MaxInfSubSAreaClass,
                                      axis=1).reshape(subcatchment,1)
                        ),
                        np.sum(I_DailyRainAmount,
                                           axis=1).reshape(subcatchment,1) -
                        np.sum(D_InterceptEvap,
                                           axis=1).reshape(subcatchment,1) -
                        np.sum(D_Infiltration,
                                           axis=1).reshape(subcatchment,1)),
                    I_MaxDynGWArea - D_GWArea[time]))
            # print D_DeepInfiltration
            # print 'D_DeepInfiltration', D_DeepInfiltration.shape, D_GWArea[time].shape
            D_ActEvapTransp = np.multiply(
                isL_Lake != 1,
                np.multiply(
                    I_PotEvapTransp -
                    np.multiply(I_InterceptEffectonTransp, D_InterceptEvap),
                    D_RelWaterAv))
            # print np.around(D_ActEvapTransp, decimals=2).transpose()
            # print 'D_SurfaceFlow'
            # print I_DailyRainAmount.shape, D_InterceptEvap.shape, D_Infiltration.shape, D_DeepInfiltration.shape

            D_SurfaceFlow = (
                np.multiply(isL_Lake == 1, np.sum(
                                I_DailyRainAmount,
                                axis=1).reshape(subcatchment,1)
                            ) +
                np.multiply(isL_Lake != 1, (np.sum(
                                     I_DailyRainAmount,
                                     axis=1
                                 ).reshape(subcatchment,1) -
                                  np.sum(
                                      D_InterceptEvap,
                                      axis=1
                                  ).reshape(subcatchment,1) -
                                  np.sum(
                                      D_Infiltration,
                                      axis=1
                                  ).reshape(subcatchment,1) -
                                  D_DeepInfiltration))
            )

            D_SoilQflowRelFrac = np.ones(
                shape=(subcatchment, 1)
            ) * I_SoilQflowFrac

            D_SoilDischarge_ = np.multiply(
                D_SoilQflowRelFrac,
                (D_SoilWater[time] - I_AvailWaterClass)
            )
            D_SoilDischarge = np.multiply(D_SoilDischarge_ > 0, D_SoilDischarge_)
            # print np.round(D_SoilWater[time], decimals=2).transpose()
            # print np.around(D_SoilDischarge, decimals=2).transpose()
            G_GrassAll = np_utils.array_sum(G_GrassStandingBiomass[time])
            G_Grazing = (0
                         if G_GrassAll == 0
                         else (C_StockingRate[time] *
                               C_DailyIntake *
                               G_GrassStandingBiomass[time] /
                               G_GrassAll))
            # print np.around(C_StockingRate[time], decimals=2)
            # print np.around(G_GrassStandingBiomass[time], decimals=2)
            C_TrampComp = C_DailyTrampFac * G_Grazing / C_DailyIntake
            C_DeathRate = C_StockingRate[time] * C_DailyIntake - G_GrassAll
            C_DeathRate = (C_DeathRate > 0) * C_DeathRate
            C_Destocking = min(C_StockingRate[time], C_CattleSale + C_DeathRate)
            C_Stocking = 0 * C_StockingRate[time]
            # print C_Stocking, C_Destocking
            # G_GrassFract_Biomass = np.zeros(vegClass)
            G_GrowthRate = G_WUE * np.multiply(D_ActEvapTransp.transpose(),
                                               G_GrassFract_Biomass).transpose()
            # print np.around(G_GrowthRate, decimals=2)
            # G_GrassAll = np_utils.array_sum(G_GrassStandingBiomass[time])
            G_LeafMortality = (G_GrassStandingBiomass[time] * G_GrassMortFrac +
                               G_Grazing * G_TramplingMultiplier)
            G_LitterDeposition = G_LeafMortality * G_GrassLitConv

            G_Incorporation_DecaySurfLit = (G_SurfaceLitter[time] *
                                            G_SurfLitDecFrac)
            # print G_SurfaceLitter[time]
            G_FaecesProd = G_Grazing * G_GrazingManConv
            G_Incorporation_DecayManure = (G_SurfManure[time] *
                                           G_SurfManureDecFrac)
            G_SurfaceCover = (G_GrassStandingBiomass[time] +
                              G_SurfaceLitter[time] +
                              G_SurfManure[time])
            S_RainAtSoilSurface = I_DailyRainAmount - D_InterceptEvap
            # print np.around(S_RainAtSoilSurface, decimals=2)
            # print np.around(S_RelBulkDensity[time], decimals=2)
            S_Compaction = (
                np.multiply((1.3 - S_RelBulkDensity[time]), C_TrampComp) /
                S_TrampMax)
            S_SplashErosion = (0 * np.divide(
                np.multiply(G_SurfaceCover,
                            S_RainAtSoilSurface),
                I_RainDuration,
                out=np.zeros_like(G_SurfaceCover),
                where=I_RainDuration > 0))

            S_StructureFormation = 0 * np.multiply(S_RelBulkDensity[time],
                                                   G_SurfaceCover)
            D_ReservoirVol = L_ResrDepth * np.multiply(isL_Lake, I_RelArea)
            # print D_SubcResVol[time].shape
            # print np.around(D_SubcResVol[time], decimals=2)
            D_SubCResUseFrac_ = D_SubCResUseFrac[I_RainDoY] if I_RainDoY < len(D_SubCResUseFrac) else D_SubCResUseFrac[-1]
            D_SubCResOutflow = np.add(
                np.multiply(
                    D_SubcResVol[time] > D_ReservoirVol,
                    np.subtract(D_SubcResVol[time], D_ReservoirVol)),
                np.multiply(D_SubcResVol[time] < D_ReservoirVol,
                            D_SubCResUseFrac_ * D_SubcResVol[time]))
            # print np.around(D_SubCResOutflow, decimals=2)
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
            D_TotalStreamInflow = (
                D_SurfaceFlow +
                np.multiply(
                    D_GWaDisch,
                    (1 - D_FracGWtoLake)) +
                np.sum(D_SoilDischarge, axis=1).reshape(subcatchment, 1) +
                np.multiply(D_SubCResOutflow,
                            (1 - isI_DaminThisStream)))
            # print np.around(D_GWaDisch, decimals=2)
            # print np.around(D_TotalStreamInflow, decimals=2)
            # print D_RoutingTime.shape, isD_FeedingIntoLake.shape, D_TotalStreamInflow.shape, I_ReleaseFrac.shape
            D_RivLakeSameDay = np.multiply(
                D_RoutingTime >= 0,
                np.multiply(D_RoutingTime < 1,
                            np.multiply(isD_FeedingIntoLake,
                                        np.multiply(D_TotalStreamInflow,
                                                    I_ReleaseFrac))))
            # print np.around(D_RivLakeSameDay, decimals=2)
            D_RivInflLake = np.multiply(
                np.multiply(
                    I_ReleaseFrac[:, constants.Inflowlake].reshape(subcatchment, 1),
                    D_TotRiverFlowNoDelay[time][:, constants.Inflowlake].reshape(subcatchment, 1)),
                isD_FeedingIntoLake)
            # print np.around(D_TotRiverFlowNoDelay[time], decimals=2)
            D_RivInflLake = np.repeat(D_RivInflLake, 8).reshape(subcatchment,
                                                                obsPoint)
            D_RiverFlowtoLake = (
                np_utils.array_sum(
                    D_RivLakeSameDay,
                    shape=(1, obsPoint))[0][constants.Inflowlake] +
                np_utils.array_sum(
                    D_RivInflLake,
                    shape=(1, obsPoint))[0][constants.Inflowlake]
            )
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
            D_RestartL = isO_Reset * D_CumInflowtoLake[time] / dt
            # D_TotalStreamInflow = (
            #     (D_SurfaceFlow +
            #      np.multiply(D_GWaDisch, (1 - D_FracGWtoLake)) +
            #      np_utils.array_sum(D_SoilDischarge, shape=(subcatchment, 1))) +
            #     np.multiply(D_SubCResOutflow, (1 - isI_DaminThisStream)))
            D_DirectSurfFkowObsPoint = np.multiply(
                np.multiply(D_RoutingTime >= 0, D_RoutingTime < 1),
                np.multiply(D_TotalStreamInflow, (1 - I_ReleaseFrac)))
            D_RiverDirect = np.multiply(
                np.multiply(D_RoutingTime > 0, D_RoutingTime < 1),
                np.multiply((1 - isD_FeedingIntoLake),
                            np.multiply(D_TotalStreamInflow, I_ReleaseFrac)))
            # print np.around(D_RiverDirect, decimals=2)
            D_RivInfLake = np.multiply(
                np.multiply(I_ReleaseFrac, D_TotRiverFlowNoDelay[time]),
                isD_FeedingIntoLake)
            SurFlowRiverTransitTime = np.around(np.add(np.multiply(D_RoutingTime >= 1, D_RoutingTime), np.multiply(D_RoutingTime <1, 1)))
            # print SurFlowRiverTransitTime
            # D_SurfFlowRiver = np.multiply(D_RoutingTime > 1, D_RoutingTime)
            # print np.around(D_SurfFlowRiver[time], decimals=2)
            D_CurrRivVol = (
            np.sum(
                D_StreamsSurfQ[time],
                axis=0
            )[0] +
            np.sum(
                D_TotRiverFlowNoDelay[time],
                axis=0)[0]
            )
            # print D_CurrRivVol
            D_RestartR = np.multiply(isO_Reset, D_CumTotRiverFlow[time]) / dt
            D_RiverDelay = np.multiply(
                I_ReleaseFrac,
                np.multiply(D_TotRiverFlowNoDelay[time],
                            (1 - isD_FeedingIntoLake))
            )
            # print D_RiverDelay
            D_SurfFlowObsPoint = np.multiply(D_RoutingTime >= 1,
                                             D_TotalStreamInflow)
            # print np.around(D_SurfFlowObsPoint, decimals=2)

            L_LakeTransDef = np.multiply(isL_Lake, I_PotEvapTransp[constants.AF_Kelapa] - D_ActEvapTransp[constants.AF_Kelapa])
            L_LakeArea = np.multiply(isL_Lake,
                                     I_RelArea,
                                     out=np.zeros_like(isL_Lake),
                                     where=isL_Lake != 1)
            # print L_LakeArea
            L_LakeLevel =  (
                L_LakeVol[time] /
                (1000 * np.sum(L_LakeArea)) + L_LakeBottomElev
            ) if (np.sum(L_LakeArea) > 0) else 0

            # print L_LakeLevel

            L_Lakelevelexcess = (
                L_LakeLevel -
                (1 - isL_HEPP_Active) * L_LakeElevPreHEPP -
                isL_HEPP_Active * L_LakeOverFlPostHEPP)
            # print L_LakeLevel, L_Lakelevelexcess

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
            # print L_HEPP_Outflow
            L_HEPPWatUseFlow = L_HEPP_Outflow if isL_HEPP_Active == 1 else 0
            L_HEPP_Kwh = 1000 * I_TotalArea * L_HEPPWatUseFlow / L_m3_per_kwh

            L_HEPP_OpTimeRel = (
            (L_CumHEPPUse[time] / L_HEPP_Daily_Dem) / I_Simulation_Time
            if I_Simulation_Time > 0 and isI_WarmEdUp[time] == 1
            else 0)
            L_EvapLake = min(np.sum(L_LakeTransDef),
                             L_LakeVol[time]) * L_LakeTranspMultiplier
            # print L_EvapLake
            L_SanitaryFlow = L_QmecsSanFlow * 3600 * 24 / I_TotalArea * 10 ** -3
            L_OutflTrVolPreHEPP = 1000 * (
                L_LakeElevPreHEPP -
                L_LakeBottomElev) * np.sum(L_LakeArea)
            L_OutflTrVoPostHEPP = 1000 * (
                L_LakeOverFlPostHEPP -
                L_LakeBottomElev) * np.sum(L_LakeArea)
            L_InFlowtoLake = D_RiverFlowtoLake + D_GWtoLake
            # print L_InFlowtoLake
            L_RivOutFlow = max(isL_HEPP_Active * L_SanitaryFlow,
                           min(L_LakeVol[time] - L_EvapLake - L_HEPPWatUseFlow + L_InFlowtoLake,
                               (L_LakeVol[time] -
                                L_OutflTrVoPostHEPP * isL_HEPP_Active -
                                L_OutflTrVolPreHEPP * (1 - isL_HEPP_Active)) * (
                               L_LakeOverFlowFrac) * (
                                   1 + L_Lakelevelexcess ** L_LakeOverFlPow)))
            # print L_RivOutFlow, L_LakeVol[time]

            # Total river flow -> Output in subcatchment
            O_InFlowtoLake = O_RiverFlowtoLake + D_GWLakeSub
            # print L_CumRivOutFlow[time], L_RivOutFlow
            L_RestartR = isO_Reset * L_CumRivOutFlow[time] / dt
            L_RestartH = isO_Reset * L_CumHEPPUse[time]
            L_RestartE = isO_Reset * L_CumEvapLake[time] / dt
            O_TotStreamFlow = (O_CumBaseFlow[time] +
                               O_CumSoilQFlow[time] +
                               O_CumSurfQFlow[time])
            # print O_TotStreamFlow
            D_DeltaStockRiver = D_InitRivVol[time] - D_CurrRivVol
            # print D_DeltaStockRiver
            D_SurfaceFlowAcc = np.sum(D_SurfaceFlow)
            O_DeltaGWStock = O_InitGWStock[time] - np.sum(D_GWArea[time])
            # print O_DeltaGWStock
            O_DeltaSoilWStock = O_InitSoilW[time] - np.sum(D_SoilWater[time])
            # print O_InitSoilW[time]
            O_ChkAllCatchmAccFor = (-O_CumRain[time] +
                                    O_CumIntercE[time] +
                                    O_CumTransp[time] +
                                    O_TotStreamFlow -
                                    O_DeltaGWStock -
                                    O_DeltaSoilWStock)
            O_DeltaStockLake = D_InitLakeVol[time] - L_LakeVol[time]
            # print O_DeltaStockLake
            O_ChkAllLakeAccFor = (D_CumInflowtoLake[time] -
                                  L_CumEvapLake[time] -
                                  L_CumRivOutFlow[time] -
                                  L_CumHEPPUse[time] +
                                  O_DeltaStockLake)
            D_CumTotRiverFlowAll = np.sum(D_CumTotRiverFlow[time], axis=1)[0]
            O_ChkAllRiverAccFor = (O_TotStreamFlow -
                                   D_CumTotRiverFlowAll -
                                   D_CumInflowtoLake[time] +
                                   D_DeltaStockRiver)
            O_DailyRainSubCtm = np_utils.array_sum(I_DailyRainAmount, shape=(subcatchment, 1))
            O_FrBaseFlow = (O_CumBaseFlow[time] / O_TotStreamFlow
                            if O_TotStreamFlow > 0
                            else 0)
            # print D_CumTotRiverFlowAll, O_FrBaseFlow
            O_FrSoilQuickFlow = (O_CumSoilQFlow[time] / O_TotStreamFlow
                                 if O_TotStreamFlow > 0
                                 else 0)
            O_FrSurfQuickFlow = (O_CumSurfQFlow[time] / O_TotStreamFlow
                                 if O_TotStreamFlow else 0)
            O_RainYesterday = O_RainYest[time] * I_WarmedUp
            O_RainHalfDelayed = (np_utils.array_sum(O_RainYesterday) +
                                 np_utils.array_sum(I_DailyRainAmount)) / 2
            O_RelWatAvVegSubc = np.multiply(D_RelWaterAv, I_FracVegClassNow)
            # print np.around(O_RelWatAvVegSubc.transpose(), decimals=2)
            O_RelWatAv_Subc = np.divide(
                np.mean(O_RelWatAvVegSubc, axis=1).reshape(subcatchment, 1),
                np.sum(I_FracVegClassNow, axis=1).reshape(subcatchment, 1),
                out=np.ones(shape=(subcatchment, 1)),
                where=np.sum(I_FracVegClassNow, axis=1).reshape(subcatchment, 1) > 0)
            # print O_RelWatAv_Subc
            O_RelWatAv_Overall = np_utils.array_mean(O_RelWatAv_Subc)
            O_Rel_ET_Subc = np.divide(
                D_InterceptEvap +
                D_ActEvapTransp,
                I_PotEvapTransp,
                out=np.zeros_like(I_PotEvapTransp),
                where=I_PotEvapTransp != 0)
            # O_Reset = 1 if I_WarmedUp == 1 or I_WUcorrection == 1 else 0
            # S_RainAtSoilSurface = I_DailyRainAmount - D_InterceptEvap

            O_InitLake = isO_Reset * (L_LakeVol[time] - D_InitLakeVol[time])
            O_InitRiv = isO_Reset * (D_CurrRivVol - D_InitLakeVol[time])
            # print D_InitLakeVol[time]
            O_BaseFlowAcc = np.sum(D_GWaDisch) * I_WarmedUp
            # print O_BaseFlowAcc
            # O_CumDeepInfAcc = np_utils.array_sum(D_DeepInfiltration) * I_WarmedUp
            O_EvapoTransAcc = (np.sum(I_PotEvapTransp) > 0) * (np.sum(D_ActEvapTransp) + np.sum(D_InterceptEvap)) * I_WarmedUp
            # O_InfAcc = np_utils.array_sum(D_Infiltration) * I_WarmedUp
            O_AccET = np.sum(D_InterceptEvap) * I_WarmedUp
            O_PercAcc = np.sum(D_Percolation) * I_WarmedUp

            O_RainAcc = np.sum(I_DailyRainAmount) * I_WarmedUp
            # print O_EvapoTransAcc, O_AccET, O_PercAcc, O_RainAcc

            # O_CumSoilQFlowAcc = np.sum(D_SoilDischarge) * I_WarmedUp
            O_SurfQFlowAcc = np.sum(D_SurfaceFlow) * I_WarmedUp
            # print O_SurfQFlowAcc

            O_TranspAcc = np.sum(D_ActEvapTransp) * I_WarmedUp
            O_InitGW = isO_Reset * (
                np.sum(D_GWArea[time]) -
                O_InitGWStock[time]
            )
            O_InitSW = isO_Reset * (
                np.sum(D_SoilWater[time]) -
                O_InitSoilW[time]
            )
            O_RainToday = np.sum(
                I_DailyRainAmount,
                axis=1
            ).reshape(subcatchment, 1) * I_WarmedUp
            O_LastYearHEPP = (O_LastYHepp[time] > 0) * (O_ThisYHepp[time] - O_LastYHepp[time])/(365 * L_HEPP_Daily_Dem)
            O_BYP = (O_LastYearHEPP > 0 and O_LastYearHEPP > O_BestYyHEPP[time]) * (-O_BestYyHEPP[time] + O_LastYearHEPP)

            O_StarMYear = np.array([4, 6, 8]).reshape(measurePeriod, 1)
            O_StartDOY = np.array([1, 1, 1]).reshape(measurePeriod, 1)
            O_StartMDay = (O_StarMYear - 1) * 365 + 1 + (O_StartDOY - 1)
            O_EndMDay = O_StartMDay + O_MPeriodLength
            # print O_StartMDay, O_EndMDay
            Yearly_Tick = 1 if I_WarmedUp == 1 and time % 365 == 0 else 0
            time_stage = I_Simulation_Time / 1460
            I_DebitTime = I_RFlowData[time_stage]
            # for index, stage in enumerate(I_RainDoY_Stage):
            #     I_DebitTime = (I_RFlowData[index]
            #                    if I_Simulation_Time <= stage
            #                     else I_RFlowData[6] if I_Simulation_Time <= 10220
            #                     else I_RFlowData[7])
            I_RFlowDataQmecs = I_DebitTime[Simulation_Time]
            I_ContrSubcArea = np.multiply(I_RelArea, isI_SubcContr)
            I_RFlowdata_mmday = 0 if np.sum(I_ContrSubcArea) == 0 else (I_RFlowDataQmecs*24*3600*10**3)/(np.sum(I_ContrSubcArea) * I_TotalArea * 10**6)
            # print 'O_Ch_in_GWStockMP', O_InitGWStockMP[time].shape, O_Ch_inGWStock[time].shape
            O_Ch_in_GWStockMP = np.multiply(
                np.multiply(O_StartMDay < time, O_EndMDay + 1 > time),
                (np.sum(D_GWArea[time]) -
                O_InitGWStockMP[time] -
                O_Ch_inGWStock[time])
            )
            O_Ch_in_WStockMP = np.multiply(
                np.multiply(O_StartMDay < time, O_EndMDay + 1 > time),
                (np.sum(D_SoilWater[time]) -
                 O_InitSWMP[time] -
                 O_Ch_inWStock[time])
            )
            O_BaseFlowAccMP = (I_Simulation_Time >= O_StartMDay and I_Simulation_Time < O_EndMDay and isI_StillWarmUp == 0) * np.sum(D_GWaDisch)

            O_DebitDataAccMP = (I_Simulation_Time >= O_StartMDay and I_Simulation_Time < O_EndMDay and isI_StillWarmUp == 0) * I_RFlowdata_mmday        # print 'D_RiverFlowtoLake', D_RiverFlowtoLake
            O_DebitPredAccMP = (I_Simulation_Time >= O_StartMDay and I_Simulation_Time < O_EndMDay and isI_StillWarmUp == 0) * D_RiverFlowtoLake

            O_EvapLakeMP = (I_Simulation_Time >= O_StartMDay and I_Simulation_Time < O_EndMDay and isI_StillWarmUp == 0) * L_EvapLake

            O_Ch_in_EvapoTrans = (I_Simulation_Time >= O_StartMDay and I_Simulation_Time < O_EndMDay and isI_StillWarmUp == 0) * (np.sum(D_CumEvapTranspClass) - O_InitEvapoMP[time] - O_CumEvapTransMP[time])

            O_GWAccMP = np.multiply(
                np_utils.array_sum(D_GWArea[time]),
                np.multiply(time > O_StartMDay, time < O_EndMDay))

            O_HEPPOutFlowMP = np.multiply(
                L_HEPPWatUseFlow,
                np.multiply(time > O_StartMDay, time < O_EndMDay))

            O_InfAccMP = np.multiply(
                np_utils.array_sum(D_Infiltration),
                np.multiply(I_Simulation_Time >= O_StartMDay,
                            np.multiply(I_Simulation_Time < O_EndMDay,
                                        isI_StillWarmUp == 0)))
            O_IntercAccMP = np.multiply(
                np_utils.array_sum(D_InterceptEvap),
                np.multiply(I_Simulation_Time >= O_StartMDay,
                            np.multiply(I_Simulation_Time < O_EndMDay,
                                        isI_StillWarmUp == 0)))
            O_RainAccMP = np.multiply(
                np_utils.array_sum(I_DailyRainAmount),
                np.multiply(I_Simulation_Time >= O_StartMDay,
                            np.multiply(I_Simulation_Time < O_EndMDay,
                                        isI_StillWarmUp == 0)))
            O_RivInflowtoLakeMP = np.multiply(
                L_InFlowtoLake,
                np.multiply(I_Simulation_Time >= O_StartMDay,
                            np.multiply(I_Simulation_Time < O_EndMDay,
                                        isI_StillWarmUp == 0)))
            O_RivOutFlowMP = np.multiply(
                L_RivOutFlow,
                np.multiply(I_Simulation_Time >= O_StartMDay,
                            np.multiply(I_Simulation_Time < O_EndMDay,
                                        isI_StillWarmUp == 0)))
            O_SoilQFlowAccMP = np.multiply(
                np_utils.array_sum(D_SoilDischarge),
                np.multiply(I_Simulation_Time >= O_StartMDay,
                            np.multiply(I_Simulation_Time < O_EndMDay,
                                        isI_StillWarmUp == 0)))
            O_SoilWAccMP = np.multiply(
                np_utils.array_sum(D_SoilWater[time]),
                np.multiply(I_Simulation_Time >= O_StartMDay,
                            np.multiply(I_Simulation_Time < O_EndMDay,
                                        isI_StillWarmUp == 0)))
            O_SurfQFlowAccMP = np.multiply(
                np_utils.array_sum(D_SurfaceFlow),
                np.multiply(I_Simulation_Time >= O_StartMDay,
                            np.multiply(I_Simulation_Time < O_EndMDay,
                                        isI_StillWarmUp == 0)))
            O_TranspAccMP = np.multiply(
                np_utils.array_sum(D_ActEvapTransp),
                np.multiply(I_Simulation_Time >= O_StartMDay,
                            np.multiply(I_Simulation_Time < O_EndMDay,
                                        isI_StillWarmUp == 0)))
            O_Ch_in_CatchmStMP = np.multiply(
                O_Ch_inGWStock[time] +
                O_Ch_in_GWStockMP +
                O_Ch_inWStock[time] +
                O_Ch_in_WStockMP -
                O_DeltaCatchmStMP[time],
                np.multiply(time > O_StartMDay, time < O_EndMDay + 1))

            O_Hepp_ElctrProd = np.multiply(
                L_HEPP_Kwh / (O_EndMDay - O_StartMDay),
                np.multiply(I_Simulation_Time >= O_StartMDay,
                            np.multiply(I_Simulation_Time < O_EndMDay,
                                        isI_StillWarmUp == 0)))
            # print 'O_Hepp_ElctrProd', O_Hepp_ElctrProd.shape
            O_Ch_EvapoTran = np.multiply(np_utils.array_sum(D_CumEvapTranspClass),
                                         time == O_StartMDay)
            O_ChGWMP = np.multiply(
                np_utils.array_sum(D_GWArea[time]),
                time == O_StartMDay
            )
            O_ChSoilWMP = np.multiply(np_utils.array_sum(D_SoilWater[time]),
                                      time == O_StartMDay)
            O_ChSoilWMP = np.multiply(np_utils.array_sum(D_SoilWater[time]),
                                      time == O_StartMDay)
            O_HeppUseF1 = Yearly_Tick * O_ThisYHepp[time]
            O_HeppUseF2 = Yearly_Tick * O_LastYHepp[time]
            O_HeppUseF0 = Yearly_Tick * L_CumHEPPUse[time]
            O_HeppUseF1 = Yearly_Tick * O_ThisYHepp[time]
            O_CumET_LandMP = O_CumIntercEvapMP + O_CumTranspMP
            O_CurrentETall = np_utils.array_sum(D_ActEvapTransp)
            O_WYP = (- O_WorstYHEPP[time] + O_LastYearHEPP
                     if 0 < O_LastYearHEPP < O_WorstYHEPP[time]
                     else 0)
            O_CumET_LandMP = O_CumIntercEvapMP + O_CumTranspMP
            O_CurrentETall = np_utils.array_sum(D_ActEvapTransp)
            O_RelOpTimeHEPPMP = ((O_CumHEPPOutFlowMP[time] /
                                  L_HEPP_Daily_Dem) /
                                 (O_EndMDay - O_StartMDay))
            O_SoilWaterTot = np_utils.array_sum(D_SoilWater[time])
            O_DeepInfAcc = np_utils.array_sum(
                D_DeepInfiltration
            ) * isI_WarmEdUp[time]

            O_InfAcc = (
                np_utils.array_sum(D_Infiltration) * isI_WarmEdUp[time]
            )
            O_IntercAcc = (
                np_utils.array_sum(D_InterceptEvap) * isI_WarmEdUp[time]
            )

            O_SoilQFlowAcc = (
                np_utils.array_sum(D_SoilDischarge) * isI_WarmEdUp[time]
            )

            O_SoilQflow_Subca = np_utils.array_sum(
                D_SoilDischarge,
                shape=(subcatchment, 1)
            )
            D_EvaporReservoir = I_Evapotrans[I_MoY % 12] * np_utils.array_sum(isL_Lake)
            D_Influx_to_Resr = np.multiply(
                isI_DaminThisStream == 1,
                (D_GWaDisch +
                 np_utils.array_sum(D_SoilDischarge, shape=(subcatchment, 1))
                 + D_SurfaceFlow)
            )

            calculate.update(
                C_StockingRate,
                inflow=C_Stocking,
                outflow=C_Destocking,
                dt=dt
            )
            calculate.update(
                D_InitLakeVol,
                inflow=O_InitLake,
                dt=dt
            )
            calculate.update(
                D_InitRivVol,
                inflow=O_InitRiv,
                dt=dt
            )
            calculate.update(
                O_CumBaseFlow,
                inflow=O_BaseFlowAcc,
                dt=dt
            )
            calculate.update(
                O_CumDeepInfilt,
                inflow=O_DeepInfAcc,
                dt=dt
            )
            calculate.update(
                O_CumEvapotrans,
                inflow=O_EvapoTransAcc,
                dt=dt
            )
            calculate.update(
                O_CumInfiltration,
                inflow=O_InfAcc,
                dt=dt
            )
            calculate.update(
                O_CumIntercE,
                inflow=O_AccET,
                dt=dt
            )
            calculate.update(
                O_CumIntercepEvap,
                inflow=O_IntercAcc,
                dt=dt
            )
            calculate.update(
                O_CumPercolation,
                inflow=O_PercAcc,
                dt=dt
            )
            calculate.update(
                O_CumRain,
                inflow=O_RainAcc,
                dt=dt
            )
            calculate.update(
                O_CumSoilQFlow,
                inflow=O_SoilQFlowAcc,
                dt=dt
            )
            calculate.update(
                O_CumSoilQFlow_Subca_1,
                inflow=O_SoilQflow_Subca,
                dt=dt
            )
            calculate.update(
                O_CumSurfQFlow,
                inflow=O_SurfQFlowAcc,
                dt=dt
            )
            calculate.update(
                O_CumTransp,
                inflow=O_TranspAcc,
                dt=dt
            )
            calculate.update(
                O_InitGWStock,
                inflow=O_InitGW,
                dt=dt
            )
            calculate.update(
                O_InitSoilW,
                inflow=O_InitSW,
                dt=dt
            )
            calculate.update(
                O_RainYest,
                inflow=O_RainToday,
                outflow=O_RainYesterday,
                dt=dt
            )
            calculate.update(
                G_GrassStandingBiomass,
                inflow=G_GrowthRate,
                outflow=G_Grazing+G_LeafMortality,
                dt=dt
            )
            calculate.update(
                G_SurfaceLitter,
                inflow=G_LitterDeposition,
                outflow=G_Incorporation_DecaySurfLit,
                dt=dt
            )
            calculate.update(
                G_SurfManure,
                inflow=G_FaecesProd,
                outflow=G_Incorporation_DecayManure,
                dt=dt
            )
            calculate.update(
                isI_WarmEdUp,
                inflow=I_Warmedup,
                dt=dt
            )
            calculate.update(
                O_CumDebitData,
                inflow=I_RFlowdata_mmday,
                dt=dt
            )
            calculate.update(
                L_CumEvapLake,
                inflow=L_EvapLake,
                outflow=L_RestartE,
                dt=dt
            )
            calculate.update(
                L_CumHEPPUse,
                inflow=L_HEPPWatUseFlow,
                outflow=L_RestartH,
                dt=dt
            )
            calculate.update(
                L_CumRivOutFlow,
                inflow=L_RivOutFlow,
                outflow=L_RestartR,
                dt=dt
            )
            calculate.update(
                L_LakeVol,
                inflow=L_InFlowtoLake,
                outflow=L_EvapLake + L_RivOutFlow + L_HEPPWatUseFlow,
                dt=dt
            )
            calculate.update(
                O_BestYyHEPP,
                inflow=O_BYP,
                dt=dt
            )
            calculate.update(
                O_Ch_inGWStock,
                inflow=O_Ch_in_GWStockMP,
                dt=dt
            )
            calculate.update(
                O_Ch_inWStock,
                inflow=O_Ch_in_WStockMP,
                dt=dt
            )
            calculate.update(
                O_CumBaseFlowMP,
                inflow=O_BaseFlowAccMP,
                dt=dt
            )
            calculate.update(
                O_CumDebitDataMP,
                inflow=O_DebitDataAccMP,
                dt=dt
            )
            calculate.update(
                O_CumDebitPredMP,
                inflow=O_DebitPredAccMP,
                dt=dt
            )
            calculate.update(
                O_CumEvapLakeMP,
                inflow=O_EvapLakeMP,
                dt=dt
            )
            calculate.update(
                O_CumEvapTransMP,
                inflow=O_Ch_in_EvapoTrans,
                dt=dt
            )
            calculate.update(
                O_CumGWMP,
                inflow=O_GWAccMP,
                dt=dt
            )
            calculate.update(
                O_CumHEPPOutFlowMP,
                inflow=O_HEPPOutFlowMP,
                dt=dt
            )
            calculate.update(
                O_CumInfiltrationMP,
                inflow=O_InfAccMP,
                dt=dt
            )
            calculate.update(
                O_CumIntercEvapMP,
                inflow=O_IntercAccMP,
                dt=dt
            )
            calculate.update(
                O_CumRainMP,
                inflow=O_RainAccMP,
                dt=dt
            )
            calculate.update(
                O_CumRivInflowtoLakeMP,
                inflow=O_RivInflowtoLakeMP,
                dt=dt
            )
            calculate.update(
                O_CumRivOutFlowMP,
                inflow=O_RivOutFlowMP,
                dt=dt
            )
            calculate.update(
                O_CumSoilQFlowMP,
                inflow=O_SoilQFlowAccMP,
                dt=dt
            )
            calculate.update(
                O_CumSoilWMP,
                inflow=O_SoilWAccMP,
                dt=dt
            )
            calculate.update(
                O_CumSurfQFlowMP,
                inflow=O_SurfQFlowAccMP,
                dt=dt
            )
            calculate.update(
                O_CumTranspMP,
                inflow=O_TranspAccMP,
                dt=dt
            )
            calculate.update(
                O_DeltaCatchmStMP,
                inflow=O_Ch_in_CatchmStMP,
                dt=dt
            )
            calculate.update(
                O_Hepp_Kwh_per_dayMP,
                inflow=O_Hepp_ElctrProd,
                dt=dt
            )
            calculate.update(
                O_InitEvapoMP,
                inflow=O_Ch_EvapoTran,
                dt=dt
            )
            calculate.update(
                O_InitGWStockMP,
                inflow=O_ChGWMP,
                dt=dt
            )
            calculate.update(
                O_InitSWMP,
                inflow=O_ChSoilWMP,
                dt=dt
            )
            calculate.update(
                O_LastYHepp,
                inflow=O_HeppUseF1,
                outflow=O_HeppUseF2,
                dt=dt
            )
            calculate.update(
                O_ThisYHepp,
                inflow=O_HeppUseF0,
                outflow=O_HeppUseF1,
                dt=dt
            )
            calculate.update(
                O_WorstYHEPP,
                inflow=O_WYP,
                dt=dt
            )
            calculate.update(
                O_YearSim,
                inflow=Yearly_Tick,
                dt=dt
            )
            calculate.update(
                D_CumEvapTranspClass,
                inflow=D_ActEvapTransp + D_InterceptEvap,
                dt=dt
            )
            calculate.update(
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
            calculate.update(
                D_EvapTranspClass,
                inflow=D_WaterEvapIrrigation,
                dt=dt
            )
            calculate.update(
                D_GWArea,
                inflow=np.add(np.sum(D_Percolation, axis=1).reshape(subcatchment, 1), D_DeepInfiltration),
                outflow=np.add(
                    D_GWaDisch,
                    np.sum(D_WaterEvapIrrigation, axis=1).reshape(subcatchment, 1)
                ),
                dt=dt
            )
            calculate.update(
                D_SoilWater,
                inflow=D_Infiltration,
                outflow=(
                    D_ActEvapTransp +
                    D_Percolation +
                    D_SoilDischarge
                ),
                dt=dt
            )
            calculate.update(
                S_RelBulkDensity,
                inflow=(
                    S_StructureFormation +
                    S_RippingSurface +
                    S_SplashErosion
                ),
                outflow=S_Compaction,
                dt=dt
            )
            calculate.update(
                D_CumInflowtoLake,
                inflow=D_RiverFlowtoLake + D_GWtoLake,
                outflow=D_RestartL,
                dt=dt
            )
            calculate.update(
                D_CumTotRiverFlow,
                inflow=D_RiverDelay + D_RiverDirect,
                outflow=D_RestartR,
                dt=dt
            )
            calculate.update_conveyor(
                stock=D_StreamsSurfQ,
                inflow=D_SurfFlowObsPoint,
                outflow=D_SurfFlowRiver,
                transitTime=SurFlowRiverTransitTime,
                time=time,
                dt=dt
            )
            calculate.update(
                D_TotRiverFlowNoDelay,
                inflow=D_SurfFlowRiver[time] + D_DirectSurfFkowObsPoint,
                outflow=D_RiverDelay + D_RivInflLake,
                dt=dt
            )
            calculate.update(
                D_CumResvEvap,
                inflow=D_EvaporReservoir,
                dt=dt
            )
            calculate.update(
                D_SubcResVol,
                inflow=D_SubcResVol[time] + D_Influx_to_Resr,
                outflow=D_EvaporReservoir + D_SubCResOutflow,
                dt=dt
            )
            self.output['map']['O_EvapoTransAcc'].append(
                D_ActEvapTransp +
                D_InterceptEvap
            )
            self.output['map']['L_InFlowtoLake'].append(O_InFlowtoLake)
            self.output['map']['O_PercAcc'].append(D_Percolation)
            self.output['map']['O_RainAcc'].append(I_DailyRainAmount)
            self.output['map']['O_SurfQFlowAcc'].append(D_SurfaceFlow)
            self.output['map']['O_BaseFlowAcc'].append(
                np.multiply(
                    D_GWaDisch,
                    np.multiply(I_Simulation_Time >= O_StartMDay,
                                np.multiply(I_Simulation_Time < O_EndMDay,
                                            isI_StillWarmUp == 0)).transpose()
                )
            )
            self.output['map']['O_DeepInfAcc'].append(
                D_DeepInfiltration
            )
            self.output['map']['O_IntercAcc'].append(D_InterceptEvap)
            self.output['map']['O_SoilQFlowAcc'].append(D_SoilDischarge)
            self.output['map']['O_InfAcc'].append(D_Infiltration)
            self.output['map']['D_GWaDisch'].append(D_GWaDisch)
            self.output['map']['D_SoilDischarge'].append(D_SoilDischarge)

            # Display Water Balance
            self.output['timeseries']['display']['Water Balance']['I_RFlowdata_mmday'].append(I_RFlowdata_mmday)
            self.output['timeseries']['display']['Water Balance']['L_InFlowtoLake'].append(L_InFlowtoLake)

            # Display HEPP
            self.output['timeseries']['display']['HEPP']['L_HEPPWatUseFlow'].append(L_HEPPWatUseFlow)
            self.output['timeseries']['display']['HEPP']['L_LakeVol'].append(L_LakeVol[time])
            self.output['timeseries']['display']['HEPP']['L_HEPP_Kwh'].append(L_HEPP_Kwh)
            self.output['timeseries']['display']['HEPP']['L_LakeLevel'].append(L_LakeLevel)

            # Data Water Balance:
            self.output['timeseries']['data']['Water Balance']['I_RFlowdata_mmday'].append(I_RFlowdata_mmday)
            self.output['timeseries']['data']['Water Balance']['L_InFlowtoLake'].append(L_InFlowtoLake)
            self.output['timeseries']['data']['Water Balance']['O_RainAcc'].append(O_RainAcc)
            self.output['timeseries']['data']['Water Balance']['O_IntercAcc'].append(O_IntercAcc)
            self.output['timeseries']['data']['Water Balance']['O_EvapoTransAcc'].append(O_EvapoTransAcc)
            self.output['timeseries']['data']['Water Balance']['O_SoilQFlowAcc'].append(O_SoilQFlowAcc)
            self.output['timeseries']['data']['Water Balance']['O_InfAcc'].append(O_InfAcc)
            self.output['timeseries']['data']['Water Balance']['O_PercAcc'].append(O_PercAcc)
            self.output['timeseries']['data']['Water Balance']['O_DeepInfAcc'].append(O_DeepInfAcc)
            self.output['timeseries']['data']['Water Balance']['O_BaseFlowAcc'].append(O_BaseFlowAcc)
            self.output['timeseries']['data']['Water Balance']['O_SurfQFlowAcc'].append(O_SurfQFlowAcc)

            # Data Watershed Indicator
            self.output['timeseries']['data']['Watershed Indicator']['I_RainDoY'].append(I_RainDoY)
            self.output['timeseries']['data']['Watershed Indicator']['L_InFlowtoLake'].append(L_InFlowtoLake)
            self.output['timeseries']['data']['Watershed Indicator']['O_RainAcc'].append(O_RainAcc)
            self.output['timeseries']['data']['Watershed Indicator']['O_IntercAcc'].append(O_IntercAcc)
            self.output['timeseries']['data']['Watershed Indicator']['O_EvapoTransAcc'].append(O_EvapoTransAcc)
            self.output['timeseries']['data']['Watershed Indicator']['O_SoilQFlowAcc'].append(O_SoilQFlowAcc)
            self.output['timeseries']['data']['Watershed Indicator']['O_InfAcc'].append(O_InfAcc)
            self.output['timeseries']['data']['Watershed Indicator']['O_PercAcc'].append(O_PercAcc)
            self.output['timeseries']['data']['Watershed Indicator']['I_RFlowdata_mmday'].append(I_RFlowdata_mmday)
            self.output['timeseries']['data']['Watershed Indicator']['O_SurfQFlowAcc'].append(O_SurfQFlowAcc)

            # Data HEPP
            self.output['timeseries']['data']['HEPP']['O_BestYyHEPP'].append(O_BestYyHEPP[time])
            self.output['timeseries']['data']['HEPP']['O_WorstYHEPP'].append(O_WorstYHEPP[time])
            self.output['timeseries']['data']['HEPP']['L_CumHEPPUse'].append(L_CumHEPPUse[time])
            self.output['timeseries']['data']['HEPP']['O_FrBaseFlow'].append(O_FrBaseFlow)
            self.output['timeseries']['data']['HEPP']['O_FrSoilQuickFlow'].append(O_SoilQFlowAcc)
            self.output['timeseries']['data']['HEPP']['O_FrSurfQuickFlow'].append(O_SurfQFlowAcc)

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



            self.emit(QtCore.SIGNAL('update'), self.output, time)
            time = time + 1
