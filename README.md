# stella
# This work has two parts
## Part 1: Use Python to read an Excel input file. Use openpyxls (https://openpyxl.readthedocs.io/en/default/usage.html)

## Part 2: 
  - Build Stella fundamental classes like classes in Python: Stock, Flow, Converter, Connector
  - Translate from Stella graph model to Python model

## Extension:
  - Using maps to calculate subcatchment path: Run another program to calculate subcatchment path and then input data to the Excel file

## Build Stella fundamental classes of in Python
  - Stock: 
    - Declare a stock: s = Stock(init_value)
    - Update the stock in each run: s()
    - Getting all values of stock: s.values()
  - Converter:
    - Equivalent to a function in Python.
    - Declare a converter: c = Converter(f_converter)
    - Getting value of the converter: c(parameters)
  - Flow:
    - Declare a flow: f = Flow(time_step, f_flow, source_stock, destination_stock)
    - Run a flow: f(parameters)
    - A flow will run to update the values of stocks inside it for each time step.
  - While:
    - init_value, time_step: numbers
    - f_converter, f_flow: functions
    - source_stock, destination_stock: Stocks
    - svalues(): Array of numbers