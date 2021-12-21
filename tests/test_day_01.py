import numpy as np

import pytest

from advent_of_code_2021.api.parsers.day_01 import delim_to_int_list
from advent_of_code_2021.day_01.day_01 import increases, sum_increases


def test_output_to_numpy(day_01_example_text_input: pytest.fixture) -> np.ndarray:
    # GIVEN the example text
    # WHEN transformed into an integer list
    # THEN the actual array should equal the expected arrray
    actual = delim_to_int_list(day_01_example_text_input)

    expected = np.array(
        [
            199,
            200,
            208,
            210,
            200,
            207,
            240,
            269,
            260,
            263
        ]
    )

    assert actual, 'No data pulled from input file.'
    assert np.array_equal(expected, actual), 'Input file data differs from expected array.'

    return actual

def test_increase_or_decrease(day_01_example_text_input: np.ndarray) -> (np.ndarray, np.ndarray):
    # GIVEN the the content of the input file
    # WHEN passed through the `increases` function
    # THEN return an array that matches the expected output
    data_array = test_output_to_numpy(day_01_example_text_input)

    expected_output_string = [
        'increased',
        'increased',
        'increased',
        'decreased',
        'increased',
        'increased',
        'increased',
        'decreased',
        'increased',
    ]

    assert len(expected_output_string) == len(data_array)-1, 'Array size mismatch.'

    expected = [x == 'increased' for x in expected_output_string]

    actual = increases(data_array)

    assert np.array_equal(expected, actual), 'Output of `increase` does not match expected value.'

    return actual, expected

def test_correct_sum(day_01_example_text_input):
    # GIVEN the output arrays of `test_increase_or_decrease`
    # WHEN summed
    # THEN the sum value should equal the expected sum value
    data_array, increase_bool_array = test_increase_or_decrease(day_01_example_text_input)

    expect_sum = 7

    actual_sum = data_array.sum()

    assert sum(increase_bool_array) == expect_sum
    assert actual_sum == expect_sum
