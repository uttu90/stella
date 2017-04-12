import numpy as np
import calculate
import config


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
