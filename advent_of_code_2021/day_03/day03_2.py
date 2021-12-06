from operator import gt, lt
import numpy as np
from scipy import stats

from advent_of_code_2021.day_03 import data

data = np.array([[int(x) for x in element] for element in data])
breakpoint()

mode, count = [np.array(x[0]) for x in stats.mode(data, axis=0)]
flipped = [1 if x == 0 else 0 for x in mode]

def bin_list_to_int(bin_list: str) -> int:
    """bin_to_int.

    Parameters
    ----------
    binary : str
        Binary number string

    Returns
    -------
    int
        Base 2 integer derived from binary number string.

    """
    return int(''.join([str(x) for x in bin_list.ravel()]), 2)

def count_from_left(array: np.ndarray) -> int:
    """count_from_left.

    Parameters
    ----------
    array : np.ndarray
        Binary array.

    Returns
    -------
    i: int
        Number of conseucitve True elements.

    """
    i = 0

    for element in array:
        if element:
            i += 1
        else:
            return i

    return i

def get_rating(data: np.ndarray,
               min_max,
               default: int
              ) -> np.ndarray:
    """get_rating.

    Parameters
    ----------
    data : np.ndarray
        Complete data input.
    array : np.ndarray
        Comparison array.
    counts : np.ndarray
        Instances of values in `array` occuring in each column of `data`.

    Returns
    -------
    np.ndarray
        Line of `data` that corresponds to the highest number of consecutive 
        matches of values in `array`.

    """
    temp_data = data.copy()

    for x in range(0, temp_data.shape[1]):

        if temp_data.shape[0] == 1:
            return temp_data

        counts = {(temp_data[:, x] == y).sum(): y for y in (0, 1)}

        if len(set(counts.keys())) == 1:
            value = default
        else:
            min_max_key = min_max(list(counts.keys()))
            value = counts[min_max_key]

        keep = temp_data[:, x] == value

        temp_data = temp_data[keep]

    return temp_data


oxygen = get_rating(data, max, 1)
breakpoint()
carbon_dioxide = get_rating(data, min, 0)

breakpoint()

print(bin_list_to_int(oxygen)*bin_list_to_int(carbon_dioxide))
