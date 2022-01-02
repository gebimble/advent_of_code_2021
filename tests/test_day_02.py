from io import StringIO
import numpy as np

import pytest

from advent_of_code_2021.api.parsers.day_02 import get_vector
from advent_of_code_2021.day_02.day02_1 import move, cum_move
from advent_of_code_2021.day_02.day02_2 import move_dict


def test_output_to_numpy(day_02_example_text_input: pytest.fixture,
                         day_02_example_data: pytest.fixture) -> np.ndarray:
    # GIVEN the example text
    # WHEN transformed into an integer list
    # THEN the actual array should equal the expected arrray
    actual = [get_vector(l)
              for l in StringIO(day_02_example_text_input).readlines()]

    expected = day_02_example_data

    assert actual, 'No data pulled from input file.'
    assert actual == expected, 'Input file data differs from expected array.'

    return expected

def test_move_01(day_02_example_data: pytest.fixture) -> np.ndarray:
    # GIVEN the data harvested from `day_02_example_text_input`
    # WHEN a `Vector` is passed to the part 1 `move` function
    # THEN the elements of a `position` variable should equal those expected

    data = day_02_example_data

    position = move(data.pop(0))

    horizontal, depth = position

    assert horizontal == 5
    assert depth == 0

    position = move(data.pop(0), position=position)

    horizontal, depth = position

    assert horizontal == 5
    assert depth == 5

def test_move_02(day_02_example_data: pytest.fixture) -> np.ndarray:
    # GIVEN the data harvested from `day_02_example_text_input`
    # WHEN a `Vector` is passed to the part 1 `move` function
    # THEN the elements of a `position` variable should equal those expected

    data = day_02_example_data

    position = move(data.pop(0),
                    move_dict=move_dict, start_position=np.array([0,0,0]))

    horizontal, depth, aim = position

    assert horizontal == 5
    assert depth == 0
    assert aim == 0

    position = move(data.pop(0), position=position,
                    move_dict=move_dict, start_position=np.array([0,0,0]))

    horizontal, depth, aim = position

    assert horizontal == 5
    assert depth == 0
    assert aim == 5

    position = move(data.pop(0), position=position,
                    move_dict=move_dict, start_position=np.array([0,0,0]))

    horizontal, depth, aim = position

    assert horizontal == 13
    assert depth == 40
    assert aim == 5

    position = move(data.pop(0), position=position,
                    move_dict=move_dict, start_position=np.array([0,0,0]))

    horizontal, depth, aim = position

    assert horizontal == 13
    assert depth == 40
    assert aim == 2

    position = move(data.pop(0), position=position,
                    move_dict=move_dict, start_position=np.array([0,0,0]))

    horizontal, depth, aim = position

    assert horizontal == 13
    assert depth == 40
    assert aim == 10

    position = move(data.pop(0), position=position,
                    move_dict=move_dict, start_position=np.array([0,0,0]))

    horizontal, depth, aim = position

    assert horizontal == 15
    assert depth == 60
    assert aim == 10

def test_cumulative_move_01(day_02_example_data: pytest.fixture) -> np.ndarray:
    # GIVEN the data harvested from `day_02_example_text_input`
    # WHEN that data is passed to the cumulative move (`cum_move`) function
    # THEN `cum_move` returns the cumulative position information from all
    #   elements in the data

    data = day_02_example_data

    position = cum_move(data)

    horizontal, depth = position

    assert horizontal == 15  # anticipated horizontal position for test case
    assert depth == 10  # anticipated depth for test case

    expected = 150
    actual = np.prod(position)

    assert actual == expected

def test_cumulative_move_02(day_02_example_data: pytest.fixture) -> np.ndarray:
    # GIVEN the data harvested from `day_02_example_text_input`
    # WHEN that data is passed to the part 1 cumulative move (`cum_move`) function
    # THEN the elements of a `position` variable should equal those expected

    data = day_02_example_data

    position = cum_move(data, move_dict=move_dict, start_position=np.array([0,0,0]))

    horizontal, depth, aim = position

    assert horizontal == 15
    assert depth == 60
    assert aim == 10
