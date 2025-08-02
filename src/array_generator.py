import numpy as np

def generate_1d_array(size, low=1, high=100):
    return np.random.randint(low, high, size)

def generate_2d_array(rows, cols, low=1, high=100):
    return np.random.randint(low, high, (rows, cols))

def generate_3d_array(shape, low=1, high=100):
    return np.random.randint(low, high, shape)
