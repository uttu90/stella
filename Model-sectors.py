__author__ = 'TuHV'

import numpy as np
from pylab import *
from Read_Input import *

# Constants

# 0. RAINFALL
I_UseSpatVarRain_ = 0.0
I_RainMultiplier = 1.0
I_RainCycle_ = 0.0
I_Rain_IntensMean = 10.0
I_Rain_IntensCoefVar = 0.30
II_Rain_GenSeed = 200.0

# 1. SOIL AND PLANT WATER

# Infiltration, mm day-1
I_MaxInf = 700
I_MaxInfSSoil = 200
I_PowerInfiltRed = 3.5

# Water Available for Plant, mm
I_SoilPropConst = 0.0
I_AvailWaterConst = 300
I_SoilSatMinFCConst = 100

# Ground Water, mm
I_InitRelGW = 1.0
I_GWRelFracConst_ = 0.0
I_MaxDymGWConst = 100.0
I_GWRelFracConst = 0.01

# Rainfall Interception, mm
I_InterceptEffectionTransp = 0.1
I_RainIntercDripRt = 10.0
I_RainMaxIntDripDur = 0.5

# Percolation
I_PercFracMultiplier = 0.05

# Initial Soil Water
I_InitRelSoil = 1.0

# Evapotranspiration
I_EvapotransMethod = 1.0

# Soil Quick Flow
I_SoiQflowFrac = 0.10

# 2. LAKE
# Lake in Subcatchment
Lake_in_Subcatchment_ = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Lake Outflows
L_LakeBottomElev = 160.0
L_LakeElevPreHEPP = 362.3
L_LakeOverFIPostHEPP = 362.6
L_LakeLevelFullHEPP = 362.3
L_LakeLevelHalfHEPP = 361.8
L_LakeLevelNoHEPP = 359.5
L_FoodTresh = 363.0
L_QmecsHEPP = 47.1
L_QmecsScanFlow = 3.0
L_LakeOverFlowFrac = 0.1
L_LakeOverFIPow = 4.0
L_m3_per_kwh = 1.584
L_ResrDepth = 10000.0

L_HEPP_Active_ = 0.0
L_LakeTransMultiplier = 1.0
D_SubCResUseFrac=[0.01, 0.005, 0.02, 0.03, 0.205, 0.325, 0.360, 0.335, 0.315, 0.195, 0.020, 0.010, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015]

# 3.SUBCATCHMENT BALANCE

O_CumRainMP = [0.0, 0.0, 0.0]
O_CumIntercEvapMP = [0.0, 0.0, 0.0]
O_CumTranspMP = [0.0, 0.0, 0.0]
O_CumET_LandMP = [0.0, 0.0, 0.0]
O_CumEvapTransMP = [0.0, 0.0, 0.0]
O_CumSurfQFlowMP = [0.0, 0.0, 0.0]
O_CumInfiltrationMP = [0.0, 0.0, 0.0]
O_CumSoilQFlowMP = [0.0, 0.0, 0.0]
O_CumBaseFlowMP = [0.0, 0.0, 0.0]
O_CumDebitPredMP = [0.0, 0.0, 0.0]
O_CumDebitDataMP = [0.0, 0.0, 0.0]

# 4. SOIL STRUCTURE DYNAMIC
S_TrampMax = 100.0

# 5. GRASS & CATTLE

C_DailyTrampFac = 1.0
C_CattleSale = 0.0
C_DailyIntake = 1.0
G_GrazingManCov = 0.1
G_SurfLitDecFrac = 0.03
G_SurfManureDecFrac = 0.01
G_GrassLitConv = 1.0
G_GrassMortFrac = 0.03
G_WUE = 0.04

G_TramplingMultiplier = 0.0

# 5. LAKE/HEPP
O_CumRivInflowtoLakeMP = [0.0, 0.0, 0.0]
O_CumRivOutFlowMP = [0.0, 0.0, 0.0]
O_FrBaseFlow = 0.0
O_FrSoilQuickFlow = 0.0
O_FrSurfQuickFlow = 0.0
O_Hepp_Kwh_per_dayMP = [0.0, 0.0, 0.0]
O_CumHEPPOutFlowMP = [0.0, 0.0, 0.0]
O_RelOpTimeHEPPMP = [0.0, 0.0, 0.0]


# Translate sector



