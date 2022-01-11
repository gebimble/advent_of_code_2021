from typing import List
from itertools import filterfalse

import numpy as np

from advent_of_code_2021 import Coordinate
from advent_of_code_2021.day_05 import data


def remove_diagonal(coords: List[Coordinate]) -> List[Coordinate]:
    determine = lambda c: ~(
        (c[0][0] == c[1][0])
        or (c[0][1] == c[1][1])
    )
    return list(filterfalse(determine, coords))

def produce_diagram(coords: List[Coordinate]) -> List[List[str]]:

    xmin, ymin = -np.inf, -np.inf
    xmax, ymax = np.inf, np.inf

    points = np.array(coords)

    xmin, ymin = points.min(axis=(0, 1))
    xmax, ymax = points.max(axis=(0, 1))

    array = np.zeros((xmax+1, ymax+1))

    for start, end in coords:
        if start[0] == end[0]:
            x_range = start[0]
        else:
            s, e = sorted((start[0], end[0]))
            x_range = slice(s, e+1)

        if start[1] == end[1]:
            y_range = start[1]
        else:
            s, e = sorted((start[1], end[1]))
            y_range = slice(s, e+1)


        array[x_range, y_range] += 1

    return array.T

def sum_crossovers(array: np.ndarray) -> int:
    return (array > 1).sum()

if __name__ == '__main__':
    filtered_data = remove_diagonal(data)
    crossovers = produce_diagram(filtered_data)
    print(sum_crossovers(crossovers))

