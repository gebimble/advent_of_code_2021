from dataclasses import dataclass
import numpy as np

from advent_of_code_2021.day_02 import data


move_dict = {
    'forward': (0, np.add),
    'down': (1, np.add),
    'up': (1, np.subtract),
}

position = np.array([0, 0])

for direction, magnitude in data:
    index, op = move_dict[direction]

    position[index] = op(position[index], magnitude)

print(np.prod(position))
