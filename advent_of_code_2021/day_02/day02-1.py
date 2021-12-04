from pathlib import Path
from dataclasses import dataclass
import numpy as np

from advent_of_code_2021.get_data import get_data


move_dict = {
    'forward': (0, np.add),
    'down': (1, np.add),
    'up': (1, np.subtract),
}

json = get_data(2)

position = np.array([0, 0])

for direction, magnitude in json['data']:
    index, op = move_dict[direction]

    position[index] = op(position[index], magnitude)

print(np.prod(position))
