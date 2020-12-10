import numpy as np
import pandas as pd
from itertools import groupby
from pdb import set_trace

def get_diff(data):
    # get the difference between the smallest pair
    diff = []
    data.sort()
    while len(data) > 0:
        curr_min = data.pop(0)
        if len(data) == 0:
            break
        diff.append(-curr_min + min(data))
        #print(diff)
    return diff

def find_all_arragements(data):
    diff = []
    data.sort()
    while len(data) > 0:
        curr_min = data.pop(0)
        if len(data) == 0:
            break
        diff.append(-curr_min + min(data))
        #print(diff)
    return diff

def count_freq(arr):
    arr.sort()
    freq = [len(list(group)) for key, group in groupby(arr)]
    # add one more 1 and 3's for starting and ending
    freq = [x+1 for x in freq] 
    print(freq)
    print(freq[0] * freq[1])

if __name__ == '__main__':
    data = pd.read_csv('data/2020_d10_input.txt', header=None).iloc[:, 0].to_numpy().tolist()
    diff = get_diff(data)
    count_freq(diff)
