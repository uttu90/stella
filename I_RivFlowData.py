import numpy as np
import config
import calculate

I_SubcContr_ = 1
O_CumDebitData = [0]

I_RFlowData_Year_1_to_4 = np.zeros(config.FOURYEARS)
I_RFlowData_Year_5_to_8 = np.zeros(config.FOURYEARS)
I_RFlowData_Year_9_to_12 = np.zeros(config.FOURYEARS)
I_RFlowData_Year_13_to_16 = np.zeros(config.FOURYEARS)
I_RFlowData_Year_17_to_20 = np.zeros(config.FOURYEARS)
I_RFlowData_Year_21_to_24 = np.zeros(config.FOURYEARS)
I_RFlowData_Year_25_to_28 = np.zeros(config.FOURYEARS)
I_RFlowData_Year_29_to_32 = np.zeros(config.FOURYEARS)

if I_Simulation_Time <= 1460:
    I_DebitTime = I_RFlowData_Year_1_to_4
elif I_Simulation_Time <= 2920:
    I_DebitTime = I_RFlowData_Year_5_to_8
elif I_Simulation_Time <= 4380:
    I_DebitTime = I_RFlowData_Year_9_to_12
elif I_Simulation_Time <= 5840:
    I_DebitTime = I_RFlowData_Year_13_to_16
elif I_Simulation_Time <= 7300:
    I_DebitTime = I_RFlowData_Year_17_to_20
elif I_Simulation_Time <= 8760:
    I_DebitTime = I_RFlowData_Year_21_to_24
elif I_Simulation_Time <= 10220:
    I_DebitTime = I_RFlowData_Year_25_to_28
else:
    I_DebitTime = I_RFlowData_Year_29_to_32

I_ContrSubcArea = I_RelArea * I_SubcContr_
I_RFlowDataQmecs = I_DebitTime

I_RFlowdata_mmday = ((I_RFlowDataQmecs*24*3600*10^3)/(np.sum(I_ContrSubcArea)*I_TotalArea*10^6
                     if np.sum(I_ContrSubcArea) > 0
                     else 0))
calculate.update(O_CumDebitData, inflow=I_RFlowdata_mmday, outflow=0, dt=config.dt)
