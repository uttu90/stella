dt = 1
x = [1]
y = [1]
dx = 1
dy = 1
for i in range(0, 12):
    x.append(x[i] + dx * dt)
    y.append(y[i] + x[i] * dt)

print x
print y