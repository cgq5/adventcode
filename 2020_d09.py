import numpy as np
import pandas as pd
from pdb import set_trace

def identify_invalid(nums, win_size):
    for i in range(win_size, len(nums)):
        cnt = win_size 
        for j in range(win_size):
            #set_trace()
            if nums[i] - nums[i-j-1] in nums[i-win_size:i]:
                continue
            cnt -= 1
            if cnt == 0:
                return nums[i]
    return -1

def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

def get_combination_indices(win_size):
    indices = []
    for r in range(3, win_size+1):
        com = combinations(range(win_size), r)
        for i in com:
            indices.append(np.asarray(i))
    return indices

def find_continguous_set(nums, win_size, first_invalid):
    indices = get_combination_indices(win_size)
    set_trace()
    i = 0
    while i + win_size <= len(nums):
        for idx in indices:
            if sum(nums[i:i+win_size][idx]) == first_invalid:
                return min(nums[i:i+win_size][idx]), max(nums[i:i+win_size][idx])
        i += 1
    return -1

if __name__ == '__main__':
    data = pd.read_csv('data/2020_d09_input.txt', header=None).iloc[:, 0].to_numpy()
    first_invalid = identify_invalid(data, 25)
    weakness = find_continguous_set(data, 15, first_invalid)
    print(weakness)
