import numpy as np

def update(stock, inflow=0, outflow=0, dt=1, non_negative=True):
    value = np.add(stock[-1], (inflow - outflow) * dt)
    if non_negative:
        value = np.maximum(0, value)
    stock.append(value)


def update_conveyor(stock, inflow=0, outflow=1, time=0, dt=1):
    leak = np.multiply(outflow> time, np.ones_like(outflow))
    value = np.add(stock[-1], (inflow - inflow * leak) * dt)
    stock.append(value)

if __name__ == '__main__':
    stock = [0]
    inflow = 2
    outflow = 2
    dt = 1
    simulation_time = range(12)
    for time in simulation_time:
        update_conveyor(stock, inflow, outflow, time, dt)
    print stock
