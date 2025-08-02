import numpy as np

def stack_arrays(arr1, arr2, axis=0):
    return np.stack((arr1, arr2), axis=axis)

def concatenate_arrays(arr1, arr2, axis=0):
    return np.concatenate((arr1, arr2), axis=axis)
