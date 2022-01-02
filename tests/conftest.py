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
