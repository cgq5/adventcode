import numpy as np
import pandas as pd
from pdb import set_trace

def parse_input(arr):
    print(arr[0]*arr[1]*arr[2])

if __name__ == '__main__':
    data = pd.read_csv('data/2020_d01_input.txt', header=None).iloc[:, 0].to_numpy()
    print(triplet)
