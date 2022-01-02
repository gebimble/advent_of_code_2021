from pathlib import Path


def delim_to_int_list(input_string: str):
    """delim_to_int_list.

    Parameters
    ----------
    input_string : str
        Raw string.
    delimeter : str
        Delimeter used to split `input_string`.
    """
    return [int(x.strip()) for x in input_string.split()]

def parse(input_file: Path) -> dict:

    return {'data': delim_to_int_list(input_file.read_text())}