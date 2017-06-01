import numpy as np


def array_sum(array, shape=None):
    if not shape:
        return np.sum(array)
    array_shape = array.shape
    axis = 1 if array_shape[0] in shape else 0
    return np.sum(array, axis=axis).reshape(shape)