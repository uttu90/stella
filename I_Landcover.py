import numpy as np

import config

I_InterceptClass = np.zeros(config.LANDCOVERTYPE)
I_RelDroughtFract = np.zeros(config.LANDCOVERTYPE)

D_FeedingIntoLake_ = np.zeros(config.SUBCATCHMENT)
I_RoutingDistance = np.zeros(config.SUBCATCHMENT)
I_Area = np.zeros(config.SUBCATCHMENT)
I_TotalArea = np.sum(I_Area)
I_RelArea = I_Area/I_TotalArea if I_TotalArea else 0

I_Frac_1_1 = np.zeros(config.SUBCATCHMENT)
I_Frac_2_1 = np.zeros(config.SUBCATCHMENT)
I_Frac_3_1 = np.zeros(config.SUBCATCHMENT)
I_Frac_4_1 = np.zeros(config.SUBCATCHMENT)
I_Frac_5_1 = np.zeros(config.SUBCATCHMENT)
I_Frac_6_1 = np.zeros(config.SUBCATCHMENT)
I_Frac_7_1 = np.zeros(config.SUBCATCHMENT)
I_Frac_8_1 = np.zeros(config.SUBCATCHMENT)
I_Frac_9_1 = np.zeros(config.SUBCATCHMENT)
I_Frac_10_1 = np.zeros(config.SUBCATCHMENT)
I_Frac_11_1 = np.zeros(config.SUBCATCHMENT)
I_Frac_12_1 = np.zeros(config.SUBCATCHMENT)
I_Frac_13_1 = np.zeros(config.SUBCATCHMENT)
I_Frac_14_1 = np.zeros(config.SUBCATCHMENT)
I_Frac_15_1 = np.zeros(config.SUBCATCHMENT)
I_Frac_16_1 = np.zeros(config.SUBCATCHMENT)
I_Frac_17_1 = np.zeros(config.SUBCATCHMENT)
I_Frac_18_1 = np.zeros(config.SUBCATCHMENT)
I_Frac_19_1 = np.zeros(config.SUBCATCHMENT)
I_Frac_20_1 = np.zeros(config.SUBCATCHMENT)
I_FracVegClass_1 = np.concatenate((I_Frac_1_1, I_Frac_2_1, I_Frac_3_1, I_Frac_4_1, I_Frac_5_1,
                                   I_Frac_6_1, I_Frac_7_1, I_Frac_8_1, I_Frac_9_1, I_Frac_10_1,
                                   I_Frac_11_1, I_Frac_12_1, I_Frac_13_1, I_Frac_14_1, I_Frac_15_1,
                                   I_Frac_16_1, I_Frac_17_1, I_Frac_18_1, I_Frac_19_1, I_Frac_20_1))

I_Frac_1_2 = np.zeros(config.SUBCATCHMENT)
I_Frac_2_2 = np.zeros(config.SUBCATCHMENT)
I_Frac_3_2 = np.zeros(config.SUBCATCHMENT)
I_Frac_4_2 = np.zeros(config.SUBCATCHMENT)
I_Frac_5_2 = np.zeros(config.SUBCATCHMENT)
I_Frac_6_2 = np.zeros(config.SUBCATCHMENT)
I_Frac_7_2 = np.zeros(config.SUBCATCHMENT)
I_Frac_8_2 = np.zeros(config.SUBCATCHMENT)
I_Frac_9_2 = np.zeros(config.SUBCATCHMENT)
I_Frac_10_2 = np.zeros(config.SUBCATCHMENT)
I_Frac_11_2 = np.zeros(config.SUBCATCHMENT)
I_Frac_12_2 = np.zeros(config.SUBCATCHMENT)
I_Frac_13_2 = np.zeros(config.SUBCATCHMENT)
I_Frac_14_2 = np.zeros(config.SUBCATCHMENT)
I_Frac_15_2 = np.zeros(config.SUBCATCHMENT)
I_Frac_16_2 = np.zeros(config.SUBCATCHMENT)
I_Frac_17_2 = np.zeros(config.SUBCATCHMENT)
I_Frac_18_2 = np.zeros(config.SUBCATCHMENT)
I_Frac_19_2 = np.zeros(config.SUBCATCHMENT)
I_Frac_20_2 = np.zeros(config.SUBCATCHMENT)
I_FracVegClass_2 = np.concatenate((I_Frac_1_2, I_Frac_2_2, I_Frac_3_2, I_Frac_4_2, I_Frac_5_2,
                                   I_Frac_6_2, I_Frac_7_2, I_Frac_8_2, I_Frac_9_2, I_Frac_10_2,
                                   I_Frac_11_2, I_Frac_12_2, I_Frac_13_2, I_Frac_14_2, I_Frac_15_2,
                                   I_Frac_16_2, I_Frac_17_2, I_Frac_18_2, I_Frac_19_2, I_Frac_20_2))
I_Frac_1_3 = np.zeros(config.SUBCATCHMENT)
I_Frac_2_3 = np.zeros(config.SUBCATCHMENT)
I_Frac_3_3 = np.zeros(config.SUBCATCHMENT)
I_Frac_4_3 = np.zeros(config.SUBCATCHMENT)
I_Frac_5_3 = np.zeros(config.SUBCATCHMENT)
I_Frac_6_3 = np.zeros(config.SUBCATCHMENT)
I_Frac_7_3 = np.zeros(config.SUBCATCHMENT)
I_Frac_8_3 = np.zeros(config.SUBCATCHMENT)
I_Frac_9_3 = np.zeros(config.SUBCATCHMENT)
I_Frac_10_3 = np.zeros(config.SUBCATCHMENT)
I_Frac_11_3 = np.zeros(config.SUBCATCHMENT)
I_Frac_12_3 = np.zeros(config.SUBCATCHMENT)
I_Frac_13_3 = np.zeros(config.SUBCATCHMENT)
I_Frac_14_3 = np.zeros(config.SUBCATCHMENT)
I_Frac_15_3 = np.zeros(config.SUBCATCHMENT)
I_Frac_16_3 = np.zeros(config.SUBCATCHMENT)
I_Frac_17_3 = np.zeros(config.SUBCATCHMENT)
I_Frac_18_3 = np.zeros(config.SUBCATCHMENT)
I_Frac_19_3 = np.zeros(config.SUBCATCHMENT)
I_Frac_20_3 = np.zeros(config.SUBCATCHMENT)
I_FracVegClass_3 = np.concatenate((I_Frac_1_3, I_Frac_2_3, I_Frac_3_3, I_Frac_4_3, I_Frac_5_3,
                                   I_Frac_6_3, I_Frac_7_3, I_Frac_8_3, I_Frac_9_3, I_Frac_10_3,
                                   I_Frac_11_3, I_Frac_12_3, I_Frac_13_3, I_Frac_14_3, I_Frac_15_3,
                                   I_Frac_16_3, I_Frac_17_3, I_Frac_18_3, I_Frac_19_3, I_Frac_20_3))
I_Frac_1_4 = np.zeros(config.SUBCATCHMENT)
I_Frac_2_4 = np.zeros(config.SUBCATCHMENT)
I_Frac_3_4 = np.zeros(config.SUBCATCHMENT)
I_Frac_4_4 = np.zeros(config.SUBCATCHMENT)
I_Frac_5_4 = np.zeros(config.SUBCATCHMENT)
I_Frac_6_4 = np.zeros(config.SUBCATCHMENT)
I_Frac_7_4 = np.zeros(config.SUBCATCHMENT)
I_Frac_8_4 = np.zeros(config.SUBCATCHMENT)
I_Frac_9_4 = np.zeros(config.SUBCATCHMENT)
I_Frac_10_4 = np.zeros(config.SUBCATCHMENT)
I_Frac_11_4 = np.zeros(config.SUBCATCHMENT)
I_Frac_12_4 = np.zeros(config.SUBCATCHMENT)
I_Frac_13_4 = np.zeros(config.SUBCATCHMENT)
I_Frac_14_4 = np.zeros(config.SUBCATCHMENT)
I_Frac_15_4 = np.zeros(config.SUBCATCHMENT)
I_Frac_16_4 = np.zeros(config.SUBCATCHMENT)
I_Frac_17_4 = np.zeros(config.SUBCATCHMENT)
I_Frac_18_4 = np.zeros(config.SUBCATCHMENT)
I_Frac_19_4 = np.zeros(config.SUBCATCHMENT)
I_Frac_20_4 = np.zeros(config.SUBCATCHMENT)
I_FracVegClass_4 = np.concatenate((I_Frac_1_4, I_Frac_2_4, I_Frac_3_4, I_Frac_4_4, I_Frac_5_4,
                                   I_Frac_6_4, I_Frac_7_4, I_Frac_8_4, I_Frac_9_4, I_Frac_10_4,
                                   I_Frac_11_4, I_Frac_12_4, I_Frac_13_4, I_Frac_14_4, I_Frac_15_4,
                                   I_Frac_16_4, I_Frac_17_4, I_Frac_18_4, I_Frac_19_4, I_Frac_20_4))
I_FracVegClasses = np.concatenate((I_FracVegClass_1, I_FracVegClass_2, I_FracVegClass_3, I_FracVegClass_4))

I_InputDataYears = [0, 10, 24, 30]
I_Flag1 = 1 if I_Simulation_Time < I_InputDataYears[1] else 0 # 0: Start, 1: Trans1, 2: Trans2, 3: End
I_Flag2 = 1 if I_Simulation_Time < I_InputDataYears[2] and I_Flag1 == 0 else 0

I_GWRelFrac1 = np.zeros(config.SUBCATCHMENT)
I_GWRelFrac2 = np.zeros(config.SUBCATCHMENT)
I_GWRelFrac3 = np.zeros(config.SUBCATCHMENT)
I_GWRelFrac4 = np.zeros(config.SUBCATCHMENT)
I_GWRelFracs = np.concatenate((I_GWRelFrac1, I_GWRelFrac2, I_GWRelFrac3, I_GWRelFrac4))

I_MaxDynGWSub1 = np.zeros(config.SUBCATCHMENT)
I_MaxDynGWSub2 = np.zeros(config.SUBCATCHMENT)
I_MaxDynGWSub3 = np.zeros(config.SUBCATCHMENT)
I_MaxDynGWSub4 = np.zeros(config.SUBCATCHMENT)
I_MaxDynGWSubs = np.concatenate((I_MaxDynGWSub1, I_MaxDynGWSub2, I_MaxDynGWSub3, I_MaxDynGWSub4))

I_PWPSub1 = np.zeros(config.SUBCATCHMENT)
I_PWPSub2 = np.zeros(config.SUBCATCHMENT)
I_PWPSub3 = np.zeros(config.SUBCATCHMENT)
I_PWPSub4 = np.zeros(config.SUBCATCHMENT)
I_PWPSubs = np.concatenate((I_PWPSub1, I_PWPSub2, I_PWPSub3, I_PWPSub4))

I_SoilSatminFCSub1 = np.zeros(config.SUBCATCHMENT)
I_SoilSatminFCSub2 = np.zeros(config.SUBCATCHMENT)
I_SoilSatminFCSub3 = np.zeros(config.SUBCATCHMENT)
I_SoilSatminFCSub4 = np.zeros(config.SUBCATCHMENT)
I_SoilSatminFCSubs = np.concatenate((I_SoilSatminFCSub1, I_SoilSatminFCSub2, I_SoilSatminFCSub3, I_SoilSatminFCSub4))

I_RivFlowTime1 = np.zeros(config.SUBCATCHMENT)
I_RivFlowTime2 = np.zeros(config.SUBCATCHMENT)
I_RivFlowTime3 = np.zeros(config.SUBCATCHMENT)
I_RivFlowTime4 = np.zeros(config.SUBCATCHMENT)
I_RivFlowTimes = np.concatenate((I_RivFlowTime1, I_RivFlowTime2, I_RivFlowTime3, I_RivFlowTime4))

I_AvailWatSub1 = np.zeros(config.SUBCATCHMENT)
I_AvailWatSub2 = np.zeros(config.SUBCATCHMENT)
I_AvailWatSub3 = np.zeros(config.SUBCATCHMENT)
I_AvailWatSub4 = np.zeros(config.SUBCATCHMENT)
I_AvailWatSubs = np.concatenate((I_AvailWatSub1, I_AvailWatSub2, I_AvailWatSub3, I_AvailWatSub4))

I_TopSoilBD_BDRef1 = np.zeros(config.SUBCATCHMENT)
I_TopSoilBD_BDRef2 = np.zeros(config.SUBCATCHMENT)
I_TopSoilBD_BDRef3 = np.zeros(config.SUBCATCHMENT)
I_TopSoilBD_BDRef4 = np.zeros(config.SUBCATCHMENT)
I_TopSoilBD_BDRefs = np.concatenate((I_TopSoilBD_BDRef1, I_TopSoilBD_BDRef2, I_TopSoilBD_BDRef3, I_TopSoilBD_BDRef4))

def get_variable_now(array_values):
    global I_Simulation_Time
    global I_InputDataYears
    global I_Flag1
    global I_Flag2
    if I_Flag1:
        result = (array_values[0] +
                  (array_values[1] - array_values[0]) *
                  (int(I_Simulation_Time/365) - I_InputDataYears[0]) /
                  (I_InputDataYears[1] - I_InputDataYears[0]))
    elif I_Flag2:
        result = (array_values[1] +
                  (array_values[2] - array_values[1]) *
                  (int(I_Simulation_Time/365) - I_InputDataYears[1]) /
                  (I_InputDataYears[2] - I_InputDataYears[1]))
    else:
        result = (array_values[2] +
                  (array_values[3] - array_values[2]) *
                  (int(I_Simulation_Time/365) - I_InputDataYears[2]) /
                  (I_InputDataYears[3] - I_InputDataYears[2]))
    return result

I_GWRelFracNow = get_variable_now(I_GWRelFracs)
I_MaxDynGwSubNow = get_variable_now(I_MaxDynGWSubs)
I_FracVegClassNow = get_variable_now(I_FracVegClasses)
I_PWPSubNow = get_variable_now(I_PWPSubs)
I_SoilSatminFCSubNow = get_variable_now(I_SoilSatminFCSubs)
I_RivFlowTimeNow = get_variable_now(I_RivFlowTimes)
I_TopSoilBD_BDRefNow = get_variable_now(I_TopSoilBD_BDRefs)
I_AvailWatClassNow = get_variable_now(I_AvailWatSubs)

I_FracVegClassSum1 = np.sum(I_FracVegClass_1)
I_FracVegClassSum2 = np.sum(I_FracVegClass_2)
I_FracVegClassSum3 = np.sum(I_FracVegClass_3)
I_FracVegClassSum4 = np.sum(I_FracVegClass_4)
I_FracVegClassSumNow = np.sum(I_FracVegClassNow)
