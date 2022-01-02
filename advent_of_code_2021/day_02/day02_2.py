import numpy as np

from advent_of_code_2021.day_02 import data
from advent_of_code_2021.day_02.day02_1 import move, cum_move


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


if __name__ == '__main__':
    position = cum_move(data, position=None, move_dict=move_dict, start_position=np.array([0,0,0]))

    print(np.prod(position[:2]))
