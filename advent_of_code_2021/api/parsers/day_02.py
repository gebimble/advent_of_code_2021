from pathlib import Path


def parse(input_file: Path) -> dict:

    content = []

    with input_file.open('r') as f:
        for line in f:
            direction, magnitude = line.split()
            magnitude = int(magnitude)

            content.append([direction, magnitude])

    return {'data': content}
