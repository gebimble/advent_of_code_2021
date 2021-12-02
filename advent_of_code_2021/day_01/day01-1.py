from pathlib import Path
import numpy as np


input_file = Path(__file__).parent / 'input.txt'

data = np.loadtxt(input_file, dtype=int)

total = np.sum(data[1:] > data[:-1])

print(total)
