__author__="TuHV"

import xlrd
from os.path import join, dirname, abspath

fname = join(dirname(dirname(abspath(__file__))), 'stella','GenRiver_Vietnam (20 LC) 2014.xls')

#Open the workbook
xl_workbook = xlrd.open_workbook(fname)
sheet_names = xl_workbook.sheet_names()
print sheet_names

wksheet = xl_workbook.sheet_by_name("LINKTOSTELLA")
print wksheet.name
print wksheet.nrows
print wksheet.ncols

col = wksheet.col_values(27)
print col
col1 = [x for x in col if x != '']
print col1






