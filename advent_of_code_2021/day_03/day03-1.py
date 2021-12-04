import numpy as np
from scipy import stats

from advent_of_code_2021.day_03 import data

mode = stats.mode(data, axis=0)[0][0]

gamma = ''.join([str(x) for x in mode])
epsilon = ''.join(['1' if x == '0' else '0' for x in gamma])

def bin_to_int(binary: str) -> int:
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
    return int(binary, 2)

gamma_number = bin_to_int(gamma)
epsilon_number = bin_to_int(epsilon)

print(gamma_number * epsilon_number)
