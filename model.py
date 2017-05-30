from PyQt4 import QtCore
import numpy as np


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

        initial_run = self.parameters['initial run']
        simulationTime = initial_run['Simulation Time']
        i_StartMYear = initial_run['I_StartMYear']
        i_StartDOYear = initial_run['I_StartDOYear']
        i_RainYearStar = initial_run['I_RainYearStar']
        i_CaDOYearStar = initial_run['I_CaDOYearStar']
        i_WarmUpTime = initial_run['I_WarmUpTime']
        o_MPeriodLength = initial_run['O_MPeriodLength']

        rainfall = self.parameters['rainfall']
        isI_UseSpatVarRain = rainfall['I_UseSpatVarRain?']
        i_RainMultiplier = rainfall['I_RainMultiplier']
        isI_RainCycle = rainfall['I_RainCycle?']
        i_Rain_IntensMean = rainfall['I_Rain_IntensMean']
        i_Rain_IntensCoefVar = rainfall['I_Rain_IntensCoefVar']
        i_Rain_GenSeed = rainfall['I_Rain_GenSeed']

        river = self.parameters['river']
        i_RoutVeloc_m_per_s = river['I_RoutVeloc_m_per_s']
        i_Tortuosity = river['I_Tortuosity']
        i_RiverflowDispersalFactor = river['I_RiverflowDispersalFactor']
        i_SurfLossFrac = river['I_SurfLossFrac']
        i_DaminThisStream = river['I_DaminThisStream']

        soilAndWaterBalance = self.parameters['soi and water balance']
        i_MaxInf = soilAndWaterBalance['I_MaxInf']
        i_MaxInfSoil = soilAndWaterBalance['I_MaxInfSoil']
        i_PowerInfiltRed = soilAndWaterBalance['I_PowerInfiltRed']
        isI_SoilPropConst = soilAndWaterBalance['I_SoilPropConst?']
        i_AvailWaterClassConst = soilAndWaterBalance['I_AvailWaterClassConst']
        i_SoilSatMinFCConst = soilAndWaterBalance['I_SoilSatMinFCConst']
        i_InitRelGW = soilAndWaterBalance['I_InitRelGW']
        isI_GWRelFracConst = soilAndWaterBalance['I_GWRelFracConst?']
        i_MaxDynGWConst = soilAndWaterBalance['I_MaxDynGWConst']
        i_GWRelFracConst = soilAndWaterBalance['I_GWRelFracConst']
        i_IntercepEffectionTransp = soilAndWaterBalance[
            'I_IntercepEffectionTransp']
        i_RainIntercDripRt = soilAndWaterBalance['I_RainIntercDripRt']
        i_RainMaxIntDripDur = soilAndWaterBalance['I_RainMaxIntDripDur']
        i_PercFracMultiplier = soilAndWaterBalance['I_PercFracMultiplier']
        i_InitRelSoil = soilAndWaterBalance['I_InitRelSoil']
        i_EvapotransMethod = soilAndWaterBalance['I_EvapotransMethod']
        i_SoilQflowFract = soilAndWaterBalance['I_SoilQflowFract']

        lake = self.parameters['lake']
        isL_Lake = lake['L_Lake?']
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

        subcatchment = 20
        i_Frac_1_1 = np.array(
            self.data['I_Frac_1_1']
        ).reshape(subcatchment, 1)
        i_Frac_2_1 = np.array(
            self.data['I_Frac_2_1']
        ).reshape(subcatchment, 1)
        i_Frac_3_1 = np.array(
            self.data['I_Frac_3_1']
        ).reshape(subcatchment, 1)
        i_Frac_4_1 = np.array(
            self.data['I_Frac_4_1']
        ).reshape(subcatchment, 1)
        i_Frac_5_1 = np.array(
            self.data['I_Frac_5_1']
        ).reshape(subcatchment, 1)
        i_Frac_6_1 = np.array(
            self.data['I_Frac_6_1']
        ).reshape(subcatchment, 1)
        i_Frac_7_1 = np.array(
            self.data['I_Frac_7_1']
        ).reshape(subcatchment, 1)
        i_Frac_8_1 = np.array(
            self.data['I_Frac_8_1']
        ).reshape(subcatchment, 1)
        i_Frac_9_1 = np.array(
            self.data['I_Frac_9_1']
        ).reshape(subcatchment, 1)
        i_Frac_10_1 = np.array(
            self.data['I_Frac_10_1']
        ).reshape(subcatchment, 1)
        i_Frac_11_1 = np.array(
            self.data['I_Frac_11_1']
        ).reshape(subcatchment, 1)
        i_Frac_12_1 = np.array(
            self.data['I_Frac_12_1']
        ).reshape(subcatchment, 1)
        i_Frac_13_1 = np.array(
            self.data['I_Frac_13_1']
        ).reshape(subcatchment, 1)
        i_Frac_14_1 = np.array(
            self.data['I_Frac_14_1']
        ).reshape(subcatchment, 1)
        i_Frac_15_1 = np.array(
            self.data['I_Frac_15_1']
        ).reshape(subcatchment, 1)
        i_Frac_16_1 = np.array(
            self.data['I_Frac_16_1']
        ).reshape(subcatchment, 1)
        i_Frac_17_1 = np.array(
            self.data['I_Frac_17_1']
        ).reshape(subcatchment, 1)
        i_Frac_18_1 = np.array(
            self.data['I_Frac_18_1']
        ).reshape(subcatchment, 1)
        i_Frac_19_1 = np.array(
            self.data['I_Frac_19_1']
        ).reshape(subcatchment, 1)
        i_Frac_20_1 = np.array(
            self.data['I_Frac_20_1']
        ).reshape(subcatchment, 1)
        i_FracVegClass_1 = np.column_stacks(
            i_Frac_1_1,
            i_Frac_2_1,
            i_Frac_3_1,
            i_Frac_4_1,
            i_Frac_5_1,
            i_Frac_6_1,
            i_Frac_7_1,
            i_Frac_8_1,
            i_Frac_9_1,
            i_Frac_10_1,
            i_Frac_11_1,
            i_Frac_12_1,
            i_Frac_13_1,
            i_Frac_14_1,
            i_Frac_15_1,
            i_Frac_16_1,
            i_Frac_17_1,
            i_Frac_18_1,
            i_Frac_19_1,
            i_Frac_20_1
        )

        i_Frac_1_2 = np.array(
            self.data['I_Frac_1_2 ']
        ).reshape(subcatchment, 1)
        i_Frac_2_2 = np.array(
            self.data['I_Frac_2_2 ']
        ).reshape(subcatchment, 1)
        i_Frac_3_2 = np.array(
            self.data['I_Frac_3_2 ']
        ).reshape(subcatchment, 1)
        i_Frac_4_2 = np.array(
            self.data['I_Frac_4_2 ']
        ).reshape(subcatchment, 1)
        i_Frac_5_2 = np.array(
            self.data['I_Frac_5_2 ']
        ).reshape(subcatchment, 1)
        i_Frac_6_2 = np.array(
            self.data['I_Frac_6_2 ']
        ).reshape(subcatchment, 1)
        i_Frac_7_2 = np.array(
            self.data['I_Frac_7_2 ']
        ).reshape(subcatchment, 1)
        i_Frac_8_2 = np.array(
            self.data['I_Frac_8_2 ']
        ).reshape(subcatchment, 1)
        i_Frac_9_2 = np.array(
            self.data['I_Frac_9_2 ']
        ).reshape(subcatchment, 1)
        i_Frac_10_2 = np.array(
            self.data['I_Frac_10_2']
        ).reshape(subcatchment, 1)
        i_Frac_11_2 = np.array(
            self.data['I_Frac_11_2']
        ).reshape(subcatchment, 1)
        i_Frac_12_2 = np.array(
            self.data['I_Frac_12_2']
        ).reshape(subcatchment, 1)
        i_Frac_13_2 = np.array(
            self.data['I_Frac_13_2']
        ).reshape(subcatchment, 1)
        i_Frac_14_2 = np.array(
            self.data['I_Frac_14_2']
        ).reshape(subcatchment, 1)
        i_Frac_15_2 = np.array(
            self.data['I_Frac_15_2']
        ).reshape(subcatchment, 1)
        i_Frac_16_2 = np.array(
            self.data['I_Frac_16_2']
        ).reshape(subcatchment, 1)
        i_Frac_17_2 = np.array(
            self.data['I_Frac_17_2']
        ).reshape(subcatchment, 1)
        i_Frac_18_2 = np.array(
            self.data['I_Frac_18_2']
        ).reshape(subcatchment, 1)
        i_Frac_19_2 = np.array(
            self.data['I_Frac_19_2']
        ).reshape(subcatchment, 1)
        i_Frac_20_2 = np.array(
            self.data['I_Frac_20_2']
        ).reshape(subcatchment, 1)
        i_FracVegClass_2 = np.column_stacks(
            i_Frac_1_2,
            i_Frac_2_2,
            i_Frac_3_2,
            i_Frac_4_2,
            i_Frac_5_2,
            i_Frac_6_2,
            i_Frac_7_2,
            i_Frac_8_2,
            i_Frac_9_2,
            i_Frac_10_2,
            i_Frac_11_2,
            i_Frac_12_2,
            i_Frac_13_2,
            i_Frac_14_2,
            i_Frac_15_2,
            i_Frac_16_2,
            i_Frac_17_2,
            i_Frac_18_2,
            i_Frac_19_2,
            i_Frac_20_2
        )

        i_Frac_1_3 = np.array(
            self.data['I_Frac_1_2 ']
        ).reshape(subcatchment, 1)
        i_Frac_2_3 = np.array(
            self.data['I_Frac_2_2 ']
        ).reshape(subcatchment, 1)
        i_Frac_3_3 = np.array(
            self.data['I_Frac_3_2 ']
        ).reshape(subcatchment, 1)
        i_Frac_4_3 = np.array(
            self.data['I_Frac_4_2 ']
        ).reshape(subcatchment, 1)
        i_Frac_5_3 = np.array(
            self.data['I_Frac_5_2 ']
        ).reshape(subcatchment, 1)
        i_Frac_6_3 = np.array(
            self.data['I_Frac_6_2 ']
        ).reshape(subcatchment, 1)
        i_Frac_7_3 = np.array(
            self.data['I_Frac_7_2 ']
        ).reshape(subcatchment, 1)
        i_Frac_8_3 = np.array(
            self.data['I_Frac_8_2 ']
        ).reshape(subcatchment, 1)
        i_Frac_9_3 = np.array(
            self.data['I_Frac_9_2 ']
        ).reshape(subcatchment, 1)
        i_Frac_10_3 = np.array(
            self.data['I_Frac_10_2']
        ).reshape(subcatchment, 1)
        i_Frac_11_3 = np.array(
            self.data['I_Frac_11_2']
        ).reshape(subcatchment, 1)
        i_Frac_12_3 = np.array(
            self.data['I_Frac_12_2']
        ).reshape(subcatchment, 1)
        i_Frac_13_3 = np.array(
            self.data['I_Frac_13_2']
        ).reshape(subcatchment, 1)
        i_Frac_14_3 = np.array(
            self.data['I_Frac_14_2']
        ).reshape(subcatchment, 1)
        i_Frac_15_3 = np.array(
            self.data['I_Frac_15_2']
        ).reshape(subcatchment, 1)
        i_Frac_16_3 = np.array(
            self.data['I_Frac_16_2']
        ).reshape(subcatchment, 1)
        i_Frac_17_3 = np.array(
            self.data['I_Frac_17_2']
        ).reshape(subcatchment, 1)
        i_Frac_18_3 = np.array(
            self.data['I_Frac_18_2']
        ).reshape(subcatchment, 1)
        i_Frac_19_3 = np.array(
            self.data['I_Frac_19_2']
        ).reshape(subcatchment, 1)
        i_Frac_20_3 = np.array(
            self.data['I_Frac_20_2']
        ).reshape(subcatchment, 1)
        i_FracVegClass_3 = np.column_stacks(
            i_Frac_1_3,
            i_Frac_2_3,
            i_Frac_3_3,
            i_Frac_4_3,
            i_Frac_5_3,
            i_Frac_6_3,
            i_Frac_7_3,
            i_Frac_8_3,
            i_Frac_9_3,
            i_Frac_10_3,
            i_Frac_11_3,
            i_Frac_12_3,
            i_Frac_13_3,
            i_Frac_14_3,
            i_Frac_15_3,
            i_Frac_16_3,
            i_Frac_17_3,
            i_Frac_18_3,
            i_Frac_19_3,
            i_Frac_20_3
        )

        i_Frac_1_4 = np.array(
            self.data['I_Frac_1_2 ']
        ).reshape(subcatchment, 1)
        i_Frac_2_4 = np.array(
            self.data['I_Frac_2_2 ']
        ).reshape(subcatchment, 1)
        i_Frac_3_4 = np.array(
            self.data['I_Frac_3_2 ']
        ).reshape(subcatchment, 1)
        i_Frac_4_4 = np.array(
            self.data['I_Frac_4_2 ']
        ).reshape(subcatchment, 1)
        i_Frac_5_4 = np.array(
            self.data['I_Frac_5_2 ']
        ).reshape(subcatchment, 1)
        i_Frac_6_4 = np.array(
            self.data['I_Frac_6_2 ']
        ).reshape(subcatchment, 1)
        i_Frac_7_4 = np.array(
            self.data['I_Frac_7_2 ']
        ).reshape(subcatchment, 1)
        i_Frac_8_4 = np.array(
            self.data['I_Frac_8_2 ']
        ).reshape(subcatchment, 1)
        i_Frac_9_4 = np.array(
            self.data['I_Frac_9_2 ']
        ).reshape(subcatchment, 1)
        i_Frac_10_4 = np.array(
            self.data['I_Frac_10_2']
        ).reshape(subcatchment, 1)
        i_Frac_11_4 = np.array(
            self.data['I_Frac_11_2']
        ).reshape(subcatchment, 1)
        i_Frac_12_4 = np.array(
            self.data['I_Frac_12_2']
        ).reshape(subcatchment, 1)
        i_Frac_13_4 = np.array(
            self.data['I_Frac_13_2']
        ).reshape(subcatchment, 1)
        i_Frac_14_4 = np.array(
            self.data['I_Frac_14_2']
        ).reshape(subcatchment, 1)
        i_Frac_15_4 = np.array(
            self.data['I_Frac_15_2']
        ).reshape(subcatchment, 1)
        i_Frac_16_4 = np.array(
            self.data['I_Frac_16_2']
        ).reshape(subcatchment, 1)
        i_Frac_17_4 = np.array(
            self.data['I_Frac_17_2']
        ).reshape(subcatchment, 1)
        i_Frac_18_4 = np.array(
            self.data['I_Frac_18_2']
        ).reshape(subcatchment, 1)
        i_Frac_19_4 = np.array(
            self.data['I_Frac_19_2']
        ).reshape(subcatchment, 1)
        i_Frac_20_4 = np.array(
            self.data['I_Frac_20_2']
        ).reshape(subcatchment, 1)
        i_FracVegClass_4 = np.column_stacks(
            i_Frac_1_4,
            i_Frac_2_4,
            i_Frac_3_4,
            i_Frac_4_4,
            i_Frac_5_4,
            i_Frac_6_4,
            i_Frac_7_4,
            i_Frac_8_4,
            i_Frac_9_4,
            i_Frac_10_4,
            i_Frac_11_4,
            i_Frac_12_4,
            i_Frac_13_4,
            i_Frac_14_4,
            i_Frac_15_4,
            i_Frac_16_4,
            i_Frac_17_4,
            i_Frac_18_4,
            i_Frac_19_4,
            i_Frac_20_4
        )

        i_FracVegClasses = [
            i_FracVegClass_1,
            i_FracVegClass_2,
            i_FracVegClass_3,
            i_FracVegClass_4
        ]

        i_GWRelFrac1 = np.array(
            self.data['I_GWRelFrac1']
        ).reshape(subcatchment, 1)
        i_GWRelFrac2 = np.array(
            self.data['I_GWRelFrac2']
        ).reshape(subcatchment, 1)
        i_GWRelFrac3 = np.array(
            self.data['I_GWRelFrac3']
        ).reshape(subcatchment, 1)
        i_GWRelFrac4 = np.array(
            self.data['I_GWRelFrac4']
        ).reshape(subcatchment, 1)

        i_GWRelFracs = [
            i_GWRelFrac1,
            i_GWRelFrac2,
            i_GWRelFrac3,
            i_GWRelFrac4
        ]

        i_MaxDynGWSub1 = np.array(
            self.data['I_MaxDynGWSub1']
        ).reshape(subcatchment, 1)
        i_MaxDynGWSub2 = np.array(
            self.data['I_MaxDynGWSub2']
        ).reshape(subcatchment, 1)
        i_MaxDynGWSub3 = np.array(
            self.data['I_MaxDynGWSub3']
        ).reshape(subcatchment, 1)
        i_MaxDynGWSub4 = np.array(
            self.data['I_MaxDynGWSub4']
        ).reshape(subcatchment, 1)

        i_MaxDynGWSubs = [
            i_MaxDynGWSub1,
            i_MaxDynGWSub2,
            i_MaxDynGWSub3,
            i_MaxDynGWSub4
        ]

        i_PWPSub1 = np.array(
            self.data['I_PWPSub1']
        ).reshape(subcatchment, 1)
        i_PWPSub2 = np.array(
            self.data['I_PWPSub2']
        ).reshape(subcatchment, 1)
        i_PWPSub3 = np.array(
            self.data['I_PWPSub3']
        ).reshape(subcatchment, 1)
        i_PWPSub4 = np.array(
            self.data['I_PWPSub4']
        ).reshape(subcatchment, 1)
        i_PWPSubs = [i_PWPSub1, i_PWPSub2, i_PWPSub3, i_PWPSub4]

        i_SoilSatminFCSub1 = np.array(
            self.data['I_SoilSatminFCSub1']
        ).reshape(subcatchment, 1)
        i_SoilSatminFCSub2 = np.array(
            self.data['I_SoilSatminFCSub2']
        ).reshape(subcatchment, 1)
        i_SoilSatminFCSub3 = np.array(
            self.data['I_SoilSatminFCSub3']
        ).reshape(subcatchment, 1)
        i_SoilSatminFCSub4 = np.array(
            self.data['I_SoilSatminFCSub4']
        ).reshape(subcatchment, 1)
        i_SoilSatminFCSubs = [
            i_SoilSatminFCSub1,
            i_SoilSatminFCSub2,
            i_SoilSatminFCSub3,
            i_SoilSatminFCSub4
        ]

        i_RivFlowTime1 = np.array(
            self.data['I_RivFlowTime1']
        ).reshape(subcatchment, 1)
        i_RivFlowTime2 = np.array(
            self.data['I_RivFlowTime2']
        ).reshape(subcatchment, 1)
        i_RivFlowTime3 = np.array(
            self.data['I_RivFlowTime3']
        ).reshape(subcatchment, 1)
        i_RivFlowTime4 = np.array(
            self.data['I_RivFlowTime4']
        ).reshape(subcatchment, 1)
        i_RivFlowTimes = [
            i_RivFlowTime1,
            i_RivFlowTime2,
            i_RivFlowTime3,
            i_RivFlowTime4
        ]


        i_AvailWatSub1 = np.array(
            self.data['I_AvailWatSub1']
        ).reshape(subcatchment, 1)
        i_AvailWatSub2 = np.array(
            self.data['I_AvailWatSub2']
        ).reshape(subcatchment, 1)
        i_AvailWatSub3 = np.array(
            self.data['I_AvailWatSub3']
        ).reshape(subcatchment, 1)
        i_AvailWatSub4 = np.array(
            self.data['I_AvailWatSub4']
        ).reshape(subcatchment, 1)
        i_AvailWatSubs = [
            i_AvailWatSub1,
            i_AvailWatSub2,
            i_AvailWatSub3,
            i_AvailWatSub4
        ]

        i_TopSoilBD_BDRef1 = np.array(
            self.data['I_TopSoilBD_BDRef1']
        ).reshape(subcatchment, 1)
        i_TopSoilBD_BDRef2 = np.array(
            self.data['I_TopSoilBD_BDRef2']
        ).reshape(subcatchment, 1)
        i_TopSoilBD_BDRef3 = np.array(
            self.data['I_TopSoilBD_BDRef3']
        ).reshape(subcatchment, 1)
        i_TopSoilBD_BDRef4 = np.array(
            self.data['I_TopSoilBD_BDRef4']
        ).reshape(subcatchment, 1)
        i_TopSoilBD_BDRefs = [
            i_TopSoilBD_BDRef1,
            i_TopSoilBD_BDRef2,
            i_TopSoilBD_BDRef3,
            i_TopSoilBD_BDRef4
        ]

        i_DailyRainYear_1_to_4 = self.data['I_DailyRainYear_1_to_4']
        i_DailyRainYear_5_to_8 = self.data['I_DailyRainYear_5_to_8']
        i_DailyRainYear_9_to_12 = self.data['I_DailyRainYear_9_to_12']
        i_DailyRainYear_13_to_16 = self.data['I_DailyRainYear_13_to_16']
        i_DailyRainYear_17_to_20 = self.data['I_DailyRainYear_17_to_20']
        i_DailyRainYear_21_to_24 = self.data['I_DailyRainYear_21_to_24']
        i_DailyRainYear_25_to_28 = self.data['I_DailyRainYear_25_to_28']
        i_DailyRainYear = [
            i_DailyRainYear_1_to_4,
            i_DailyRainYear_5_to_8,
            i_DailyRainYear_9_to_12,
            i_DailyRainYear_13_to_16,
            i_DailyRainYear_17_to_20,
            i_DailyRainYear_21_to_24,
            i_DailyRainYear_25_to_28,
        ]

        i_Daily_Evap_1_to_4 = self.data['I_Daily_Evap_1_to_4']
        i_Daily_Evap_5_to_8 = self.data['I_Daily_Evap_5_to_8']
        i_Daily_Evap_9_to_12 = self.data['I_Daily_Evap_9_to_12']
        i_Daily_Evap_13_to_16 = self.data['I_Daily_Evap_13_to_16']
        i_Daily_Evap_17_to_20 = self.data['I_Daily_Evap_17_to_20']
        i_Daily_Evap_21_to_24 = self.data['I_Daily_Evap_21_to_24']
        i_Daily_Evap_25_to_28 = self.data['I_Daily_Evap_25_to_28']
        i_Daily_Evap_29_to_32 = self.data['I_Daily_Evap_29_to_32']
        i_Daily_Evap = [
            i_Daily_Evap_1_to_4,
            i_Daily_Evap_5_to_8,
            i_Daily_Evap_9_to_12,
            i_Daily_Evap_13_to_16,
            i_Daily_Evap_17_to_20,
            i_Daily_Evap_21_to_24,
            i_Daily_Evap_25_to_28,
            i_Daily_Evap_29_to_32,
        ]

        i_RFlowData_Year_1_to_4 = self.data['I_RFlowData_Year_1_to_4']
        i_RFlowData_Year_5_to_8 = self.data['I_RFlowData_Year_5_to_8']
        i_RFlowData_Year_9_to_12 = self.data['I_RFlowData_Year_9_to_12']
        i_RFlowData_Year_13_to_16 = self.data['I_RFlowData_Year_13_to_16']
        i_RFlowData_Year_17_to_20 = self.data['I_RFlowData_Year_17_to_20']
        i_RFlowData_Year_21_to_24 = self.data['I_RFlowData_Year_21_to_24']
        i_RFlowData_Year_25_to_28 = self.data['I_RFlowData_Year_25_to_28']
        i_RFlowData_Year_29_to_32 = self.data['I_RFlowData_Year_29_to_32']

        i_RFlowData = [
            i_RFlowData_Year_1_to_4,
            i_RFlowData_Year_5_to_8,
            i_RFlowData_Year_9_to_12,
            i_RFlowData_Year_13_to_16,
            i_RFlowData_Year_17_to_20,
            i_RFlowData_Year_21_to_24,
            i_RFlowData_Year_25_to_28,
            i_RFlowData_Year_29_to_32,
        ]

        i_InputDataYears = self.data['I_InputDataYears']
        i_InterceptClass = self.data['I_InterceptClass']
        i_RelDroughtFact = self.data['I_RelDroughtFact']
        i_Area = np.array(
            self.data['I_Area']
        ).reshape(subcatchment, 1)
        i_RoutingDistance = np.array(
            self.data['I_RoutingDistance']
        ).reshape(subcatchment, 1)

        # Initial value



