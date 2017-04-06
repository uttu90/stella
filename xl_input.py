__author__="TuHV"

import xlrd
from os.path import join, dirname, abspath

import utils

fname = join(dirname(dirname(abspath(__file__))), 'stella','GenRiver_Vietnam (20 LC) 2014.xls')

xl_workbook = xlrd.open_workbook(fname)
sheet_names = xl_workbook.sheet_names()

wksheet = xl_workbook.sheet_by_name("LINKTOSTELLA")

yearlyData = utils.read_array_data(wksheet, col_start=1, col_end=25, row_start=3, row_end=1460)
I_InputDataYears = wksheet.col_values(colx=26, start_rowx=4, end_rowx=8)
landCoverData = utils.read_table_data(wksheet, col_start=27, col_end=30, row_start=3, row_end=15)
monthlyData = utils.read_table_data(wksheet, col_start=30, col_end=43, row_start=3, row_end=16)
subcatchmentData = utils.read_table_data(wksheet, col_start=49, col_end=86, row_start=3, row_end=24)

wksheet2 = xl_workbook.sheet_by_name("LinktoStella9(2)")
ifracData = utils.read_array_data(wksheet2, col_start=0, col_end=80, row_start=4, row_end=24)
