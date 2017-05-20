import numpy as np

x1 = np.array([[1, 2, 3], [4, 5, 6]])
x2 = np.array([[1], [5]])

print x1.shape, x2.shape
print np.add(x1, x2)
print np.multiply(x1, x2)


x = np.array([1,2,3])
print x.shape
print np.array([x]).shape

print np.sum(x1, axis=0)
print np.sum(x1, axis=1).shape

SUBCATCHMENT=3
COL = 2

testArray = np.zeros(shape=(SUBCATCHMENT, COL))
print testArray.shape

testVector = np.array([[1], [2], [3]])
print testVector.shape

np.add(testArray, testVector)
np.multiply(testArray, testVector)

print np.sum(testArray, axis=0), np.sum(testArray, axis=1)

print np.sum(testArray, axis=1).reshape(3, 1)
m = np.array([[1], [2], [3]])
print np.repeat(m, 2).reshape(3, 2)

np.divide(1, m)
np.minimum(1, m)