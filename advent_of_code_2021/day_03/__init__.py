import numpy as np

from advent_of_code_2021.get_data import get_data


json = get_data(3)
data = np.array(json['data'], dtype=int)

