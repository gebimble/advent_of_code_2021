from pathlib import Path


def delim_to_int_list(input_string: str, delimeter: str = '\n'):
    return [int(x.strip()) for x in input_string.split()]

def parse(input_file: Path) -> dict:

    return {'data': delim_to_int_list(input_file.read_text())}
