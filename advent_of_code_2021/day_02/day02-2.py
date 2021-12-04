from pathlib import Path
from dataclasses import dataclass
import numpy as np

from advent_of_code_2021.get_data import get_data


def forward_func(arr: np.ndarray, magnitude: int) -> np.ndarray:
    """forward_func.

    Parameters
    ----------
    arr : np.ndarray
        Input array.
    magnitude : int
        Size of forward movement.

    Returns
    -------
    np.ndarray

    """
    arr[0] += magnitude
    arr[1] += arr[2] * magnitude
    return arr

move_dict = {
    'forward': (np.s_[:], forward_func),
    'down': (np.s_[2], np.add),
    'up': (np.s_[2], np.subtract),
}


json = get_data(2)

position = np.array([0, 0, 0])

for direction, magnitude in json['data']:
    index, op = move_dict[direction]

    position[index] = op(position[index], magnitude)

print(np.prod(position[:2]))
