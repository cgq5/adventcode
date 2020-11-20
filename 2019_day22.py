import numpy as np
import pandas as pd
from pdb import set_trace

def deal(arr):
    arr = arr[::-1] 
    return arr

def cut(arr, n):
    if n < 0:
        n = len(arr) + n
    arr = arr[n:] + arr[:n]
    return arr

def increment(arr, pivot):
    new_arr = np.empty(len(arr))
    new_arr[:] = np.nan
    curr_idx = 0
    new_arr[curr_idx] = arr[0]
    for i in range(1, len(arr)):
        curr_idx = curr_idx + pivot
        if curr_idx > len(arr):
            curr_idx = curr_idx - len(arr)
        idx_nan = np.argwhere(np.isnan(new_arr))
        curr_idx = idx_nan[idx_nan - curr_idx >= 0][0]
        new_arr[curr_idx] = arr[i]
    return list(new_arr.astype(int))

def ops(arr, filename):
    with open(filename, 'r') as fr:
        for line in fr:
            if line[:4] == 'cut ':
                n = int(line[4:])
                arr = cut(arr, n)
            elif line[:4] == 'deal':
                if line[5:9] == 'with':
                    n = int(line[20:])
                    arr = increment(arr, n)
                else:
                    arr = deal(arr)
    return arr

if __name__ == '__main__':
    #arr = list(range(119315717514047))
    arr = list(range(50024))
    filename = 'input.txt'
    times = 101741582076661
    times = 2 
    for i in range(times):
        print('Current time is ' + str(i+1))
        arr = ops(arr, filename)
    print(arr.index(2019))
    #print(arr)
