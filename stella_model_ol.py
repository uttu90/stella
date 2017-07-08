__author__ = 'TuHV'

from pylab import *


class Stock(object):
    ''''''
    def __init__(self, init_value):
        self.value = init_value
        self._values = []
        self._values.append(self.value)
        # self.change_value = init_value

    @property
    def values(self):
        return self._values

    def __call__(self):
        self._values.append(self.value)


class Flow(object):
    ''''''
    def __init__(self, time_step, change_function, source_stock, destination_stock):
        self.change = change_function
        self.source_stock = source_stock
        self.destination_stock = destination_stock
        self.time_step = time_step
        # self._value = None

    def __call__(self, *args):
        if self.source_stock is not None:
            self.source_stock.value = self.source_stock.value - self.change(args)*self.time_step

        if self.destination_stock is not None:
            self.destination_stock.value = self.destination_stock.value + self.change(args)*self.time_step

        self._value = self.change(args) * self.time_step

    @property
    def value(self):
        return self._value
        # return self.change(args)


class Converter(object):
    '''

    '''
    def __init__(self, convert_function):
        self.convert_function = convert_function

    def __call__(self, *args):
        self._value = self.convert_function(args)

    @property
    def value(self):
        return self._value
