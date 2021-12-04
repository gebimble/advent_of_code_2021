import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

from advent_of_code_2021.day_01 import data



def count_increases(data: np.ndarray, window: int = 1) -> int:
    """count.

    Parameters
    ----------
    data : np.ndarray
        Input array.

    Returns
    -------
    int
        Sum of instances of the current element having a greater value than the
        previous element.

    """
    data = sliding_window_view(data, window_shape=window).sum(axis=1)
    return np.sum(data[1:] > data[:-1])

print(f'Part 1 solution: {count_increases(data)}')
print(f'Part 2 solution: {count_increases(data, window=3)}')
