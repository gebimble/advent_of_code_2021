import os
import requests


os.environ['NO_PROXY'] = '127.0.0.1'

def get_data(day: int) -> dict:
    return requests.get(f'http://127.0.0.1:5000/data/{day}').json()
