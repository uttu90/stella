__author__ = 'TuHV'

from pylab import *


class Stock(object):
    ''''''
    def __init__(self, init_value):
        self._values = []
        self._values.append(init_value)
        self.change_value = init_value

    def current_value(self):
        return self._values[-1]

    def values(self):
        return self._values

    def __call__(self):
        self._values.append(self.change_value)

class Flow(object):
    ''''''
    def __init__(self, time_step, change_function, source_stock, destination_stock):
        self.change = change_function
        self.source_stock = source_stock
        self.destination_stock = destination_stock
        self.time_step = time_step

    def __call__(self, *args):
        if self.source_stock is not None:
            self.source_stock.change_value = self.source_stock.change_value - self.change(args)*self.time_step

        if self.destination_stock is not None:
            self.destination_stock.change_value = self.destination_stock.change_value + self.change(args)*self.time_step

        return self.change(args)


class Converter(object):
    '''

    '''
    def __init__(self, convert_function):
        self.convert_function = convert_function

    def __call__(self, *args):
        return self.convert_function(args)

if __name__ == '__main__':

    def v_flow(x):
        return x[0]

    def x_flow(x):
        return x[0]

    init_v = 0
    init_x = 0

    velocity = Stock(init_v)
    position = Stock(init_x)

    velocity_flow = Flow(v_flow, None, velocity)
    position_flow = Flow(x_flow, None, position)

    for i in range(0, 1000):
        velocity_flow(1)
        position_flow(velocity.current_value())
        velocity()
        position()
    print(position.values)
    plot(position.values)
    show()
    plot(velocity.values)
    show()
