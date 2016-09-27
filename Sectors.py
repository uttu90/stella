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
I_InterceptClass = [0 for i in range(11)]
I_RelDroughtFact = [0 for i in range(11)]

Subcatchment = 20
D_FeedingIntoLake_ = [1 for i in range(20)]
I_RoutingDistance = [0 for i in range(20)]
I_Area = [0 for i in range(20)]
I_TotalArea = sum(I_Area)
I_RelArea = I_Area/I_TotalArea




