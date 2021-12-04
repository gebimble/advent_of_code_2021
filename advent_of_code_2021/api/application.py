from pathlib import Path
from flask import Flask


app = Flask(__name__)

data_directory = Path(__file__).parent / '../../data/'

@app.route('/')
def index():
    return 'Merry Christmas!'

@app.route('/data/<day>')
def get_data(day):
    day = int(day)

    data_file = data_directory / f'input{day:02d}.txt'
    parser = None

    return {'data': f'The data from {str(data_file)}'}
