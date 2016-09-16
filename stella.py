__author__ = 'TuHV'

from pylab import *


class Stock(object):
    ''''''
    def __init__(self, init_value):
        self.values = []
        self.values.append(init_value)

    def run(self):
        return self.values[-1]

    def update(self, new_value):
        self.values.append(new_value)

class Flow(object):
    ''''''
    def __init__(self, change_function, source_stock, destination_stock):
        self.change = change_function
        self.source_stock = source_stock
        self.destination_stock = destination_stock


    def __call__(self, *args):
        flow_in = 0 if not self.destination_stock else self.destination_stock() + self.change(args)
        flow_out = 0 if not self.source_stock else self.source_stock() + self.change(args)
        return flow_in, flow_out


class Converter(object):
    '''

    '''
    def __init__(self, convert_function):
        self.convert_function = convert_function


    def __call__(self, *args):
        return self.convert_function(args)

if __name__ == '__main__':
    def v_flow():

    init_v = 0
    init_x = 0

    velocity = Stock(init_v)
    position = Stock(init_x)
