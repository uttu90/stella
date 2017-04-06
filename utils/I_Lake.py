import numpy as np
import config
import calculate

time = 0

L_CumEvapLake = [0]
L_CumRivOutFlow = [0]
L_CumHEPPUse = [0]

L_FloodTresh = 363
L_HEPP_Active_ = 1
L_LakeLevelFullHEPP = 362.3
L_LakeLevelHalfHEPP = 361.8
L_LakeLevelNoHEPP = 359.5
L_LakeOverFlowFrac = 0.1
L_LakeOverFlPostHEPP = 362.6
L_LakeOverFlPow = 4
L_m3_per_kwh = 1.584
L_QmecsHEPP = 47.1
L_QmecsSanFlow = 3
L_LakeBottomElev = 160
L_LakeElevPreHEPP = 362.3
L_LakeTranspMultiplier = 1

L_Lake_ = np.zeros(config.SUBCATCHMENT)

L_LakeArea = np.multiply(L_Lake_, I_RelArea)
L_OutflTrVolPreHEPP = 1000*(L_LakeElevPreHEPP-L_LakeBottomElev)*np.sum(L_LakeArea)
L_OutflTrVoPostHEPP = 1000*(L_LakeOverFlPostHEPP-L_LakeBottomElev)*np.sum(L_LakeArea)
L_HEPP_Daily_Dem = L_QmecsHEPP*3600*24/I_TotalArea*10^-3
L_LakeVol = [L_OutflTrVoPostHEPP*L_HEPP_Active_+(1-L_HEPP_Active_)*L_OutflTrVolPreHEPP]
L_SanitaryFlow = L_QmecsSanFlow* 3600*24/I_TotalArea*10^-3
L_LakeLevel = L_LakeVol(time)/(1000*np.sum(L_LakeArea)) + L_LakeBottomElev if np.sum(L_LakeArea)>0 else 0
L_Lakelevelexcess = L_LakeLevel-(1-L_HEPP_Active_)*L_LakeElevPreHEPP-L_HEPP_Active_*L_LakeOverFlPostHEPP
L_LakeTransDef = np.multiply(L_Lake_,
                             D_ActEvapTransp[config.LANDCOVER['AF_Kelapa']] +
                             I_PotEvapTransp_[config.LANDCOVER['AF_Kelapa']])
L_InFlowtoLake =  D_RiverFlowtoLake + D_GWtoLake
L_EvapLake = min(np.sum(L_LakeTransDef), L_LakeVol[time]) * L_LakeTranspMultiplier
L_RivOutFlow = max(L_HEPP_Active_*L_SanitaryFlow,
                   (L_LakeVol-(L_OutflTrVoPostHEPP*L_HEPP_Active_)-
                    L_OutflTrVolPreHEPP*(1-L_HEPP_Active_))*
                   (L_LakeOverFlowFrac)*(1+L_Lakelevelexcess^L_LakeOverFlPow))
L_HEPP_Outflow = (L_HEPP_Daily_Dem
                  if L_LakeLevel>L_LakeLevelFullHEPP
                  else L_HEPP_Daily_Dem*0.5*(1+max(0,(L_LakeLevel-L_LakeLevelHalfHEPP)/(L_LakeLevelFullHEPP-L_LakeLevelHalfHEPP)))
                  if L_LakeLevel>L_LakeLevelNoHEPP
                  else 0)
L_HEPPWatUseFlow = L_HEPP_Outflow if L_HEPP_Active_ == 1 else 0
calculate.update(L_LakeVol, inflow=L_InFlowtoLake, outflow=L_EvapLake + L_RivOutFlow + L_HEPPWatUseFlow, dt=config.dt)
L_FloodingCurrent_ = 1 if L_LakeLevel>L_FloodTresh else 0

L_RestartR = O_Reset_*L_CumRivOutFlow[time]/config.dt
calculate.update(L_CumRivOutFlow, inflow=L_RivOutFlow, outflow=L_RestartR, dt=config.dt)

L_HEPPWatUseFlow = L_HEPP_Outflow if L_HEPP_Active_ == 1 else 0
L_RestartH = O_Reset_ * L_CumHEPPUse[time]
calculate.update(L_CumHEPPUse, inflow=L_HEPPWatUseFlow, outflow=L_RestartH, dt=config.dt)

L_RestartE = O_Reset_ * L_CumEvapLake[time]/config.dt
calculate.update(L_CumEvapLake, inflow=L_EvapLake, outflow=L_RestartE, dt=config.dt)
