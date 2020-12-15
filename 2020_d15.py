import numpy as np
import pandas as pd
from copy import deepcopy
from pdb import set_trace

def gen_nums_pt1(init):
    nums = deepcopy(init)
    for i in range(len(init), 30000000):
        last = nums[i-1]
        indices = np.where(np.asarray(nums) == last)[0] 
        if len(indices) > 1:
            nums.append(indices[-1] - indices[-2])
        else:
            nums.append(0)
    print(nums[-1])

if __name__ == '__main__':
    data = '18,11,9,0,5,1'
    test = '0,3,6'
    ins = data 
    init = [int(n) for n in ins.split(',')] 
    gen_nums_pt1(init)
