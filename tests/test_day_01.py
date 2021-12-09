import numpy as np

from advent_of_code_2021.api.parsers.day_01 import delim_to_int_list
from advent_of_code_2021.day_01.day_01 import increases, sum_increases


def test_output_to_numpy(day_01_example_text_input):
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

    assert actual
    assert np.array_equal(expected, actual)

    return actual

def test_increase_or_decrease(day_01_example_text_input):
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

    assert len(expected_output_string) == len(data_array)-1

    expected = [x == 'increased' for x in expected_output_string]

    actual = increases(data_array)

    assert np.array_equal(expected, actual)

    return actual, expected

def test_correct_sum(day_01_example_text_input):
    data_array, increase_bool_array = test_increase_or_decrease(day_01_example_text_input)

    expect_sum = 7

    actual_sum = data_array.sum()

    assert sum(increase_bool_array) == expect_sum
    assert actual_sum == expect_sum
