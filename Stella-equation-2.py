__author__ = 'tuhv'

from pylab import *
from stella_model_ol import *
import numpy as np

# Form the time simulation
start = 0
stop = 50.0
step = 0.25
time_simulation = np.arange(start, stop, step)

# Form the model
stock = Stock(np.array([50, 100]))


def f_flow(x):
    # print x
    return np.multiply(x[0], x[1])


def f_converter(x):
    return 0.1


flow = Flow(step, f_flow, source_stock=None, destination_stock=stock)
converter = Converter(f_converter)

#Simulation
for time in time_simulation:
    converter()
    flow(converter.value, stock.value)
    stock()

plot(np.append(time_simulation, stop), stock.values)
show()
