import numpy as np
import pandas as pd
from itertools import groupby, combinations
from toolz import memoize, concatv
from pdb import set_trace

def get_diff(data):
    # get the difference between the smallest pair
    data = data.tolist()
    diff = []
    while len(data) > 0:
        curr_min = data.pop(0)
        if len(data) == 0:
            break
        diff.append(-curr_min + min(data))
        #print(diff)
    return diff

@memoize
def get_all_assignments(data):
    if len(data) <= 2:
        return 1
    start, rest = data[0], data[1:]
    return sum(
        get_all_assignments(r) for r in map(lambda n: rest[n:], range(len(rest))) if r[0] - 3 <= start
    )

def count_freq(arr):
    freq = [len(list(group)) for key, group in groupby(arr)]
    # add one more 1 and 3's for starting and ending
    freq = [x+1 for x in freq] 
    #print(freq)
    print(freq[0] * freq[1])

if __name__ == '__main__':
    data = pd.read_csv('data/2020_d10_input.txt', header=None).iloc[:, 0].to_numpy()
    data.sort()
    # part 1
    #diff = get_diff(data)
    #count_freq(diff)
    # part 2 
    data = tuple(concatv([0], data, [data[-1] + 3]))
    num_combs = get_all_assignments(data)
    print(num_combs)
