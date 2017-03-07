import numpy as np


def update(value, diff, delta):
    value.append(value[-1] + diff * delta)

VegClass = 20
Subcatchment = 20

# Initial
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

# Simulation
time = 1
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
                          out=np.zeros_like(I_PotEvapTransp),
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
G_GrassFract_Biomass = np.zeros_like(VegClass) # Check for input
G_GrassLitConv = 1
G_GrassMortFrac = 0.03
G_GrazingManConv = 0.1
G_SurfaceCover = G_GrassStandingBiomass[-1] + G_SurfaceLitter[-1] + G_SurfMaunre[-1]
G_SurfLitDecFrac = 0.03
G_SurfManureDecFrac = 0.01
G_TramplingMultiplier = 0
G_WUE = 0.04

# I Daily Evapotranspiration
I_Daily_Evapotrans = I_RainDoY[time]

# I Land cover
D_FeedingIntoLake

I_Flag1 = 1 if time < I_InputDataYears[1] * 365 else 0
I_Flag2 = 1 if time < I_InputDataYears[2] and I_Flag1 ==0 else 0
if I_Flag1 == 1:
    I_AvailWatClassNow = (I_PlantAvWatSub1 +
                          (I_PlantAvWatSub2-I_PlantAvWatSub1) *
                          (int(time/365) -
                           I_InputDataYears[0])/(I_InputDataYears[1] - I_InputDataYears[0]))
    I_BD_BDRefVegNow = (I_TopSoilBD_BDRef1 +
                        (I_TopSoilBD_BDRef2-I_TopSoilBD_BDRef1) *
                        (int(time/365) -
                         I_InputDataYears[0])/(I_InputDataYears[1] - I_InputDataYears[0]))
elif I_Flag2 == 1:
    I_AvailWatClassNow = (I_PlantAvWatSub2 +
                          (I_PlantAvWatSub3 - I_PlantAvWatSub2) *
                          (int(time / 365) -
                           I_InputDataYears[1]) / (I_InputDataYears[2] - I_InputDataYears[1]))
    I_BD_BDRefVegNow = (I_TopSoilBD_BDRef2 +
                        (I_TopSoilBD_BDRef3-I_TopSoilBD_BDRef4) *
                        (int(time/365) -
                         I_InputDataYears[1])/(I_InputDataYears[2] - I_InputDataYears[2]))
else:
    I_AvailWatClassNow = (I_PlantAvWatSub3 +
                          (I_PlantAvWatSub4 - I_PlantAvWatSub3) *
                          (int(time/365)-I_InputDataYears[2])/(I_InputDataYears[3]-I_InputDataYears[2]))
    I_BD_BDRefVegNow = (I_TopSoilBD_BDRef3 +
                        (I_TopSoilBD_BDRef4-I_TopSoilBD_BDRef3) *
                        (int(time/365)-I_InputDataYears[2])/(I_InputDataYears[3]-I_InputDataYears[2]))

I_FracVegClass1 = I_Frac1 # Reading table from Excel
I_FracVegClass2 = I_Frac2
I_FracVegClass3 = I_Flag3
I_FracVegClass4 = I_Frac4

D_FeedingIntoLake = np.ones(Subcatchment)
I_RoutingDistance = np.zeros(Subcatchment)
I_Area = np.zeros(Subcatchment)
I_TotalArea = np.sum(I_Area)
I_RelArea = I_Area/I_TotalArea
I_FracVegClassNow = np.zeros_like(I_FracVegClass1)
for i in range(Subcatchment):
    if I_RelArea[i] > 0:
        if I_Flag1 == 1:
            I_FracVegClassNow[:][i] = ((I_FracVegClass1[:][i] +
                                        (I_FracVegClass2[:][i] - I_FracVegClass1[:][i]) *
                                        (int(time/365)-I_InputDataYears[0])/
                                        (I_InputDataYears[1]-I_InputDataYears[0]))/
                                       np.sum(I_FracVegClass1, axis=1))
        elif I_Flag2 == 1:
            I_FracVegClassNow[:][i] = ((I_FracVegClass2[:][i] +
                                        (I_FracVegClass3[:][i] - I_FracVegClass2[:][i])*
                                        (int(time/365) - I_InputDataYears[1])/
                                        (I_InputDataYears[2]-I_InputDataYears[1]))/np.sum(I_FracVegClass2, axis=1))
        else:
            I_FracVegClassNow[:][i] = ((I_FracVegClass3[:][i] +
                                        (I_FracVegClass4[:][i] - I_FracVegClass3[:][i])*
                                        (int(time/365) - I_InputDataYears[2])/
                                        (I_InputDataYears[3]-I_InputDataYears[2]))/np.sum(I_FracVegClass3, axis=1))
    else:
        I_FracVegClassNow[:][i] = 0

I_FracVegClassSum1 = np.sum(I_FracVegClass1)
I_FracVegClassSum2 = np.sum(I_FracVegClass2)
I_FracVegClassSum3 = np.sum(I_FracVegClass3)
I_FracVegClassSum4 = np.sum(I_FracVegClass4)
I_FracVegClassSumNow = np.sum(I_FracVegClassNow)

I_GWRelFrac1 = np.zeros_like(Subcatchment)
I_GWRelFrac2 = np.zeros_like(Subcatchment)
I_GWRelFrac3 = np.zeros_like(Subcatchment)
I_GWRelFrac4 = np.zeros_like(Subcatchment)

