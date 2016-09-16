__author__ = 'tuhv'

from pylab import *
from stella import *
import numpy as np

# Form the time simulation
start = 0
stop = 50.0
step = 0.25
time_simulation = np.arange(start, stop, step)

# Form the model
stockX = Stock(100)
stockY = Stock(100)


def f_flow_1(x):
    return x[0]*x[1]

def f_flow_2(x):
    return x[0]*x[1]*x[2]

def f_flow_3(x):
    return x[0]*x[1]

def f_converter_a(x):
    return 0.2

def f_converter_b(x):
    return 0.001

def f_converter_c(x):
    return 0.01

a = Converter(f_converter_a)
b = Converter(f_converter_b)
c = Converter(f_converter_c)

flow_1 = Flow(step, f_flow_1, None, stockX)
flow_2 = Flow(step, f_flow_2, stockX, stockY)
flow_3 = Flow(step, f_flow_3, stockY, None)


#Simulation
for time in time_simulation:
    flow_1(a(), stockX.current_value())
    flow_2(stockX.current_value(), b(), stockY.current_value())
    flow_3(stockY.current_value(),c())
    stockX()
    stockY()

plot(np.append(time_simulation, stop), stockX.values(),'r--',np.append(time_simulation, stop) ,stockY.values())
show()


