from pathlib import Path

import werkzeug
from flask import Flask, jsonify


app = Flask(__name__)

data_directory = Path(__file__).parent / '../../data/'

class DataRequestError(ValueError):
    pass

@app.errorhandler(DataRequestError)
def handle_data_exception(error):
    return 'Please provide an integer between 0 and 25.'

@app.route('/')
def index() -> str:
    """'homepage' of the webapp. Returns a festive message to demonstrate
    that everything is working!
    """

    return 'Merry Christmas!'

@app.route('/data/<day>')
def get_data(day: str) -> dict:
    """Data return mechanism for challenge inputs.

    Parameters
    ----------
    day : str
        Day of the month corresponding to desired problem input.

    Returns
    -------
    dict
        Dictionary of challenge data, JSON style.

    Raises
    ------
    ValueError
        Raised if `day` is not an integer between 0 and 25.
    """

    import importlib.util
    import sys

    # ints between 1 and 25 only, please!
    try:
        day = int(day)

        if not 1 <= day <= 25:
            raise DataRequestError

    except:
        raise DataRequestError


    data_file = data_directory / f'input_{day:02d}.txt'

    # programatically find the path to the right parser
    parser = Path(f'parsers/day_{day:02d}.py')
    module_name = parser.stem
    file_path = str(parser.absolute())

    # programatically import the parser
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)

    return module.parse(data_file)
