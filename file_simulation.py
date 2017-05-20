import numpy as np
import config
import calculate

subCatchment = len(config.SUBCATCHMENT)
vegClass = len(config.VEGCLASS)
measurePeriod = len(config.MEASUREPERIOD)
obsPoint = len(config.OBSPOINT)
obsPoint1 = len(config.OBSPOINT1)

I_GWRelFracConst = config.I_GWRelFracConst
I_GWRelFracConst_ = config.I_GWRelFracConst_
I_InitRelGW = config.I_InitRelGW
I_InitRelSoil = config.I_InitRelSoil
I_DaminThisStream_ = config.I_DaminThisStream_
I_EvapotransMethod = config.I_EvapotransMethod
I_InterceptEffectonTransp = config.I_InterceptEffectonTransp
I_MaxDynGWConst = config.I_MaxDynGWConst
I_MaxInf = config.I_MaxInf
I_MaxInfSSoil = config.I_MaxInfSSoil
I_PercFracMultiplier = config.I_PercFracMultiplier
I_PowerInfiltRed = config.I_PowerInfiltRed
I_RiverflowDispersalFactor = config.I_RiverflowDispersalFactor
I_RoutVeloc_m_per_s = config.I_RoutVeloc_m_per_s
I_SoilPropConst_ = config.I_SoilPropConst_
I_Tortuosity = config.I_Tortuosity
I_SoilSatMinFCConst = config.I_SoilSatMinFCConst
I_SurfLossFrac = config.I_SurfLossFrac
L_LakeTranspMultiplier = config.L_LakeTranspMultiplier
L_ResrDepth = config.L_ResrDepth
I_AvailWaterConst = config.I_AvailWaterConst

FOURYEARS = config.FOURYEARS
MONTH = config.MONTH
LANDCOVER = config.LANDCOVER
dt = config.dt

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

L_SanitaryFlow = 0
L_OutflTrVolPreHEPP = 0
L_OutflTrVoPostHEPP = 0
S_TrampMax = 100

I_SoilQflowFrac = 0.1
I_RainIntercDripRt = 10
I_RainMaxIntDripDur = 0.5

isD_GWUseFacility = np.ones(shape=(subCatchment, vegClass))
D_GW_Utilization_fraction = 0.02
D_IrrigEfficiency = np.zeros(shape=(subCatchment, 1))
isL_Lake = np.zeros(shape=(subCatchment, 1))

# Subcatchment param

# Patch Balance

# Stream Network
D_FracGWtoLake = np.zeros(shape=(subCatchment, 1))

# Measurement Period
O_MPeriodLength = [365, 365, 365]


# Getting data from excel file

I_Frac_1_1 = np.zeros(shape=(subCatchment, 1))
I_Frac_2_1 = np.zeros(shape=(subCatchment, 1))
I_Frac_3_1 = np.zeros(shape=(subCatchment, 1))
I_Frac_4_1 = np.zeros(shape=(subCatchment, 1))
I_Frac_5_1 = np.zeros(shape=(subCatchment, 1))
I_Frac_6_1 = np.zeros(shape=(subCatchment, 1))
I_Frac_7_1 = np.zeros(shape=(subCatchment, 1))
I_Frac_8_1 = np.zeros(shape=(subCatchment, 1))
I_Frac_9_1 = np.zeros(shape=(subCatchment, 1))
I_Frac_10_1 = np.zeros(shape=(subCatchment, 1))
I_Frac_11_1 = np.zeros(shape=(subCatchment, 1))
I_Frac_12_1 = np.zeros(shape=(subCatchment, 1))
I_Frac_13_1 = np.zeros(shape=(subCatchment, 1))
I_Frac_14_1 = np.zeros(shape=(subCatchment, 1))
I_Frac_15_1 = np.zeros(shape=(subCatchment, 1))
I_Frac_16_1 = np.zeros(shape=(subCatchment, 1))
I_Frac_17_1 = np.zeros(shape=(subCatchment, 1))
I_Frac_18_1 = np.zeros(shape=(subCatchment, 1))
I_Frac_19_1 = np.zeros(shape=(subCatchment, 1))
I_Frac_20_1 = np.zeros(shape=(subCatchment, 1))
I_FracVegClass_1 = np.concatenate(
    (I_Frac_1_1, I_Frac_2_1, I_Frac_3_1, I_Frac_4_1,
     I_Frac_5_1, I_Frac_6_1, I_Frac_7_1, I_Frac_8_1,
     I_Frac_9_1, I_Frac_10_1, I_Frac_11_1, I_Frac_12_1,
     I_Frac_13_1, I_Frac_14_1, I_Frac_15_1, I_Frac_16_1,
     I_Frac_17_1, I_Frac_18_1, I_Frac_19_1, I_Frac_20_1),
    axis=1)

I_Frac_1_2 = np.zeros(shape=(subCatchment, 1))
I_Frac_2_2 = np.zeros(shape=(subCatchment, 1))
I_Frac_3_2 = np.zeros(shape=(subCatchment, 1))
I_Frac_4_2 = np.zeros(shape=(subCatchment, 1))
I_Frac_5_2 = np.zeros(shape=(subCatchment, 1))
I_Frac_6_2 = np.zeros(shape=(subCatchment, 1))
I_Frac_7_2 = np.zeros(shape=(subCatchment, 1))
I_Frac_8_2 = np.zeros(shape=(subCatchment, 1))
I_Frac_9_2 = np.zeros(shape=(subCatchment, 1))
I_Frac_10_2 = np.zeros(shape=(subCatchment, 1))
I_Frac_11_2 = np.zeros(shape=(subCatchment, 1))
I_Frac_12_2 = np.zeros(shape=(subCatchment, 1))
I_Frac_13_2 = np.zeros(shape=(subCatchment, 1))
I_Frac_14_2 = np.zeros(shape=(subCatchment, 1))
I_Frac_15_2 = np.zeros(shape=(subCatchment, 1))
I_Frac_16_2 = np.zeros(shape=(subCatchment, 1))
I_Frac_17_2 = np.zeros(shape=(subCatchment, 1))
I_Frac_18_2 = np.zeros(shape=(subCatchment, 1))
I_Frac_19_2 = np.zeros(shape=(subCatchment, 1))
I_Frac_20_2 = np.zeros(shape=(subCatchment, 1))
I_FracVegClass_2 = np.concatenate(
    (I_Frac_1_2, I_Frac_2_2, I_Frac_3_2, I_Frac_4_2,
     I_Frac_5_2, I_Frac_6_2, I_Frac_7_2, I_Frac_8_2,
     I_Frac_9_2, I_Frac_10_2, I_Frac_11_2, I_Frac_12_2,
     I_Frac_13_2, I_Frac_14_2, I_Frac_15_2, I_Frac_16_2,
     I_Frac_17_2, I_Frac_18_2, I_Frac_19_2, I_Frac_20_2),
    axis=1)

I_Frac_1_3 = np.zeros(shape=(subCatchment, 1))
I_Frac_2_3 = np.zeros(shape=(subCatchment, 1))
I_Frac_3_3 = np.zeros(shape=(subCatchment, 1))
I_Frac_4_3 = np.zeros(shape=(subCatchment, 1))
I_Frac_5_3 = np.zeros(shape=(subCatchment, 1))
I_Frac_6_3 = np.zeros(shape=(subCatchment, 1))
I_Frac_7_3 = np.zeros(shape=(subCatchment, 1))
I_Frac_8_3 = np.zeros(shape=(subCatchment, 1))
I_Frac_9_3 = np.zeros(shape=(subCatchment, 1))
I_Frac_10_3 = np.zeros(shape=(subCatchment, 1))
I_Frac_11_3 = np.zeros(shape=(subCatchment, 1))
I_Frac_12_3 = np.zeros(shape=(subCatchment, 1))
I_Frac_13_3 = np.zeros(shape=(subCatchment, 1))
I_Frac_14_3 = np.zeros(shape=(subCatchment, 1))
I_Frac_15_3 = np.zeros(shape=(subCatchment, 1))
I_Frac_16_3 = np.zeros(shape=(subCatchment, 1))
I_Frac_17_3 = np.zeros(shape=(subCatchment, 1))
I_Frac_18_3 = np.zeros(shape=(subCatchment, 1))
I_Frac_19_3 = np.zeros(shape=(subCatchment, 1))
I_Frac_20_3 = np.zeros(shape=(subCatchment, 1))
I_FracVegClass_3 = np.concatenate(
    (I_Frac_1_3, I_Frac_2_3, I_Frac_3_3, I_Frac_4_3,
     I_Frac_5_3, I_Frac_6_3, I_Frac_7_3, I_Frac_8_3,
     I_Frac_9_3, I_Frac_10_3, I_Frac_11_3, I_Frac_12_3,
     I_Frac_13_3, I_Frac_14_3, I_Frac_15_3, I_Frac_16_3,
     I_Frac_17_3, I_Frac_18_3, I_Frac_19_3, I_Frac_20_3),
    axis=1)
I_Frac_1_4 = np.zeros(shape=(subCatchment, 1))
I_Frac_2_4 = np.zeros(shape=(subCatchment, 1))
I_Frac_3_4 = np.zeros(shape=(subCatchment, 1))
I_Frac_4_4 = np.zeros(shape=(subCatchment, 1))
I_Frac_5_4 = np.zeros(shape=(subCatchment, 1))
I_Frac_6_4 = np.zeros(shape=(subCatchment, 1))
I_Frac_7_4 = np.zeros(shape=(subCatchment, 1))
I_Frac_8_4 = np.zeros(shape=(subCatchment, 1))
I_Frac_9_4 = np.zeros(shape=(subCatchment, 1))
I_Frac_10_4 = np.zeros(shape=(subCatchment, 1))
I_Frac_11_4 = np.zeros(shape=(subCatchment, 1))
I_Frac_12_4 = np.zeros(shape=(subCatchment, 1))
I_Frac_13_4 = np.zeros(shape=(subCatchment, 1))
I_Frac_14_4 = np.zeros(shape=(subCatchment, 1))
I_Frac_15_4 = np.zeros(shape=(subCatchment, 1))
I_Frac_16_4 = np.zeros(shape=(subCatchment, 1))
I_Frac_17_4 = np.zeros(shape=(subCatchment, 1))
I_Frac_18_4 = np.zeros(shape=(subCatchment, 1))
I_Frac_19_4 = np.zeros(shape=(subCatchment, 1))
I_Frac_20_4 = np.zeros(shape=(subCatchment, 1))
I_FracVegClass_4 = np.concatenate(
    (I_Frac_1_4, I_Frac_2_4, I_Frac_3_4, I_Frac_4_4,
     I_Frac_5_4, I_Frac_6_4, I_Frac_7_4, I_Frac_8_4,
     I_Frac_9_4, I_Frac_10_4, I_Frac_11_4, I_Frac_12_4,
     I_Frac_13_4, I_Frac_14_4, I_Frac_15_4, I_Frac_16_4,
     I_Frac_17_4, I_Frac_18_4, I_Frac_19_4, I_Frac_20_4),
    axis=1
)
I_FracVegClasses = [
    I_FracVegClass_1, I_FracVegClass_2,
    I_FracVegClass_3, I_FracVegClass_4
]

I_InputDataYears = [00, 24, 30]

I_GWRelFrac1 = np.zeros(shape=(subCatchment, 1))
I_GWRelFrac2 = np.zeros(shape=(subCatchment, 1))
I_GWRelFrac3 = np.zeros(shape=(subCatchment, 1))
I_GWRelFrac4 = np.zeros(shape=(subCatchment, 1))
I_GWRelFracs = [
    I_GWRelFrac1, I_GWRelFrac2,
    I_GWRelFrac3, I_GWRelFrac4
]

I_MaxDynGWSub1 = np.zeros(shape=(subCatchment, 1))
I_MaxDynGWSub2 = np.zeros(shape=(subCatchment, 1))
I_MaxDynGWSub3 = np.zeros(shape=(subCatchment, 1))
I_MaxDynGWSub4 = np.zeros(shape=(subCatchment, 1))
I_MaxDynGWSubs = [
    I_MaxDynGWSub1,
    I_MaxDynGWSub2,
    I_MaxDynGWSub3,
    I_MaxDynGWSub4
]

I_PWPSub1 = np.zeros(shape=(subCatchment, 1))
I_PWPSub2 = np.zeros(shape=(subCatchment, 1))
I_PWPSub3 = np.zeros(shape=(subCatchment, 1))
I_PWPSub4 = np.zeros(shape=(subCatchment, 1))
I_PWPSubs = [I_PWPSub1, I_PWPSub2, I_PWPSub3, I_PWPSub4]

I_SoilSatminFCSub1 = np.zeros(shape=(subCatchment, 1))
I_SoilSatminFCSub2 = np.zeros(shape=(subCatchment, 1))
I_SoilSatminFCSub3 = np.zeros(shape=(subCatchment, 1))
I_SoilSatminFCSub4 = np.zeros(shape=(subCatchment, 1))
I_SoilSatminFCSubs = [
    I_SoilSatminFCSub1,
    I_SoilSatminFCSub2,
    I_SoilSatminFCSub3,
    I_SoilSatminFCSub4
]

I_RivFlowTime1 = np.zeros(shape=(subCatchment, 1))
I_RivFlowTime2 = np.zeros(shape=(subCatchment, 1))
I_RivFlowTime3 = np.zeros(shape=(subCatchment, 1))
I_RivFlowTime4 = np.zeros(shape=(subCatchment, 1))
I_RivFlowTimes = [
    I_RivFlowTime1,
    I_RivFlowTime2,
    I_RivFlowTime3,
    I_RivFlowTime4
]

I_AvailWatSub1 = np.zeros(shape=(subCatchment, 1))
I_AvailWatSub2 = np.zeros(shape=(subCatchment, 1))
I_AvailWatSub3 = np.zeros(shape=(subCatchment, 1))
I_AvailWatSub4 = np.zeros(shape=(subCatchment, 1))
I_AvailWatSubs = [
    I_AvailWatSub1,
    I_AvailWatSub2,
    I_AvailWatSub3,
    I_AvailWatSub4
]

I_TopSoilBD_BDRef1 = np.zeros(shape=(subCatchment, 1))
I_TopSoilBD_BDRef2 = np.zeros(shape=(subCatchment, 1))
I_TopSoilBD_BDRef3 = np.zeros(shape=(subCatchment, 1))
I_TopSoilBD_BDRef4 = np.zeros(shape=(subCatchment, 1))
I_TopSoilBD_BDRefs = [
    I_TopSoilBD_BDRef1,
    I_TopSoilBD_BDRef2,
    I_TopSoilBD_BDRef3,
    I_TopSoilBD_BDRef4
]


def initial_array(value, repeats=1):
    return [value for repeat in range(repeats)]


I_DailyRainYear_1_to_4 = initial_array(
    np.zeros(shape=(subCatchment, 1)),
    FOURYEARS
)

I_DailyRainYear_5_to_8 = initial_array(
    np.zeros(shape=(subCatchment, 1)),
    FOURYEARS
)
I_DailyRainYear_9_to_12 = initial_array(
    np.zeros(shape=(subCatchment, 1)),
    FOURYEARS
)
I_DailyRainYear_13_to_16 = initial_array(
    np.zeros(shape=(subCatchment, 1)),
    FOURYEARS
)
I_DailyRainYear_17_to_20 = initial_array(
    np.zeros(shape=(subCatchment, 1)),
    FOURYEARS
)
I_DailyRainYear_21_to_24 = initial_array(
    np.zeros(shape=(subCatchment, 1)),
    FOURYEARS
)
I_DailyRainYear_25_to_28 = initial_array(
    np.zeros(shape=(subCatchment, 1)),
    FOURYEARS
)

I_DailyRainYear = [
    I_DailyRainYear_1_to_4,
    I_DailyRainYear_5_to_8,
    I_DailyRainYear_9_to_12,
    I_DailyRainYear_13_to_16,
    I_DailyRainYear_17_to_20,
    I_DailyRainYear_21_to_24,
    I_DailyRainYear_25_to_28,
]


I_Daily_Evap_1_to_4 = initial_array(0, FOURYEARS)
I_Daily_Evap_5_to_8 = initial_array(0, FOURYEARS)
I_Daily_Evap_9_to_12 = initial_array(0, FOURYEARS)
I_Daily_Evap_13_to_16 = initial_array(0, FOURYEARS)
I_Daily_Evap_17_to_20 = initial_array(0, FOURYEARS)
I_Daily_Evap_21_to_24 = initial_array(0, FOURYEARS)
I_Daily_Evap_25_to_28 = initial_array(0, FOURYEARS)
I_Daily_Evap_29_to_32 = initial_array(0, FOURYEARS)

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

I_RFlowData_Year_1_to_4 = initial_array(0, FOURYEARS)
I_RFlowData_Year_5_to_8 = initial_array(0, FOURYEARS)
I_RFlowData_Year_9_to_12 = initial_array(0, FOURYEARS)
I_RFlowData_Year_13_to_16 = initial_array(0, FOURYEARS)
I_RFlowData_Year_17_to_20 = initial_array(0, FOURYEARS)
I_RFlowData_Year_21_to_24 = initial_array(0, FOURYEARS)
I_RFlowData_Year_25_to_28 = initial_array(0, FOURYEARS)
I_RFlowData_Year_29_to_32 = initial_array(0, FOURYEARS)

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

I_MultiplierEvapoTrans = [
    np.zeros(shape=(subCatchment, 1)) for i in range(MONTH)
    ]
I_EvapoTrans = [0 for i in range(MONTH)]

I_RelDroughtFact = np.zeros(shape=(1, vegClass))
D_SubCResUseFrac = np.zeros(shape=(subCatchment, 1))
isI_DaminThisStream = np.zeros(shape=(subCatchment, 1))
isI_SubcContr = np.ones(shape=(subCatchment, 1))


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
O_CumSoilQFlow_Subca_1 = [np.zeros(shape=(subCatchment, obsPoint))]
O_CumSurfQFlow = [0]
O_CumTransp = [0]
# O_InitGWStock = arraysum(I_MaxDynGWArea[*])*I_InitRelGW
O_InitGWStock = [0]
# O_InitSoilW = arraysum(I_AvailWaterClass[*,*])*I_InitRelSoil
O_InitSoilW = [0]
O_RainYest = [np.zeros(shape=(subCatchment, 1))]
G_GrassStandingBiomass = [np.ones(shape=(subCatchment, vegClass))]
G_SurfaceLitter = [np.zeros(shape=(subCatchment, vegClass))]
G_SurfManure = [np.ones(shape=(subCatchment, vegClass))]
isI_WarmEdUp = [0]
O_CumDebitData = [0]
L_CumEvapLake = [0]
L_CumHEPPUse = [0]
L_CumRivOutFlow = [0]
L_LakeVol = [0]
O_BestYyHEPP = [0]
O_Ch_inGWStock = [np.zeros(shape=(measurePeriod, 1))]
O_Ch_inWStock = [np.zeros(shape=(measurePeriod, 1))]
O_CumBaseFlowMP = [np.zeros(shape=(measurePeriod, 1))]
O_CumDebitDataMP = [np.zeros(shape=(measurePeriod, 1))]
O_CumDebitPredMP = [np.zeros(shape=(measurePeriod, 1))]
O_CumEvapLakeMP = [np.zeros(shape=(measurePeriod, 1))]
O_CumEvapTransMP = [np.zeros(shape=(measurePeriod, 1))]
O_CumGWMP = [np.zeros(shape=(measurePeriod, 1))]
O_CumHEPPOutFlowMP = [np.zeros(shape=(measurePeriod, 1))]
O_CumInfiltrationMP = [np.zeros(shape=(measurePeriod, 1))]
O_CumIntercEvapMP = [np.zeros(shape=(measurePeriod, 1))]
O_CumRainMP = [np.zeros(shape=(measurePeriod, 1))]
O_CumRivInflowtoLakeMP = [np.zeros(shape=(measurePeriod, 1))]
O_CumRivOutFlowMP = [np.zeros(shape=(measurePeriod, 1))]
O_CumSoilQFlowMP = [np.zeros(shape=(measurePeriod, 1))]
O_CumSoilWMP = [np.zeros(shape=(measurePeriod, 1))]
O_CumSurfQFlowMP = [np.zeros(shape=(measurePeriod, 1))]
O_CumTranspMP = [np.zeros(shape=(measurePeriod, 1))]
O_DeltaCatchmStMP = [np.zeros(shape=(measurePeriod, 1))]
O_Hepp_Kwh_per_dayMP = [np.zeros(shape=(measurePeriod, 1))]
O_InitEvapoMP = [np.zeros(shape=(measurePeriod, 1))]
O_InitGWStockMP = [np.zeros(shape=(measurePeriod, 1))]
O_InitSWMP = [np.zeros(shape=(measurePeriod, 1))]
O_LastYHepp = [0]
O_ThisYHepp = [0]
O_WorstYHEPP = [1]
O_YearSim = [1]
D_CumEvapTranspClass = [np.zeros(shape=(subCatchment, vegClass))]
D_CumNegRain = [np.zeros(shape=(subCatchment, 1))]
D_EvapTranspClass = [np.zeros(shape=(subCatchment, vegClass))]
D_GWArea = [np.zeros(shape=(subCatchment, 1))]
D_SoilWater = [np.zeros(shape=(subCatchment, vegClass))]
S_RelBulkDensity = [np.zeros(shape=(subCatchment, vegClass))]
D_CumInflowtoLake = [0]
D_CumTotRiverFlow = [np.zeros(shape=(subCatchment, obsPoint))]
D_StreamsSurfQ = [np.zeros(shape=(subCatchment, obsPoint))]
D_TotRiverFlowNoDelay = [np.zeros(shape=(subCatchment, obsPoint))]
D_CumResvEvap = [0]
D_SubcResVol = [np.zeros(shape=(subCatchment, 1))]

# Simulation

time = 0

I_Simulation_Time = (
    time + I_CaDOYStart +
    365 * I_RainYearStart -
    isI_WarmEdUp[time] * (I_WarmUpTime + 1)
)

I_Flag1 = 1 if I_Simulation_Time < I_InputDataYears[1] else 0
I_Flag2 = 1 if I_Simulation_Time < I_InputDataYears[2] and I_Flag1 == 0 else 0

I_RainDoY = (I_Simulation_Time
             if (isI_RainCycle == 0)
             else 1 + I_Simulation_Time % 365)
I_SpatRain1 = initial_array(
    np.zeros(shape=(subCatchment, 1)),
    FOURYEARS
)
I_SpatRain2 = initial_array(
    np.zeros(shape=(subCatchment, 1)),
    FOURYEARS
)
I_SpatRain3 = initial_array(
    np.zeros(shape=(subCatchment, 1)),
    FOURYEARS
)
I_SpatRain4 = initial_array(
    np.zeros(shape=(subCatchment, 1)),
    FOURYEARS
)
I_SpatRain5 = initial_array(
    np.zeros(shape=(subCatchment, 1)),
    FOURYEARS
)
I_SpatRain6 = initial_array(
    np.zeros(shape=(subCatchment, 1)),
    FOURYEARS
)
I_SpatRain7 = initial_array(
    np.zeros(shape=(subCatchment, 1)),
    FOURYEARS
)
I_SpatRain = [
    I_SpatRain1,
    I_SpatRain2,
    I_SpatRain3,
    I_SpatRain4,
    I_SpatRain5,
    I_SpatRain6,
    I_SpatRain7,
]

I_RainDoY_Stage = [1460, 2920, 4380, 5840, 7300, 8760]
for index, stage in enumerate(I_RainDoY_Stage):
    I_SpatRainTime = (I_SpatRain[index][I_Simulation_Time]
                      if I_RainDoY < stage
                      else I_SpatRain[6][I_Simulation_Time]) * I_RainMultiplier
for index, stage in enumerate(I_RainDoY_Stage):
    I_DailyRain = ((I_DailyRainYear[index][I_Simulation_Time]
                   if I_RainDoY <= stage
                   else I_DailyRainYear[6][I_Simulation_Time]) *
                         I_RainMultiplier)
I_RainPerDay = I_SpatRainTime if isI_UseSpatVarRain else I_DailyRain

I_RainDuration = ((I_RainPerDay / I_Rain_IntensMean) *
                  min(max(0,
                          1 - 3 * I_Rain_IntensCoefVar,
                          np.random.normal(1,
                                           I_Rain_IntensCoefVar,
                                           I_Rain_GenSeed + 11250)[0]),
                      1 + 3 * I_Rain_IntensCoefVar))
# Getting input data
isD_FeedingIntoLake = np.zeros(shape=(subCatchment, 1))
I_RoutingDistance = np.zeros(shape=(subCatchment, obsPoint))
I_Area = np.zeros(shape=(subCatchment, 1))
I_TotalArea = np.sum(I_Area)
I_RelArea = (I_Area/I_TotalArea
             if I_TotalArea
             else np.zeros(shape=(subCatchment, 1)))

I_InterceptClass = np.zeros(shape=(len(LANDCOVER), 1))
I_RelDroughtFract = np.zeros(shape=(len(LANDCOVER), 1))

D_FeedingIntoLake_ = np.zeros(shape=(subCatchment, 1))
I_Area = np.zeros(shape=(subCatchment, 1))
I_TotalArea = np.sum(I_Area)


def ARRAY_SUM(array, shape):
    array_shape = array.shape
    axis = 1 if array_shape[0] in shape else 0
    return np.sum(array, axis=axis).reshape(shape)


def get_variable_now(array_values):
    global I_RelArea
    global I_Simulation_Time
    global I_InputDataYears
    global I_Flag1
    global I_Flag2
    global subCatchment
    if array_values[0].shape[1] == 1:
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
            result = np.divide(
                (array_values[0] +
                 (array_values[1] - array_values[0]) *
                 (int(I_Simulation_Time/365) - I_InputDataYears[0]) /
                 (I_InputDataYears[1] - I_InputDataYears[0])),
                ARRAY_SUM(array_values[0], shape=(subCatchment, 1)),
                out=np.zeros_like(array_values[0]),
                where=I_RelArea != 0)
        elif I_Flag2:
            result = np.divide(
                (array_values[1] +
                 (array_values[2] - array_values[1]) *
                 (int(I_Simulation_Time/365) - I_InputDataYears[1]) /
                 (I_InputDataYears[2] - I_InputDataYears[1])),
                ARRAY_SUM(array_values[1], shape=(subCatchment, 1)),
                out=np.zeros_like(array_values[0]),
                where=I_RelArea != 0)
        else:
            result = np.divide(
                (array_values[2] +
                 (array_values[3] - array_values[2]) *
                 (int(I_Simulation_Time/365) - I_InputDataYears[2]) /
                 (I_InputDataYears[3] - I_InputDataYears[2])),
                ARRAY_SUM(array_values[2], shape=(subCatchment, 1)),
                out=np.zeros_like(array_values[0]),
                where=I_RelArea != 0)
        result = np.multiply(I_RelArea > 0, result)
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

I_DailyRainAmount = np.multiply(
    I_RainPerDay,
    np.multiply(I_FracVegClassNow, I_RelArea)
)
# OK
isI_StillWarmUp = 1 if time <= I_WarmUpTime else 0
I_WUcorrection = 1 if time == int(I_WarmUpTime + 1 ) else 0
I_WarmedUp = 1 if time == int(I_WarmUpTime) else 0
isO_Reset = 1 if I_WarmedUp == 1 or I_WUcorrection == 1 else 0
calculate.update(stock=isI_WarmEdUp, inflow=I_WarmedUp, dt=dt)

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

I_TimeEvap = (0
              if I_RainDoY == 0
              else 365 if I_RainDoY % 365 == 0 else I_RainDoY % 365)
I_MoY = 0 if I_RainDoY == 0 else int(I_TimeEvap/30.5) + 1
if I_EvapotransMethod == 1:
    I_PotEvapTransp = np.multiply(
        I_EvapoTrans[I_MoY],
        np.multiply(I_MultiplierEvapoTrans[I_MoY], I_FracArea)
    )
else:
    I_PotEvapTransp = np.multiply(
        I_Daily_Evapotrans,
        np.multiply(I_MultiplierEvapoTrans, I_FracArea)
    )

I_MaxInfSubSAreaClass = I_MaxInfSSoil * I_FracArea
I_MaxInfArea = I_MaxInf * np.multiply(
    I_FracArea,
    np.power(np.divide(0.7,
                       I_TopSoilBD_BDRefNow,
                       out=np.zeros_like(I_TopSoilBD_BDRefNow),
                       where=I_TopSoilBD_BDRefNow != 0),
             I_PowerInfiltRed
             )
)
I_CanIntercAreaClass = np.multiply(I_InterceptClass, I_FracArea)
I_AvailWaterClass = (I_AvailWaterConst * I_FracArea
                     if I_SoilPropConst_
                     else np.multiply(I_AvailWatClassNow, I_FracArea))
I_SoilSatClass = ((I_AvailWaterConst + I_SoilSatMinFCConst) * I_FracArea
                  if I_SoilPropConst_
                  else np.add(I_SoilSatminFCSubNow,
                              np.multiply(I_AvailWatClassNow, I_FracArea)))
I_GWRelFrac = I_GWRelFracConst if I_SoilPropConst_ else I_GWRelFracNow
I_MaxDynGWact = I_MaxDynGWConst if I_GWRelFracConst_ else I_MaxDynGwSubNow
I_MaxDynGWArea = np.multiply(I_MaxDynGWact, I_RelArea)
I_InitTotGW = np.add(I_MaxDynGWArea, I_InitRelGW)

D_InterceptEvap = np.multiply(I_CanIntercAreaClass,
                              (1 -
                               np.exp(-np.divide(
                                   I_DailyRainAmount,
                                   I_CanIntercAreaClass,
                                   out=np.zeros_like(I_CanIntercAreaClass),
                                   where=I_CanIntercAreaClass!=0))))

I_FracVegClassNow_Multiply_I_RelArea = np.multiply(I_FracVegClassNow, I_RelArea)
D_RainInterc = np.divide(D_InterceptEvap,
                         I_FracVegClassNow_Multiply_I_RelArea,
                         out=np.ones_like(D_InterceptEvap),
                         where=I_FracVegClassNow_Multiply_I_RelArea!=0)
D_RainIntercDelay = (np.minimum(I_RainMaxIntDripDur,
                               ARRAY_SUM(D_RainInterc,
                                         shape=(subCatchment, 1))) /
                     I_RainIntercDripRt)
I_RainTimeAvForInf = np.minimum(24, I_RainDuration + D_RainIntercDelay)
D_Infiltration = np.multiply(
    (1 - isL_Lake),
    np.minimum(np.minimum(I_SoilSatClass - D_SoilWater[time],
                          np.multiply(I_MaxInfArea,
                                      I_RainTimeAvForInf)/24),
               I_DailyRainAmount - D_InterceptEvap))
I_RelDroughtFact_AvailWaterClass = np.multiply(I_RelDroughtFact,
                                               I_AvailWaterClass)
D_RelWaterAv = np.minimum(1, np.divide(
    D_SoilWater[time],
    I_RelDroughtFact_AvailWaterClass,
    out=np.ones_like(D_SoilWater[time]),
    where=I_RelDroughtFact_AvailWaterClass!=0))
x = np.multiply(D_GWArea[time],
                np.multiply(isD_GWUseFacility,
                            np.multiply(D_GW_Utilization_fraction,
                                        np.subtract(1, D_RelWaterAv))))
D_Irrigation = np.minimum(
    np.divide(
        np.multiply(D_GWArea[time],
                    np.multiply(isD_GWUseFacility,
                                np.multiply(D_GW_Utilization_fraction,
                                            np.subtract(1, D_RelWaterAv)))),
        D_IrrigEfficiency,
        out=np.zeros(shape=(subCatchment, vegClass)),
        where=D_IrrigEfficiency!=0),
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
    D_Irrigation *(1-D_IrrigEfficiency))

D_GWaDisch = np.multiply(D_GWArea[time], I_GWRelFrac)

D_DeepInfiltration = np.multiply(
    isL_Lake == 1,
    np.minimum(
        np.minimum(
            np.minimum(
                np.multiply(
                    ARRAY_SUM(I_MaxInfArea, shape=(subCatchment, 1)),
                    I_RainTimeAvForInf
                )/24 - ARRAY_SUM(I_SoilSatClass, shape=(subCatchment, 1)) +
                ARRAY_SUM(D_SoilWater[time], shape=(subCatchment, 1)),
                ARRAY_SUM(I_MaxInfSubSAreaClass, shape=(subCatchment, 1))
            ),
            ARRAY_SUM(I_DailyRainAmount, shape=(subCatchment, 1)) -
            ARRAY_SUM(D_InterceptEvap, shape=(subCatchment, 1)) -
            ARRAY_SUM(D_Infiltration, shape=(subCatchment, 1))),
        I_MaxDynGWArea - D_GWArea[time]))

D_ActEvapTransp = np.multiply(
    isL_Lake != 1,
    np.multiply(
        I_PotEvapTransp -
        np.multiply(I_InterceptEffectonTransp, D_InterceptEvap),
        D_RelWaterAv))
D_SurfaceFlow = (np.multiply(isL_Lake == 1,
                             (ARRAY_SUM(I_DailyRainAmount,
                                        shape=(subCatchment, 1)) +
                              np.multiply(isL_Lake != 1,(
                                  ARRAY_SUM(I_DailyRainAmount,
                                            shape=(subCatchment, 1)) -
                                  ARRAY_SUM(D_InterceptEvap,
                                            shape=(subCatchment, 1)) -
                                  ARRAY_SUM(D_Infiltration,
                                            shape=(subCatchment, 1)) -
                                  D_DeepInfiltration)))))
D_SoilQflowRelFrac = np.repeat(
    I_SoilQflowFrac,
    subCatchment).reshape((subCatchment, 1))
D_SoilDischarge = np.multiply(D_SoilQflowRelFrac,
                              (D_SoilWater[time] - I_AvailWaterClass))
calculate.update(D_CumNegRain,
                 inflow=0,
                 outflow=(D_InterceptEvap +
                          D_Infiltration +
                          D_DeepInfiltration +
                          D_SurfaceFlow),
                 dt=dt,
                 non_negative=False)
calculate.update(D_CumEvapTranspClass,
                 inflow=D_ActEvapTransp,
                 outflow=D_InterceptEvap,
                 dt=dt)
calculate.update(D_SoilWater,
                 inflow=D_Infiltration,
                 outflow=(D_ActEvapTransp +
                          D_Percolation +
                          D_SoilDischarge),
                 dt=dt)
calculate.update(D_GWArea,
                 inflow=(D_Percolation +
                         D_DeepInfiltration),
                 outflow=(D_GWaDisch +
                          D_WaterEvapIrrigation),
                 dt=dt)
calculate.update(D_EvapTranspClass, inflow=D_WaterEvapIrrigation, dt=dt)

G_GrassAll = np.sum(G_GrassStandingBiomass[time])
G_Grazing = (0
             if G_GrassAll == 0
             else (C_StockingRate *
                   C_DailyIntake *
                   G_GrassStandingBiomass[time] /
                   G_GrassAll))
C_TrampComp = C_DailyTrampFrac * G_Grazing / C_DailyIntake
C_DeathRate = C_StockingRate[time] * C_DailyIntake - G_GrassAll
C_Destoking = min(C_StockingRate[time], C_CattleSale + C_DeathRate)
C_Stocking = 0 * C_StockingRate[time]
calculate.update(C_StockingRate,
                 inflow=C_Stocking,
                 outflow=C_Destoking,
                 dt=dt)

G_GrassFract_Biomass = np.zeros(vegClass)
G_GrowthRate = G_WUE * np.multiply(D_ActEvapTransp, G_GrassFract_Biomass)
G_GrassAll = np.sum(G_GrassStandingBiomass[time])
G_LeafMortality = (G_GrassStandingBiomass[time] * G_GrassMortFrac +
                   G_Grazing * G_TramplingMultiplier)
G_LitterDeposition = G_LeafMortality * G_GrassLitConv
calculate.update(G_GrassStandingBiomass,
                 inflow=G_GrowthRate,
                 outflow=G_Grazing + G_LeafMortality,
                 dt=dt)

G_Incorporation_DecaySurfLit = G_SurfaceLitter[time] * G_SurfLitDecFrac
calculate.update(G_SurfaceLitter,
                 inflow=G_LitterDeposition,
                 outflow=G_Incorporation_DecaySurfLit,
                 dt=dt)

G_FaecesProd = G_Grazing * G_GrazingManConv
G_Incorporation_DecayManure = G_SurfManure[time] * G_SurfManureDecFrac
calculate.update(G_SurfManure,
                 inflow=G_FaecesProd,
                 outflow=G_Incorporation_DecayManure,
                 dt=dt)

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
    where=I_RainDuration!=0))

S_StructureFormation = 0 * np.multiply(S_RelBulkDensity, G_SurfaceCover)
S_RippingSurface = 0

calculate.update(S_RelBulkDensity,
                 inflow=S_SplashErosion +
                        S_StructureFormation +
                        S_RippingSurface,
                 outflow=S_Compaction,
                 dt=dt)

D_ReservoirVol = L_ResrDepth*np.multiply(isL_Lake, I_RelArea)

D_SubCResOutflow = np.add(
    np.multiply(
        np.divide(
            D_SubcResVol[time],
            D_ReservoirVol) > 1,
        np.subtract(D_SubcResVol[time], D_ReservoirVol)),
    np.multiply(np.divide(D_SubcResVol[time], D_ReservoirVol) <= 1,
    np.multiply(D_SubCResUseFrac, D_SubcResVol[time])))
D_RoutingTime = np.divide(
    I_RoutingDistance,
    (np.multiply(I_RivFlowTimeNow,
                 I_RoutVeloc_m_per_s)*3.6*24*I_Tortuosity))
I_ReleaseFrac = np.minimum(
    1,
    np.divide(I_RiverflowDispersalFactor,
              D_RoutingTime,
              out=np.ones(shape=(subCatchment, obsPoint))))
D_TotalStreamInflow = (
    D_SurfaceFlow +
    np.multiply(
        D_GWaDisch,
        (1-D_FracGWtoLake) +
        ARRAY_SUM(D_SoilDischarge,
                  shape=(subCatchment, 1))) +
    np.multiply(D_SubCResOutflow,
                (1-isI_DaminThisStream)))
D_RivLakeSameDay = np.multiply(
    D_RoutingTime>=0,
    np.multiply(D_RoutingTime < 1,
                np.multiply(isD_FeedingIntoLake,
                            np.multiply(D_TotalStreamInflow,
                                        I_ReleaseFrac))))

D_RivInflLake = np.multiply(
    np.multiply(
        I_ReleaseFrac[:, 0].reshape(subCatchment, 1),
        D_TotRiverFlowNoDelay[time][:, 0].reshape(subCatchment, 1)),
    isD_FeedingIntoLake)
D_RivInflLake = np.repeat(D_RivInflLake, 8).reshape(subCatchment, obsPoint)
D_RiverFlowtoLake = (ARRAY_SUM(D_RivLakeSameDay,
                               shape=(obsPoint, 1)) +
                     ARRAY_SUM(D_RivInflLake,
                               shape=(obsPoint, 1)))
D_GWLakeSub = np.multiply(D_FracGWtoLake, D_GWaDisch)
D_GWtoLake = np.sum(D_GWLakeSub)
D_RestartL = isO_Reset * D_CumInflowtoLake[time]/dt
I_ReleaseFract = np.minimum(
    1,
    np.divide(I_RiverflowDispersalFactor,
              D_RoutingTime,
              out=np.ones_like(D_RoutingTime),
              where=D_RoutingTime>0))
D_TotalStreamInflow = (
    (D_SurfaceFlow +
     np.multiply(D_GWaDisch, (1-D_FracGWtoLake)) +
     np.sum(D_SoilDischarge, axis=0).reshape(subCatchment, 1)) +
    np.multiply(D_SubCResOutflow, (1-isI_DaminThisStream)))
D_SurfFlowObsPoint = np.multiply(D_RoutingTime>=1, D_TotalStreamInflow)
D_DirectSurfFkowObsPoint = np.multiply(
    np.multiply(D_RoutingTime>=0, D_RoutingTime<1),
    np.multiply(D_TotalStreamInflow, (1-I_ReleaseFrac)))
D_RiverDirect = np.multiply(
    np.multiply(D_RoutingTime>0, D_RoutingTime<1),
    np.multiply((1-D_FeedingIntoLake_),
                np.multiply(D_TotalStreamInflow, (I_ReleaseFrac))))
D_RivInfLake = np.multiply(
    np.multiply(I_ReleaseFrac, D_TotRiverFlowNoDelay[time]),
    D_FeedingIntoLake_)
D_SurfFlowRiver = np.multiply(D_RoutingTime>1, D_RoutingTime)
D_CurrRivVol = (ARRAY_SUM(D_StreamsSurfQ[time], shape=(1, obsPoint))[0] +
                ARRAY_SUM(D_TotRiverFlowNoDelay[time], shape=(1, obsPoint))[0])
D_RestartR = np.multiply(isO_Reset, D_CumTotRiverFlow)/dt
calculate.update(D_CumInflowtoLake,
                 inflow=D_RiverFlowtoLake + D_GWtoLake,
                 outflow=D_RestartL,
                 dt=dt)
D_RiverDelay = np.multiply(I_ReleaseFrac,
                           np.multiply(D_TotRiverFlowNoDelay[time],
                                       (1-isD_FeedingIntoLake)))

calculate.update(D_CumTotRiverFlow,
                 inflow=D_RiverDelay + D_RiverDirect,
                 outflow=D_RestartR,
                 dt=dt)
calculate.update(D_TotRiverFlowNoDelay,
                 inflow=D_SurfFlowRiver+D_DirectSurfFkowObsPoint,
                 outflow=D_RiverDelay+D_RivInflLake,
                 dt=dt)
D_SurfFlowObsPoint = np.multiply(D_RoutingTime >= 1, D_TotalStreamInflow)
# calculate.update_conveyor(D_StreamsSurfQ, inflow=D_SurfFlowObsPoint, outflow=D_SurfFlowRiver, time=time, dt=dt)

L_LakeTransDef = np.add(
    np.multiply(isL_Lake,
                (-D_ActEvapTransp[LANDCOVER["AF_Kelapa"]])),
    I_PotEvapTransp[LANDCOVER["AF_Kelapa"]])
L_LakeArea = np.multiply(isL_Lake,
                         I_RelArea,
                         out=np.zeros_like(isL_Lake),
                         where=isL_Lake!=1)
L_LakeLevel = np.multiply(
    np.sum(L_LakeArea) > 0,
    L_LakeVol[time] / (1000 * np.sum(L_LakeArea)) + L_LakeBottomElev)
L_Lakelevelexcess = (
    L_LakeLevel -
    (1 - isL_HEPP_Active) * L_LakeElevPreHEPP -
    isL_HEPP_Active * L_LakeOverFlPostHEPP)
L_LakeArea = np.multiply(
    isL_Lake==1,
    np.multiply(isL_Lake, I_RelArea))
L_HEPP_Outflow = (
    L_HEPP_Daily_Dem
    if L_LakeLevel > L_LakeLevelFullHEPP
    else L_HEPP_Daily_Dem * 0.5 * (1 +
                                   max(0,
                                       (L_LakeLevel - L_LakeLevelHalfHEPP) /
                                       (L_LakeLevelFullHEPP -
                                        L_LakeLevelHalfHEPP)))
    if L_LakeLevel > L_LakeLevelNoHEPP else 0)
L_HEPP_OpTimeRel = ((L_CumHEPPUse / L_HEPP_Daily_Dem) / I_Simulation_Time
                    if I_Simulation_Time > 0 and isI_WarmEdUp[time] == 1
                    else 0)
L_EvapLake = min(np.sum(L_LakeTransDef),
                 L_LakeVol[time]) * L_LakeTranspMultiplier
L_RivOutFlow = max(isL_HEPP_Active * L_SanitaryFlow,
                   (L_LakeVol[time]-(
                       L_OutflTrVoPostHEPP
                       * isL_HEPP_Active)-L_OutflTrVolPreHEPP * (
                       1 - isL_HEPP_Active)) * (L_LakeOverFlowFrac) * (
                       1 + L_Lakelevelexcess ** L_LakeOverFlPow))
L_InFlowtoLake =  D_RiverFlowtoLake+D_GWtoLake
L_RestartR = isO_Reset * L_CumRivOutFlow[time] / dt
L_RestartH = isO_Reset * L_CumHEPPUse[time]
L_HEPPWatUseFlow = L_HEPP_Outflow if isL_HEPP_Active==1 else 0
L_RestartE = isO_Reset * L_CumEvapLake[time] / dt

calculate.update(L_CumEvapLake,
                 inflow=L_EvapLake,
                 outflow=L_RestartE,
                 dt=dt)
calculate.update(L_CumHEPPUse,
                 inflow=L_HEPPWatUseFlow,
                 outflow=L_RestartH,
                 dt=dt)
calculate.update(L_CumRivOutFlow,
                 inflow=L_RivOutFlow,
                 outflow=L_RestartR,
                 dt=dt)
calculate.update(L_LakeVol,
                 inflow=L_InFlowtoLake,
                 outflow=L_EvapLake,
                 dt=dt)
O_TotStreamFlow = (O_CumBaseFlow[time] +
                   O_CumSoilQFlow[time] +
                   O_CumSurfQFlow[time])
D_DeltaStockRiver = D_InitRivVol[time] - D_CurrRivVol
D_SurfaceFlowAcc = np.sum(D_SurfaceFlow[time])
O_DeltaGWStock = O_InitGWStock[time] - np.sum(D_GWArea[time])
O_DeltaSoilWStock = O_InitSoilW[time] - np.sum(D_SoilWater[time])
O_ChkAllCatchmAccFor = (-O_CumRain[time] +
                        O_CumIntercE[time] +
                        O_CumTransp[time] +
                        O_TotStreamFlow -
                        O_DeltaGWStock -
                        O_DeltaSoilWStock)
O_DeltaStockLake =D_InitLakeVol[time] - L_LakeVol[time]
O_ChkAllLakeAccFor = (D_CumInflowtoLake[time] -
                      L_CumEvapLake[time] -
                      L_CumRivOutFlow[time] -
                      L_CumHEPPUse[time] +
                      O_DeltaStockLake)
D_CumTotRiverFlowAll = np.sum(D_CumTotRiverFlow, axis=0)[0]
O_ChkAllRiverAccFor = (O_TotStreamFlow -
                       D_CumTotRiverFlowAll -
                       D_CumInflowtoLake[time] +
                       D_DeltaStockRiver)
O_DailyRainSubCtm = np.sum(I_DailyRainAmount, axis=0)
O_FrBaseFlow = (O_CumBaseFlow[time]/O_TotStreamFlow
                if O_TotStreamFlow > 0
                else 0)
O_FrSoilQuickFlow = (O_CumSoilQFlow[time]/O_TotStreamFlow
                     if O_TotStreamFlow > 0
                     else 0)
O_FrSurfQuickFlow = (O_CumSurfQFlow[time]/O_TotStreamFlow
                     if O_TotStreamFlow else 0)
O_RainYesterday = O_RainYest[time] * I_WarmedUp
O_RainHalfDelayed = (np.sum(O_RainYesterday[time]) +
                     np.sum(I_DailyRainAmount)) / 2
O_RelWatAvVegSubc = np.multiply(D_RelWaterAv, I_FracVegClassNow)
O_RelWatAv_Subc = np.divide(
    np.mean(O_RelWatAvVegSubc, axis=0),
    np.sum(I_FracVegClassNow, axis=0),
    out=np.ones(subCatchment),
    where=np.sum(I_FracVegClassNow, axis=0)>0)
O_RelWatAv_Overall = np.mean(O_RelWatAv_Subc)
O_RealWatAv_subc = np.divide(
    np.mean(O_RelWatAvVegSubc, axis=1),
    np.sum(I_FracVegClassNow, axis=1),
    out=np.ones_like(np.mean(O_RelWatAvVegSubc, axis=1)),
    where=np.sum(I_FracVegClassNow, axis=1)!= 0)
O_Rel_ET_Subc = np.divide(
    D_InterceptEvap +
    D_ActEvapTransp,
    I_PotEvapTransp,
    out=np.zeros_like(I_PotEvapTransp),
    where=I_PotEvapTransp!=0)
O_Reset = 1 if I_WarmedUp == 1 or I_WUcorrection == 1 else 0
S_RainAtSoilSurface = I_DailyRainAmount - D_InterceptEvap

O_InitLake = O_Reset * (L_LakeVol[time] - D_InitLakeVol[time])
calculate.update(D_InitLakeVol, O_InitLake, dt=dt)

O_InitRiv = O_Reset * (D_CurrRivVol - D_InitLakeVol[time])
calculate.update(D_InitRivVol, O_InitRiv, dt=dt)

O_BaseFlowAcc = np.sum(D_GWaDisch) * I_WarmedUp
calculate.update(O_CumBaseFlow, O_BaseFlowAcc, dt=dt)

O_CumDeepInfAcc = np.sum(D_DeepInfiltration) * I_WarmedUp
calculate.update(O_CumBaseFlow, O_CumDeepInfAcc, dt=dt)

O_EvapoTransAcc = ((np.sum(D_ActEvapTransp) +
                    np.sum(D_InterceptEvap)) * I_WarmedUp
                   if np.sum(I_PotEvapTransp) > 0 else 0)
calculate.update(O_CumEvapotrans, O_EvapoTransAcc, dt=dt)

O_InfAcc = np.sum(D_Infiltration) * I_WarmedUp
calculate.update(O_CumInfiltration, O_InfAcc, dt=dt)

O_AccET = np.sum(D_InterceptEvap) * I_WarmedUp
calculate.update(O_CumIntercE, O_AccET, dt=dt)

O_PercAcc = np.sum(D_Percolation) * I_WarmedUp
calculate.update(O_CumPercolation, O_PercAcc, dt=dt)

O_RainAcc = np.sum(I_DailyRainAmount) * I_WarmedUp
calculate.update(O_CumRain, O_RainAcc, dt=dt)

O_CumSoilQFlowAcc = np.sum(D_SoilDischarge) * I_WarmedUp
calculate.update(O_CumSoilQFlow, O_CumSoilQFlowAcc, dt=dt)

O_SurfQFlowAcc = np.sum(D_SurfaceFlow) * I_WarmedUp
calculate.update(O_CumSoilQFlow, O_SurfQFlowAcc, dt=dt)

O_TranspAcc = np.sum(D_ActEvapTransp) * I_WarmedUp
calculate.update(O_CumTransp, O_TranspAcc, dt=dt)

O_InitGW = (np.sum(D_GWArea[time]) - O_InitGWStock[time])
calculate.update(O_InitGWStock, O_InitGW, dt=dt)

O_InitSW = O_Reset * (np.sum(D_SoilWater[time]) - O_InitSoilW[time])
calculate.update(O_InitSoilW, O_InitSW, dt=dt)

O_RainToday = np.sum(I_DailyRainAmount, axis=0) * I_WarmedUp
calculate.update(O_RainYest, O_RainToday - O_RainYesterday, dt=dt)
O_LastYearHEPP = ((O_ThisYHepp[time] -
                   O_LastYHepp[time]) /
                  (365 * L_HEPP_Daily_Dem)
                  if O_LastYHepp[time] > 0
                  else 0)
O_BYP = (-O_BestYyHEPP + O_LastYearHEPP
         if O_LastYearHEPP > 0 and O_LastYearHEPP > O_BestYyHEPP
         else 0)
calculate.update(O_BestYyHEPP, O_BYP, dt=dt)
O_StarMYear = np.array([4, 6, 8]).reshape((1, measurePeriod))
O_StartDOY = np.array([1, 1, 1]).reshape((1, measurePeriod))
O_StartMDay = (O_StarMYear-1)*365+1+(O_StartDOY-1)
O_EndMDay = O_StartMDay+O_MPeriodLength
Yearly_Tick = 1 if I_WarmedUp == 1 and time%365 == 0 else 0
I_DebitTime = (I_RFlowData_Year_1_to_4 if I_Simulation_Time <= 1460
               else I_RFlowData_Year_5_to_8 if I_Simulation_Time <= 2920
               else I_RFlowData_Year_9_to_12 if I_Simulation_Time <= 4380
               else I_RFlowData_Year_13_to_16 if I_Simulation_Time <= 5840
               else I_RFlowData_Year_17_to_20 if I_Simulation_Time <= 7300
               else I_RFlowData_Year_21_to_24 if I_Simulation_Time <= 8760
               else I_RFlowData_Year_25_to_28 if I_Simulation_Time <= 10220
               else I_RFlowData_Year_29_to_32)
I_RFlowDataQmecs = I_DebitTime
I_ContrSubcArea = np.multiply(I_RelArea, isI_SubcContr)
I_RFlowdata_mmday = (I_RFlowDataQmecs*24*3600*10^3)/(np.sum(I_ContrSubcArea)*I_TotalArea*10^6) if np.sum(I_ContrSubcArea) > 0 else 0
# O_Ch_inGWStock(t) = O_Ch_inGWStock(t - dt=dt) + (O_Ch_in_GWStockMP) * dt=dt
O_Ch_in_GWStockMP = np.multiply(np.multiply(O_StartMDay < time , O_EndMDay + 1 > time), np.sum(D_GWArea[time]) - O_InitGWStockMP - O_Ch_inGWStock)
calculate.update(O_Ch_inGWStock, O_Ch_in_GWStockMP, dt=dt)

# O_Ch_inWStock(t) = O_Ch_inWStock(t - dt=dt) + (O_Ch_in_WStockMP) * dt=dt

O_Ch_in_WStockMP = np.multiply(np.multiply(O_StartMDay < time , O_EndMDay + 1 > time), np.sum(D_SoilWater[time]) - O_InitSWMP - O_Ch_inWStock)
calculate.update(O_Ch_inWStock, O_Ch_in_WStockMP, dt=dt)

# O_CumBaseFlowMP(t) = O_CumBaseFlowMP(t - dt=dt) + (O_BaseFlowAccMP) * dt=dt
O_BaseFlowAccMP = np.multiply(np.sum(D_GWaDisch), np.multiply(I_Simulation_Time >= O_StartMDay, np.multiply(I_Simulation_Time < O_EndMDay, isI_StillWarmUp == 0)))
calculate.update(O_CumBaseFlowMP, O_BaseFlowAccMP, dt=dt)

#O_CumDebitDataMP(t) = O_CumDebitDataMP[MeasurePeriod](t - dt=dt) + (O_DebitDataAccMP[MeasurePeriod]) * dt=dt
O_DebitDataAccMP = np.multiply(I_RFlowdata_mmday, np.multiply(I_Simulation_Time >= O_StartMDay, np.multiply(I_Simulation_Time < O_EndMDay, isI_StillWarmUp == 0)))
calculate.update(O_CumDebitDataMP, O_DebitDataAccMP, dt=dt)

# O_CumDebitPredMP[MeasurePeriod](t) = O_CumDebitPredMP[MeasurePeriod](t - dt=dt) + (O_DebitPredAccMP[MeasurePeriod]) * dt=dt
O_DebitPredAccMP = np.multiply(D_RiverFlowtoLake, np.multiply(I_Simulation_Time >= O_StartMDay, np.multiply(I_Simulation_Time < O_EndMDay, isI_StillWarmUp == 0)))
# calculate.update(O_CumDebitPredMP, O_DebitPredAccMP, dt=dt) Need check

# O_CumEvapLakeMP[MeasurePeriod](t) = O_CumEvapLakeMP[MeasurePeriod](t - dt=dt) + (O_EvapLakeMP[MeasurePeriod]) * dt=dt
O_EvapLakeMP = np.multiply(L_EvapLake, np.multiply(I_Simulation_Time >= O_StartMDay, np.multiply(I_Simulation_Time < O_EndMDay, isI_StillWarmUp == 0)))
calculate.update(O_CumEvapLakeMP, O_EvapLakeMP, dt=dt)

# O_CumEvapTransMP[MeasurePeriod](t) = O_CumEvapTransMP[MeasurePeriod](t - dt=dt) + (O_Ch_in_EvapoTrans[MeasurePeriod]) * dt=dt
O_Ch_in_EvapoTrans = np.multiply(np.sum(D_CumEvapTranspClass) - O_InitEvapoMP - O_CumEvapTransMP, np.multiply(I_Simulation_Time >= O_StartMDay, np.multiply(I_Simulation_Time < O_EndMDay, isI_StillWarmUp == 0)))
calculate.update(O_CumEvapTransMP, O_Ch_in_EvapoTrans, dt=dt)

# O_CumGWMP[MeasurePeriod](t) = O_CumGWMP[MeasurePeriod](t - dt=dt) + (O_GWAccMP[MeasurePeriod]) * dt=dt
O_GWAccMP = np.multiply(np.sum(D_GWArea[time]), np.multiply(time > O_StartMDay, time < O_EndMDay))
calculate.update(O_CumGWMP, O_GWAccMP, dt=dt)

# O_CumHEPPOutFlowMP[MeasurePeriod](t) = O_CumHEPPOutFlowMP[MeasurePeriod](t - dt=dt) + (O_HEPPOutFlowMP[MeasurePeriod]) * dt=dt
O_HEPPOutFlowMP = np.multiply(L_HEPPWatUseFlow, np.multiply(time > O_StartMDay, time < O_EndMDay))
calculate.update(O_CumHEPPOutFlowMP, O_HEPPOutFlowMP, dt=dt)

# O_CumInfiltrationMP[MeasurePeriod](t) = O_CumInfiltrationMP[MeasurePeriod](t - dt=dt) + (O_InfAccMP[MeasurePeriod]) * dt=dt
O_InfAccMP = np.multiply(np.sum(D_Infiltration), np.multiply(I_Simulation_Time >= O_StartMDay, np.multiply(I_Simulation_Time < O_EndMDay, isI_StillWarmUp == 0)))
calculate.update(O_CumInfiltrationMP, O_InfAccMP, dt=dt)

# O_CumIntercEvapMP[MeasurePeriod](t) = O_CumIntercEvapMP[MeasurePeriod](t - dt=dt) + (O_IntercAccMP[MeasurePeriod]) * dt=dt
O_IntercAccMP = np.multiply(np.sum(D_InterceptEvap), np.multiply(I_Simulation_Time >= O_StartMDay, np.multiply(I_Simulation_Time < O_EndMDay, isI_StillWarmUp == 0)))
calculate.update(O_CumIntercEvapMP, O_IntercAccMP, dt=dt)

# O_CumRainMP[MeasurePeriod](t) = O_CumRainMP[MeasurePeriod](t - dt=dt) + (O_RainAccMP[MeasurePeriod]) * dt=dt
O_RainAccMP = np.multiply(np.sum(I_DailyRainAmount), np.multiply(I_Simulation_Time >= O_StartMDay, np.multiply(I_Simulation_Time < O_EndMDay, isI_StillWarmUp == 0)))
calculate.update(O_CumRainMP, O_RainAccMP, dt=dt)

# O_CumRivInflowtoLakeMP[MeasurePeriod](t) = O_CumRivInflowtoLakeMP[MeasurePeriod](t - dt=dt) + (O_RivInflowtoLakeMP[MeasurePeriod]) * dt=dt
O_RivInflowtoLakeMP = np.multiply(L_InFlowtoLake, np.multiply(I_Simulation_Time >= O_StartMDay, np.multiply(I_Simulation_Time < O_EndMDay, isI_StillWarmUp == 0)))
# calculate.update(O_CumRivInflowtoLakeMP, O_RivInflowtoLakeMP, dt=dt) # Need check

# O_CumRivOutFlowMP[MeasurePeriod](t) = O_CumRivOutFlowMP[MeasurePeriod](t - dt=dt) + (O_RivOutFlowMP[MeasurePeriod]) * dt=dt
O_RivOutFlowMP = np.multiply(L_RivOutFlow, np.multiply(I_Simulation_Time >= O_StartMDay, np.multiply(I_Simulation_Time < O_EndMDay, isI_StillWarmUp == 0)))
# calculate.update(O_CumRivOutFlowMP, O_RivOutFlowMP, dt=dt)

# O_CumSoilQFlowMP[MeasurePeriod](t) = O_CumSoilQFlowMP[MeasurePeriod](t - dt=dt) + (O_SoilQFlowAccMP[MeasurePeriod]) * dt=dt
O_SoilQFlowAccMP = np.multiply(np.sum(D_SoilDischarge), np.multiply(I_Simulation_Time >= O_StartMDay, np.multiply(I_Simulation_Time < O_EndMDay, isI_StillWarmUp == 0)))
# calculate.update(O_CumSoilQFlowMP, O_SoilQFlowAccMP, dt=dt)

# O_CumSoilWMP[MeasurePeriod](t) = O_CumSoilWMP[MeasurePeriod](t - dt=dt) + (O_SoilWAccMP[MeasurePeriod]) * dt=dt
O_SoilWAccMP = np.multiply(np.sum(D_SoilWater[time]), np.multiply(I_Simulation_Time >= O_StartMDay, np.multiply(I_Simulation_Time < O_EndMDay, isI_StillWarmUp == 0)))
# calculate.update(O_CumSoilWMP, O_SoilWAccMP, dt=dt)

# O_CumSurfQFlowMP[MeasurePeriod](t) = O_CumSurfQFlowMP[MeasurePeriod](t - dt=dt) + (O_SurfQFlowAccMP[MeasurePeriod]) * dt=dt
O_SurfQFlowAccMP = np.multiply(np.sum(D_SurfaceFlow), np.multiply(I_Simulation_Time >= O_StartMDay, np.multiply(I_Simulation_Time < O_EndMDay, isI_StillWarmUp == 0)))
# calculate.update(O_CumSurfQFlowMP, O_SurfQFlowAccMP, dt=dt)

# O_CumTranspMP[MeasurePeriod](t) = O_CumTranspMP[MeasurePeriod](t - dt=dt) + (O_TranspAccMP[MeasurePeriod]) * dt=dt
O_TranspAccMP = np.multiply(np.sum(D_ActEvapTransp), np.multiply(I_Simulation_Time >= O_StartMDay, np.multiply(I_Simulation_Time < O_EndMDay, isI_StillWarmUp == 0)))
# calculate.update(O_CumTranspMP, O_TranspAccMP, dt=dt)

# O_DeltaCatchmStMP[MeasurePeriod](t) = O_DeltaCatchmStMP[MeasurePeriod](t - dt=dt) + (O_Ch_in_CatchmStMP[MeasurePeriod]) * dt=dt
O_Ch_in_CatchmStMP = np.multiply(O_Ch_inGWStock[time] + O_Ch_in_GWStockMP + O_Ch_inWStock[time] + O_Ch_in_WStockMP - O_DeltaCatchmStMP, np.multiply(time > O_StartMDay, time < O_EndMDay + 1))
# calculate.update(O_DeltaCatchmStMP, O_Ch_in_CatchmStMP, dt=dt)

# O_Hepp_Kwh_per_dayMP[MeasurePeriod](t) = O_Hepp_Kwh_per_dayMP[MeasurePeriod](t - dt=dt) + (O_Hepp_ElctrProd[MeasurePeriod]) * dt=dt
O_Hepp_ElctrProd = np.multiply(L_HEPP_Kwh /( O_EndMDay-O_StartMDay), np.multiply(I_Simulation_Time >= O_StartMDay, np.multiply(I_Simulation_Time < O_EndMDay, isI_StillWarmUp == 0)))
# calculate.update(O_Hepp_Kwh_per_dayMP, O_Hepp_ElctrProd, dt=dt)

# O_InitEvapoMP[MeasurePeriod](t) = O_InitEvapoMP[MeasurePeriod](t - dt=dt) + (O_Ch_EvapoTran[MeasurePeriod]) * dt=dt
O_Ch_EvapoTran = np.multiply(np.sum(D_CumEvapTranspClass), time == O_StartMDay)
# calculate.update(O_InitEvapoMP, O_Ch_EvapoTran, dt=dt)

# O_InitGWStockMP[MeasurePeriod](t) = O_InitGWStockMP[MeasurePeriod](t - dt=dt) + (O_ChGWMP[MeasurePeriod]) * dt=dt
O_ChGWMP = np.multiply(np.sum(D_GWArea[time]), time == O_StartMDay)
# calculate.update(O_InitGWStockMP, O_ChGWMP, dt=dt)

# O_InitSWMP[MeasurePeriod](t) = O_InitSWMP[MeasurePeriod](t - dt=dt) + (O_ChSoilWMP[MeasurePeriod]) * dt=dt
O_ChSoilWMP = np.multiply(np.sum(D_SoilWater[time]), time == O_StartMDay)
# calculate.update(O_InitSWMP, O_ChSoilWMP, dt=dt)

# O_InitSWMP[MeasurePeriod](t) = O_InitSWMP[MeasurePeriod](t - dt=dt) + (O_ChSoilWMP[MeasurePeriod]) * dt=dt
O_ChSoilWMP =  np.multiply(np.sum(D_SoilWater[time]), time == O_StartMDay)
# calculate.update(O_InitSWMP, O_ChSoilWMP, dt=dt)

# O_LastYHepp(t) = O_LastYHepp(t - dt=dt) + (O_HeppUseF1 - O_HeppUseF2) * dt=dt
O_HeppUseF1 = Yearly_Tick*O_ThisYHepp
O_HeppUseF2 = Yearly_Tick*O_LastYHepp
# calculate.update(O_LastYHepp, O_HeppUseF1 - O_HeppUseF2, dt=dt)

# O_ThisYHepp(t) = O_ThisYHepp(t - dt=dt) + (O_HeppUseF0 - O_HeppUseF1) * dt=dt
O_HeppUseF0 = Yearly_Tick * L_CumHEPPUse
O_HeppUseF1 = Yearly_Tick * O_ThisYHepp
# calculate.update(O_ThisYHepp, O_HeppUseF0 - O_HeppUseF1, dt=dt)

# O_WorstYHEPP(t) = O_WorstYHEPP(t - dt=dt) + (O_WYP) * dt=dt
O_WYP = -O_WorstYHEPP+O_LastYearHEPP if O_LastYearHEPP>0 and O_LastYearHEPP< O_WorstYHEPP else 0
# calculate.update(O_WorstYHEPP, O_WYP, dt=dt)

# O_YearSim(t) = O_YearSim(t - dt=dt) + (Yearly_Tick) * dt=dt
calculate.update(O_YearSim, Yearly_Tick, dt=dt)

O_CumET_LandMP= O_CumIntercEvapMP + O_CumTranspMP
O_CurrentETall = np.sum(D_ActEvapTransp)
O_RelOpTimeHEPPMP = (O_CumHEPPOutFlowMP[time]/L_HEPP_Daily_Dem)/(O_EndMDay - O_StartMDay )
O_SoilWaterTot = np.sum(D_SoilWater[time])

