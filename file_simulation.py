__author__ = 'tuhv'


import numpy as np
import config
import calculate


# Getting input data

# Rainfall
I_WarmUpTime = 730
I_CaDOYStart = 0
I_RainYearStart = 0
isI_UseSpatVarRain = 0
I_RainMultiplier = 1
isI_RainCycle = 0
I_Rain_IntensMean = 10
I_Rain_IntensCoefVar = 0.3
I_Rain_GenSeed = 200

# Grass
G_GrassLitConv = 1
G_GrassMortFrac = 0.03
G_GrazingManConv = 0.1
G_SurfLitDecFrac = 0.03
G_SurfManureDecFrac = 0.01
G_TramplingMultiplier = 0
G_WUE = 0.04

# Cattle
C_DailyIntake = 1
C_DailyTrampFrac = 1
C_CattleSale = 0

# Lake
L_FloodTresh = 363
isL_HEPP_Active = 1
# L_HEPP_Daily_Dem = L_QmecsHEPP*3600*24/I_TotalArea*10^-3
# L_HEPP_Kwh = 1000*I_TotalArea*L_HEPPWatUseFlow/L_m3_per_kwh
L_HEPP_Daily_Dem = 0
L_HEPP_Kwh = 0
L_LakeBottomElev = 160
L_LakeElevPreHEPP = 362.3
L_LakeLevelFullHEPP = 362.3
L_LakeLevelHalfHEPP = 361.8
L_LakeLevelNoHEPP = 359.5
L_LakeOverFlowFrac = 0.1
L_LakeOverFlPostHEPP = 362.6
L_LakeOverFlPow = 4
L_m3_per_kwh = 1.584
L_QmecsHEPP = 47.1
L_QmecsSanFlow = 3
# L_SanitaryFlow = L_QmecsSanFlow* 3600*24/I_TotalArea*10^-3
# L_OutflTrVolPreHEPP = 1000*(L_LakeElevPreHEPP-L_LakeBottomElev)*np.sum(L_LakeArea)
# L_OutflTrVoPostHEPP = 1000*(L_LakeOverFlPostHEPP-L_LakeBottomElev)*np.sum(L_LakeArea)
L_SanitaryFlow = 0
L_OutflTrVolPreHEPP = 0
L_OutflTrVoPostHEPP = 0
S_TrampMax = 100

I_SoilQflowFrac = 0.1
I_RainIntercDripRt = 10
I_RainMaxIntDripDur = 0.5

isD_GWUseFacility = np.ones(shape=(len(config.SUBCATCHMENT), len(config.VEGCLASS)))
D_GW_Utilization_fraction = 0.02
D_IrrigEfficiency = np.zeros(len(config.SUBCATCHMENT))
I_PercFracMultiplier = 0.05
isL_Lake = np.zeros(len(config.SUBCATCHMENT))

# Subcatchment param

I_InitRelGW = 1

# Patch Balance
I_InterceptEffectonTransp = 0.1

L_LakeTranspMultiplier = 1

# Getting data from excel file

I_Frac_1_1 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_2_1 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_3_1 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_4_1 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_5_1 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_6_1 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_7_1 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_8_1 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_9_1 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_10_1 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_11_1 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_12_1 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_13_1 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_14_1 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_15_1 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_16_1 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_17_1 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_18_1 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_19_1 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_20_1 = np.zeros(len(config.SUBCATCHMENT))
I_FracVegClass_1 = np.array([I_Frac_1_1, I_Frac_2_1, I_Frac_3_1, I_Frac_4_1, I_Frac_5_1,
                                   I_Frac_6_1, I_Frac_7_1, I_Frac_8_1, I_Frac_9_1, I_Frac_10_1,
                                   I_Frac_11_1, I_Frac_12_1, I_Frac_13_1, I_Frac_14_1, I_Frac_15_1,
                                   I_Frac_16_1, I_Frac_17_1, I_Frac_18_1, I_Frac_19_1, I_Frac_20_1])

I_Frac_1_2 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_2_2 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_3_2 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_4_2 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_5_2 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_6_2 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_7_2 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_8_2 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_9_2 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_10_2 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_11_2 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_12_2 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_13_2 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_14_2 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_15_2 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_16_2 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_17_2 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_18_2 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_19_2 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_20_2 = np.zeros(len(config.SUBCATCHMENT))
I_FracVegClass_2 = np.array([I_Frac_1_2, I_Frac_2_2, I_Frac_3_2, I_Frac_4_2, I_Frac_5_2,
                                   I_Frac_6_2, I_Frac_7_2, I_Frac_8_2, I_Frac_9_2, I_Frac_10_2,
                                   I_Frac_11_2, I_Frac_12_2, I_Frac_13_2, I_Frac_14_2, I_Frac_15_2,
                                   I_Frac_16_2, I_Frac_17_2, I_Frac_18_2, I_Frac_19_2, I_Frac_20_2])
I_Frac_1_3 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_2_3 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_3_3 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_4_3 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_5_3 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_6_3 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_7_3 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_8_3 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_9_3 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_10_3 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_11_3 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_12_3 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_13_3 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_14_3 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_15_3 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_16_3 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_17_3 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_18_3 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_19_3 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_20_3 = np.zeros(len(config.SUBCATCHMENT))
I_FracVegClass_3 = np.array([I_Frac_1_3, I_Frac_2_3, I_Frac_3_3, I_Frac_4_3, I_Frac_5_3,
                                   I_Frac_6_3, I_Frac_7_3, I_Frac_8_3, I_Frac_9_3, I_Frac_10_3,
                                   I_Frac_11_3, I_Frac_12_3, I_Frac_13_3, I_Frac_14_3, I_Frac_15_3,
                                   I_Frac_16_3, I_Frac_17_3, I_Frac_18_3, I_Frac_19_3, I_Frac_20_3])
I_Frac_1_4 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_2_4 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_3_4 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_4_4 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_5_4 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_6_4 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_7_4 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_8_4 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_9_4 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_10_4 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_11_4 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_12_4 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_13_4 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_14_4 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_15_4 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_16_4 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_17_4 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_18_4 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_19_4 = np.zeros(len(config.SUBCATCHMENT))
I_Frac_20_4 = np.zeros(len(config.SUBCATCHMENT))
I_FracVegClass_4 = np.array([I_Frac_1_4, I_Frac_2_4, I_Frac_3_4, I_Frac_4_4, I_Frac_5_4,
                                   I_Frac_6_4, I_Frac_7_4, I_Frac_8_4, I_Frac_9_4, I_Frac_10_4,
                                   I_Frac_11_4, I_Frac_12_4, I_Frac_13_4, I_Frac_14_4, I_Frac_15_4,
                                   I_Frac_16_4, I_Frac_17_4, I_Frac_18_4, I_Frac_19_4, I_Frac_20_4])
I_FracVegClasses = np.array([I_FracVegClass_1, I_FracVegClass_2, I_FracVegClass_3, I_FracVegClass_4])

I_InputDataYears = [00, 24, 30]

I_GWRelFrac1 = np.zeros(len(config.SUBCATCHMENT))
I_GWRelFrac2 = np.zeros(len(config.SUBCATCHMENT))
I_GWRelFrac3 = np.zeros(len(config.SUBCATCHMENT))
I_GWRelFrac4 = np.zeros(len(config.SUBCATCHMENT))
I_GWRelFracs = np.array([I_GWRelFrac1, I_GWRelFrac2, I_GWRelFrac3, I_GWRelFrac4])

I_MaxDynGWSub1 = np.zeros(len(config.SUBCATCHMENT))
I_MaxDynGWSub2 = np.zeros(len(config.SUBCATCHMENT))
I_MaxDynGWSub3 = np.zeros(len(config.SUBCATCHMENT))
I_MaxDynGWSub4 = np.zeros(len(config.SUBCATCHMENT))
I_MaxDynGWSubs = np.array([I_MaxDynGWSub1, I_MaxDynGWSub2, I_MaxDynGWSub3, I_MaxDynGWSub4])

I_PWPSub1 = np.zeros(len(config.SUBCATCHMENT))
I_PWPSub2 = np.zeros(len(config.SUBCATCHMENT))
I_PWPSub3 = np.zeros(len(config.SUBCATCHMENT))
I_PWPSub4 = np.zeros(len(config.SUBCATCHMENT))
I_PWPSubs = np.array([I_PWPSub1, I_PWPSub2, I_PWPSub3, I_PWPSub4])

I_SoilSatminFCSub1 = np.zeros(len(config.SUBCATCHMENT))
I_SoilSatminFCSub2 = np.zeros(len(config.SUBCATCHMENT))
I_SoilSatminFCSub3 = np.zeros(len(config.SUBCATCHMENT))
I_SoilSatminFCSub4 = np.zeros(len(config.SUBCATCHMENT))
I_SoilSatminFCSubs = np.array([I_SoilSatminFCSub1, I_SoilSatminFCSub2, I_SoilSatminFCSub3, I_SoilSatminFCSub4])

I_RivFlowTime1 = np.zeros(len(config.SUBCATCHMENT))
I_RivFlowTime2 = np.zeros(len(config.SUBCATCHMENT))
I_RivFlowTime3 = np.zeros(len(config.SUBCATCHMENT))
I_RivFlowTime4 = np.zeros(len(config.SUBCATCHMENT))
I_RivFlowTimes = np.array([I_RivFlowTime1, I_RivFlowTime2, I_RivFlowTime3, I_RivFlowTime4])

I_AvailWatSub1 = np.zeros(len(config.SUBCATCHMENT))
I_AvailWatSub2 = np.zeros(len(config.SUBCATCHMENT))
I_AvailWatSub3 = np.zeros(len(config.SUBCATCHMENT))
I_AvailWatSub4 = np.zeros(len(config.SUBCATCHMENT))
I_AvailWatSubs = np.array([I_AvailWatSub1, I_AvailWatSub2, I_AvailWatSub3, I_AvailWatSub4])

I_TopSoilBD_BDRef1 = np.zeros(len(config.SUBCATCHMENT))
I_TopSoilBD_BDRef2 = np.zeros(len(config.SUBCATCHMENT))
I_TopSoilBD_BDRef3 = np.zeros(len(config.SUBCATCHMENT))
I_TopSoilBD_BDRef4 = np.zeros(len(config.SUBCATCHMENT))
I_TopSoilBD_BDRefs = np.array([I_TopSoilBD_BDRef1, I_TopSoilBD_BDRef2, I_TopSoilBD_BDRef3, I_TopSoilBD_BDRef4])

I_DailyRainYear_1_to_4 = [0 for i in range(config.FOURYEARS)]
I_DailyRainYear_5_to_8 = [0 for i in range(config.FOURYEARS)]
I_DailyRainYear_9_to_12 = [0 for i in range(config.FOURYEARS)]
I_DailyRainYear_13_to_16 = [0 for i in range(config.FOURYEARS)]
I_DailyRainYear_17_to_20 = [0 for i in range(config.FOURYEARS)]
I_DailyRainYear_21_to_24 = [0 for i in range(config.FOURYEARS)]
I_DailyRainYear_25_to_28 = [0 for i in range(config.FOURYEARS)]


I_Daily_Evap_1_to_4 = [0 for i in range(config.FOURYEARS)]
I_Daily_Evap_5_to_8 = [0 for i in range(config.FOURYEARS)]
I_Daily_Evap_9_to_12 = [0 for i in range(config.FOURYEARS)]
I_Daily_Evap_13_to_16 = [0 for i in range(config.FOURYEARS)]
I_Daily_Evap_17_to_20 = [0 for i in range(config.FOURYEARS)]
I_Daily_Evap_21_to_24 = [0 for i in range(config.FOURYEARS)]
I_Daily_Evap_25_to_28 = [0 for i in range(config.FOURYEARS)]
I_Daily_Evap_29_to_32 = [0 for i in range(config.FOURYEARS)]

I_MultiplierEvapoTrans = [np.zeros(len(config.SUBCATCHMENT)) for i in range(config.MONTH)]
I_EvapoTrans = [0 for i in range(config.MONTH)]

I_RelDroughtFact = np.zeros(len(config.VEGCLASS))

# Stocks initialisation

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
O_CumSoilQFlow_Subca_1 = [np.zeros(shape=(len(config.SUBCATCHMENT), len(config.OBSPOINT)))]
O_CumSurfQFlow = [0]
O_CumTransp = [0]
# O_InitGWStock = arraysum(I_MaxDynGWArea[*])*I_InitRelGW
O_InitGWStock = [0]
# O_InitSoilW = arraysum(I_AvailWaterClass[*,*])*I_InitRelSoil
O_InitSoilW = [0]
O_RainYest = [np.zeros(shape=(len(config.SUBCATCHMENT), 1))]
G_GrassStandingBiomass = [np.ones(shape=(len(config.SUBCATCHMENT), len(config.VEGCLASS)))]
G_SurfaceLitter = [np.zeros(shape=(len(config.SUBCATCHMENT), len(config.VEGCLASS)))]
G_SurfManure = [np.ones(shape=(len(config.SUBCATCHMENT), len(config.VEGCLASS)))]
isI_WarmEdUp = [0]
O_CumDebitData = [0]
L_CumEvapLake = [0]
L_CumHEPPUse = [0]
L_CumRivOutFlow = [0]
# L_LakeVol = L_OutflTrVoPostHEPP*L_HEPP_Active?+(1-L_HEPP_Active?)*L_OutflTrVolPreHEPP
L_LakeVol = [0]
O_BestYyHEPP = [0]
O_Ch_inGWStock = [np.zeros(shape=(len(config.MEASUREPERIOD), 1))]
O_Ch_inWStock = [np.zeros(shape=(len(config.MEASUREPERIOD), 1))]
O_CumBaseFlowMP = [np.zeros(shape=(len(config.MEASUREPERIOD), 1))]
O_CumDebitDataMP = [np.zeros(shape=(len(config.MEASUREPERIOD), 1))]
O_CumDebitPredMP = [np.zeros(shape=(len(config.MEASUREPERIOD), 1))]
O_CumEvapLakeMP = [np.zeros(shape=(len(config.MEASUREPERIOD), 1))]
O_CumEvapTransMP = [np.zeros(shape=(len(config.MEASUREPERIOD), 1))]
O_CumGWMP = [np.zeros(shape=(len(config.MEASUREPERIOD), 1))]
O_CumHEPPOutFlowMP = [np.zeros(shape=(len(config.MEASUREPERIOD), 1))]
O_CumInfiltrationMP = [np.zeros(shape=(len(config.MEASUREPERIOD), 1))]
O_CumIntercEvapMP = [np.zeros(shape=(len(config.MEASUREPERIOD), 1))]
O_CumRainMP = [np.zeros(shape=(len(config.MEASUREPERIOD), 1))]
O_CumRivInflowtoLakeMP = [np.zeros(shape=(len(config.MEASUREPERIOD), 1))]
O_CumRivOutFlowMP = [np.zeros(shape=(len(config.MEASUREPERIOD), 1))]
O_CumSoilQFlowMP = [np.zeros(shape=(len(config.MEASUREPERIOD), 1))]
O_CumSoilWMP = [np.zeros(shape=(len(config.MEASUREPERIOD), 1))]
O_CumSurfQFlowMP = [np.zeros(shape=(len(config.MEASUREPERIOD), 1))]
O_CumTranspMP = [np.zeros(shape=(len(config.MEASUREPERIOD), 1))]
O_DeltaCatchmStMP = [np.zeros(shape=(len(config.MEASUREPERIOD), 1))]
O_Hepp_Kwh_per_dayMP = [np.zeros(shape=(len(config.MEASUREPERIOD), 1))]
O_InitEvapoMP = [np.zeros(shape=(len(config.MEASUREPERIOD), 1))]
O_InitGWStockMP = [np.zeros(shape=(len(config.MEASUREPERIOD), 1))]
O_InitSWMP = [np.zeros(shape=(len(config.MEASUREPERIOD), 1))]
O_LastYHepp = [0]
O_ThisYHepp = [0]
O_WorstYHEPP = [1]
O_YearSim = [1]
D_CumEvapTranspClass = [np.zeros(shape=(len(config.VEGCLASS), len(config.SUBCATCHMENT)))]
D_CumNegRain = [np.zeros(shape=(len(config.SUBCATCHMENT), 1))]
D_EvapTranspClass = [np.zeros(shape=(len(config.SUBCATCHMENT), len(config.VEGCLASS)))]
# D_GWArea[Subcatchement] = I_MaxDynGWArea[Subcatchement]*I_InitRelGW
D_GWArea = [np.zeros(shape=(len(config.SUBCATCHMENT), 1))]
# D_SoilWater[VegClass,Subcatchement] = I_AvailWaterClass[VegClass,Subcatchement]*I_InitRelSoil
D_SoilWater = [np.zeros(shape=(len(config.VEGCLASS), len(config.SUBCATCHMENT)))]
# S_RelBulkDensity[Subcatchement,VegClass] = I_BD_BDRefVegNow[Subcatchement]
S_RelBulkDensity = [np.zeros(shape=(len(config.SUBCATCHMENT), len(config.VEGCLASS)))]
D_CumInflowtoLake = [0]
D_CumTotRiverFlow = [np.zeros(shape=(len(config.SUBCATCHMENT), len(config.OBSPOINT)))]
D_StreamsSurfQ = [np.zeros(shape=(len(config.SUBCATCHMENT), len(config.OBSPOINT)))]
D_TotRiverFlowNoDelay = [np.zeros(shape=(len(config.SUBCATCHMENT), len(config.OBSPOINT)))]
D_CumResvEvap = [0]
# D_SubcResVol[Subcatchement] = D_ReservoirVol[Subcatchement]*I_DaminThisStream?[Subcatchement]
D_SubcResVol = [np.zeros(shape=(len(config.SUBCATCHMENT), 1))]


# Simulation

time = 0

I_Simulation_Time = time + I_CaDOYStart + 365 * I_RainYearStart - isI_WarmEdUp[time] * (I_WarmUpTime + 1)

I_Flag1 = 1 if I_Simulation_Time < I_InputDataYears[1] else 0 # 0: Start: Trans1, 2: Trans2, 3: End
I_Flag2 = 1 if I_Simulation_Time < I_InputDataYears[2] and I_Flag1 == 0 else 0

I_RainDoY = I_Simulation_Time if (isI_RainCycle == 0) else 1 + I_Simulation_Time % 365
I_SpatRain1 = [np.zeros(len(config.SUBCATCHMENT)) for i in range(config.FOURYEARS)]
I_SpatRain2 = [np.zeros(len(config.SUBCATCHMENT)) for i in range(config.FOURYEARS)]
I_SpatRain3 = [np.zeros(len(config.SUBCATCHMENT)) for i in range(config.FOURYEARS)]
I_SpatRain4 = [np.zeros(len(config.SUBCATCHMENT)) for i in range(config.FOURYEARS)]
I_SpatRain5 = [np.zeros(len(config.SUBCATCHMENT)) for i in range(config.FOURYEARS)]
I_SpatRain6 = [np.zeros(len(config.SUBCATCHMENT)) for i in range(config.FOURYEARS)]
I_SpatRain7 = [np.zeros(len(config.SUBCATCHMENT)) for i in range(config.FOURYEARS)]

if I_RainDoY <= 1460:
    I_SpatRainTime = I_SpatRain1[I_Simulation_Time] * I_RainMultiplier
elif I_RainDoY <= 2920:
    I_SpatRainTime = I_SpatRain2[I_Simulation_Time] * I_RainMultiplier
elif I_RainDoY <= 4380:
    I_SpatRainTime = I_SpatRain3[I_Simulation_Time] * I_RainMultiplier
elif I_RainDoY <= 5840:
    I_SpatRainTime = I_SpatRain4[I_Simulation_Time] * I_RainMultiplier
elif I_RainDoY <= 7300:
    I_SpatRainTime = I_SpatRain5[I_Simulation_Time] * I_RainMultiplier
elif I_RainDoY <= 8760:
    I_SpatRainTime = I_SpatRain6[I_Simulation_Time] * I_RainMultiplier
else:
    I_SpatRainTime = I_SpatRain7[I_Simulation_Time] * I_RainMultiplier

if I_RainDoY <= 1460:
    I_DailyRain = I_DailyRainYear_1_to_4[I_Simulation_Time] * I_RainMultiplier
elif I_RainDoY <= 2920:
    I_DailyRain = I_DailyRainYear_5_to_8[I_Simulation_Time] * I_RainMultiplier
elif I_RainDoY <= 4380:
    I_DailyRain = I_DailyRainYear_9_to_12[I_Simulation_Time] * I_RainMultiplier
elif I_RainDoY <= 5840:
    I_DailyRain = I_DailyRainYear_13_to_16[I_Simulation_Time] * I_RainMultiplier
elif I_RainDoY <= 7300:
    I_DailyRain = I_DailyRainYear_17_to_20[I_Simulation_Time] * I_RainMultiplier
elif I_RainDoY <= 8760:
    I_DailyRain = I_DailyRainYear_21_to_24[I_Simulation_Time] * I_RainMultiplier
else:
    I_DailyRain = I_DailyRainYear_25_to_28[I_Simulation_Time] * I_RainMultiplier

I_RainPerDay = I_SpatRainTime if isI_UseSpatVarRain else I_DailyRain

I_RainDuration = ((I_RainPerDay / I_Rain_IntensMean) *
                  min(max(0,
                          1 - 3 * I_Rain_IntensCoefVar,
                          np.random.normal(1, I_Rain_IntensCoefVar, I_Rain_GenSeed + 11250)[0]),
                      1 + 3 * I_Rain_IntensCoefVar))
# Getting input data
isD_FeedingIntoLake = np.zeros(len(config.SUBCATCHMENT))
I_RoutingDistance = np.zeros(len(config.SUBCATCHMENT))
I_Area = np.zeros(len(config.SUBCATCHMENT))
I_TotalArea = np.sum(I_Area)
I_RelArea = I_Area/I_TotalArea if I_TotalArea else 0

I_InterceptClass = np.zeros(config.LANDCOVERTYPE)
I_RelDroughtFract = np.zeros(config.LANDCOVERTYPE)

D_FeedingIntoLake_ = np.zeros(len(config.SUBCATCHMENT))
I_Area = np.zeros(len(config.SUBCATCHMENT))
I_TotalArea = np.sum(I_Area)

def get_variable_now(array_values):
    global I_RelArea
    global I_Simulation_Time
    global I_InputDataYears
    global I_Flag1
    global I_Flag2
    if len(array_values.shape) == 1:
        if I_Flag1:
            result = (array_values[0] +
                      (array_values[1] - array_values[0]) *
                      (int(I_Simulation_Time/365) - I_InputDataYears[0]) /
                      (I_InputDataYears[1] - I_InputDataYears[0]))
        elif I_Flag2:
            result = (array_values[1] +
                      (array_values[2] - array_values[1]) *
                      (int(I_Simulation_Time/365) - I_InputDataYears[1]) /
                      (I_InputDataYears[2] - I_InputDataYears[1]))
        else:
            result = (array_values[2] +
                      (array_values[3] - array_values[2]) *
                      (int(I_Simulation_Time/365) - I_InputDataYears[2]) /
                      (I_InputDataYears[3] - I_InputDataYears[2]))
    else:
        if I_Flag1:
            result = np.divide((array_values[0] +
                      (array_values[1] - array_values[0]) *
                      (int(I_Simulation_Time/365) - I_InputDataYears[0]) /
                      (I_InputDataYears[1] - I_InputDataYears[0])), np.sum(array_values[0], axis=0),
                               out=np.zeros_like(array_values[0]),
                               where=I_RelArea != 0)
        elif I_Flag2:
            result = np.divide((array_values[1] +
                      (array_values[2] - array_values[1]) *
                      (int(I_Simulation_Time/365) - I_InputDataYears[1]) /
                      (I_InputDataYears[2] - I_InputDataYears[1])), np.sum(array_values[1], axis=0),
                               out=np.zeros_like(array_values[0]),
                               where=I_RelArea != 0)
        else:
            result = np.divide((array_values[2] +
                      (array_values[3] - array_values[2]) *
                      (int(I_Simulation_Time/365) - I_InputDataYears[2]) /
                      (I_InputDataYears[3] - I_InputDataYears[2])), np.sum(array_values[2], axis=0),
                               out=np.zeros_like(array_values[0]),
                               where=I_RelArea != 0)
        result = np.multiply(I_RelArea>0, result)
    return result

I_GWRelFracNow = get_variable_now(I_GWRelFracs)
I_MaxDynGwSubNow = get_variable_now(I_MaxDynGWSubs)
I_FracVegClassNow = get_variable_now(I_FracVegClasses)
I_PWPSubNow = get_variable_now(I_PWPSubs)
I_SoilSatminFCSubNow = get_variable_now(I_SoilSatminFCSubs)
I_RivFlowTimeNow = get_variable_now(I_RivFlowTimes)
I_TopSoilBD_BDRefNow = get_variable_now(I_TopSoilBD_BDRefs)
I_AvailWatClassNow = get_variable_now(I_AvailWatSubs)
I_AvailWatClassNow = np.array([I_AvailWatClassNow for i in range(len(config.VEGCLASS))])

I_FracVegClassSum1 = np.sum(I_FracVegClass_1)
I_FracVegClassSum2 = np.sum(I_FracVegClass_2)
I_FracVegClassSum3 = np.sum(I_FracVegClass_3)
I_FracVegClassSum4 = np.sum(I_FracVegClass_4)
I_FracVegClassSumNow = np.sum(I_FracVegClassNow)

I_DailyRainAmount = np.multiply(I_RainPerDay, np.multiply(I_FracVegClassNow, I_RelArea))

I_StillWarmUp_ = 1 if time <= I_WarmUpTime else 0
I_WUcorrection = 1 if time == int(I_WarmUpTime + 1 ) else 0
I_WarmedUp = 1 if time == int(I_WarmUpTime) else 0
calculate.update(stock=isI_WarmEdUp, inflow=I_WarmedUp, dt=config.dt)

if I_RainDoY <= 1460:
    I_Daily_Evapotrans = I_Daily_Evap_1_to_4
elif I_RainDoY <= 2920:
    I_Daily_Evapotrans = I_Daily_Evap_5_to_8
elif I_RainDoY <= 4380:
    I_Daily_Evapotrans = I_Daily_Evap_9_to_12
elif I_RainDoY <= 5840:
    I_Daily_Evapotrans = I_Daily_Evap_13_to_16
elif I_RainDoY <= 7300:
    I_Daily_Evapotrans = I_Daily_Evap_17_to_20
elif I_RainDoY <= 8760:
    I_Daily_Evapotrans = I_Daily_Evap_21_to_24
else:
    I_Daily_Evapotrans = I_Daily_Evap_25_to_28

I_FracArea = np.multiply(I_FracVegClassNow,  I_RelArea)

I_TimeEvap = 0 if I_RainDoY == 0 else 365 if I_RainDoY % 365 == 0 else I_RainDoY % 365
I_MoY = 0 if I_RainDoY == 0 else int(I_TimeEvap/30.5) + 1
if config.I_EvapotransMethod == 1:
    I_PotEvapTransp = np.multiply(I_EvapoTrans[I_MoY],
                                 np.multiply(I_MultiplierEvapoTrans[I_MoY],
                                             I_FracArea))
else:
    I_PotEvapTransp = np.multiply(I_Daily_Evapotrans,
                                  np.multiply(I_MultiplierEvapoTrans,
                                              I_FracArea))
I_MaxInfSubSAreaClass = config.I_MaxInfSSoil * I_FracArea
I_MaxInfArea = config.I_MaxInf * np.multiply(I_FracArea,
                                             np.power(np.divide(0.7, I_TopSoilBD_BDRefNow,
                                                                out=np.zeros_like(I_TopSoilBD_BDRefNow),
                                                                where=I_TopSoilBD_BDRefNow != 0),
                                                      config.I_PowerInfiltRed))
I_CanIntercAreaClass = np.multiply(I_InterceptClass, I_FracArea)
I_AvailWaterClass = (config.I_AvailWaterConst * I_FracArea
                     if config.I_SoilPropConst_
                     else np.multiply(I_AvailWatClassNow, I_FracArea))
I_SoilSatClass = ((config.I_AvailWaterConst + config.I_SoilSatMinFCConst) * I_FracArea if config.I_SoilPropConst_
                  else np.add(I_SoilSatminFCSubNow, np.multiply(I_AvailWatClassNow, I_FracArea)))
I_GWRelFrac = config.I_GWRelFracConst if config.I_SoilPropConst_ else I_GWRelFracNow
I_MaxDynGWact = config.I_MaxDynGWConst if config.I_GWRelFracConst_ else I_MaxDynGwSubNow
I_MaxDynGWArea = np.multiply(I_MaxDynGWact, I_RelArea)
I_InitTotGW = np.add(I_MaxDynGWArea, I_InitRelGW)

D_InterceptEvap = np.multiply(I_CanIntercAreaClass,
                              (1 - np.exp(-np.divide(I_DailyRainAmount,
                                                   I_CanIntercAreaClass,
                                                   out=np.zeros_like(I_CanIntercAreaClass),
                                                   where=I_CanIntercAreaClass!=0))))

I_FracVegClassNow_Multiply_I_RelArea = np.multiply(I_FracVegClassNow, I_RelArea)
D_RainInterc = np.divide(D_InterceptEvap, I_FracVegClassNow_Multiply_I_RelArea,
                         out=np.ones_like(D_InterceptEvap),
                         where=I_FracVegClassNow_Multiply_I_RelArea!=0)
D_RainIntercDelay = np.minimum(I_RainMaxIntDripDur, np.sum(D_RainInterc, axis=1))/I_RainIntercDripRt
I_RainTimeAvForInf = np.minimum(24, I_RainDuration + D_RainIntercDelay)
D_Infiltration = np.multiply((1 - isL_Lake), np.minimum(np.minimum(I_SoilSatClass - D_SoilWater,
                                                                  np.multiply(I_MaxInfArea, I_RainTimeAvForInf)/24),
                                                       I_DailyRainAmount - D_InterceptEvap))
I_RelDroughtFact_AvailWaterClass = np.multiply(I_RelDroughtFact, I_AvailWaterClass)
D_RelWaterAv = np.minimum(1, np.divide(D_SoilWater[time], I_RelDroughtFact_AvailWaterClass,
                               out=np.ones_like(D_SoilWater[time]),
                               where=I_RelDroughtFact_AvailWaterClass!=0))
x = np.multiply(D_GWArea[time],
                                                np.multiply(isD_GWUseFacility,
                                                            np.multiply(D_GW_Utilization_fraction,
                                                                        np.subtract(1, D_RelWaterAv))))
D_Irrigation = np.minimum(np.divide(np.multiply(D_GWArea[time],
                                                np.multiply(isD_GWUseFacility,
                                                            np.multiply(D_GW_Utilization_fraction,
                                                                        np.subtract(1, D_RelWaterAv)))),
                                    D_IrrigEfficiency,
                                    out=np.zeros(shape=(len(config.SUBCATCHMENT), len(config.VEGCLASS))),
                                    where=D_IrrigEfficiency!=0),
                          I_PotEvapTransp)
D_Percolation = np.multiply(I_AvailWaterClass > 0,  np.minimum(I_MaxInfSubSAreaClass, np.minimum(np.multiply(D_SoilWater, np.multiply(I_PercFracMultiplier, I_GWRelFrac)),I_MaxDynGWArea-D_GWArea[time]))
- np.multiply(D_IrrigEfficiency, D_Irrigation)) - np.multiply((I_AvailWaterClass <= 0), np.multiply(D_IrrigEfficiency, D_Irrigation))

D_WaterEvapIrrigation = np.multiply(D_IrrigEfficiency > 0, D_Irrigation *(1-D_IrrigEfficiency))
D_GWaDisch = np.multiply(D_GWArea[time], I_GWRelFrac)

D_DeepInfiltration = np.multiply(isL_Lake == 1, np.minimum(np.minimum(np.minimum(np.multiply(np.sum(I_MaxInfArea, axis=1),
                                                                                           I_RainTimeAvForInf)/24 -
                                                                               np.sum(I_SoilSatClass, axis=1) +
                                                                               np.sum(D_SoilWater, axis=1),
                                                                               np.sum(I_MaxInfSubSAreaClass, axis=1)),
                                                                    np.sum(I_DailyRainAmount, axis=1) -
                                                                    np.sum(D_InterceptEvap, axis=1) -
                                                                    np.sum(D_Infiltration, axis=1)),
                                                         I_MaxDynGWArea-D_GWArea[time]))
D_ActEvapTransp = np.multiply(isL_Lake != 1,
                              np.multiply(I_PotEvapTransp -
                                          np.multiply(I_InterceptEffectonTransp,
                                                     D_InterceptEvap), D_RelWaterAv))
D_SurfaceFlow = (np.multiply(isL_Lake == 1, np.sum(I_DailyRainAmount, axis=1)) +
                 np.multiply(isL_Lake != 1,
                            np.sum(I_DailyRainAmount, axis=1) -
                            np.sum(D_InterceptEvap, axis=0) -
                            np.sum(D_Infiltration, axis=0) -
                            D_DeepInfiltration))
D_SoilQflowRelFrac = np.array([I_SoilQflowFrac for i in range(len(config.SUBCATCHMENT))])
D_SoilDischarge = np.multiply(D_SoilQflowRelFrac, (D_SoilWater - I_AvailWaterClass))
calculate.update(D_CumNegRain, inflow=0, outflow=D_InterceptEvap + D_Infiltration + D_DeepInfiltration + D_SurfaceFlow, dt=config.dt, non_negative=False)
calculate.update(D_CumEvapTranspClass, inflow=D_ActEvapTransp, outflow=D_InterceptEvap, dt=config.dt)
calculate.update(D_SoilWater, inflow=D_Infiltration, outflow=D_ActEvapTransp + D_Percolation + D_SoilDischarge, dt=config.dt)
calculate.update(D_GWArea, inflow=D_Percolation + D_DeepInfiltration, outflow=D_GWaDisch+D_WaterEvapIrrigation, dt=config.dt)
calculate.update(D_EvapTranspClass, inflow=D_WaterEvapIrrigation, dt=config.dt)

G_GrassAll = np.sum(G_GrassStandingBiomass[time])
G_Grazing = 0 if G_GrassAll == 0 else C_StockingRate * C_DailyIntake * G_GrassStandingBiomass[time] / G_GrassAll
C_TrampComp = C_DailyTrampFrac * G_Grazing / C_DailyIntake
C_DeathRate = C_StockingRate[time] * C_DailyIntake - G_GrassAll
C_Destoking = min(C_StockingRate[time], C_CattleSale + C_DeathRate)
C_Stocking = 0 * C_StockingRate[time]
calculate.update(C_StockingRate, inflow=C_Stocking, outflow=C_Destoking, dt=config.dt)

G_GrassFract_Biomass = np.zeros(len(config.VEGCLASS))
G_GrowthRate = G_WUE * np.multiply(D_ActEvapTransp, G_GrassFract_Biomass)
G_GrassAll = np.sum(G_GrassStandingBiomass[time])
G_LeafMortality = G_GrassStandingBiomass[time] * G_GrassMortFrac + G_Grazing * G_TramplingMultiplier
G_LitterDeposition = G_LeafMortality * G_GrassLitConv
calculate.update(G_GrassStandingBiomass, inflow=G_GrowthRate, outflow=G_Grazing + G_LeafMortality, dt=config.dt)

G_Incorporation_DecaySurfLit = G_SurfaceLitter[time] * G_SurfLitDecFrac
calculate.update(G_SurfaceLitter, inflow=G_LitterDeposition, outflow=G_Incorporation_DecaySurfLit, dt=config.dt)

G_FaecesProd = G_Grazing * G_GrazingManConv
G_Incorporation_DecayManure = G_SurfManure[time] * G_SurfManureDecFrac
calculate.update(G_SurfManure, inflow=G_FaecesProd, outflow=G_Incorporation_DecayManure, dt=config.dt)

G_SurfaceCover = G_GrassStandingBiomass[time] + G_SurfaceLitter[time] + G_SurfManure[time]
S_RainAtSoilSurface = I_DailyRainAmount - D_InterceptEvap.T
S_Compaction = np.multiply((1.3 - S_RelBulkDensity[time]), C_TrampComp)/S_TrampMax
S_SplashErosion = 0 * np.divide(np.multiply(G_SurfaceCover, S_RainAtSoilSurface),
                                I_RainDuration,
                                out=np.zeros_like(G_SurfaceCover),
                                where=I_RainDuration!=0)
S_StructureFormation = 0 * np.multiply(S_RelBulkDensity, G_SurfaceCover)
S_RippingSurface = 0

calculate.update(S_RelBulkDensity,
                 inflow=S_SplashErosion + S_StructureFormation + S_RippingSurface,
                 outflow=S_Compaction,
                 dt=config.dt)
isO_Reset = 1 if I_WarmedUp == 1 or I_WUcorrection == 1 else 0
L_LakeTransDef = np.add(np.multiply(isL_Lake, (-D_ActEvapTransp[config.LANDCOVER["AF_Kelapa"]])),
                        I_PotEvapTransp[config.LANDCOVER["AF_Kelapa"]])
L_LakeArea = np.multiply(isL_Lake, I_RelArea, out= np.zeros_like(isL_Lake), where=isL_Lake!=1)
L_LakeLevel = np.multiply(np.sum(L_LakeArea)>0, L_LakeVol/(1000*np.sum(L_LakeArea)) + L_LakeBottomElev)
L_Lakelevelexcess = L_LakeLevel-(1-isL_HEPP_Active)*L_LakeElevPreHEPP-isL_HEPP_Active*L_LakeOverFlPostHEPP
L_LakeArea = np.multiply(isL_Lake==1, np.multiply(isL_Lake*I_RelArea))
L_HEPP_Outflow = L_HEPP_Daily_Dem if L_LakeLevel>L_LakeLevelFullHEPP else L_HEPP_Daily_Dem*0.5*(1 + max(0,(L_LakeLevel-L_LakeLevelHalfHEPP)/(L_LakeLevelFullHEPP-L_LakeLevelHalfHEPP))) if L_LakeLevel>L_LakeLevelNoHEPP else 0
L_HEPP_OpTimeRel = ( L_CumHEPPUse/L_HEPP_Daily_Dem)/I_Simulation_Time if I_Simulation_Time>0 and isI_WarmEdUp[time] == 1 else 0
L_EvapLake = min(np.sum(L_LakeTransDef),L_LakeVol)*L_LakeTranspMultiplier
L_RivOutFlow = max(isL_HEPP_Active*L_SanitaryFlow,(L_LakeVol-(L_OutflTrVoPostHEPP*isL_HEPP_Active)-L_OutflTrVolPreHEPP*(1-isL_HEPP_Active))*(L_LakeOverFlowFrac)*(1+L_Lakelevelexcess^L_LakeOverFlPow))
L_InFlowtoLake =  D_RiverFlowtoLake+D_GWtoLake
L_RestartR = isO_Reset * L_CumRivOutFlow / config.dt
L_RivOutFlow = max(isL_HEPP_Active*L_SanitaryFlow,(L_LakeVol-(L_OutflTrVoPostHEPP*isL_HEPP_Active)-L_OutflTrVolPreHEPP*(1-isL_HEPP_Active))*(L_LakeOverFlowFrac)*(1+L_Lakelevelexcess^L_LakeOverFlPow))
L_RestartH = isO_Reset * L_CumHEPPUse
L_HEPPWatUseFlow = L_HEPP_Outflow if isL_HEPP_Active==1 else 0
L_RestartE = isO_Reset * L_CumEvapLake / config.dt
L_EvapLake = min(np.sum(L_LakeTransDef),L_LakeVol)*L_LakeTranspMultiplier

calculate.update(L_CumEvapLake, inflow=L_EvapLake, outflow=L_RestartE, dt=config.dt)
calculate.update(L_CumHEPPUse, inflow=L_HEPPWatUseFlow, outflow=L_RestartH, dt=config.dt)
calculate.update(L_CumRivOutFlow, inflow=L_RivOutFlow, outflow=L_RestartR, dt=config.dt)
calculate.update(L_LakeVol, inflow=L_InFlowtoLake, outflow=L_EvapLake, dt=config.dt)
