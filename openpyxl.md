# Installation
  - pip install openpyxl

# Basic tutorial
## Open a workbook:
  - Note: Only '.xlsx', '.xslm' can be opened.
  - If we use to open '.xls' file: convert to '.xlsx' or '.xslm' file.

  1. Syntax:
    - file = openpyxl.load_workbook(filename, ..)
    - attributes:
      - active: the active worksheet
      - sheetnames: a list contains names of worksheets 
  2.  