from io import StringIO
import numpy as np

import pytest

from advent_of_code_2021.api.parsers.day_05 import (
    get_line_ends,
    remove_diagonal,
    produce_diagram,
)


def test_output_to_xys(
    day_05_example_text_input: pytest.fixture,
):
    # GIVEN an example line from the input file
    # WHEN passed through the line parser
    # THEN return a pair of coordinates

    data = StringIO(day_05_example_text_input).readlines()

    start, end = get_line_ends(data[0])

    assert isinstance(start, np.ndarray)
    assert start[0] == 0
    assert start[1] == 9

    assert isinstance(start, np.ndarray)
    assert end[0] == 5
    assert end[1] == 9

def test_parse_text(
    day_05_example_text_input: pytest.fixture,
    day_05_example_data: pytest.fixture
):
    # GIVEN an example input
    # WHEN iterated over and parsed
    # THEN the actual output equals the expected output

    actual = [get_line_ends(line) for line in StringIO(day_05_example_text_input)]

    for e, a in zip(day_05_example_data, actual):
        for exp, act in zip(e, a):
            assert np.equal(exp, act).all()

    return actual

def test_remove_diagonals(day_05_example_data: pytest.fixture):
    # GIVEN some example data
    # WHEN filtered to remove diagonal lines
    # THEN the expected number of outputs are returned

    filtered = remove_diagonal(day_05_example_data)

    assert len(filtered) != len(day_05_example_data)
    assert len(filtered) == 6

def test_create_output(day_05_example_data: pytest.fixture,
                       day_05_example_text_output: pytest.fixture):
    # GIVEN some prepared input data
    # WHEN passed through the output picture production algorithm
    # THEN the resultant output should match the anticipated output

    filtered = remove_diagonal(day_05_example_data)

    actual = produce_diagram(filtered)

    assert np.equal(day_05_example_text_output, actual).all()

    assert (actual>1).sum() == 5
