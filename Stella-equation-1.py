__author__ = 'tuhv'

from pylab import *
from stella_model_ol import *
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
    converter()
    flow(converter.value)
    stock()

values = [100]
for timve in time_simulation:
    values.append(values[-1] + 10 * step)

plot(np.append(time_simulation, stop), values)
show()
