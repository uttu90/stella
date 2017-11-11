import numpy as np


def update(stock, inflow=0, outflow=0, dt=1, non_negative=True):
    value = np.add(stock[-1], (inflow - outflow) * dt)
    if non_negative:
        value = np.maximum(0, value)
    stock.append(value)


def update_conveyor(stock, inflow=0, outflow=[0], transitTime=0, time=0, dt=1):
    # None
    new_value = np.add(stock[time], np.subtract(inflow, outflow[time]) * dt)
    # new_value = np.zeros_like(stock[time])
    stock.append(new_value)
    ts = int(np.max(np.around(transitTime)) + 1)
    # for future in range(1, ts):

    if len(outflow) < time + ts:
        outflow += [np.zeros_like(outflow[time]) for _ in range(len(outflow), time + ts)]
    for future in range(1, ts):
        outflow[time + future] = np.add(outflow[time + future], np.multiply(transitTime == future, inflow))
