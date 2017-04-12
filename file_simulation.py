__author__ = 'tuhv'


import numpy as np
import config
import calculate


# Getting data from excel file


# Getting input data
# Rainfall
I_WarmUpTime = 730
I_CaDOYStart = 0
I_RainYearStart = 0
isI_UseSpatVarRain = 0,
I_RainMultiplier = 1,
isI_RainCycle = 0,
I_Rain_IntensMean = 10,
I_Rain_IntensCoefVar = 0.3,
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
L_HEPP_Active_ = 1
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
O_Ch_inGWStock = [np.zeros(shape=(len(config.MEASUREPERIOD, 1)))]
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
D_SoilWater = [np.zeros(shape=(len(config.VEGCLASS, len(config.SUBCATCHMENT))))]
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
I_RainDoY = I_Simulation_Time if (isI_RainCycle == 0) else 1 + I_Simulation_Time % 365
I_SpatRain1 = [np.zeros(config.SUBCATCHMENT) for i in range(config.FOURYEARS)]
I_SpatRain2 = [np.zeros(config.SUBCATCHMENT) for i in range(config.FOURYEARS)]
I_SpatRain3 = [np.zeros(config.SUBCATCHMENT) for i in range(config.FOURYEARS)]
I_SpatRain4 = [np.zeros(config.SUBCATCHMENT) for i in range(config.FOURYEARS)]
I_SpatRain5 = [np.zeros(config.SUBCATCHMENT) for i in range(config.FOURYEARS)]
I_SpatRain6 = [np.zeros(config.SUBCATCHMENT) for i in range(config.FOURYEARS)]
I_SpatRain7 = [np.zeros(config.SUBCATCHMENT) for i in range(config.FOURYEARS)]

if I_RainDoY <= 1460:
    I_SpatRainTime = I_SpatRain1 * I_RainMultiplier
elif I_RainDoY <= 2920:
    I_SpatRainTime = I_SpatRain2 * I_RainMultiplier
elif I_RainDoY <= 4380:
    I_SpatRainTime = I_SpatRain3 * I_RainMultiplier
elif I_RainDoY <= 5840:
    I_SpatRainTime = I_SpatRain4 * I_RainMultiplier
elif I_RainDoY <= 7300:
    I_SpatRainTime = I_SpatRain5 * I_RainMultiplier
elif I_RainDoY <= 8760:
    I_SpatRainTime = I_SpatRain6 * I_RainMultiplier
else:
    I_SpatRainTime = I_SpatRain7 * I_RainMultiplier

I_DailyRainYear_1_to_4 = [0 for i in range(config.FOURYEARS)]
I_DailyRainYear_5_to_8 = [0 for i in range(config.FOURYEARS)]
I_DailyRainYear_9_to_12 = [0 for i in range(config.FOURYEARS)]
I_DailyRainYear_13_to_16 = [0 for i in range(config.FOURYEARS)]
I_DailyRainYear_17_to_20 = [0 for i in range(config.FOURYEARS)]
I_DailyRainYear_21_to_24 = [0 for i in range(config.FOURYEARS)]
I_DailyRainYear_25_to_28 = [0 for i in range(config.FOURYEARS)]

if I_RainDoY <= 1460:
    I_DailyRain = I_DailyRainYear_1_to_4 * I_RainMultiplier
elif I_RainDoY <= 2920:
    I_DailyRain = I_DailyRainYear_5_to_8 * I_RainMultiplier
elif I_RainDoY <= 4380:
    I_DailyRain = I_DailyRainYear_9_to_12 * I_RainMultiplier
elif I_RainDoY <= 5840:
    I_DailyRain = I_DailyRainYear_13_to_16 * I_RainMultiplier
elif I_RainDoY <= 7300:
    I_DailyRain = I_DailyRainYear_17_to_20 * I_RainMultiplier
elif I_RainDoY <= 8760:
    I_DailyRain = I_DailyRainYear_21_to_24 * I_RainMultiplier
else:
    I_DailyRain = I_DailyRainYear_25_to_28 * I_RainMultiplier

I_RainPerDay = I_SpatRainTime if isI_UseSpatVarRain else I_DailyRain

I_RainDuration = ((I_RainPerDay / I_Rain_IntensMean) *
                  min(max(0,
                          1-3 * I_Rain_IntensCoefVar,
                          np.normal(1, I_Rain_IntensCoefVar, I_Rain_GenSeed + 11250)),
                      1 + 3 * I_Rain_IntensCoefVar))
# Getting input data
isD_FeedingIntoLake = np.zeros(len(config.SUBCATCHMENT), 1)
I_RoutingDistance = np.zeros(len(config.SUBCATCHMENT), 1)
I_Area = np.zeros(len(config.SUBCATCHMENT), 1)
I_TotalArea = np.sum(I_Area)
I_RelArea = I_Area/I_TotalArea if I_TotalArea else 0

I_InterceptClass = np.zeros(config.LANDCOVERTYPE)
I_RelDroughtFract = np.zeros(config.LANDCOVERTYPE)

D_FeedingIntoLake_ = np.zeros(len(config.SUBCATCHMENT), 1)
I_Area = np.zeros(len(config.SUBCATCHMENT), 1)
I_TotalArea = np.sum(I_Area)

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
I_FracVegClass_1 = np.append((I_Frac_1_1, I_Frac_2_1, I_Frac_3_1, I_Frac_4_1, I_Frac_5_1,
                                   I_Frac_6_1, I_Frac_7_1, I_Frac_8_1, I_Frac_9_1, I_Frac_10_1,
                                   I_Frac_11_1, I_Frac_12_1, I_Frac_13_1, I_Frac_14_1, I_Frac_15_1,
                                   I_Frac_16_1, I_Frac_17_1, I_Frac_18_1, I_Frac_19_1, I_Frac_20_1))

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
I_FracVegClass_2 = np.append((I_Frac_1_2, I_Frac_2_2, I_Frac_3_2, I_Frac_4_2, I_Frac_5_2,
                                   I_Frac_6_2, I_Frac_7_2, I_Frac_8_2, I_Frac_9_2, I_Frac_10_2,
                                   I_Frac_11_2, I_Frac_12_2, I_Frac_13_2, I_Frac_14_2, I_Frac_15_2,
                                   I_Frac_16_2, I_Frac_17_2, I_Frac_18_2, I_Frac_19_2, I_Frac_20_2))
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
I_FracVegClass_3 = np.append((I_Frac_1_3, I_Frac_2_3, I_Frac_3_3, I_Frac_4_3, I_Frac_5_3,
                                   I_Frac_6_3, I_Frac_7_3, I_Frac_8_3, I_Frac_9_3, I_Frac_10_3,
                                   I_Frac_11_3, I_Frac_12_3, I_Frac_13_3, I_Frac_14_3, I_Frac_15_3,
                                   I_Frac_16_3, I_Frac_17_3, I_Frac_18_3, I_Frac_19_3, I_Frac_20_3))
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
I_FracVegClass_4 = np.append((I_Frac_1_4, I_Frac_2_4, I_Frac_3_4, I_Frac_4_4, I_Frac_5_4,
                                   I_Frac_6_4, I_Frac_7_4, I_Frac_8_4, I_Frac_9_4, I_Frac_10_4,
                                   I_Frac_11_4, I_Frac_12_4, I_Frac_13_4, I_Frac_14_4, I_Frac_15_4,
                                   I_Frac_16_4, I_Frac_17_4, I_Frac_18_4, I_Frac_19_4, I_Frac_20_4))
I_FracVegClasses = np.append((I_FracVegClass_1, I_FracVegClass_2, I_FracVegClass_3, I_FracVegClass_4))

I_InputDataYears = [00, 24, 30]
I_Flag1 = 1 if I_Simulation_Time < I_InputDataYears[1] else 0 # 0: Start: Trans1, 2: Trans2, 3: End
I_Flag2 = 1 if I_Simulation_Time < I_InputDataYears[2] and I_Flag1 == 0 else 0

I_GWRelFrac1 = np.zeros(len(config.SUBCATCHMENT))
I_GWRelFrac2 = np.zeros(len(config.SUBCATCHMENT))
I_GWRelFrac3 = np.zeros(len(config.SUBCATCHMENT))
I_GWRelFrac4 = np.zeros(len(config.SUBCATCHMENT))
I_GWRelFracs = np.append((I_GWRelFrac1, I_GWRelFrac2, I_GWRelFrac3, I_GWRelFrac4))

I_MaxDynGWSub1 = np.zeros(len(config.SUBCATCHMENT))
I_MaxDynGWSub2 = np.zeros(len(config.SUBCATCHMENT))
I_MaxDynGWSub3 = np.zeros(len(config.SUBCATCHMENT))
I_MaxDynGWSub4 = np.zeros(len(config.SUBCATCHMENT))
I_MaxDynGWSubs = np.append((I_MaxDynGWSub1, I_MaxDynGWSub2, I_MaxDynGWSub3, I_MaxDynGWSub4))

I_PWPSub1 = np.zeros(len(config.SUBCATCHMENT))
I_PWPSub2 = np.zeros(len(config.SUBCATCHMENT))
I_PWPSub3 = np.zeros(len(config.SUBCATCHMENT))
I_PWPSub4 = np.zeros(len(config.SUBCATCHMENT))
I_PWPSubs = np.append((I_PWPSub1, I_PWPSub2, I_PWPSub3, I_PWPSub4))

I_SoilSatminFCSub1 = np.zeros(len(config.SUBCATCHMENT))
I_SoilSatminFCSub2 = np.zeros(len(config.SUBCATCHMENT))
I_SoilSatminFCSub3 = np.zeros(len(config.SUBCATCHMENT))
I_SoilSatminFCSub4 = np.zeros(len(config.SUBCATCHMENT))
I_SoilSatminFCSubs = np.append((I_SoilSatminFCSub1, I_SoilSatminFCSub2, I_SoilSatminFCSub3, I_SoilSatminFCSub4))

I_RivFlowTime1 = np.zeros(len(config.SUBCATCHMENT))
I_RivFlowTime2 = np.zeros(len(config.SUBCATCHMENT))
I_RivFlowTime3 = np.zeros(len(config.SUBCATCHMENT))
I_RivFlowTime4 = np.zeros(len(config.SUBCATCHMENT))
I_RivFlowTimes = np.append((I_RivFlowTime1, I_RivFlowTime2, I_RivFlowTime3, I_RivFlowTime4))

I_AvailWatSub1 = np.zeros(len(config.SUBCATCHMENT))
I_AvailWatSub2 = np.zeros(len(config.SUBCATCHMENT))
I_AvailWatSub3 = np.zeros(len(config.SUBCATCHMENT))
I_AvailWatSub4 = np.zeros(len(config.SUBCATCHMENT))
I_AvailWatSubs = np.append((I_AvailWatSub1, I_AvailWatSub2, I_AvailWatSub3, I_AvailWatSub4))

I_TopSoilBD_BDRef1 = np.zeros(len(config.SUBCATCHMENT))
I_TopSoilBD_BDRef2 = np.zeros(len(config.SUBCATCHMENT))
I_TopSoilBD_BDRef3 = np.zeros(len(config.SUBCATCHMENT))
I_TopSoilBD_BDRef4 = np.zeros(len(config.SUBCATCHMENT))
I_TopSoilBD_BDRefs = np.append((I_TopSoilBD_BDRef1, I_TopSoilBD_BDRef2, I_TopSoilBD_BDRef3, I_TopSoilBD_BDRef4))

def get_variable_now(array_values):
    global I_Simulation_Time
    global I_InputDataYears
    global I_Flag1
    global I_Flag2
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
    return result

I_GWRelFracNow = get_variable_now(I_GWRelFracs)
I_MaxDynGwSubNow = get_variable_now(I_MaxDynGWSubs)
I_FracVegClassNow = get_variable_now(I_FracVegClasses)
I_PWPSubNow = get_variable_now(I_PWPSubs)
I_SoilSatminFCSubNow = get_variable_now(I_SoilSatminFCSubs)
I_RivFlowTimeNow = get_variable_now(I_RivFlowTimes)
I_TopSoilBD_BDRefNow = get_variable_now(I_TopSoilBD_BDRefs)
I_AvailWatClassNow = get_variable_now(I_AvailWatSubs)

I_FracVegClassSum1 = np.sum(I_FracVegClass_1)
I_FracVegClassSum2 = np.sum(I_FracVegClass_2)
I_FracVegClassSum3 = np.sum(I_FracVegClass_3)
I_FracVegClassSum4 = np.sum(I_FracVegClass_4)
I_FracVegClassSumNow = np.sum(I_FracVegClassNow)

I_DailyRainAmount = np.multiply(I_RainPerDay, np.multiply(I_FracVegClassNow, I_RelArea))

I_StillWarmUp_ = 1 if time <= I_WarmUpTime else 0
I_WUcorrection = 1 if time == int(I_WarmUpTime + 1 ) else 0

calculate.update(stock=isI_WarmEdUp, inflow=I_WarmUpTime, dt=config.dt)

