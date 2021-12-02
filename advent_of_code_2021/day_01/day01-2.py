from pathlib import Path
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view


input_file = Path(__file__).parent / 'input01-1.txt'

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

data = np.loadtxt(input_file, dtype=int)

print(count_increases(data))
print(count_increases(data, window=3))
