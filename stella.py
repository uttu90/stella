__author__ = 'TuHV'

from pylab import *


class Stock(object):
    ''''''
    def __init__(self, init_value, flow_in=None, flow_out=None, description=None, unit=None):
        self.values = []
        self.values.append(init_value)
        self.flow_in = flow_in
        self.flow_out = flow_out
        self.description = description
        self.unit = unit

    def run(self, delta):
        flow_in = 0 if not self.flow_in else self.flow_in.change(self.values[-1])
        flow_out = 0 if not self.flow_out else self.flow_out.change(self.values[-1])
        new_value = self.values[-1] + (flow_in - flow_out)  * delta
        self.values.append(new_value)


class Flow(object):
    ''''''
    def __init__(self, change_function):
        self.change = change_function
        #self.my_args = args

if __name__ == '__main__':
    def f(x):
        return x
    flow = Flow(f)
    stock = Stock(1, flow)
    for i in range(0, 99):
        stock.run(1)
    plot(stock.values)
    print(stock.values)
    show()
