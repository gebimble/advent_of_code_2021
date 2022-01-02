from pathlib import Path
from advent_of_code_2021 import Vector


def get_vector(line: str) -> Vector:
    d, m = line.split()
    m = int(m)

    return d, m

def parse(input_file: Path) -> dict:

    content = []

    with input_file.open('r') as f:
        for line in f:
            content.append(get_vector(line))

    return {'data': content}
