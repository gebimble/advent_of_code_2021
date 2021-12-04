from pathlib import Path


def parse(input_file: Path) -> dict:

    content = []

    with input_file.open('r') as f:
        content.append([[int(x) for x in line.split()] for line in f])

    return {'data': content}
