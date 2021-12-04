from pathlib import Path


def parse(input_file: Path) -> dict:

    with input_file.open('r') as f:
        content = [int(x.strip()) for x in f.readlines()]

    return {'data': content}
