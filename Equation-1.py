__author__ = 'tuhv'

from pylab import *
from stella import *


stock_1 = Stock(200000)
stock_2 = Stock(100000)


def f1(x):
    return 10*x[0]


def f2(x):
    return x[0]

flow_1 = Flow(f1, stock_1, None)
flow_2 = Flow(f2, stock_2, None)

for i in range(0, 100):
    x = flow_2(10)
    print("x: " + str(x))
    y = flow_1(x)
    print("y: " + str(y))
    stock_2()
    stock_1()

print(stock_1.values)
print(stock_2.values)

plot(stock_1.values)
plot(stock_2.values)
show()