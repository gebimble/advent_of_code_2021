from typing import List, Dict
import numpy as np
from copy import deepcopy

from advent_of_code_2021.day_02 import data
from advent_of_code_2021 import Vector


move_dict = {
    'forward': (0, np.add),
    'down': (1, np.add),
    'up': (1, np.subtract),
}

def move(vector: Vector,
         position: np.ndarray = None,
         move_dict: Dict = move_dict,
         start_position: np.ndarray = np.array([0, 0])) -> np.ndarray:

    direction, magnitude = vector

    index, op = move_dict[direction]

    if position is None:
        position = deepcopy(start_position)

    position[index] = op(position[index], magnitude)

    return  position

def cum_move(move_list: List[Vector], position=None, **kwargs) -> np.ndarray:

    position = position

    for vector in move_list:
        position = move(vector, position=position, **kwargs)

    return position

if __name__ == '__main__':
    position = cum_move(data)

    print(np.prod(position))
