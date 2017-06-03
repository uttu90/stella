from PyQt4 import QtCore
import numpy as np
import utils as np_utils
import spatrain
import calculate


class SimulatingThread(QtCore.QThread):
    def __init__(self, parameters, data):
        super(SimulatingThread, self).__init__()
        self.parameters = parameters
        self.data = data

    def __del__(self):
        self.wait()

    def run(self):
        run_specs = self.parameters['run specs']
        begin = run_specs['from']
        end = run_specs['to']
        dt = run_specs['dt']
        obsPoint = 8
        vegClass = 20
        measurePeriod = 3
        subcatchment = 20

        initial_run = self.parameters['initial run']
        simulationTime = initial_run['Simulation Time']
        I_StartMYear = initial_run['I_StartMYear']
        I_StartDOYear = initial_run['I_StartDOYear']
        I_RainYearStar = initial_run['I_RainYearStar']
        I_CaDOYearStar = initial_run['I_CaDOYearStar']
        I_WarmUpTime = initial_run['I_WarmUpTime']
        O_MPeriodLength = initial_run['O_MPeriodLength']

        rainfall = self.parameters['rainfall']
        isI_UseSpatVarRain = rainfall['I_UseSpatVarRain?']
        I_RainMultiplier = rainfall['I_RainMultiplier']
        isI_RainCycle = rainfall['I_RainCycle?']
        I_Rain_IntensMean = rainfall['I_Rain_IntensMean']
        I_Rain_IntensCoefVar = rainfall['I_Rain_IntensCoefVar']
        I_Rain_GenSeed = rainfall['I_Rain_GenSeed']

        river = self.parameters['river']
        I_RoutVeloc_m_per_s = river['I_RoutVeloc_m_per_s']
        I_Tortuosity = river['I_Tortuosity']
        I_RiverflowDispersalFactor = river['I_RiverflowDispersalFactor']
        I_SurfLossFrac = river['I_SurfLossFrac']
        isI_DaminThisStream = np.array(
            river['I_DaminThisStream']
        ).reshape(subcatchment, 1)

        soilAndWaterBalance = self.parameters['soi and water balance']
        I_MaxInf = soilAndWaterBalance['I_MaxInf']
        I_MaxInfSoil = soilAndWaterBalance['I_MaxInfSoil']
        I_PowerInfiltRed = soilAndWaterBalance['I_PowerInfiltRed']
        isI_SoilPropConst = soilAndWaterBalance['I_SoilPropConst?']
        I_AvailWaterClassConst = soilAndWaterBalance['I_AvailWaterClassConst']
        I_SoilSatMinFCConst = soilAndWaterBalance['I_SoilSatMinFCConst']
        I_InitRelGW = soilAndWaterBalance['I_InitRelGW']
        isI_GWRelFracConst = soilAndWaterBalance['I_GWRelFracConst?']
        I_MaxDynGWConst = soilAndWaterBalance['I_MaxDynGWConst']
        I_GWRelFracConst = soilAndWaterBalance['I_GWRelFracConst']
        I_IntercepEffectionTransp = soilAndWaterBalance[
            'I_IntercepEffectionTransp']
        I_RainIntercDripRt = soilAndWaterBalance['I_RainIntercDripRt']
        I_RainMaxIntDripDur = soilAndWaterBalance['I_RainMaxIntDripDur']
        I_PercFracMultiplier = soilAndWaterBalance['I_PercFracMultiplier']
        I_InitRelSoil = soilAndWaterBalance['I_InitRelSoil']
        I_EvapotransMethod = soilAndWaterBalance['I_EvapotransMethod']
        I_SoilQflowFract = soilAndWaterBalance['I_SoilQflowFract']

        lake = self.parameters['lake']
        isL_Lake = np.array(lake['L_Lake?']).reshape(subcatchment, 1)
        isL_HEPP_Active = lake['L_HEPP_Active?']
        l_LakeTransMultiplier = lake['L_LakeTransMultiplier']
        l_LakeBottomElev = lake['L_LakeBottomElev']
        l_LakeElevPreHEPP = lake['L_LakeElevPreHEPP']
        l_LakeOverFIPostHEPP = lake['L_LakeOverFIPostHEPP']
        l_LakeLevelFullHEPP = lake['L_LakeLevelFullHEPP']
        l_LakeLevelHalfHEPP = lake['L_LakeLevelHalfHEPP']
        l_LakeLevelNoHEPP = lake['L_LakeLevelNoHEPP']
        l_LakeFloodTresh = lake['L_LakeFloodTresh']
        l_LakeQmecsHEPP = lake['L_LakeQmecsHEPP']
        l_LakeQmecsSanFlow = lake['L_LakeQmecsSanFlow']
        l_LakeOverFlowFract = lake['L_LakeOverFlowFract']
        l_LakeOverFIFlow = lake['L_LakeOverFIFlow']
        l_m3_per_kwh = lake['L_m3_per_kwh']
        l_ResrDepth = lake['L_ResrDepth']

        lake_hepp = self.parameters['lake hepp']
        o_CumRivInflowtoLakeMP = lake_hepp['O_CumRivInflowtoLakeMP']
        o_CumRivOutFlowMP = lake_hepp['O_CumRivOutFlowMP']
        o_HEPP_Kwh_per_dayMP = lake_hepp['O_HEPP_Kwh_per_dayMP']
        o_CumHEPPOutFlowMP = lake_hepp['O_CumHEPPOutFlowMP']
        o_RelOPTimeHEPPMP = lake_hepp['O_RelOPTimeHEPPMP']
        o_FrBaseFlow = lake_hepp['O_FrBaseFlow']
        o_FrSoilQuickFlow = lake_hepp['O_FrSoilQuickFlow']
        o_FrSurfQuickFlow = lake_hepp['O_FrSurfQuickFlow']

        grassAndCattle = self.parameters['Grass and Cattle']
        c_DailyTrampFac = grassAndCattle['C_DailyTrampFac']
        c_CattleSale = grassAndCattle['C_CattleSale']
        c_DailyIntake = grassAndCattle['C_DailyIntake']
        c_GrazingManConv = grassAndCattle['C_GrazingManConv']
        c_SurfLitDecFrac = grassAndCattle['C_SurfLitDecFrac']
        c_SurfManureDecFrac = grassAndCattle['C_SurfManureDecFrac']
        c_GrassLitConv = grassAndCattle['C_GrassLitConv']
        c_GrassLitMortFrac = grassAndCattle['C_GrassLitMortFrac']
        g_WUE = grassAndCattle['G_WUE']
        g_TramplingMultiplier = grassAndCattle['G_TramplingMultiplier']

        soilStructureDynamic = self.parameters['Soil Structure Dynamic']
        s_TrampMax = soilStructureDynamic['S_TrampMax']

        subcatchmentBalance = self.parameters['Subcatchment Balance']
        o_CumRainMP = subcatchmentBalance['O_CumRainMP']
        o_CumIntercEvapMP = subcatchmentBalance['O_CumIntercEvapMP']
        o_CumTranspMP = subcatchmentBalance['O_CumTranspMP']
        o_CumETLandMP = subcatchmentBalance['O_CumETLandMP']
        o_CumEvapTransMP = subcatchmentBalance['O_CumEvapTransMP']
        o_CumSurfQFlow = subcatchmentBalance['O_CumSurfQFlow']
        o_CumInfiltrationMP = subcatchmentBalance['O_CumInfiltrationMP']
        o_CumSoilQFlowMP = subcatchmentBalance['O_CumSoilQFlowMP']
        o_CumDebitPredMP = subcatchmentBalance['O_CumDebitPredMP']
        o_CumBaseFlowMP = subcatchmentBalance['O_CumBaseFlowMP']
        o_CumDebitDataMP = subcatchmentBalance['O_CumDebitDataMP']

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
            I_SoilSatminFCSub4
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

        I_AvailWatSub1 = np.array(
            self.data['I_AvailWatSub1']
        ).reshape(subcatchment, 1)
        I_AvailWatSub2 = np.array(
            self.data['I_AvailWatSub2']
        ).reshape(subcatchment, 1)
        I_AvailWatSub3 = np.array(
            self.data['I_AvailWatSub3']
        ).reshape(subcatchment, 1)
        I_AvailWatSub4 = np.array(
            self.data['I_AvailWatSub4']
        ).reshape(subcatchment, 1)
        I_AvailWatSubs = [
            I_AvailWatSub1,
            I_AvailWatSub2,
            I_AvailWatSub3,
            I_AvailWatSub4
        ]

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
            self.data['I_InterceptClass'] +
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ).reshape(1, vegClass)
        I_RelDroughtFact = np.array(
            self.data['I_RelDroughtFact'] +
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ).reshape(1, vegClass)
        I_Area = np.array(
            self.data['I_Area']
        ).reshape(subcatchment, 1)
        I_RoutingDistanceLoad = np.array(
            self.data['I_RoutingDistance']
        )
        insert_value = [0 for _ in range(20)]
        I_RoutingDistance = np.column_stack((
            I_RoutingDistanceLoad,
            insert_value,
            insert_value
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
        L_LakeVol = [(L_OutflTrVolPreHEPP * isL_HEPP_Active +
                     (1 - isL_HEPP_Active) * L_OutflTrVolPreHEPP)]
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
        I_MaxDynGWact = (np.multiply(I_GWRelFracConst, I_MaxDynGWConst) +
                         np.multiply(1 - I_GWRelFracConst, I_InitMaxDynGWSub))
        I_MaxDynGWArea = np.multiply(I_MaxDynGWact, I_RelArea)
        D_GWArea = [I_MaxDynGWArea * I_InitRelGW]
        O_InitGWStock = [np_utils.array_sum(I_MaxDynGWArea) * I_InitRelGW]
        I_InitPlantAvWat = I_PlantAvWatSub1
        I_InitFracVegClass = np.multiply(I_RelArea > 0, I_FracVegClass_1)
        I_AvailWaterConst = 250
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
        S_RelBulkDensity = [I_InitBD_BDRefVeg]
        D_CumInflowtoLake = [0]
        D_CumTotRiverFlow = [np.zeros(shape=(subcatchment, obsPoint))]
        D_StreamsSurfQ = [np.zeros(shape=(subcatchment, obsPoint))]
        D_TotRiverFlowNoDelay = [np.zeros(shape=(subcatchment, obsPoint))]
        D_CumResvEvap = [0]
        L_ResrDepth = 10000
        D_ReservoirVol = L_ResrDepth * np.multiply(isL_Lake, I_RelArea)
        D_SubcResVol = [np.multiply(D_ReservoirVol, isI_DaminThisStream)]
        print 'D_SubcResVol' + str(D_SubcResVol[0].shape)

        # const
        I_MaxInf = 700
        I_CaDOYStart = 0
        I_RainYearStart = 0
        Start = 0
        Trans1 = 1
        Trans2 = 2
        End = 3
        I_RainMultiplier = 1
        I_RainDoY_Stage = [1460, 2920, 4380, 5840, 7300, 8760]
        simulationTime = 10
        I_Rain_GenSeed = 200
        I_Rain_IntensCoefVar = 0.3
        I_Rain_IntensMean = 10
        isD_FeedingIntoLake = np.ones(shape=(subcatchment, 1))
        I_EvapotransMethod = 1
        I_MaxInfSSoil = 150
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

        for time in range(int(simulationTime)):
            I_Simulation_Time = int(
                time +
                I_CaDOYStart +
                365 * I_RainYearStart -
                isI_WarmEdUp[time] * (I_WarmUpTime + 1))
            I_Warmedup = 1 if time == int(I_WarmUpTime) else 0
            I_RainDoY = (I_Simulation_Time
                         if (isI_RainCycle == 0)
                         else 1 + I_Simulation_Time % 365)
            I_Flag1 = 1 if I_Simulation_Time < I_InputDataYears[Trans1] else 0
            I_Flag2 = (1
                       if I_Simulation_Time < I_InputDataYears[Trans2]
                          and I_Flag1 == 0
                       else 0)

            for index, stage in enumerate(I_RainDoY_Stage):
                I_SpatRainTime = I_RainMultiplier * (
                    spatrain.I_SpatRain[index][I_Simulation_Time]
                    if I_RainDoY < stage
                    else spatrain.I_SpatRain[6][I_Simulation_Time]
                )
                I_Daily_Evapotrans = (
                    I_Daily_Evap
                    if I_RainDoY < stage
                    else I_Daily_Evap[6]
                )
                for index, stage in enumerate(I_RainDoY_Stage):
                    I_DailyRain = (
                        (I_DailyRainYear[index][I_Simulation_Time]
                         if I_RainDoY <= stage
                         else I_DailyRainYear[6][
                            I_Simulation_Time]) *
                        np.ones(shape=(subcatchment, 1)) *
                        I_RainMultiplier
                    )
            I_RainPerDay = I_SpatRainTime if isI_UseSpatVarRain else I_DailyRain

            I_RainDuration = ((I_RainPerDay / I_Rain_IntensMean) *
                              min(max(0,
                                      1 - 3 * I_Rain_IntensCoefVar,
                                      np.random.normal(1,
                                                       I_Rain_IntensCoefVar,
                                                       I_Rain_GenSeed + 11250)[
                                          0]),
                                  1 + 3 * I_Rain_IntensCoefVar))

            I_GWRelFracNow = np_utils.get_variable_now(
                I_GWRelFracs,
                I_Flag1,
                I_Flag2,
                I_Simulation_Time,
                I_InputDataYears,
                subcatchment,
                I_RelArea)
            I_MaxDynGwSubNow = np_utils.get_variable_now(
                I_MaxDynGWSubs,
                I_Flag1,
                I_Flag2,
                I_Simulation_Time,
                I_InputDataYears,
                subcatchment,
                I_RelArea
            )
            I_FracVegClassNow = np_utils.get_variable_now(
                I_FracVegClasses,
                I_Flag1,
                I_Flag2,
                I_Simulation_Time,
                I_InputDataYears,
                subcatchment,
                I_RelArea
            )
            I_PWPSubNow = np_utils.get_variable_now(
                I_PWPSubs,
                I_Flag1,
                I_Flag2,
                I_Simulation_Time,
                I_InputDataYears,
                subcatchment,
                I_RelArea
            )
            I_SoilSatminFCSubNow = np_utils.get_variable_now(
                I_SoilSatminFCSubs,
                I_Flag1,
                I_Flag2,
                I_Simulation_Time,
                I_InputDataYears,
                subcatchment,
                I_RelArea
            )
            I_RivFlowTimeNow = np_utils.get_variable_now(
                I_RivFlowTimes,
                I_Flag1,
                I_Flag2,
                I_Simulation_Time,
                I_InputDataYears,
                subcatchment,
                I_RelArea
            )
            I_TopSoilBD_BDRefNow = np_utils.get_variable_now(
                I_TopSoilBD_BDRefs,
                I_Flag1,
                I_Flag2,
                I_Simulation_Time,
                I_InputDataYears,
                subcatchment,
                I_RelArea
            )
            I_AvailWatClassNow = np_utils.get_variable_now(
                I_AvailWatSubs,
                I_Flag1,
                I_Flag2,
                I_Simulation_Time,
                I_InputDataYears,
                subcatchment,
                I_RelArea
            )
            I_FracVegClassSum1 = np_utils.array_sum(I_FracVegClass_1)
            I_FracVegClassSum2 = np_utils.array_sum(I_FracVegClass_2)
            I_FracVegClassSum3 = np_utils.array_sum(I_FracVegClass_3)
            I_FracVegClassSum4 = np_utils.array_sum(I_FracVegClass_4)
            I_FracVegClassSumNow = np_utils.array_sum(I_FracVegClassNow)
            I_DailyRainAmount = np.multiply(
                I_RainPerDay,
                np.multiply(I_FracVegClassNow, I_RelArea)
            )
            print I_DailyRainAmount.shape == (20, 20)
            isI_StillWarmUp = 1 if time <= I_WarmUpTime else 0
            I_WUcorrection = 1 if time == int(I_WarmUpTime + 1) else 0
            I_WarmedUp = 1 if time == int(I_WarmUpTime) else 0
            isO_Reset = 1 if I_WarmedUp == 1 or I_WUcorrection == 1 else 0
            I_FracArea = np.multiply(I_FracVegClassNow, I_RelArea)
            I_TimeEvap = (
                0
                if I_RainDoY == 0
                else 365 if I_RainDoY % 365 == 0 else I_RainDoY % 365
            )
            I_MoY = 0 if I_RainDoY == 0 else int(I_TimeEvap / 30.5) + 1
            if I_EvapotransMethod == 1:
                I_PotEvapTransp = np.multiply(
                    I_Evapotrans[I_MoY],
                    np.multiply(I_MultiplierEvapoTrans[I_MoY], I_FracArea)
                )
            else:
                I_PotEvapTransp = np.multiply(
                    I_Daily_Evapotrans[I_MoY],
                    np.multiply(I_MultiplierEvapoTrans, I_FracArea)
                )
            print I_PotEvapTransp.shape == (20, 20)
            I_MaxInfSubSAreaClass = I_MaxInfSSoil * I_FracArea
            print I_MaxInfSubSAreaClass.shape == (20, 20)
            I_MaxInfArea = I_MaxInf * np.multiply(
                I_FracArea,
                np.power(np.divide(0.7,
                                   I_TopSoilBD_BDRefNow,
                                   out=np.zeros_like(I_TopSoilBD_BDRefNow),
                                   where=I_TopSoilBD_BDRefNow != 0),
                         I_PowerInfiltRed
                         )
            )
            print I_MaxInfArea.shape == (20, 20)
            I_CanIntercAreaClass = np.multiply(I_InterceptClass, I_FracArea)
            print I_CanIntercAreaClass.shape == (20, 20)
            I_AvailWaterClass = (I_AvailWaterConst * I_FracArea
                                 if isI_SoilPropConst
                                 else np.multiply(I_AvailWatClassNow,
                                                  I_FracArea))
            print I_AvailWaterClass.shape == (20, 20)
            I_SoilSatClass = (
            (I_AvailWaterConst + I_SoilSatMinFCConst) * I_FracArea
            if isI_SoilPropConst
            else np.add(I_SoilSatminFCSubNow,
                        np.multiply(I_AvailWatClassNow, I_FracArea)))
            print I_SoilSatClass.shape == (20, 20)
            I_GWRelFrac = I_GWRelFracConst if isI_SoilPropConst else I_GWRelFracNow
            I_MaxDynGWact = I_MaxDynGWConst if I_GWRelFracConst else I_MaxDynGwSubNow
            I_MaxDynGWArea = np.multiply(I_MaxDynGWact, I_RelArea)
            print I_MaxDynGWArea.shape == (20, 1)
            I_InitTotGW = np.add(I_MaxDynGWArea, I_InitRelGW)
            D_InterceptEvap = np.multiply(
                I_CanIntercAreaClass,
                (1 - np.exp(-np.divide(
                    I_DailyRainAmount,
                    I_CanIntercAreaClass,
                    out=np.zeros_like(
                        I_CanIntercAreaClass),
                    where=I_CanIntercAreaClass != 0))))
            print D_InterceptEvap.shape == (20, 20)
            I_FracVegClassNow_Multiply_I_RelArea = np.multiply(
                I_FracVegClassNow,
                I_RelArea
            )
            D_RainInterc = np.divide(
                D_InterceptEvap,
                I_FracVegClassNow_Multiply_I_RelArea,
                out=np.ones_like(D_InterceptEvap),
                where=I_FracVegClassNow_Multiply_I_RelArea != 0)
            D_RainIntercDelay = (
                np.minimum(
                    I_RainMaxIntDripDur,
                    np_utils.array_sum(D_RainInterc, shape=(subcatchment, 1))
                ) / I_RainIntercDripRt)
            I_RainTimeAvForInf = np.minimum(
                24,
                I_RainDuration + D_RainIntercDelay
            )
            D_Infiltration = np.multiply(
                (1 - isL_Lake),
                np.minimum(
                    np.minimum(I_SoilSatClass - D_SoilWater[time],
                               np.multiply(I_MaxInfArea,
                                           I_RainTimeAvForInf) / 24),
                    I_DailyRainAmount - D_InterceptEvap))
            I_RelDroughtFact_AvailWaterClass = np.multiply(
                I_RelDroughtFact,
                I_AvailWaterClass)
            D_RelWaterAv = np.minimum(
                1,
                np.divide(
                    D_SoilWater[time],
                    I_RelDroughtFact_AvailWaterClass,
                    out=np.ones_like(D_SoilWater[time]),
                    where=I_RelDroughtFact_AvailWaterClass != 0
                )
            )
            D_Irrigation = np.minimum(
                np.divide(
                    np.multiply(D_GWArea[time],
                                np.multiply(isD_GWUseFacility,
                                            np.multiply(
                                                D_GW_Utilization_fraction,
                                                np.subtract(1, D_RelWaterAv)))),
                    D_IrrigEfficiency,
                    out=np.zeros(shape=(subcatchment, vegClass)),
                    where=D_IrrigEfficiency != 0),
                I_PotEvapTransp)

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

            D_WaterEvapIrrigation = np.multiply(
                D_IrrigEfficiency > 0,
                D_Irrigation * (1 - D_IrrigEfficiency))

            D_GWaDisch = np.multiply(D_GWArea[time], I_GWRelFrac)

            D_DeepInfiltration = np.multiply(
                isL_Lake == 1,
                np.minimum(
                    np.minimum(
                        np.minimum(
                            np.multiply(
                                np_utils.array_sum(I_MaxInfArea,
                                                    shape=(subcatchment, 1)),
                                I_RainTimeAvForInf
                            ) / 24 - np_utils.array_sum(
                                I_SoilSatClass,
                                shape=(subcatchment, 1)) +
                            np_utils.array_sum(D_SoilWater[time],
                                      shape=(subcatchment, 1)),
                            np_utils.array_sum(I_MaxInfSubSAreaClass,
                                      shape=(subcatchment, 1))
                        ),
                        np_utils.array_sum(I_DailyRainAmount,
                                           shape=(subcatchment, 1)) -
                        np_utils.array_sum(D_InterceptEvap,
                                           shape=(subcatchment, 1)) -
                        np_utils.array_sum(D_Infiltration,
                                           shape=(subcatchment, 1))),
                    I_MaxDynGWArea - D_GWArea[time]))
            print 'D_DeepInfiltration', D_DeepInfiltration.shape, D_GWArea[time].shape
            D_ActEvapTransp = np.multiply(
                isL_Lake != 1,
                np.multiply(
                    I_PotEvapTransp -
                    np.multiply(I_InterceptEffectonTransp, D_InterceptEvap),
                    D_RelWaterAv))
            print 'D_SurfaceFlow'
            print I_DailyRainAmount.shape, D_InterceptEvap.shape, D_Infiltration.shape, D_DeepInfiltration.shape
            D_SurfaceFlow = (
                np.multiply(isL_Lake == 1,
                            (np_utils.array_sum(
                                I_DailyRainAmount,
                                shape=(subcatchment, 1)) +
                             np.multiply(
                                 isL_Lake != 1,
                                 (np_utils.array_sum(
                                     I_DailyRainAmount,
                                     shape=(subcatchment, 1)
                                 ) -
                                  np_utils.array_sum(
                                      D_InterceptEvap,
                                      shape=(subcatchment, 1)
                                  ) -
                                  np_utils.array_sum(
                                      D_Infiltration,
                                      shape=(subcatchment, 1)
                                  ) -
                                  D_DeepInfiltration)
                             ))))
            D_SoilQflowRelFrac = np.ones(
                shape=(subcatchment, 1)
            ) * I_SoilQflowFrac

            D_SoilDischarge = np.multiply(
                D_SoilQflowRelFrac,
                (D_SoilWater[time] - I_AvailWaterClass)
            )
            G_GrassAll = np_utils.array_sum(G_GrassStandingBiomass[time])
            G_Grazing = (0
                         if G_GrassAll == 0
                         else (C_StockingRate[time] *
                               C_DailyIntake *
                               G_GrassStandingBiomass[time] /
                               G_GrassAll))
            C_TrampComp = C_DailyTrampFac * G_Grazing / C_DailyIntake
            C_DeathRate = C_StockingRate[time] * C_DailyIntake - G_GrassAll
            C_Destoking = min(C_StockingRate[time], C_CattleSale + C_DeathRate)
            C_Stocking = 0 * C_StockingRate[time]
            G_GrassFract_Biomass = np.zeros(vegClass)
            G_GrowthRate = G_WUE * np.multiply(D_ActEvapTransp,
                                               G_GrassFract_Biomass)
            G_GrassAll = np_utils.array_sum(G_GrassStandingBiomass[time])
            G_LeafMortality = (G_GrassStandingBiomass[time] * G_GrassMortFrac +
                               G_Grazing * G_TramplingMultiplier)
            G_LitterDeposition = G_LeafMortality * G_GrassLitConv
            G_Incorporation_DecaySurfLit = (G_SurfaceLitter[time] *
                                            G_SurfLitDecFrac)
            G_FaecesProd = G_Grazing * G_GrazingManConv
            G_Incorporation_DecayManure = (G_SurfManure[time] *
                                           G_SurfManureDecFrac)
            G_SurfaceCover = (G_GrassStandingBiomass[time] +
                              G_SurfaceLitter[time] +
                              G_SurfManure[time])
            S_RainAtSoilSurface = I_DailyRainAmount - D_InterceptEvap.T
            S_Compaction = (
                np.multiply((1.3 - S_RelBulkDensity[time]), C_TrampComp) /
                S_TrampMax)
            S_SplashErosion = (0 * np.divide(
                np.multiply(G_SurfaceCover,
                            S_RainAtSoilSurface),
                I_RainDuration,
                out=np.zeros_like(G_SurfaceCover),
                where=I_RainDuration != 0))

            S_StructureFormation = 0 * np.multiply(S_RelBulkDensity[time],
                                                   G_SurfaceCover)
            D_ReservoirVol = L_ResrDepth * np.multiply(isL_Lake, I_RelArea)
            print D_SubcResVol[time].shape
            D_SubCResOutflow = np.add(
                np.multiply(
                    D_SubcResVol[time] > D_ReservoirVol,
                    np.subtract(D_SubcResVol[time], D_ReservoirVol)),
                np.multiply(D_SubcResVol[time] < D_ReservoirVol,
                            D_SubCResUseFrac[I_RainDoY] * D_SubcResVol[time]))
            D_RoutingTime = np.divide(
                I_RoutingDistance,
                (np.multiply(I_RivFlowTimeNow,
                             I_RoutVeloc_m_per_s) * 3.6 * 24 * I_Tortuosity))
            print D_RoutingTime.shape
            I_ReleaseFrac = np.minimum(
                1,
                np.divide(I_RiverflowDispersalFactor,
                          D_RoutingTime,
                          out=np.ones(shape=(subcatchment, obsPoint)),
                          where=D_RoutingTime!=0))
            print D_SurfaceFlow.shape, D_GWaDisch.shape, D_FracGWtoLake.shape, D_SoilDischarge.shape, D_SubCResOutflow.shape, isI_DaminThisStream.shape
            D_TotalStreamInflow = (
                D_SurfaceFlow +
                np.multiply(
                    D_GWaDisch,
                    (1 - D_FracGWtoLake) +
                    np_utils.array_sum(D_SoilDischarge,
                                       shape=(subcatchment, 1))) +
                np.multiply(D_SubCResOutflow,
                            (1 - isI_DaminThisStream)))
            print D_RoutingTime.shape, isD_FeedingIntoLake.shape, D_TotalStreamInflow.shape, I_ReleaseFrac.shape
            D_RivLakeSameDay = np.multiply(
                D_RoutingTime >= 0,
                np.multiply(D_RoutingTime < 1,
                            np.multiply(isD_FeedingIntoLake,
                                        np.multiply(D_TotalStreamInflow,
                                                    I_ReleaseFrac))))

            D_RivInflLake = np.multiply(
                np.multiply(
                    I_ReleaseFrac[:, 0].reshape(subcatchment, 1),
                    D_TotRiverFlowNoDelay[time][:, 0].reshape(subcatchment, 1)),
                isD_FeedingIntoLake)
            D_RivInflLake = np.repeat(D_RivInflLake, 8).reshape(subcatchment,
                                                                obsPoint)
            D_RiverFlowtoLake = (np_utils.array_sum(D_RivLakeSameDay,
                                                    shape=(1, obsPoint))[0][0] +
                                 np_utils.array_sum(D_RivInflLake,
                                                    shape=(1, obsPoint))[0][0])
            D_GWLakeSub = np.multiply(D_FracGWtoLake, D_GWaDisch)
            D_GWtoLake = np_utils.array_sum(D_GWLakeSub)
            D_RestartL = isO_Reset * D_CumInflowtoLake[time] / dt
            I_ReleaseFract = np.minimum(
                1,
                np.divide(I_RiverflowDispersalFactor,
                          D_RoutingTime,
                          out=np.ones_like(D_RoutingTime),
                          where=D_RoutingTime > 0))
            D_TotalStreamInflow = (
                (D_SurfaceFlow +
                 np.multiply(D_GWaDisch, (1 - D_FracGWtoLake)) +
                 np_utils.array_sum(D_SoilDischarge, shape=(subcatchment, 1))) +
                np.multiply(D_SubCResOutflow, (1 - isI_DaminThisStream)))
            D_DirectSurfFkowObsPoint = np.multiply(
                np.multiply(D_RoutingTime >= 0, D_RoutingTime < 1),
                np.multiply(D_TotalStreamInflow, (1 - I_ReleaseFrac)))
            D_RiverDirect = np.multiply(
                np.multiply(D_RoutingTime > 0, D_RoutingTime < 1),
                np.multiply((1 - isD_FeedingIntoLake),
                            np.multiply(D_TotalStreamInflow, I_ReleaseFrac)))
            D_RivInfLake = np.multiply(
                np.multiply(I_ReleaseFrac, D_TotRiverFlowNoDelay[time]),
                isD_FeedingIntoLake)
            D_SurfFlowRiver = np.multiply(D_RoutingTime > 1, D_RoutingTime)
            D_CurrRivVol = (
            np_utils.array_sum(
                D_StreamsSurfQ[time],
                shape=(1, obsPoint)
            )[0][0] +
            np_utils.array_sum(
                D_TotRiverFlowNoDelay[time],
                shape=(1, obsPoint))[0][0]
            )
            D_RestartR = np.multiply(isO_Reset, D_CumTotRiverFlow[time]) / dt
            D_RiverDelay = np.multiply(
                I_ReleaseFrac,
                np.multiply(D_TotRiverFlowNoDelay[time],
                            (1 - isD_FeedingIntoLake))
            )
            D_SurfFlowObsPoint = np.multiply(D_RoutingTime >= 1,
                                             D_TotalStreamInflow)

            L_LakeTransDef = np.add(
                np.multiply(isL_Lake,
                            (-D_ActEvapTransp[5])),
                I_PotEvapTransp[5])

            L_LakeArea = np.multiply(isL_Lake,
                                     I_RelArea,
                                     out=np.zeros_like(isL_Lake),
                                     where=isL_Lake != 1)

            L_LakeLevel = (
                (np_utils.array_sum(L_LakeArea) > 0) *
                L_LakeVol[time] / (
                    1000 * np_utils.array_sum(L_LakeArea) + L_LakeBottomElev)
            )

            L_Lakelevelexcess = (
                L_LakeLevel -
                (1 - isL_HEPP_Active) * L_LakeElevPreHEPP -
                isL_HEPP_Active * L_LakeOverFlPostHEPP)
            L_LakeArea = np.multiply(
                isL_Lake == 1,
                np.multiply(isL_Lake, I_RelArea))
            L_HEPP_Daily_Dem = L_QmecsHEPP * 3600 * 24 / I_TotalArea * 10 ** -3
            L_HEPPWatUseFlow = L_HEPP_Outflow if isL_HEPP_Active == 1 else 0
            L_HEPP_Kwh = 1000 * I_TotalArea * L_HEPPWatUseFlow / L_m3_per_kwh
            L_HEPP_Outflow = (
                L_HEPP_Daily_Dem
                if L_LakeLevel > L_LakeLevelFullHEPP
                else L_HEPP_Daily_Dem * 0.5 * (
                    1 +
                    max(0,
                        (L_LakeLevel - L_LakeLevelHalfHEPP) /
                        (L_LakeLevelFullHEPP - L_LakeLevelHalfHEPP)))
                if L_LakeLevel > L_LakeLevelNoHEPP else 0)
            L_HEPP_OpTimeRel = (
            (L_CumHEPPUse[time] / L_HEPP_Daily_Dem) / I_Simulation_Time
            if I_Simulation_Time > 0 and isI_WarmEdUp[time] == 1
            else 0)
            L_EvapLake = min(np_utils.array_sum(L_LakeTransDef),
                             L_LakeVol[time]) * L_LakeTranspMultiplier
            L_SanitaryFlow = L_QmecsSanFlow * 3600 * 24 / I_TotalArea * 10 ** -3
            L_OutflTrVolPreHEPP = 1000 * (
                L_LakeElevPreHEPP -
                L_LakeBottomElev) * np_utils.array_sum(L_LakeArea)
            L_OutflTrVoPostHEPP = 1000 * (
                L_LakeOverFlPostHEPP -
                L_LakeBottomElev) * np_utils.array_sum(L_LakeArea)
            L_RivOutFlow = max(isL_HEPP_Active * L_SanitaryFlow,
                               (L_LakeVol[time] - (
                                   L_OutflTrVoPostHEPP
                                   * isL_HEPP_Active) - L_OutflTrVolPreHEPP * (
                                    1 - isL_HEPP_Active)) * (
                               L_LakeOverFlowFrac) * (
                                   1 + L_Lakelevelexcess ** L_LakeOverFlPow))
            L_InFlowtoLake = D_RiverFlowtoLake + D_GWtoLake
            L_RestartR = isO_Reset * L_CumRivOutFlow[time] / dt
            L_RestartH = isO_Reset * L_CumHEPPUse[time]
            L_RestartE = isO_Reset * L_CumEvapLake[time] / dt
            O_TotStreamFlow = (O_CumBaseFlow[time] +
                               O_CumSoilQFlow[time] +
                               O_CumSurfQFlow[time])
            D_DeltaStockRiver = D_InitRivVol[time] - D_CurrRivVol
            D_SurfaceFlowAcc = np_utils.array_sum(D_SurfaceFlow[time])
            O_DeltaGWStock = O_InitGWStock[time] - np_utils.array_sum(D_GWArea[time])
            O_DeltaSoilWStock = O_InitSoilW[time] - np_utils.array_sum(D_SoilWater[time])
            O_ChkAllCatchmAccFor = (-O_CumRain[time] +
                                    O_CumIntercE[time] +
                                    O_CumTransp[time] +
                                    O_TotStreamFlow -
                                    O_DeltaGWStock -
                                    O_DeltaSoilWStock)
            O_DeltaStockLake = D_InitLakeVol[time] - L_LakeVol[time]
            O_ChkAllLakeAccFor = (D_CumInflowtoLake[time] -
                                  L_CumEvapLake[time] -
                                  L_CumRivOutFlow[time] -
                                  L_CumHEPPUse[time] +
                                  O_DeltaStockLake)
            D_CumTotRiverFlowAll = np_utils.array_sum(D_CumTotRiverFlow[time], shape=(1, obsPoint))[0][0]
            O_ChkAllRiverAccFor = (O_TotStreamFlow -
                                   D_CumTotRiverFlowAll -
                                   D_CumInflowtoLake[time] +
                                   D_DeltaStockRiver)
            O_DailyRainSubCtm = np_utils.array_sum(I_DailyRainAmount, shape=(subcatchment, 1))
            O_FrBaseFlow = (O_CumBaseFlow[time] / O_TotStreamFlow
                            if O_TotStreamFlow > 0
                            else 0)
            O_FrSoilQuickFlow = (O_CumSoilQFlow[time] / O_TotStreamFlow
                                 if O_TotStreamFlow > 0
                                 else 0)
            O_FrSurfQuickFlow = (O_CumSurfQFlow[time] / O_TotStreamFlow
                                 if O_TotStreamFlow else 0)
            O_RainYesterday = O_RainYest[time] * I_WarmedUp
            O_RainHalfDelayed = (np_utils.array_sum(O_RainYesterday[time]) +
                                 np_utils.array_sum(I_DailyRainAmount)) / 2
            O_RelWatAvVegSubc = np.multiply(D_RelWaterAv, I_FracVegClassNow)
            O_RelWatAv_Subc = np.divide(
                np_utils.array_mean(O_RelWatAvVegSubc, shape=(subcatchment, 1)),
                np_utils.array_sum(I_FracVegClassNow, shape=(subcatchment, 1)),
                out=np.ones(shape=(subcatchment, 1)),
                where=np_utils.array_sum(I_FracVegClassNow, shape=(subcatchment, 1)) > 0)
            O_RelWatAv_Overall = np_utils.array_mean(O_RelWatAv_Subc)
            O_Rel_ET_Subc = np.divide(
                D_InterceptEvap +
                D_ActEvapTransp,
                I_PotEvapTransp,
                out=np.zeros_like(I_PotEvapTransp),
                where=I_PotEvapTransp != 0)
            O_Reset = 1 if I_WarmedUp == 1 or I_WUcorrection == 1 else 0
            S_RainAtSoilSurface = I_DailyRainAmount - D_InterceptEvap

            O_InitLake = O_Reset * (L_LakeVol[time] - D_InitLakeVol[time])
            O_InitRiv = O_Reset * (D_CurrRivVol - D_InitLakeVol[time])
            O_BaseFlowAcc = np_utils.array_sum(D_GWaDisch) * I_WarmedUp
            O_CumDeepInfAcc = np_utils.array_sum(D_DeepInfiltration) * I_WarmedUp
            O_EvapoTransAcc = ((np_utils.array_sum(D_ActEvapTransp) +
                                np_utils.array_sum(D_InterceptEvap)) * I_WarmedUp
                               if np_utils.array_sum(I_PotEvapTransp) > 0 else 0)
            _InfAcc = np_utils.array_sum(D_Infiltration) * I_WarmedUp
            O_AccET = np_utils.array_sum(D_InterceptEvap) * I_WarmedUp
            O_PercAcc = np_utils.array_sum(D_Percolation) * I_WarmedUp
            O_RainAcc = np_utils.array_sum(I_DailyRainAmount) * I_WarmedUp
            O_CumSoilQFlowAcc = np_utils.array_sum(D_SoilDischarge) * I_WarmedUp
            O_SurfQFlowAcc = np_utils.array_sum(D_SurfaceFlow) * I_WarmedUp
            O_TranspAcc = np_utils.array_sum(D_ActEvapTransp) * I_WarmedUp
            O_InitGW = (np_utils.array_sum(D_GWArea[time]) - O_InitGWStock[time])
            O_InitSW = O_Reset * (np_utils.array_sum(D_SoilWater[time]) - O_InitSoilW[time])
            O_RainToday = np_utils.array_sum(I_DailyRainAmount, shape=(subcatchment, 1)) * I_WarmedUp
            O_LastYearHEPP = ((O_ThisYHepp[time] -
                               O_LastYHepp[time]) /
                              (365 * L_HEPP_Daily_Dem)
                              if O_LastYHepp[time] > 0
                              else 0)
            O_BYP = (-O_BestYyHEPP + O_LastYearHEPP
                     if O_LastYearHEPP > 0 and O_LastYearHEPP > O_BestYyHEPP
                     else 0)
            O_StarMYear = np.array([4, 6, 8]).reshape((1, measurePeriod))
            O_StartDOY = np.array([1, 1, 1]).reshape((1, measurePeriod))
            O_StartMDay = (O_StarMYear - 1) * 365 + 1 + (O_StartDOY - 1)
            O_EndMDay = O_StartMDay + O_MPeriodLength
            Yearly_Tick = 1 if I_WarmedUp == 1 and time % 365 == 0 else 0
            for index, stage in enumerate(I_RainDoY_Stage):
                I_DebitTime = (I_RFlowData[index]
                               if I_Simulation_Time <= stage
                                else I_RFlowData[6] if I_Simulation_Time <= 10220
                                else I_RFlowData[7])
            I_RFlowDataQmecs = I_DebitTime[I_Simulation_Time]
            I_ContrSubcArea = np.multiply(I_RelArea, isI_SubcContr)
            I_RFlowDataQ = I_RFlowDataQmecs * 24 * 3600 * 10 ** 3
            I_ContrAr = np_utils.array_sum(
                I_ContrSubcArea
            ) * I_TotalArea * 10 ** 6
            if np_utils.array_sum(I_ContrSubcArea) > 0:
                I_RFlowdata_mmday = I_RFlowDataQ / I_ContrAr
            else:
                I_RFlowdata_mmday = 0
            print 'O_Ch_in_GWStockMP', O_InitGWStockMP[time].shape, O_Ch_inGWStock[time].shape
            O_Ch_in_GWStockMP = np.multiply(
                np.multiply(O_StartMDay < time, O_EndMDay + 1 > time),
                np_utils.array_sum(D_GWArea[time]) - O_InitGWStockMP[time] - O_Ch_inGWStock[time])
            O_Ch_in_WStockMP = np.multiply(
                np.multiply(O_StartMDay < time, O_EndMDay + 1 > time),
                np_utils.array_sum(D_SoilWater[time]) - O_InitSWMP[time] - O_Ch_inWStock[time])
            O_BaseFlowAccMP = np.multiply(
                np_utils.array_sum(D_GWaDisch),
                np.multiply(I_Simulation_Time >= O_StartMDay,
                            np.multiply(I_Simulation_Time < O_EndMDay,
                                        isI_StillWarmUp == 0)))
            O_DebitDataAccMP = np.multiply(
                I_RFlowdata_mmday,
                np.multiply(I_Simulation_Time >= O_StartMDay,
                            np.multiply(I_Simulation_Time < O_EndMDay,
                                        isI_StillWarmUp == 0)))
            print 'D_RiverFlowtoLake', D_RiverFlowtoLake
            O_DebitPredAccMP = np.multiply(
                D_RiverFlowtoLake,
                np.multiply(I_Simulation_Time >= O_StartMDay,
                            np.multiply(I_Simulation_Time < O_EndMDay,
                                        isI_StillWarmUp == 0)))
            O_EvapLakeMP = np.multiply(
                L_EvapLake,
                np.multiply(I_Simulation_Time >= O_StartMDay,
                            np.multiply(I_Simulation_Time < O_EndMDay,
                                        isI_StillWarmUp == 0)))
            O_Ch_in_EvapoTrans = np.multiply(
                np_utils.array_sum(D_CumEvapTranspClass) - O_InitEvapoMP[time] - O_CumEvapTransMP[time],
                np.multiply(I_Simulation_Time >= O_StartMDay,
                            np.multiply(I_Simulation_Time < O_EndMDay,
                                        isI_StillWarmUp == 0)))
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
            print 'O_Hepp_ElctrProd', O_Hepp_ElctrProd.shape
            O_Ch_EvapoTran = np.multiply(np_utils.array_sum(D_CumEvapTranspClass),
                                         time == O_StartMDay)
            O_ChGWMP = np.multiply(np_utils.array_sum(D_GWArea[time]), time == O_StartMDay)
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
            O_InfAcc = np_utils.array_sum(D_Infiltration) * isI_WarmEdUp[time]
            O_IntercAcc = np_utils.array_sum(D_InterceptEvap) * isI_WarmEdUp[time]
            O_SoilQFlowAcc = np_utils.array_sum(D_SoilDischarge) * isI_WarmEdUp[time]
            O_SoilQflow_Subca = np_utils.array_sum(
                D_SoilDischarge,
                shape=(subcatchment, 1)
            )
            D_EvaporReservoir = I_Evapotrans[I_MoY] * np_utils.array_sum(isL_Lake)
            D_Influx_to_Resr = np.multiply(
                isI_DaminThisStream == 1,
                (D_GWaDisch +
                 np_utils.array_sum(D_SoilDischarge, shape=(subcatchment, 1))
                 + D_SurfaceFlow)
            )
            calculate.update(
                C_StockingRate,
                inflow=C_Stocking,
                outflow=C_Destoking,
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
            print 'D_EvapTranspClass', D_EvapTranspClass[time].shape, D_EvapTranspClass[time]
            calculate.update(
                D_EvapTranspClass,
                inflow=D_WaterEvapIrrigation,
                dt=dt
            )
            calculate.update(
                D_GWArea,
                inflow=np_utils.array_sum(D_Percolation, shape=(subcatchment, 1)),
                outflow=(
                    D_DeepInfiltration +
                    D_GWaDisch +
                    np_utils.array_sum(D_WaterEvapIrrigation, shape=(subcatchment, 1)
                )),
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
                D_StreamsSurfQ,
                inflow=D_SurfFlowObsPoint,
                outflow=D_SurfFlowRiver,
                time=time,
                dt=dt
            )
            calculate.update(
                D_TotRiverFlowNoDelay,
                inflow=D_SurfFlowRiver + D_DirectSurfFkowObsPoint,
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
            print 'calculating' + str(time)

        print ('calculate finished')
