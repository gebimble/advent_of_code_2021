import numpy as np
from scipy import stats

from advent_of_code_2021.day_03 import data

mode = stats.mode(data, axis=0)[0][0]

gamma_rate_binary = ''.join([str(x) for x in mode])
epsilon_rate_binary = ''.join(['1' if x == '0' else '0' for x in gamma_rate_binary])

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

gamma_rate = bin_to_int(gamma_rate_binary)
epsilon_rate = bin_to_int(epsilon_rate_binary)

print(gamma_rate * epsilon_rate)
