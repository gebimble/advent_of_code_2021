from pathlib import Path
from itertools import filterfalse
import re

from advent_of_code_2021 import Coordinate

str_format = r'(\d+),(\d+) -> (\d+),(\d+)'
line_ends = re.compile(str_format)

def get_line_ends(line: str) -> Coordinate:

   x1, y1, x2, y2 = [int(x) for x in line_ends.match(line).groups()]

   return [x1, y1], [x2, y2]

def parse(input_file: Path) -> dict:

    with input_file.open('r') as f:
        content = [get_line_ends(line) for line in f]

    return {
        'data': content
    }
