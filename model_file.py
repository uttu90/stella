import numpy as np


def update(value, diff, delta):
    value.append(value[-1] + diff * delta)

VegClass = 20
Subcatchment = 20

# Initial
# Input time
I_InputDataYears = [0, 5, 10, 15]
I_RainMultiplier = 1
I_RainYearStart = 0
I_Rain_GenSeed = 200
I_Rain_IntensCoefVar = 0.3
I_Rain_IntensMean = 10

# Cattle
C_StockingRate = [1]
C_DailyIntake = 1
C_DailyTrampFrac = 1

# Check and Balance
D_InitLakeVol = [0]
D_InitRivVol = [0]
O_CumBaseFlow = [0]
O_CumDeepInfilt = [0]
O_CumEvapotrans = [0]
O_CumInfiltration = [0]
O_CumIntercE = [0]
O_CumPercolation = [0]
O_CumRain = [0]
O_CumSoilQFlow = [0]
O_CumSoilQFlow_Subca_1 = [0]
O_CumSurfQFlow = [0]
O_CumTransp = [0]
O_InitGWStock = [0]
O_InitSoilW = [0]
O_RainYest = [0]

# Grass
G_GrassStandingBiomass = [1]
G_SurfaceLitter = [0]
G_SurfMaunre = [0]

# I Evapotransp
I_GWRelFrac = [0, 0, 0, 0]

# I_Rainfall
I_WarmEdUp = [0]

# Lake
L_CumEvapLake = [0]
L_CumHEPPUse = [0]
L_CumRivOutFlow = [0]
L_LakeVol = [0] # L_OutflTrVoPostHEPP*L_HEPP_Active?+(1-L_HEPP_Active?)*L_OutflTrVolPreHEPP


# Simulation
I_Simulation_Time  = 1
dt = 0.25
# Cattle
C_CattleSale = 0
C_DeathRate = C_StockingRate[-1] * C_DailyIntake - G_GrassAll
C_TrampComp = C_DailyTrampFrac * G_Grazing/C_DailyIntake
C_Stocking = 0
C_Destocking = min(C_StockingRate, C_CattleSale + C_DeathRate)
update(C_StockingRate, C_Stocking - C_Destocking, dt)

# Checks and Balance
O_TotStreamFlow = O_CumBaseFlow[-1] + O_CumSoilQFlow[-1] + O_CumSurfQFlow[-1]
D_DeltaStockRiver = D_InitRivVol[-1] - D_CurrRivVol
D_SurfaceFlowAcc = np.sum(D_SurfaceFlow[-1])
O_DeltaGWStock = O_InitGWStock[-1] - np.sum(D_GWArea)
O_DeltaSoilStock = O_InitSoilW[-1] - np.sum(D_SoilWater)
O_ChkAllCatchmAccFor = -O_CumRain[-1] + O_CumIntercE[-1] + O_CumTransp[-1] + O_TotStreamFlow - O_DeltaGWStock - O_DeltaSoilWStock
O_ChkAllLakeAccFor = D_CumInflowtoLake[-1] - L_CumEvapLake[-1] - L_CumRivOutFlow[-1] - L_CumHEPPUSe[-1] + O_DeltaStockLake[-1]
O_ChkAllRiverAccFor = O_TotStreamFlow -D_CumTotRiverFlowAll - D_CumInflowtoLake + D_DeltaStockRiver
O_DailyRainSubCtm = np.sum(I_DailyRainAmount, axis=0)
O_DeltaStockLake =D_InitLakeVol[-1] - L_LakeVol[-1]
O_FrBaseFlow = O_CumBaseFlow[-1]/O_TotStreamFlow if O_TotStreamFlow > 0 else 0
O_FrSoilQuickFlow = O_CumSoilQFlow[-1]/O_TotStreamFlow if O_TotStreamFlow > 0 else 0
O_FrSurfQuickFlow = O_CumSurfQFlow[-1]/O_TotStreamFlow if O_TotStreamFlow else 0
O_RainHalfDelayed = (np.sum(O_RainYesterday[-1]) + np.sum(I_DailyRainAmount))/2
O_RelWatAvVegSubc = np.multiply(D_RelQaterAv, I_FracVegClassNow)
O_RelWatAv_Overall = np.mean(O_RelWatAv_Subc)
O_RealWatAv_subc = np.divide(np.mean(O_RelWatAvVegSubc, axis=1), np.sum(I_FracVegClassNow, axis=1),
                             out=np.ones_like(np.mean(O_RelWatAvVegSubc, axis=1)),
                             where=np.sum(I_FracVegClassNow, axis=1)!= 0)
O_Rel_ET_Subc = np.divide(D_InterceptEvap + D_ActEvapTransp, I_PotEvapTransp_,
                          out=np.(I_PotEvapTransp),
                          where=I_PotEvapTransp_!=0)
O_Reset = 1 if I_Warmedup == 1 or I_WUcorrection == 1 else 0
S_RainAtSoilSurface = I_DailyRainAmount - D_InterceptEvap

O_InitLake = O_Reset * (L_LakeVol[-1] - D_InitLakeVol[-1])
update(D_InitLakeVol, O_InitLake, dt)

O_InitRiv = O_Reset * (D_CurrRivVol - D_InitLakeVol[-1])
update(D_InitRivVol, O_InitRiv, dt)

O_BaseFlowAcc = np.sum(D_GWaDisch) * I_WarmEdUp
update(O_CumBaseFlow, O_BaseFlowAcc, dt)

O_CumDeepInfAcc = np.sum(D_DeepInfiltration) * I_WarmEdUp
update(O_CumBaseFlow, O_CumDeepInfAcc, dt)

O_EvapoTransAcc = ((np.sum(D_ActEvapTransp) + np.sum(D_InterceptEvap)) * I_WarmEdUp
                   if np.sum(I_PotEvapTransp_) > 0 else 0)
update(O_CumEvapotrans, O_EvapoTransAcc, dt)

O_InfAcc = np.sum(D_Infiltration) * I_WarmEdUp
update(O_CumInfiltration, O_InfAcc, dt)

O_AccET = np.sum(D_InterceptEvap) * I_WarmEdUp
update(O_CumIntercE, O_AccET, dt)

O_PercAcc = np.sum(D_Percolation) * I_WarmEdUp
update(O_CumPercolation, O_PercAcc, dt)

O_RainAcc = np.sum(I_DailyRainAmount) * I_WarmEdUp
update(O_CumRain, O_RainAcc, dt)

O_CumSoilQFlowAcc = np.sum(D_SoilDischarge) * I_WarmEdUp
update(O_CumSoilQFlow, O_CumSoilQFlowAcc, dt)

O_SurfQFlowAcc = np.sum(D_SurfaceFlow) * I_WarmEdUp
update(O_CumSoilQFlow, O_SurfQFlowAcc, dt)

O_TranspAcc = np.sum(D_ActEvapTransp) * I_WarmEdUp
update(O_CumTransp, O_TranspAcc, dt)

O_InitGW = (np.sum(D_GWArea) - O_InitGWStock[-1])
update(O_InitGWStock, O_InitGW, dt)

O_InitSW = O_Reset * (np.sum(D_SoilWater) - O_InitSoilW[-1])
update(O_InitSoilW, O_InitSW, dt)

O_RainToday = np.sum(I_DailyRainAmount, axis=0) * I_WarmEdUp
O_RainYesterday = O_RainYest[-1] * I_WarmEdUp
update(O_RainYest, O_RainToday - O_RainYesterday, dt)

# Grass
G_GrowthRate = G_GWUE * np.multiply(D_ActEvapTransp, G_GrassFract_Biomass)
G_Grazing = 0 if G_GrassAll == 0 else C_StockingRate[-1] * C_DailyIntake * G_GrassStandingBiomass[-1]/G_GrassAll
G_LeafMortality = G_GrassStandingBiomass[-1] * G_GrassMortFrac + G_Grazing * G_TramplingMultiplier
update(G_GrassStandingBiomass, G_GrowthRate - G_Grazing - G_LeafMortality, dt)

G_LitterDeposition = G_LeafMortality * G_GrassLitCov
G_Incorporation_DecaySurfLit = G_SurfaceLitter[-1] * G_SurfLitDecFrac
update(G_SurfaceLitter, G_LitterDeposition - G_Incorporation_DecaySurfLit, dt)

G_FaecesProd = G_Grazing * G_GrazingManConv
G_Incorporation_DecayManure = G_SurfMaunre[-1] * G_SurfManunreDecFrac
update(G_SurfMaunre, G_FaecesProd - G_Incorporation_DecayManure, dt)

G_GrassAll = np.sum(G_GrassStandingBiomass)
G_GrassFract_Biomass = np.(VegClass) # Check for input
G_GrassLitConv = 1
G_GrassMortFrac = 0.03
G_GrazingManConv = 0.1
G_SurfaceCover = G_GrassStandingBiomass[-1] + G_SurfaceLitter[-1] + G_SurfMaunre[-1]
G_SurfLitDecFrac = 0.03
G_SurfManureDecFrac = 0.01
G_TramplingMultiplier = 0
G_WUE = 0.04

# I Daily Evapotranspiration
I_Daily_Evapotrans = I_RainDoY[I_Simulation_Time ]

# I Land cover
D_FeedingIntoLake

I_Flag1 = 1 if I_Simulation_Time  < I_InputDataYears[1] * 365 else 0
I_Flag2 = 1 if I_Simulation_Time  < I_InputDataYears[2] and I_Flag1 ==0 else 0
if I_Flag1 == 1:
    I_AvailWatClassNow = (I_PlantAvWatSub1 +
                          (I_PlantAvWatSub2-I_PlantAvWatSub1) *
                          (int(I_Simulation_Time /365) -
                           I_InputDataYears[0])/(I_InputDataYears[1] - I_InputDataYears[0]))
    I_BD_BDRefVegNow = (I_TopSoilBD_BDRef1 +
                        (I_TopSoilBD_BDRef2-I_TopSoilBD_BDRef1) *
                        (int(I_Simulation_Time /365) -
                         I_InputDataYears[0])/(I_InputDataYears[1] - I_InputDataYears[0]))
elif I_Flag2 == 1:
    I_AvailWatClassNow = (I_PlantAvWatSub2 +
                          (I_PlantAvWatSub3 - I_PlantAvWatSub2) *
                          (int(I_Simulation_Time  / 365) -
                           I_InputDataYears[1]) / (I_InputDataYears[2] - I_InputDataYears[1]))
    I_BD_BDRefVegNow = (I_TopSoilBD_BDRef2 +
                        (I_TopSoilBD_BDRef3-I_TopSoilBD_BDRef4) *
                        (int(I_Simulation_Time /365) -
                         I_InputDataYears[1])/(I_InputDataYears[2] - I_InputDataYears[2]))
else:
    I_AvailWatClassNow = (I_PlantAvWatSub3 +
                          (I_PlantAvWatSub4 - I_PlantAvWatSub3) *
                          (int(I_Simulation_Time /365)-I_InputDataYears[2])/(I_InputDataYears[3]-I_InputDataYears[2]))
    I_BD_BDRefVegNow = (I_TopSoilBD_BDRef3 +
                        (I_TopSoilBD_BDRef4-I_TopSoilBD_BDRef3) *
                        (int(I_Simulation_Time /365)-I_InputDataYears[2])/(I_InputDataYears[3]-I_InputDataYears[2]))

I_FracVegClass1 = I_Frac1 # Reading table from Excel
I_FracVegClass2 = I_Frac2
I_FracVegClass3 = I_Flag3
I_FracVegClass4 = I_Frac4

D_FeedingIntoLake = np.ones(Subcatchment)
I_RoutingDistance = np.zeros(Subcatchment)
I_Area = np.zeros(Subcatchment)
I_TotalArea = np.sum(I_Area)
I_RelArea = I_Area/I_TotalArea
I_FracVegClassNow = np.(I_FracVegClass1)
for i in range(Subcatchment):
    if I_RelArea[i] > 0:
        if I_Flag1 == 1:
            I_FracVegClassNow[:][i] = ((I_FracVegClass1[:][i] +
                                        (I_FracVegClass2[:][i] - I_FracVegClass1[:][i]) *
                                        (int(I_Simulation_Time /365)-I_InputDataYears[0])/
                                        (I_InputDataYears[1]-I_InputDataYears[0]))/
                                       np.sum(I_FracVegClass1, axis=1))
        elif I_Flag2 == 1:
            I_FracVegClassNow[:][i] = ((I_FracVegClass2[:][i] +
                                        (I_FracVegClass3[:][i] - I_FracVegClass2[:][i])*
                                        (int(I_Simulation_Time /365) - I_InputDataYears[1])/
                                        (I_InputDataYears[2]-I_InputDataYears[1]))/np.sum(I_FracVegClass2, axis=1))
        else:
            I_FracVegClassNow[:][i] = ((I_FracVegClass3[:][i] +
                                        (I_FracVegClass4[:][i] - I_FracVegClass3[:][i])*
                                        (int(I_Simulation_Time /365) - I_InputDataYears[2])/
                                        (I_InputDataYears[3]-I_InputDataYears[2]))/np.sum(I_FracVegClass3, axis=1))
    else:
        I_FracVegClassNow[:][i] = 0

I_FracVegClassSum1 = np.sum(I_FracVegClass1)
I_FracVegClassSum2 = np.sum(I_FracVegClass2)
I_FracVegClassSum3 = np.sum(I_FracVegClass3)
I_FracVegClassSum4 = np.sum(I_FracVegClass4)
I_FracVegClassSumNow = np.sum(I_FracVegClassNow)

I_GWRelFrac = [np.zeros(Subcatchment) for i in range(0, 4)]
I_MaxDynGWSub = [np.zeros(Subcatchment) for i in range(0, 4)]
I_PWPSub = [np.zeros(Subcatchment) for i in range(0, 4)]
I_RivFlowTime = [np.zeros(Subcatchment) for i in range(0, 4)]
I_SoilSatminFCSub = [np.zeros(Subcatchment) for i in range(0, 4)]
D_FeedingIntoLake = np.zeros(Subcatchment) # Get from GRAPH
def FracProcess(fract, flag_1, flag_2, time, time_stage):
    if flag_1 == 1:
        stage = 0
    elif flag_2 == 1:
        stage = 1
    else:
        stage = 2
    rel = (fract[stage] +
           (fract[stage + 1] - fract[stage]) *
           (int(time / 365) - time_stage[stage]) /
           (time_stage[stage + 1] - time_stage[stage]))
    return rel

I_GWRelFracNow = FracProcess(I_GWRelFrac, I_Flag1, I_Flag2, I_Simulation_Time , I_InputDataYears)
I_MaxDynGWSubNow = FracProcess(I_MaxDynGWSub, I_Flag1, I_Flag2, I_Simulation_Time , I_InputDataYears)
I_PWPSubNow = FracProcess(I_PWPSub, I_Flag1, I_Flag2, I_Simulation_Time , I_InputDataYears)
I_RivFlowTimeNow = FracProcess(I_RivFlowTime, I_Flag1, I_Flag2, I_Simulation_Time , I_InputDataYears)
I_SoilSatminFCSubNow = FracProcess(I_RivFlowTime, I_Flag1, I_Flag2, I_Simulation_Time , I_InputDataYears)

# I_Land Cover
I_PlantAvWatSub = [np.zeros(Subcatchment) for i in range(0, 4)]
I_PlantAvWatSubNow = FracProcess(I_PlantAvWatSub, I_Flag1, I_Flag2, I_Simulation_Time , I_InputDataYears)
I_TopSoilBD_BDRef = [np.zeros(Subcatchment) for i in range(0, 4)]
I_BD_BDRefVegNow = FracProcess(I_TopSoilBD_BDRef, I_Flag1, I_Flag2, I_Simulation_Time , I_InputDataYears)

# I_Rainfall
I_Warmedup = 1 if I_WarmEdUp[-1] == I_Simulation_Time  else 0
update(I_WarmEdUp, I_Warmedup, dt)
I_CaDOYStart = 0
I_DailyRain = I_DailyRainYear[I_Simulation_Time ] * I_RainMultiplier
I_DailyRainAmount = np.multiply(np.multiply(I_RainPerday, I_FracVegClassNow), I_RelArea)
I_RainCycle = 0
I_RainDoY = I_Simulation_Time  if I_RainCycle == 0 else 1 + (I_Simulation_Time  % 365)
I_RainDuration = ((I_RainPerDay/I_Rain_IntensMean) *
                  min(max(0,1 - 3 * I_Rain_IntensCoefVar,
                          np.normal(1, I_Rain_IntensCoefVar, I_Rain_GenSeed + 11250)),
                      1 + 3 * I_Rain_IntensCoefVar))
I_RainPerDay = I_SpatRainTime if I_UseSpatVarRain == 1 else I_DailyRain

I_Simulation_Time = TIME + I_CaDOYStart + 365 * I_RainYearStart - I_WarmEdUp * (I_WarmUpTime + 1)
I_SpatRainTime = I_SpatRain[TIME]
I_StillWarmUp = 1 if time <= I_WarmUpTime + 1 else 0
I_UseSpatVarRain = 0
I_WarmUpTime = 730
I_WUCorrection = 1 if time == (I_WarmUpTime + 1) else 0

# I SubcatchmParam
if I_SoilPropConst == 1:
    I_AvailWaterClass = I_AvailWaterConst * np.multiply(I_FracVegClassNow, I_RelArea)
else:
    I_AvailWaterClass = np.multiply(np.multiply(I_AvailWatClassNow, I_FracVegClassNow), I_RelArea)
I_EvapotransMethod = np.zeros(Subcatchment)
I_EvapotransMethod = 1
I_GWRelFrac = I_GWRelFracConst if I_GWRelFracConst_ == 1 else I_MaxDynGWSubNow
I_MaxDynGWArea = np.multiply(I_MaxDynGWact, I_RelArea)
I_MaxDynGWConst = 100
I_MaxInf = 700

I_MaxInfArea = I_MaxInf * np.multiply(I_RelArea, I_FracVegClassNow) * np.divide(0.7, I_BD_BDRefVegNow, out=np.zeros_like(I_BD_BDRefVegNow), where=I_BD_BDRefVegNow!=0)
I_MaxInfSSoil = 150
I_MaxInfSubSAreaClass = I_MaxInfSSoil * np.multiply(I_RelArea, I_FracVegClassNow)
I_MoY = 0 if I_RainDoY == 0 else int(I_TimeEvap / 30.5) + 1
I_PercFracMultiplier = 0.05
if I_EvapotransMethod:
    I_PotEvapTransp_ = I_Evapotrans * np.multily(np.multiply(I_MultiplierEvapoTrans, I_FracVegClassNow), I_RelArea)
else:
    I_PotEvapTransp_ = np.multiply(np.multiply(I_Daily_Evapotrans, I_MultiplierEvapoTrans), I_RelArea)
I_PowerInfiltRed = 3.5
I_RiverflowDispersalFactor = 0.6
I_RoutVeloc_m_per_s = 0.55
I_SoilPropConst_ = 0

if I_SoilPropConst_ == 1:
    I_SoilSatClass = (I_AvailWaterConst + I_SoilSatMinFCConst) * np.multiply(I_FracVegClassNow, I_RelArea)
else:
    I_SoilSatClass = np.multiply(np.multiply(np.add(I_SoilSatminFCSubNow, I_AvailWatClassNow), I_FracVegClassNow), I_RelArea)
I_SoilSatMinFCConst = 100
I_SurfLossFrac = 0
if I_RainDoY == 0:
    I_TimeEvap = 0
elif I_RainDoY % 365 == 0:
    I_TimeEvap = I_RainDoY % 365
I_Tortuosity = 0.6
L_Lake_ = np.zeros(Subcatchment)
L_LakeTranspMultiplier = 1
L_ResrDepth = 10000

# Lake

L_EvapLake = min(np.sum(L_LakeTransDef), L_LakeVol[-1]) *L_LakeTranspMultiplier
L_RestartE = O_Reset * L_CumEvapLake[-1]/dt
update(L_CumEvapLake, L_EvapLake - L_RestartE, dt)

L_RivOutFlow = max(L_HEPP_Active * L_SanitaryFlow, (L_LakeVol[-1] - L_OutflTrVoPostHEPP  *L_HEPP_Active) - L_OutflTrVolPreHEPP * (1-L_HEPP_Active) * L_LakeOverFlowFrac * (1 + L_Lakelevelexcess^L_LakeOverFlPow))
L_RestartR = O_Reset * L_CumRivOutFlow/dt

update(L_CumRivOutFlow, L_RivOutFlow - L_RestartR, dt)

L_InFlowtoLake =  D_RiverFlowtoLake+D_GWtoLake
L_HEPPWatUseFlow = L_HEPP_Outflow if L_HEPP_Active == 1 else 0
update(L_LakeVol, L_InFlowtoLake - L_EvapLake - L_RivOutFlow - L_HEPPWatUseFlow, dt)

L_FloodingCurrent = 1 if L_LakeLevel>L_FloodTresh else 0
L_FloodTresh = 363
L_HEPP_Active = 1
L_HEPP_Daily_Dem = L_QmecsHEPP * 3600 * 24 / I_TotalArea * 10^-3
L_HEPP_Kwh = 1000 * I_TotalArea * L_HEPPWatUseFlow / L_m3_per_kwh
if (I_Simulation_Time > 0 and I_WarmEdUp == 1):
    L_HEPP_OpTimeRel = ( L_CumHEPPUse/L_HEPP_Daily_Dem)/I_Simulation_Time
elif L_LakeLevel>L_LakeLevelNoHEPP:
    L_HEPP_OpTimeRel = L_HEPP_Daily_Dem * 0.5 * (1 + max(0, (L_LakeLevel - L_LakeLevelHalfHEPP) / (L_LakeLevelFullHEPP - L_LakeLevelHalfHEPP)))
else:
    L_HEPP_OpTimeRel = 0
L_LakeArea = np.multiply(L_Lake_, I_RelArea, out=np.zeros_like(L_Lake_), where=L_Lake_==1)
L_LakeBottomElev = 160
L_LakeElevPreHEPP = 362.3
L_LakeLevel = L_LakeVol/(1000 * np.sum(L_LakeArea)) + L_LakeBottomElev if np.sum(L_LakeArea) > 0 else 0
L_Lakelevelexcess = L_LakeLevel-(1-L_HEPP_Active)*L_LakeElevPreHEPP-L_HEPP_Active*L_LakeOverFlPostHEPP
L_LakeLevelFullHEPP = 362.3
L_LakeLevelHalfHEPP = 361.8
L_LakeLevelNoHEPP = 359.5
L_LakeOverFlowFrac = 0.1
L_LakeOverFlPostHEPP = 362.6
L_LakeOverFlPow = 4
L_LakeTransDef = np.multiply(L_Lake_, D_ActEvapTransp) + I_PotEvapTransp_
L_m3_per_kwh = 1.584
L_OutflTrVolPreHEPP = 1000*(L_LakeElevPreHEPP-L_LakeBottomElev)*np.sum(L_LakeArea)
L_OutflTrVoPostHEPP = 1000*(L_LakeOverFlPostHEPP-L_LakeBottomElev)*np.sum(L_LakeArea)
L_QmecsHEPP = 47.1
L_QmecsSanFlow = 3
L_SanitaryFlow = L_QmecsSanFlow* 3600*24/I_TotalArea*10^-3

# Measurement periods

# O_BestYyHEPP(t) = O_BestYyHEPP(t - dt) + (O_BYP) * dt
O_BYP = -O_BestYyHEPP+O_LastYearHEPP if O_LastYearHEPP>0 and O_LastYearHEPP>O_BestYyHEPP else 0
update(O_BestYyHEPP, O_BYP, dt)

# O_Ch_inGWStock(t) = O_Ch_inGWStock(t - dt) + (O_Ch_in_GWStockMP) * dt
O_Ch_in_GWStockMP = (np.sum(D_GWArea) - O_InitGWStockMP) -  O_Ch_inGWStock if time > O_StartMDay and time < O_EndMDay+1 else 0
update(O_Ch_inGWStock, O_Ch_in_GWStockMP, dt)

# O_Ch_inWStock(t) = O_Ch_inWStock(t - dt) + (O_Ch_in_WStockMP) * dt

O_Ch_in_WStockMP = (np.sum(D_SoilWater) - O_InitSWMP) - O_Ch_inWStock if time > O_StartMDay and time < O_EndMDay + 1 else 0
update(O_Ch_inWStock, O_Ch_in_WStockMP, dt)

# O_CumBaseFlowMP(t) = O_CumBaseFlowMP(t - dt) + (O_BaseFlowAccMP) * dt
O_BaseFlowAccMP = np.sum(D_GWaDisch) if I_Simulation_Time >= O_StartMDay and I_Simulation_Time < O_EndMDay and I_StillWarmUp == 0 else 0
update(O_CumBaseFlowMP, O_BaseFlowAccMP, dt)

#O_CumDebitDataMP(t) = O_CumDebitDataMP[MeasurePeriod](t - dt) + (O_DebitDataAccMP[MeasurePeriod]) * dt
O_DebitDataAccMP = I_RFlowdata_mmday if I_Simulation_Time >= O_StartMDay and I_Simulation_Time < O_EndMDay and I_StillWarmUp == 0  else 0
update(O_CumDebitDataMP, O_DebitDataAccMP, dt)

# O_CumDebitPredMP[MeasurePeriod](t) = O_CumDebitPredMP[MeasurePeriod](t - dt) + (O_DebitPredAccMP[MeasurePeriod]) * dt
O_DebitPredAccMP = D_RiverFlowtoLake if I_Simulation_Time >= O_StartMDay and I_Simulation_Time < O_EndMDay and I_StillWarmUp == 0 else 0
update(O_CumDebitPredMP, O_DebitPredAccMP, dt)

# O_CumEvapLakeMP[MeasurePeriod](t) = O_CumEvapLakeMP[MeasurePeriod](t - dt) + (O_EvapLakeMP[MeasurePeriod]) * dt
O_EvapLakeMP = L_EvapLake if I_Simulation_Time >= O_StartMDay and I_Simulation_Time < O_EndMDay and I_StillWarmUp == 0 else 0
update(O_CumEvapLakeMP, O_EvapLakeMP, dt)

# O_CumEvapTransMP[MeasurePeriod](t) = O_CumEvapTransMP[MeasurePeriod](t - dt) + (O_Ch_in_EvapoTrans[MeasurePeriod]) * dt
O_Ch_in_EvapoTrans = np.sum(D_CumEvapTranspClass) - O_InitEvapoMP-O_CumEvapTransMP if I_Simulation_Time >= O_StartMDay and I_Simulation_Time < O_EndMDay and I_StillWarmUp == 0  else 0
update(O_CumEvapTransMP, O_Ch_in_EvapoTrans, dt)

# O_CumGWMP[MeasurePeriod](t) = O_CumGWMP[MeasurePeriod](t - dt) + (O_GWAccMP[MeasurePeriod]) * dt
O_GWAccMP = np.sum(D_GWArea)  if time > O_StartMDay and time < O_EndMDay else 0
update(O_CumGWMP, O_GWAccMP, dt)

# O_CumHEPPOutFlowMP[MeasurePeriod](t) = O_CumHEPPOutFlowMP[MeasurePeriod](t - dt) + (O_HEPPOutFlowMP[MeasurePeriod]) * dt
O_HEPPOutFlowMP = L_HEPPWatUseFlow if time > O_StartMDay and time < O_EndMDay else 0
update(O_CumHEPPOutFlowMP, O_HEPPOutFlowMP, dt)

# O_CumInfiltrationMP[MeasurePeriod](t) = O_CumInfiltrationMP[MeasurePeriod](t - dt) + (O_InfAccMP[MeasurePeriod]) * dt
O_InfAccMP = np.sum(D_Infiltration) if I_Simulation_Time >= O_StartMDay and I_Simulation_Time < O_EndMDay and I_StillWarmUp == 0 else 0
update(O_CumInfiltrationMP, O_InfAccMP, dt)

# O_CumIntercEvapMP[MeasurePeriod](t) = O_CumIntercEvapMP[MeasurePeriod](t - dt) + (O_IntercAccMP[MeasurePeriod]) * dt
O_IntercAccMP = np.sum(D_InterceptEvap) if I_Simulation_Time >= O_StartMDay and I_Simulation_Time < O_EndMDay and I_StillWarmUp == 0 else 0
update(O_CumIntercEvapMP, O_IntercAccMP, dt)

# O_CumRainMP[MeasurePeriod](t) = O_CumRainMP[MeasurePeriod](t - dt) + (O_RainAccMP[MeasurePeriod]) * dt
O_RainAccMP = np.sum(I_DailyRainAmount) if I_Simulation_Time >= O_StartMDay and I_Simulation_Time < O_EndMDay and I_StillWarmUp == 0 else 0
update(O_CumRainMP, O_RainAccMP, dt)

# O_CumRivInflowtoLakeMP[MeasurePeriod](t) = O_CumRivInflowtoLakeMP[MeasurePeriod](t - dt) + (O_RivInflowtoLakeMP[MeasurePeriod]) * dt
O_RivInflowtoLakeMP = L_InFlowtoLake if I_Simulation_Time >= O_StartMDay and I_Simulation_Time < O_EndMDay and I_StillWarmUp == 0 else 0
update(O_CumRivInflowtoLakeMP, O_RivInflowtoLakeMP, dt)

# O_CumRivOutFlowMP[MeasurePeriod](t) = O_CumRivOutFlowMP[MeasurePeriod](t - dt) + (O_RivOutFlowMP[MeasurePeriod]) * dt
O_RivOutFlowMP = L_RivOutFlow if I_Simulation_Time >= O_StartMDay and I_Simulation_Time < O_EndMDay and I_StillWarmUp == 0 else 0
update(O_CumRivOutFlowMP, O_RivOutFlowMP, dt)

# O_CumSoilQFlowMP[MeasurePeriod](t) = O_CumSoilQFlowMP[MeasurePeriod](t - dt) + (O_SoilQFlowAccMP[MeasurePeriod]) * dt
O_SoilQFlowAccMP = np.sum(D_SoilDischarge) if I_Simulation_Time >= O_StartMDay and I_Simulation_Time < O_EndMDay and I_StillWarmUp == 0 else 0
update(O_CumSoilQFlowMP, O_SoilQFlowAccMP, dt)

# O_CumSoilWMP[MeasurePeriod](t) = O_CumSoilWMP[MeasurePeriod](t - dt) + (O_SoilWAccMP[MeasurePeriod]) * dt
O_SoilWAccMP = np.sum(D_SoilWater) if I_Simulation_Time >= O_StartMDay and I_Simulation_Time < O_EndMDay and I_StillWarmUp == 0 else 0
update(O_CumSoiMP, O_SoilAccMP, dt)

# O_CumSurfQFlowMP[MeasurePeriod](t) = O_CumSurfQFlowMP[MeasurePeriod](t - dt) + (O_SurfQFlowAccMP[MeasurePeriod]) * dt
O_SurfQFlowAccMP = np.sum(D_SurfaceFlow) if I_Simulation_Time >= O_StartMDay and I_Simulation_Time < O_EndMDay and I_StillWarmUp == 0 else 0
update(O_CumSurfQFlowMP, O_SurfQFlowAccMP, dt)

# O_CumTranspMP[MeasurePeriod](t) = O_CumTranspMP[MeasurePeriod](t - dt) + (O_TranspAccMP[MeasurePeriod]) * dt
O_TranspAccMP = np.sum(D_ActEvapTransp)  if I_Simulation_Time >= O_StartMDay and I_Simulation_Time < O_EndMDay and I_StillWarmUp == 0 else 0
update(O_CumTranspMP, O_TranspAccMP, dt)

# O_DeltaCatchmStMP[MeasurePeriod](t) = O_DeltaCatchmStMP[MeasurePeriod](t - dt) + (O_Ch_in_CatchmStMP[MeasurePeriod]) * dt
O_Ch_in_CatchmStMP = O_Ch_inGWStock+ O_Ch_in_GWStockMP+O_Ch_inWStock + O_Ch_in_WStockMP - O_DeltaCatchmStMP if time > O_StartMDay and time < O_EndMDay + 1 else 0
update(O_DeltaCatchmStMP, O_Ch_in_CatchmStMP, dt)

# O_Hepp_Kwh_per_dayMP[MeasurePeriod](t) = O_Hepp_Kwh_per_dayMP[MeasurePeriod](t - dt) + (O_Hepp_ElctrProd[MeasurePeriod]) * dt
O_Hepp_ElctrProd = L_HEPP_Kwh /( O_EndMDay-O_StartMDay) if I_Simulation_Time >= O_StartMDay and I_Simulation_Time < O_EndMDay and I_StillWarmUp ==0 else 0
upadte(O_Hepp_Kwh_per_dayMP, O_Hepp_ElctrProd, dt)

# O_InitEvapoMP[MeasurePeriod](t) = O_InitEvapoMP[MeasurePeriod](t - dt) + (O_Ch_EvapoTran[MeasurePeriod]) * dt
O_Ch_EvapoTran = np.sum(D_CumEvapTranspClass) if TIME == int(O_StartMDay) else 0
update(O_InitEvapoMP, O_Ch_EvapoTran, dt)

# O_InitGWStockMP[MeasurePeriod](t) = O_InitGWStockMP[MeasurePeriod](t - dt) + (O_ChGWMP[MeasurePeriod]) * dt
O_ChGWMP = np.sum(D_GWArea)  if TIME == int(O_StartMDay) else 0
update(O_InitGWStockMP, O_ChGWMP, dt)

# O_InitSWMP[MeasurePeriod](t) = O_InitSWMP[MeasurePeriod](t - dt) + (O_ChSoilWMP[MeasurePeriod]) * dt
O_ChSoilWMP = np.sum(D_SoilWater) if TIME == int(O_StartMDay) else 0
update(O_InitSWMP, O_ChSoilWMP, dt)

# O_InitSWMP[MeasurePeriod](t) = O_InitSWMP[MeasurePeriod](t - dt) + (O_ChSoilWMP[MeasurePeriod]) * dt
O_ChSoilWMP =  np.sum(D_SoilWater) if TIME == int(O_StartMDay) else 0
update(O_InitSWMP, O_ChSoilWMP, dt)

# O_LastYHepp(t) = O_LastYHepp(t - dt) + (O_HeppUseF1 - O_HeppUseF2) * dt
O_HeppUseF1 = Yearly_Tick*O_ThisYHepp
O_HeppUseF2 = Yearly_Tick*O_LastYHepp
update(O_LastYHepp, O_HeppUseF1 - O_HeppUseF2, dt)

# O_ThisYHepp(t) = O_ThisYHepp(t - dt) + (O_HeppUseF0 - O_HeppUseF1) * dt
O_HeppUseF0 = Yearly_Tick * L_CumHEPPUse
O_HeppUseF1 = Yearly_Tick * O_ThisYHepp
update(O_ThisYHepp, O_HeppUseF0 - O_HeppUseF1, dt)

# O_WorstYHEPP(t) = O_WorstYHEPP(t - dt) + (O_WYP) * dt
O_WYP = -O_WorstYHEPP+O_LastYearHEPP if O_LastYearHEPP>0 and O_LastYearHEPP<O_WorstYHEPPelse 0
update(O_WorstYHEPP, O_WYP, dt)

# O_YearSim(t) = O_YearSim(t - dt) + (Yearly_Tick) * dt
Yearly_Tick = 1 if I_WarmEdUp == 1 and time%365 == 0 else 0
update(O_YearSim, Yearly_Tick, dt)

O_CumET_LandMP= O_CumIntercEvapMP + O_CumTranspMP
O_CurrentETall = np.sum(D_ActEvapTransp)
O_EndMDay = O_StartMDay+O_MPeriodLength
O_LastYearHEPP = (O_ThisYHepp-O_LastYHepp)/(365*L_HEPP_Daily_Dem) if O_LastYHepp>0 else 0
O_MPeriodLength = 365
O_RelOpTimeHEPPMP =  (O_CumHEPPOutFlowMP/L_HEPP_Daily_Dem)/ (O_EndMDay - O_StartMDay )
O_SoilWaterTot = np.sum(D_SoilWater)
O_StarMYear[1] = 4
O_StarMYear[2] = 6
O_StarMYear[3] = 8
O_StartDOY[1] = 1
O_StartDOY[2] = 1
O_StartDOY[3] = 1
O_StartMDay = (O_StarMYear-1)*365+1+(O_StartDOY-1)

# Patch Water Balance
# D_CumEvapTranspClass[VegClass,Subcatchement](t) = D_CumEvapTranspClass[VegClass,Subcatchement](t - dt) + (D_ActEvapTransp[VegClass,Subcatchement] + D_InterceptEvap[VegClass,Subcatchement]) * dt
D_ActEvapTransp = np.multiply((I_PotEvapTransp_ - I_InterceptEffectonTransp*D_InterceptEvap), D_RelWaterAv, out=np.zeros_like(I_PotEvapTransp_), where=L_Lake_==1)
update(D_CUmEvapTranspClass, D_ActEvapTransp, dt)
D_InterceptEvap = np.multiply(I_CanIntercAreaClass, (1 - np.exp(np.divide(-I_DailyRainAmount, I_CanIntercAreaClass))), out=np.zeros(I_CanIntercAreaClass), where=I_CanIntercAreaClass!=0)
# D_CumNegRain[Subcatchement](t) = D_CumNegRain[Subcatchement](t - dt) + (- D_InterceptEvap[VegClass,Subcatchement] - D_Infiltration[VegClass,Subcatchement] - D_DeepInfiltration[Subcatchement] - D_SurfaceFlow[Subcatchement]) * dt
D_Infiltration[VegClass,Subcatchement] = np.min(np.min(I_SoilSatClass-D_SoilWater,np.multiply(I_MaxInfArea, I_RainTimeAvForInf)/24),
I_DailyRainAmount - D_InterceptEvap, out=np.zeros_like(D_Infiltration), where=L_Lake_!=1)

