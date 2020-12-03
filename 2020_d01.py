import numpy as np
import pandas as pd
from pdb import set_trace

def find_pair(arr, target):
    # Assuming only one pair is contained in the array
    # At least arr containts one value below one half of the target
    idx = np.argmin(abs(target/2-arr))
    small_half = arr[:idx]
    big_half = arr[idx:]
    for e in small_half:
        if target-e in big_half:
            return [e, target-e]
    return 0 

def find_triplet(arr, target):
    # At least arr containts one value below one third of the target
    idx = np.argmin(abs(target/3-arr))
    small_third = arr[:idx]
    triplet = []
    for e in small_third:
        pair = find_pair(arr, target - e)
        if len(pair) != 0:
            pair.append(e)
            return pair

def get_product(arr):
    print(arr[0]*arr[1]*arr[2])

if __name__ == '__main__':
    data = np.sort(pd.read_csv('2020_d01_input.txt', header=None).iloc[:, 0].to_numpy())
    triplet = find_triplet(data, 2020)
    get_product(triplet)
    print(triplet)
