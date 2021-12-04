from pathlib import Path


def parse(input_file: Path) -> dict:

    content = []

    with input_file.open('r') as f:
        for line in f:
            digits = [int(x) for x in line.strip()]
            content.append(digits)

    return {'data': content}
