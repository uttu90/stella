import numpy as np
import config
import calculate

time = 0

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

O_TotStreamFlow = O_CumBaseFlow[time] + O_CumSoilQFlow[time] + O_CumSurfQFlow[time]
D_DeltaStockRiver = D_InitRivVol[time] - D_CurrRivVol
D_SurfaceFlowAcc = np.sum(D_SurfaceFlow[time])
O_DeltaGWStock = O_InitGWStock[time] - np.sum(D_GWArea)
O_DeltaSoilStock = O_InitSoilW[time] - np.sum(D_SoilWater)
O_ChkAllCatchmAccFor = -O_CumRain[time] + O_CumIntercE[time] + O_CumTransp[time] + O_TotStreamFlow - O_DeltaGWStock - O_DeltaSoilWStock
O_ChkAllLakeAccFor = D_CumInflowtoLake[time] - L_CumEvapLake[time] - L_CumRivOutFlow[time] - L_CumHEPPUSe[time] + O_DeltaStockLake[time]
O_ChkAllRiverAccFor = O_TotStreamFlow -D_CumTotRiverFlowAll - D_CumInflowtoLake + D_DeltaStockRiver
O_DailyRainSubCtm = np.sum(I_DailyRainAmount, axis=0)
O_DeltaStockLake =D_InitLakeVol[time] - L_LakeVol[time]
O_FrBaseFlow = O_CumBaseFlow[time]/O_TotStreamFlow if O_TotStreamFlow > 0 else 0
O_FrSoilQuickFlow = O_CumSoilQFlow[time]/O_TotStreamFlow if O_TotStreamFlow > 0 else 0
O_FrSurfQuickFlow = O_CumSurfQFlow[time]/O_TotStreamFlow if O_TotStreamFlow else 0
O_RainHalfDelayed = (np.sum(O_RainYesterday[time]) + np.sum(I_DailyRainAmount))/2
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

O_InitLake = O_Reset * (L_LakeVol[time] - D_InitLakeVol[time])
update(D_InitLakeVol, O_InitLake, dt)

O_InitRiv = O_Reset * (D_CurrRivVol - D_InitLakeVol[time])
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

O_InitGW = (np.sum(D_GWArea) - O_InitGWStock[time])
update(O_InitGWStock, O_InitGW, dt)

O_InitSW = O_Reset * (np.sum(D_SoilWater) - O_InitSoilW[time])
update(O_InitSoilW, O_InitSW, dt)

O_RainToday = np.sum(I_DailyRainAmount, axis=0) * I_WarmEdUp
O_RainYesterday = O_RainYest[time] * I_WarmEdUp
update(O_RainYest, O_RainToday - O_RainYesterday, dt)
