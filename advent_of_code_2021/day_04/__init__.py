import numpy as np

from advent_of_code_2021.get_data import get_data


json = get_data(4)

numbers = np.array(json['data']['numbers'], dtype=int)

cards = [np.array(x, dtype=int) for x in json['data']['cards']]

