import numpy as np

import config
import calculate

TIME = 0
time = 0

I_WarmEdUp_ = [0]

I_WarmUpTime = 730
I_CaDOYStart = 0
I_RainYearStart = 0
I_RainCycle = config.rainfallConfig['I_RainCycle?']
I_RainMultiplier = config.rainfallConfig['I_RainMultiplier']
I_UseSpatVarRain = config.rainfallConfig['I_UseSpatVarRain?']
I_Rain_IntensMean = config.rainfallConfig['I_Rain_IntensMean']
I_Rain_IntensCoefVar = config.rainfallConfig['I_Rain_IntensCoefVar']
I_Rain_GenSeed = config.rainfallConfig['I_Rain_GenSeed']

I_Simulation_Time = TIME+I_CaDOYStart+365*I_RainYearStart-I_WarmEdUp_*(I_WarmUpTime+1)
I_RainDoY = I_Simulation_Time if (I_RainCycle == 0) else 1 + I_Simulation_Time % 365

I_SpatRain1 = [np.zeros(config.SUBCATCHMENT) for i in range(config.FOURYEARS)]
I_SpatRain2 = [np.zeros(config.SUBCATCHMENT) for i in range(config.FOURYEARS)]
I_SpatRain3 = [np.zeros(config.SUBCATCHMENT) for i in range(config.FOURYEARS)]
I_SpatRain4 = [np.zeros(config.SUBCATCHMENT) for i in range(config.FOURYEARS)]
I_SpatRain5 = [np.zeros(config.SUBCATCHMENT) for i in range(config.FOURYEARS)]
I_SpatRain6 = [np.zeros(config.SUBCATCHMENT) for i in range(config.FOURYEARS)]
I_SpatRain7 = [np.zeros(config.SUBCATCHMENT) for i in range(config.FOURYEARS)]

if I_RainDoY <= 1460:
    I_SpatRainTime = I_SpatRain1 * I_RainMultiplier
elif I_RainDoY <= 2920:
    I_SpatRainTime = I_SpatRain2 * I_RainMultiplier
elif I_RainDoY <= 4380:
    I_SpatRainTime = I_SpatRain3 * I_RainMultiplier
elif I_RainDoY <= 5840:
    I_SpatRainTime = I_SpatRain4 * I_RainMultiplier
elif I_RainDoY <= 7300:
    I_SpatRainTime = I_SpatRain5 * I_RainMultiplier
elif I_RainDoY <= 8760:
    I_SpatRainTime = I_SpatRain6 * I_RainMultiplier
else:
    I_SpatRainTime = I_SpatRain7 * I_RainMultiplier

I_DailyRainYear_1_to_4 = [0 for i in range(config.FOURYEARS)]
I_DailyRainYear_5_to_8 = [0 for i in range(config.FOURYEARS)]
I_DailyRainYear_9_to_12 = [0 for i in range(config.FOURYEARS)]
I_DailyRainYear_13_to_16 = [0 for i in range(config.FOURYEARS)]
I_DailyRainYear_17_to_20 = [0 for i in range(config.FOURYEARS)]
I_DailyRainYear_21_to_24 = [0 for i in range(config.FOURYEARS)]
I_DailyRainYear_25_to_28 = [0 for i in range(config.FOURYEARS)]

if I_RainDoY <= 1460:
    I_DailyRain = I_DailyRainYear_1_to_4 * I_RainMultiplier
elif I_RainDoY <= 2920:
    I_DailyRain = I_DailyRainYear_5_to_8 * I_RainMultiplier
elif I_RainDoY <= 4380:
    I_DailyRain = I_DailyRainYear_9_to_12 * I_RainMultiplier
elif I_RainDoY <= 5840:
    I_DailyRain = I_DailyRainYear_13_to_16 * I_RainMultiplier
elif I_RainDoY <= 7300:
    I_DailyRain = I_DailyRainYear_17_to_20 * I_RainMultiplier
elif I_RainDoY <= 8760:
    I_DailyRain = I_DailyRainYear_21_to_24 * I_RainMultiplier
else:
    I_DailyRain = I_DailyRainYear_25_to_28 * I_RainMultiplier

I_RainPerDay = I_SpatRainTime if I_UseSpatVarRain else I_DailyRain

I_RainDuration = ((I_RainPerDay/I_Rain_IntensMean) *
                  min(max(0,
                          1-3*I_Rain_IntensCoefVar,
                          np.normal(1, I_Rain_IntensCoefVar, I_Rain_GenSeed + 11250)),
                      1 + 3* I_Rain_IntensCoefVar))
I_DailyRainAmount = np.multiply(I_RainPerDay, np.multiply(I_FracVegClassNow, I_RelArea))

I_StillWarmUp_ = 1 if time <= I_WarmUpTime else 0
I_WUcorrection = 1 if time == int(I_WarmUpTime + 1 ) else 0

calculate.update(stock=I_WarmEdUp_, inflow=I_WarmUpTime, dt=config.dt)
