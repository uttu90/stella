__author__ = 'tuhv'

from pylab import *
from stella import *
import numpy as np

# Form the time simulation
start = 0
stop = 12.0
step = 0.25
time_simulation = np.arange(start, stop, step)

# Form the model
stock = Stock(100)


def f_flow(x):
    return x[0]


def f_converter(x):
    return 10


flow = Flow(step, f_flow, source_stock=None, destination_stock=stock)
converter = Converter(f_converter)

#Simulation
for time in time_simulation:
    flow(converter())
    stock()

plot(np.append(time_simulation, stop), stock.values)
show()

