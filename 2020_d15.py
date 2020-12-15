import numpy as np
import pandas as pd
from copy import deepcopy
from toolz import memoize, concatv
from pdb import set_trace

def gen_nums_pt1(init):
    nums = deepcopy(init)
    for i in range(len(init), 2020):
        last = nums[i-1]
        indices = np.where(np.asarray(nums) == last)[0] 
        if len(indices) > 1:
            nums.append(indices[-1] - indices[-2])
        else:
            nums.append(0)
    print(nums[-1])

def get_nums_pt2(current, history, limit=2020):
    # reversely use value as index and indices as values which is stored in dict 
    for idx in range(len(history) + 1, limit):
        prev_idx = history.get(current, 0)
        history[current] = idx
        current = idx - prev_idx if prev_idx else 0
    return current

if __name__ == '__main__':
    data = '18,11,9,0,5,1'
    test = '0,3,6'
    ins = test
    init = [int(n) for n in ins.split(',')] 
    #print(gen_nums_pt1(init))
    print(get_nums_pt2(init[-1], {num: idx + 1 for idx, num in enumerate(init[:-1])}, limit=5))
