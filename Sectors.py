__author__ =  'TuHV'
from stella import Flow, Stock
from random import normalvariate

# 1. Rainfall
time = 0
I_WarmUpTime = 730
I_StillWarmUp_ = 1 if time <= (I_WarmUpTime + 1) else 0
I_WUcorrection = 1 if time == (I_WarmUpTime + 1) else 0

def f_I_WarmedUp(I_WarmUpTime, time):
    return 1 if time == I_WarmUpTime else 0

I_WarmedUp_ = Stock(0)

I_WarmedUp = Flow(f_I_WarmedUp, None, I_WarmedUp_)

I_CaDOYStart = 0
I_RainYearStart = 0

I_Simulation_Time = time + I_CaDOYStart + 365*I_RainYearStart-I_WarmedUp_.current_value()*(I_WarmUpTime + 1)

I_RainCycle_ =0

I_RainDoY = I_Simulation_Time if I_RainCycle_ else (1 + I_Simulation_Time/365)

I_RainMultiplier = 1

subcatchment = [i for i in range(0,20)]

# Merge I_SpatRain1, 2, 3, ... to I_SpatRain
I_SpatRain = []

I_SpatRainTime = I_SpatRain[time]*I_RainMultiplier

# Merge I_DailyRainYear1to4, ... to I_DailyRainYear
I_DailyRainYear = []
I_DailyRain = I_DailyRainYear[time]*I_RainMultiplier

I_UseSpatVarRain_ = 0
I_RainPerDay = I_SpatRainTime if I_UseSpatVarRain_ else I_DailyRain

I_Rain_IntensMean = 30
I_Rain_GenSeed = 100
I_Rain_IntensCoefVar = 0.7
I_RainDuration = I_RainPerDay/I_Rain_IntensMean*min(max(0.1 - 3*I_Rain_IntensCoefVar, normalvariate(1, I_Rain_IntensCoefVar,I_Rain_GenSeed+11250)), 1+3*I_Rain_IntensCoefVar)

# I_FracVegClass and I_RefArea is calculated in other sectors

I_DailyRainAmount = I_RainPerDay*I_FracVegClassNow*I_RelArea

# 2. I RivFlowData

# Merge I_RFlowDataYear?to? to I_RFlowDataYear
I_RFlowDataYear = []
I_DebitTime = I_RFlowDataYear[time]
I_RFlowDataQmecs = I_DebitTime

I_SubcContr_ = [1 for i in range(20)]
I_ContrSubcArea = I_RelArea*I_SubcContr_

O_CumDebitData = Stock(0)

def f_I_RFlowdata_mmday(I_ContrSubcArea, I_RFlowDataQmecs, I_TotalArea):
    return I_RFlowDataQmecs*24*3600*10^3/sum(I_ContrSubcArea)*I_TotalArea if sum(I_ContrSubcArea) > 0 else 0

I_RFlowdata_mmday = Flow(f_I_RFlowdata_mmday, None, O_CumDebitData)


# 3. I Landcover
VegClass = 20
I_InterceptClass = [0 for i in range(VegClass)]
I_RelDroughtFact = [0 for i in range(VegClass)]

Subcatchment = 20
D_FeedingIntoLake_ = [1 for i in range(Subcatchment)]
I_RoutingDistance = [0 for i in range(Subcatchment)]
I_Area = [0 for i in range(Subcatchment)]
I_TotalArea = sum(I_Area)
I_RelArea = I_Area/I_TotalArea


I_Frac1_1 = [0 for i in range(Subcatchment)]
I_Frac2_1 = [0 for i in range(Subcatchment)]
I_Frac3_1 = [0 for i in range(Subcatchment)]
I_Frac4_1 = [0 for i in range(Subcatchment)]
I_Frac5_1 = [0 for i in range(Subcatchment)]
I_Frac6_1 = [0 for i in range(Subcatchment)]
I_Frac7_1 = [0 for i in range(Subcatchment)]
I_Frac8_1 = [0 for i in range(Subcatchment)]
I_Frac9_1 = [0 for i in range(Subcatchment)]
I_Frac10_1 = [0 for i in range(Subcatchment)]
I_Frac11_1 = [0 for i in range(Subcatchment)]
I_Frac12_1 = [0 for i in range(Subcatchment)]
I_Frac13_1 = [0 for i in range(Subcatchment)]
I_Frac14_1 = [0 for i in range(Subcatchment)]
I_Frac15_1 = [0 for i in range(Subcatchment)]
I_Frac16_1 = [0 for i in range(Subcatchment)]
I_Frac17_1 = [0 for i in range(Subcatchment)]
I_Frac18_1 = [0 for i in range(Subcatchment)]
I_Frac19_1 = [0 for i in range(Subcatchment)]
I_Frac20_1 = [0 for i in range(Subcatchment)]


I_Frac1_2 = [0 for i in range(Subcatchment)]
I_Frac2_2 = [0 for i in range(Subcatchment)]
I_Frac3_2 = [0 for i in range(Subcatchment)]
I_Frac4_2 = [0 for i in range(Subcatchment)]
I_Frac5_2 = [0 for i in range(Subcatchment)]
I_Frac6_2 = [0 for i in range(Subcatchment)]
I_Frac7_2 = [0 for i in range(Subcatchment)]
I_Frac8_2 = [0 for i in range(Subcatchment)]
I_Frac9_2 = [0 for i in range(Subcatchment)]
I_Frac10_2 = [0 for i in range(Subcatchment)]
I_Frac11_2 = [0 for i in range(Subcatchment)]
I_Frac12_2 = [0 for i in range(Subcatchment)]
I_Frac13_2 = [0 for i in range(Subcatchment)]
I_Frac14_2 = [0 for i in range(Subcatchment)]
I_Frac15_2 = [0 for i in range(Subcatchment)]
I_Frac16_2 = [0 for i in range(Subcatchment)]
I_Frac17_2 = [0 for i in range(Subcatchment)]
I_Frac18_2 = [0 for i in range(Subcatchment)]
I_Frac19_2 = [0 for i in range(Subcatchment)]
I_Frac20_2 = [0 for i in range(Subcatchment)]


I_Frac1_3 = [0 for i in range(Subcatchment)]
I_Frac2_3 = [0 for i in range(Subcatchment)]
I_Frac3_3 = [0 for i in range(Subcatchment)]
I_Frac4_3 = [0 for i in range(Subcatchment)]
I_Frac5_3 = [0 for i in range(Subcatchment)]
I_Frac6_3 = [0 for i in range(Subcatchment)]
I_Frac7_3 = [0 for i in range(Subcatchment)]
I_Frac8_3 = [0 for i in range(Subcatchment)]
I_Frac9_3 = [0 for i in range(Subcatchment)]
I_Frac10_3 = [0 for i in range(Subcatchment)]
I_Frac11_3 = [0 for i in range(Subcatchment)]
I_Frac12_3 = [0 for i in range(Subcatchment)]
I_Frac13_3 = [0 for i in range(Subcatchment)]
I_Frac14_3 = [0 for i in range(Subcatchment)]
I_Frac15_3 = [0 for i in range(Subcatchment)]
I_Frac16_3 = [0 for i in range(Subcatchment)]
I_Frac17_3 = [0 for i in range(Subcatchment)]
I_Frac18_3 = [0 for i in range(Subcatchment)]
I_Frac19_3 = [0 for i in range(Subcatchment)]
I_Frac20_3 = [0 for i in range(Subcatchment)]


I_Frac1_4 = [0 for i in range(Subcatchment)]
I_Frac2_4 = [0 for i in range(Subcatchment)]
I_Frac3_4 = [0 for i in range(Subcatchment)]
I_Frac4_4 = [0 for i in range(Subcatchment)]
I_Frac5_4 = [0 for i in range(Subcatchment)]
I_Frac6_4 = [0 for i in range(Subcatchment)]
I_Frac7_4 = [0 for i in range(Subcatchment)]
I_Frac8_4 = [0 for i in range(Subcatchment)]
I_Frac9_4 = [0 for i in range(Subcatchment)]
I_Frac10_4 = [0 for i in range(Subcatchment)]
I_Frac11_4 = [0 for i in range(Subcatchment)]
I_Frac12_4 = [0 for i in range(Subcatchment)]
I_Frac13_4 = [0 for i in range(Subcatchment)]
I_Frac14_4 = [0 for i in range(Subcatchment)]
I_Frac15_4 = [0 for i in range(Subcatchment)]
I_Frac16_4 = [0 for i in range(Subcatchment)]
I_Frac17_4 = [0 for i in range(Subcatchment)]
I_Frac18_4 = [0 for i in range(Subcatchment)]
I_Frac19_4 = [0 for i in range(Subcatchment)]
I_Frac20_4 = [0 for i in range(Subcatchment)]

I_FracVegClass1 = [I_Frac1_1, I_Frac2_1, I_Frac3_1, I_Frac4_1, I_Frac5_1, I_Frac6_1, I_Frac7_1, I_Frac8_1, I_Frac9_1, I_Frac10_1,
                   I_Frac11_1, I_Frac12_1, I_Frac13_1, I_Frac14_1, I_Frac15_1, I_Frac16_1, I_Frac17_1, I_Frac18_1, I_Frac19_1,
                   I_Frac20_1]

I_FracVegClass2 = [I_Frac1_2, I_Frac2_2, I_Frac3_2, I_Frac4_2, I_Frac5_2, I_Frac6_2, I_Frac7_2, I_Frac8_2, I_Frac9_2, I_Frac10_2,
                   I_Frac11_2, I_Frac12_2, I_Frac13_2, I_Frac14_2, I_Frac15_2, I_Frac16_2, I_Frac17_2, I_Frac18_2, I_Frac19_2,
                   I_Frac20_2]

I_FracVegClass3 = [I_Frac1_3, I_Frac2_3, I_Frac3_3, I_Frac4_3, I_Frac5_3, I_Frac6_3, I_Frac7_3, I_Frac8_3, I_Frac9_3, I_Frac10_3,
                   I_Frac11_3, I_Frac12_3, I_Frac13_3, I_Frac14_3, I_Frac15_3, I_Frac16_3, I_Frac17_3, I_Frac18_3, I_Frac19_3,
                   I_Frac20_3]

I_FracVegClass4 = [I_Frac1_4, I_Frac2_4, I_Frac3_4, I_Frac4_4, I_Frac5_4, I_Frac6_4, I_Frac7_4, I_Frac8_4, I_Frac9_4, I_Frac10_4,
                   I_Frac11_4, I_Frac12_4, I_Frac13_4, I_Frac14_4, I_Frac15_4, I_Frac16_4, I_Frac17_4, I_Frac18_4, I_Frac19_4,
                   I_Frac20_4]

I_FracVegClassSum1 = sum([sum(x) for x in I_FracVegClass1])
I_FracVegClassSum2 = sum([sum(x) for x in I_FracVegClass2])
I_FracVegClassSum3 = sum([sum(x) for x in I_FracVegClass3])
I_FracVegClassSum4 = sum([sum(x) for x in I_FracVegClass4])

I_OneInputDataYears = [i for i in range(4)]
I_InputDataYears = [i for i in range(4)]

I_Flag1 = 1 if time < I_InputDataYears[1] *365 else 0
I_Flag2 = 1 if time < I_InputDataYears[2] *365 else 0

if I_RelArea > 0:
    if I_Flag1 == 1:
        I_FracVegClassNow = I_FracVegClass1 + I_FracVegClass2 - I_FracVegClass1*(int(time/365) - I_InputDataYears[0])/(I_InputDataYears[1]-I_InputDataYears[0])*sum(I_FracVegClass1)

    elif I_Flag2 == 1:
        I_FracVegClassNow = I_FracVegClass2 + I_FracVegClass3 - I_FracVegClass2 * (
        int(time / 365) - I_InputDataYears[1]) / (I_InputDataYears[2] - I_InputDataYears[1]) * sum(I_FracVegClass2)

    else:
        I_FracVegClassNow = I_FracVegClass3 + I_FracVegClass4 - I_FracVegClass3 * (
        int(time / 365) - I_InputDataYears[2]) / (I_InputDataYears[2] - I_InputDataYears[1]) * sum(I_FracVegClass3)
else:
    I_FracVegClassNow = 0

I_RivFlowTime1 = [0 for i in range(Subcatchment)]
I_RivFlowTime2 = [0 for i in range(Subcatchment)]
I_RivFlowTime3 = [0 for i in range(Subcatchment)]
I_RivFlowTime4 = [0 for i in range(Subcatchment)]


if I_Flag1 ==1:
    I_RivFlowTimeNow = I_RivFlowTime1 + I_RivFlowTime2 - I_RivFlowTime1*(time/365 - I_InputDataYears[0])/(I_InputDataYears[1] - I_InputDataYears[0])
if I_Flag2 ==1:
    I_RivFlowTimeNow = I_RivFlowTime3 + I_RivFlowTime4 - I_RivFlowTime3 * (time / 365 - I_InputDataYears[2]) / (I_InputDataYears[3] - I_InputDataYears[2])


I_GWRelFrac1 = [0 for i in range(Subcatchment)]
I_GWRelFrac2 = [0 for i in range(Subcatchment)]
I_GWRelFrac3 = [0 for i in range(Subcatchment)]
I_GWRelFrac4 = [0 for i in range(Subcatchment)]

if I_Flag1 ==1:
    I_GWRelFracNow = I_GWRelFrac1 + I_GWRelFrac2 - I_GWRelFrac1*(time/365 - I_InputDataYears[0])/(I_InputDataYears[1] - I_InputDataYears[0])
if I_Flag2 ==1:
    I_GWRelFracNow = I_GWRelFrac3 + I_GWRelFrac4 - I_GWRelFrac3 * (time / 365 - I_InputDataYears[2]) / (I_InputDataYears[3] - I_InputDataYears[2])


I_MaxDynGwSub1 = [0 for i in range(Subcatchment)]
I_MaxDynGwSub2 = [0 for i in range(Subcatchment)]
I_MaxDynGwSub3 = [0 for i in range(Subcatchment)]
I_MaxDynGwSub4 = [0 for i in range(Subcatchment)]


if I_Flag1 ==1:
    I_MaxDynGwSubNow = I_MaxDynGwSub1 + I_MaxDynGwSub2 - I_MaxDynGwSub1*(time/365 - I_InputDataYears[0])/(I_InputDataYears[1] - I_InputDataYears[0])
if I_Flag2 ==1:
    I_MaxDynGwSubNow = I_MaxDynGwSub3 + I_MaxDynGwSub4 - I_MaxDynGwSub3 * (time / 365 - I_InputDataYears[2]) / (I_InputDataYears[3] - I_InputDataYears[2])


I_PlantAvWatSub1 = [0 for i in range(Subcatchment)]
I_PlantAvWatSub2 = [0 for i in range(Subcatchment)]
I_PlantAvWatSub3 = [0 for i in range(Subcatchment)]
I_PlantAvWatSub4 = [0 for i in range(Subcatchment)]


if I_Flag1 ==1:
    I_PlantAvWatSubNow = I_PlantAvWatSub1 + I_PlantAvWatSub2 - I_PlantAvWatSub1*(time/365 - I_InputDataYears[0])/(I_InputDataYears[1] - I_InputDataYears[0])
if I_Flag2 ==1:
    I_PlantAvWatSubNow = I_PlantAvWatSub3 + I_PlantAvWatSub4 - I_PlantAvWatSub3 * (time / 365 - I_InputDataYears[2]) / (I_InputDataYears[3] - I_InputDataYears[2])


I_PWPSub1 = [0 for i in range(Subcatchment)]
I_PWPSub2 = [0 for i in range(Subcatchment)]
I_PWPSub3 = [0 for i in range(Subcatchment)]
I_PWPSub4 = [0 for i in range(Subcatchment)]


if I_Flag1 ==1:
    I_PWPSubNow = I_PWPSub1 + I_PWPSub2 - I_PWPSub1*(time/365 - I_InputDataYears[0])/(I_InputDataYears[1] - I_InputDataYears[0])
if I_Flag2 ==1:
    I_PWPSubNow = I_PWPSub3 + I_PWPSub4 - I_PWPSub4 * (time / 365 - I_InputDataYears[2]) / (I_InputDataYears[3] - I_InputDataYears[2])


I_SoilSatminFCSub1 = [0 for i in range(Subcatchment)]
I_SoilSatminFCSub2 = [0 for i in range(Subcatchment)]
I_SoilSatminFCSub3 = [0 for i in range(Subcatchment)]
I_SoilSatminFCSub4 = [0 for i in range(Subcatchment)]


if I_Flag1 ==1:
    I_SoilSatminFCSubNow = I_SoilSatminFCSub1 + I_SoilSatminFCSub2 - I_SoilSatminFCSub1*(time/365 - I_InputDataYears[0])/(I_InputDataYears[1] - I_InputDataYears[0])
if I_Flag2 ==1:
    I_SoilSatminFCSubNow = I_SoilSatminFCSub3 + I_SoilSatminFCSub4 - I_SoilSatminFCSub4 * (time / 365 - I_InputDataYears[2]) / (I_InputDataYears[3] - I_InputDataYears[2])


I_TopSoilBD_BDRef1 = [0 for i in range(Subcatchment)]
I_TopSoilBD_BDRef2 = [0 for i in range(Subcatchment)]
I_TopSoilBD_BDRef3 = [0 for i in range(Subcatchment)]
I_TopSoilBD_BDRef4 = [0 for i in range(Subcatchment)]


if I_Flag1 ==1:
    I_BD_BDVegRefNow = I_TopSoilBD_BDRef1 + I_TopSoilBD_BDRef2 - I_TopSoilBD_BDRef1*(time/365 - I_InputDataYears[0])/(I_InputDataYears[1] - I_InputDataYears[0])
if I_Flag2 ==1:
    I_BD_BDVegRefNow = I_TopSoilBD_BDRef3 + I_TopSoilBD_BDRef4 - I_TopSoilBD_BDRef4 * (time / 365 - I_InputDataYears[2]) / (I_InputDataYears[3] - I_InputDataYears[2])


# 4. I Subcatchment Param

I_GWRelFracConst_ = 0
I_GWRelFracConst = 0
I_MaxDynGWConst = 0
I_InitRelGW = 0
I_AvaiWaterConst = 0
I_SoilSatMinFCConst = 0
I_SoilPropConst_ = 0
I_MaxInf = 0
I_MaxInfSSoil = 0
I_PowerInfiltRed = 0
I_PercFracMultiplier = 0
I_RoutVeloc_m_per_s = 0
I_Tortuosity = 0
I_SurfLossFrac = 0
I_RiverFlowDispersalFactor = 0
I_InterceptEffectonTransp = 0
L_ResrDepth = 0
L_LakeTranspMultiplier = 0
I_InitRelSoi = 0
L_Lake_ = [0 for i in range(subcatchment)]
I_DaminThisStream_ = [0 for i in range(subcatchment)]

if I_RainDoY == 0:
    I_TimeEvap = 0
elif (I_RainDoY % 365) == 0:
    I_TimeEvap = 365
else:
    I_TimeEvap = I_RainDoY%365

I_MoY = 0 if I_RainDoY == 0 else int(I_TimeEvap/30.5) + 1

I_MultiplierEvapoTrans = [0 for i in range(VegClass)]
I_Evapotrans = 0
I_EvapotransMethod = 0

I_GWRelFrac = I_GWRelFracConst if I_GWRelFracConst_ == 1 else I_GWRelFracNow
I_MaxDynGWact = I_MaxDynGWConst if I_GWRelFracConst_ == 1 else I_MaxDynGwSubNow
I_MaxDynGWArea = I_MaxDynGWact * I_RelArea
I_InitTotGW = sum(I_MaxDynGWArea)*I_InitRelGW
if I_SoilPropConst_ == 1:
    I_SoilSatClass = (I_AvaiWaterConst + I_SoilSatMinFCConst)*I_FracVegClassNow*I_RelArea
else:
    I_SoilSatClass = I_SoilSatminFCSubNow + I_AvaiWatClassNow * I_FracVegClassNow*I_RelArea
if I_SoilPropConst_ == 1:
    I_AvailWaterClass = I_AvailWaterConst*I_FracVegClassNow*I_RelArea
else:
    I_AvailWaterClass = I_AvailWatClassNow*I_FracVegClassNow*I_RelArea

I_CanInterAreaClass = I_InterceptClass*I_FracVegClassNow*I_RelArea
if I_BD_BDVegRefNow > 0:
    I_MaxInfArea = I_MaxInf * I_RelArea * I_FracVegClassNow*(0.7/I_BD_BDVegRefNow)^I_PowerInfiltRed
else:
    I_MaxInfArea = 0

I_MaxInfSubSAreaClass = I_MaxInfSSoil * I_RelArea * I_FracVegClassNow


# 5. Patch Water Balance

D_GW_Utilization_fraction = [0 for i in range(Subcatchment)]
D_GWUseFacility_ = [0 for i in range(Subcatchment)]
D_IrrigEfficiency = [0 for i in range(Subcatchment)]

D_EvapTranspClass = Stock([0 for i in range(Subcatchment)])
D_GWArea = Stock([0 for i in range(Subcatchment)])
D_SoilWater = Stock([0 for i in range(Subcatchment)])
D_CumNegRain = Stock([0 for i in range(Subcatchment)])
D_CumEvapTranspClass = Stock([0 for i in range(Subcatchment)])



