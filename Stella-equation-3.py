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
stock = Stock(1000)


def f_birth_flow(x):
    return x[0]*x[1]


def f_death_flow(x):
    return x[0]


def f_birth_converter(x):
    return 0.11

birth_fraction = Converter(f_birth_converter)

birth_flow = Flow(step, f_birth_flow, None, stock)
death_flow = Flow(step, f_death_flow, stock, None)


#Simulation
for time in time_simulation:
    birth_fraction()
    birth_flow(birth_fraction.value, stock.value)
    death_flow(100)
    stock()

plot(np.append(time_simulation, stop), stock.values)
show()
