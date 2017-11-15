import numpy as np


def inflow_constrain(inflow):
    return np.multiply(inflow > 0, inflow)


def biflow_constrain(biflow, stock, non_negative):
    if not non_negative:
        return biflow
    else:
        return np.add(np.multiply(biflow > 0, biflow), np.multiply(biflow < 0, np.minimum(-biflow, stock)))


def outflow_constrain(outflow=0, stock=0, inflow=0, non_negative=True, dt=1):
    if not non_negative:
        return outflow
    else:
        return np.multiply(outflow > 0, np.minimum(outflow, np.add(stock, inflow * dt)))

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
