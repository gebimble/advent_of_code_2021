from io import StringIO
import numpy as np

import pytest

from advent_of_code_2021.api.parsers.day_02 import get_vector
from advent_of_code_2021.day_02.day02_1 import move, cum_move


def test_output_to_numpy(day_02_example_text_input: pytest.fixture) -> np.ndarray:
    # GIVEN the example text
    # WHEN transformed into an integer list
    # THEN the actual array should equal the expected arrray
    actual = [get_vector(l)
              for l in StringIO(day_02_example_text_input).readlines()]

    expected = [
        ('forward', 5),
        ('down', 5),
        ('forward', 8),
        ('up', 3),
        ('down', 8),
        ('forward', 2),
    ]

    assert actual, 'No data pulled from input file.'
    assert actual == expected, 'Input file data differs from expected array.'

    return actual

def test_move(day_02_example_text_input: pytest.fixture) -> np.ndarray:
    # GIVEN the data harvested from `day_02_example_text_input`
    # WHEN a `Vector` is passed to the `move` function
    # THEN the elements of a `position` variable should equal those expected

    data = test_output_to_numpy(day_02_example_text_input)

    position = None

    position = move(data.pop(0), position)

    horizontal, depth = position

    assert horizontal == 5
    assert depth == 0

    position = move(data.pop(0), position)

    horizontal, depth = position

    assert horizontal == 5
    assert depth == 5

def test_cumulative_move(day_02_example_text_input: pytest.fixture) -> np.ndarray:
    # GIVEN the data harvested from `day_02_example_text_input`
    # WHEN that data is passed to the cumulative move (`cum_move`) function
    # THEN `cum_move` returns the cumulative position information from all
    #   elements in the data

    data = test_output_to_numpy(day_02_example_text_input)

    position = None

    for vector in data:
        position = move(vector, position)

    horizontal, depth = position

    assert horizontal == 15  # anticipated horizontal position for test case
    assert depth == 10  # anticipated depth for test case

    expected = 150
    actual = np.prod(position)

    assert actual == expected
