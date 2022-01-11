from io import StringIO
from textwrap import dedent
import numpy as np
import pytest


@pytest.fixture
def day_01_example_text_input():
    return """199
200
208
210
200
207
240
269
260
263"""


@pytest.fixture
def day_02_example_text_input():
    return """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


@pytest.fixture
def day_02_example_data():
    return [
        ("forward", 5),
        ("down", 5),
        ("forward", 8),
        ("up", 3),
        ("down", 8),
        ("forward", 2),
    ]


@pytest.fixture
def day_05_example_text_input():
    return """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


@pytest.fixture
def day_05_example_data():
    return (
        [np.array([0, 9]), np.array([5, 9])],
        [np.array([8, 0]), np.array([0, 8])],
        [np.array([9, 4]), np.array([3, 4])],
        [np.array([2, 2]), np.array([2, 1])],
        [np.array([7, 0]), np.array([7, 4])],
        [np.array([6, 4]), np.array([2, 0])],
        [np.array([0, 9]), np.array([2, 9])],
        [np.array([3, 4]), np.array([1, 4])],
        [np.array([0, 0]), np.array([8, 8])],
        [np.array([5, 5]), np.array([8, 2])],
    )

@pytest.fixture
def day_05_example_text_output():
    text = """
    .......1..
    ..1....1..
    ..1....1..
    .......1..
    .112111211
    ..........
    ..........
    ..........
    ..........
    222111....
    """
    text = dedent(text)

    text = StringIO(text.replace(".", "0"))
    return np.genfromtxt(text, delimiter=1)
