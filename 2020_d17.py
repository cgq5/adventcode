import numpy as np
import pandas as pd
from pdb import set_trace

def parse_input(filename):
    data = []
    with open(filename) as f:
        for line in f:
            line = line.rstrip().replace('#', '1').replace('.', '0')
            line = [int(c) for c in line]
            data.append(np.array(line))
    return np.array(data)

if __name__ == '__main__':
    data = parse_input('data/2020_d17_input_test.txt')
    print(data)
