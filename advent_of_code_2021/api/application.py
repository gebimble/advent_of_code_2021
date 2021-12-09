from pathlib import Path
from flask import Flask


app = Flask(__name__)

data_directory = Path(__file__).parent / '../../data/'

@app.route('/')
def index():
    return 'Merry Christmas!'

@app.route('/data/<day>')
def get_data(day):

    import importlib.util
    import sys

    day = int(day)

    data_file = data_directory / f'input_{day:02d}.txt'

    parser = Path(f'parsers/day_{day:02d}.py')
    module_name = parser.stem
    file_path = str(parser.absolute())

    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)

    return module.parse(data_file)
