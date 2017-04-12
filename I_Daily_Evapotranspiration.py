import numpy as np
from I_Rainfall import I_RainDoY

import config

I_Daily_Evap_1_to_4 = [0 for i in range(config.FOURYEARS)]
I_Daily_Evap_5_to_8 = [0 for i in range(config.FOURYEARS)]
I_Daily_Evap_9_to_12 = [0 for i in range(config.FOURYEARS)]
I_Daily_Evap_13_to_16 = [0 for i in range(config.FOURYEARS)]
I_Daily_Evap_17_to_20 = [0 for i in range(config.FOURYEARS)]
I_Daily_Evap_21_to_24 = [0 for i in range(config.FOURYEARS)]
I_Daily_Evap_25_to_28 = [0 for i in range(config.FOURYEARS)]
I_Daily_Evap_29_to_32 = [0 for i in range(config.FOURYEARS)]


if I_RainDoY <= 1460:
    I_Daily_Evapotrans = I_Daily_Evap_1_to_4
elif I_RainDoY <= 2920:
    I_Daily_Evapotrans = I_Daily_Evap_5_to_8
elif I_RainDoY <= 4380:
    I_Daily_Evapotrans = I_Daily_Evap_9_to_12
elif I_RainDoY <= 5840:
    I_Daily_Evapotrans = I_Daily_Evap_13_to_16
elif I_RainDoY <= 7300:
    I_Daily_Evapotrans = I_Daily_Evap_17_to_20
elif I_RainDoY <= 8760:
    I_Daily_Evapotrans = I_Daily_Evap_21_to_24
else:
    I_Daily_Evapotrans = I_Daily_Evap_25_to_28
