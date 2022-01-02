from typing import List
import numpy as np

from advent_of_code_2021.day_02 import data
from advent_of_code_2021 import Vector


move_dict = {
    'forward': (0, np.add),
    'down': (1, np.add),
    'up': (1, np.subtract),
}

def move(vector: Vector, position: np.ndarray = None) -> np.ndarray:
    direction, magnitude = vector

    index, op = move_dict[direction]

    if position is None:
        position = np.array([0, 0])

    position[index] = op(position[index], magnitude)

    return  position

def cum_move(move_list: List[Vector], position: np.ndarray = None) -> np.ndarray:

    if position is None:
        position = np.array([0, 0])

    for vector in data:
        position = move(vector, position)
    
    return position

position = None

position = cum_move(data, position)

print(np.prod(position))
