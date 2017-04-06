def update(stock, inflow=0, outflow=0, dt=1):
    value = stock[-1] + (inflow - outflow) * dt
    stock.append(value)
