__author__ = 'TuHV'

import xlrd
import numpy as np
from os.path import join, dirname, abspath


fname = 'GenRiver_Vietnam (20 LC) 2014.xls'
sheet_name = 'LINKTOSTELLA'

FileName = join(dirname(dirname(abspath(__file__))), 'stella', fname)
xl_workbook = xlrd.open_workbook(FileName)
wksheet = xl_workbook.sheet_by_name(sheet_name)

def column2array(wksheet, colx=0, start_row=0):
    col = wksheet.col_values(colx=colx, start_rowx=start_row)
    return [x for x in col if x != '']

I_DailyRainYear_1_to_4 = column2array(wksheet, 1, 4)
I_DailyRainYear_5_to_8 = column2array(wksheet, 2, 4)
I_DailyRainYear_9_to_12 = column2array(wksheet, 3, 4)
I_DailyRainYear_13_to_16 = column2array(wksheet, 4, 4)
I_DailyRainYear_17_to_20 = column2array(wksheet, 5, 4)
I_DailyRainYear_21_to_24 = column2array(wksheet, 6, 4)
I_DailyRainYear_25_to_28 = column2array(wksheet, 7, 4)
I_DailyRainYear_29_to_32 = column2array(wksheet, 8, 4)


I_RFlowData_Year_1_to_4 = column2array(wksheet, 9, 4)
I_RFlowData_Year_5_to_8 = column2array(wksheet, 10, 4)
I_RFlowData_Year_9_to_12 = column2array(wksheet, 11, 4)
I_RFlowData_Year_13_to_16 = column2array(wksheet, 12, 4)
I_RFlowData_Year_17_to_20 = column2array(wksheet, 13, 4)
I_RFlowData_Year_21_to_24 = column2array(wksheet, 14, 4)
I_RFlowData_Year_25_to_28 = column2array(wksheet, 15, 4)
I_RFlowData_Year_29_to_32 = column2array(wksheet, 16, 4)

I_DailyETYear_1_to_4 = column2array(wksheet, 17, 4)
I_DailyETYear_5_to_8 = column2array(wksheet, 18, 4)
I_DailyETYear_9_to_12 = column2array(wksheet, 19, 4)
I_DailyETYear_13_to_16 = column2array(wksheet, 20, 4)
I_DailyETYear_17_to_20 = column2array(wksheet, 21, 4)
I_DailyETYear_21_to_24 = column2array(wksheet, 22, 4)
I_DailyETYear_25_to_28 = column2array(wksheet, 23, 4)
I_DailyETYear_29_to_32 = column2array(wksheet, 24, 4)