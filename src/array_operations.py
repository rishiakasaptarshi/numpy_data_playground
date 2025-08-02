import numpy as np

def arithmetic_operations(arr1, arr2):
    return {
        "addition": arr1 + arr2,
        "subtraction": arr1 - arr2,
        "multiplication": arr1 * arr2,
        "division": np.divide(arr1, arr2, out=np.zeros_like(arr1, dtype=float), where=arr2!=0)
    }

def filter_even(arr):
    return arr[arr % 2 == 0]

def filter_odd(arr):
    return arr[arr % 2 != 0]

def row_col_sum(arr):
    return {"row_sum": arr.sum(axis=1), "col_sum": arr.sum(axis=0)}

def swap_rows(arr, row1, row2):
    arr[[row1, row2]] = arr[[row2, row1]]
    return arr

def swap_columns(arr, col1, col2):
    arr[:, [col1, col2]] = arr[:, [col2, col1]]
    return arr

def reshape_array(arr, new_shape):
    return arr.reshape(new_shape)
