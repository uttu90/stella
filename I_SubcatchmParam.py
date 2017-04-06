import numpy as np
from rainfall import I_RainDoY
import config

I_MultiplierEvapoTrans = [np.zeros(config.SUBCATCHMENT) for i in range(config.MONTH)]
I_EvapoTrans = [0 for i in range(config.MONTH)]

I_FracArea = np.multipy(I_FracVegClassNow,  I_RelArea)

I_TimeEvap = 0 if I_RainDoY == 0 else 365 if I_RainDoY % 365 == 0 else I_RainDoY % 365
I_MoY = 0 if I_RainDoY == 0 else int(I_TimeEvap/30.5) + 1
if config.I_EvapotransMethod == 1:
    I_PotEvapTransp = np.multily(I_EvapoTrans[I_MoY],
                                 np.multiply(I_MultiplierEvapoTrans[I_MoY],
                                             I_FracArea))
else:
    I_PotEvapTransp = np.multiply(I_Daily_Evapotrans,
                                  np.multiply(MultiplierEvapoTrans,
                                              I_FracArea))
I_MaxInfSubSAreaClass = config.I_MaxInfSSoil * I_FracArea
I_MaxInfArea = config.I_MaxInf * np.multiply(I_FracArea,
                                             np.power(np.divide(0.7, I_BD_BDRefVegNow,
                                                                out=np.zeros_like(I_BD_BDRefVegNow),
                                                                where=I_BD_BDRefVegNow != 0),
                                                      config.I_PowerInfiltRed))
I_CanIntercAreaClass = np.multiply(I_InterceptClass, I_FracArea)
I_AvailWaterClass = (config.I_AvailWaterConst * I_FracArea
                     if config.I_SoilPropConst_
                     else np.multiply(I_AvailWatClassNow, I_FracArea))
I_SoilSatClass = ((config.I_AvailWaterConst + config.I_SoilSatMinFCConst) * I_FracArea if config.I_SoilPropConst_
                  else np.add(I_SoilSatminFCSubNow, np.multiply(I_AvailWatClassNow, I_FracArea)))
I_GWRelFrac = config.I_GWRelFracConst if config.I_SoilPropConst_ else I_GWRelFracNow
I_MaxDynGWact = config.I_MaxDynGWConst if config.I_GWRelFracConst_ else I_MaxDynGwSubNow
I_MaxDynGWArea = np.multiply(I_MaxDynGWact, I_RelArea)
I_InitTotGW = np.sum(I_MaxDynGWArea, I_InitRelGW)
