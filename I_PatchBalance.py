import numpy as np
import config
import calculate

I_SoilQflowFrac = 0.1
I_RainIntercDripRt = 10
I_RainMaxIntDripDur = 0.5

D_GWUseFacility = 1
D_GW_Utilization_fraction = 0.02
D_IrrigEfficiency = 0

D_CumNegRain = [0]
D_CumEvapTranspClass = [0]
D_SoilWater = [0]
D_GWArea = [0]
D_EvapTranspClass = [0]

I_FracVegClassNow_Multiply_I_RelArea = np.multiply(I_FracVegClassNow, I_RelArea)
D_RainInterc = np.divide(D_InterceptEvap, I_FracVegClassNow_Multiply_I_RelArea,
                         out=np.ones(D_InterceptEvap),
                         where=I_FracVegClassNow_Multiply_I_RelArea!=0)
D_RainIntercDelay = np.minimum(I_RainMaxIntDripDur, np.sum(D_RainInterc, axis=1))/I_RainIntercDripRt
I_RainTimeAvForInf = np.minimum(24, I_RainDuration + D_RainIntercDelay)
D_Infiltration = np.multiply((1 - L_Lake_), np.minimum(np.minimum(I_SoilSatClass - D_SoilWater,
                                                                  np.multiply(I_MaxInfArea, I_RainTimeAvForInf)/24),
                                                       I_DailyRainAmount - D_InterceptEvap))
D_Irrigation = np.minimum(np.divide(np.multiply(D_GWArea,
                                                np.multiply(D_GWUseFacility_,
                                                            np.multiply(D_GW_Utilization_fraction,
                                                                        (1-D_RelWaterAv)))),
                                    D_IrrigEfficiency,
                                    out=np.zeros_like(D_IrrigEfficiency),
                                    where=D_IrrigEffeciency!=0),
                          I_PotEvapTransp_)
D_Percolation = np.multiply(I_AvailWaterClass > 0,  np.minimum(I_MaxInfSubSAreaClass, np.minimum(np.multiply(D_SoilWater, np.multiply(I_PercFracMultiplier, I_GWRelFrac)),I_MaxDynGWArea-D_GWArea))
- np.multiply(D_IrrigEfficiency, D_Irrigation)) - np.multiply((I_AvailWaterClass <= 0), np.multiply(D_IrrigEfficiency, D_Irrigation))

D_WaterEvapIrrigation = np.multiply(D_IrrigEfficiency > 0, D_Irrigation *(1-D_IrrigEfficiency))
D_GWaDisch = np.multiply(D_GWArea, I_GWRelFrac)

D_DeepInfiltration = np.multiply(L_Lake_ ==1, np.minimum(np.minimum(np.minimum(np.multiply(np.sum(I_MaxInfArea, axis=1),
                                                                                           I_RainTimeAvForInf)/24 -
                                                                               np.sum(I_SoilSatClass, axis=1) +
                                                                               np.sum(D_SoilWater, axis=1),
                                                                               np.sum(I_MaxInfSubSAreaClass, axis=1)),
                                                                    np.sum(I_DailyRainAmount, axis=1) -
                                                                    np.sum(D_InterceptEvap, axis=1) -
                                                                    np.sum(D_Infiltration, axis=1)),
                                                         I_MaxDynGWArea-D_GWArea))


calculate.update(D_CumNegRain, inflow=0, outflow=D_InterceptEvap + D_Infiltration + D_DeepInfiltration + D_SurfaceFlow, dt=config.dt, non_negative=False)
calculate.update(D_CumEvapTranspClass, inflow=D_ActEvapTransp, D_InterceptEvap, dt=config.dt)
calculate.update(D_SoilWater, inflow=D_Infiltration, outflow=D_ActEvapTransp + D_Percolation + D_SoilDischarge, dt=config.dt)
calculate.update(D_GWArea, inflow=D_Percolation + D_DeepInfiltration, outflow=D_GWaDisch+D_WaterEvapIrrigation, dt=config.dt)
calculate.update(D_EvapTranspClass, inflow=D_WaterEvapIrrigation, dt=config.dt)

