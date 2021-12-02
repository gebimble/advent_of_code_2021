from pathlib import Path
from dataclasses import dataclass
import numpy as np


input_file = Path(__file__).parent / '../../data/input02.txt'

move_dict = {
    'forward': (0, np.add),
    'down': (1, np.add),
    'up': (1, np.subtract),
}


position = np.array([0, 0])

with input_file.open('r') as f:
    for line in f:
        direction, magnitude = line.split()
        index, op = move_dict[direction]
        magnitude = int(magnitude)

        position[index] = op(position[index], magnitude)

print(np.prod(position))
