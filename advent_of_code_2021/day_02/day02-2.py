from pathlib import Path
from dataclasses import dataclass
import numpy as np


input_file = Path(__file__).parent / '../../data/input02.txt'

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


position = np.array([0, 0, 0])

with input_file.open('r') as f:
    for line in f:
        direction, magnitude = line.split()
        index, op = move_dict[direction]
        magnitude = int(magnitude)

        position[index] = op(position[index], magnitude)

print(np.prod(position[:2]))
