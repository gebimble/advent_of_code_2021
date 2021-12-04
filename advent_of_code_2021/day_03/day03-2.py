import numpy as np
from scipy import stats

from advent_of_code_2021.day_03 import data


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
    return int(''.join([str(x) for x in mode]), 2)

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
               array: np.ndarray,
               counts: np.ndarray) -> np.ndarray:
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

    threshold = data.shape[0]/2

    if (counts == threshold).any():
        locs = np.where(counts == threshold)
        array[locs] = 1

    match_array = np.apply_along_axis(count_from_left, 1, data == array)

    return data[np.where(match_array == match_array.max())]


oxygen = get_rating(data, mode, count)
carbon_dioxide = get_rating(data, flipped, count)

print(bin_list_to_int(oxygen)*bin_list_to_int(carbon_dioxide))
