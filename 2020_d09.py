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

def find_continguous_set(nums, win_size, first_invalid):
    i = 0
    while i + win_size <= len(nums):
        if sum(nums[i:i+win_size]) == first_invalid:
            return min(nums[i:i+win_size]), max(nums[i:i+win_size])
        i += 1
    return -1

if __name__ == '__main__':
    data = pd.read_csv('data/2020_d09_input.txt', header=None).iloc[:, 0].to_numpy()
    first_invalid = identify_invalid(data, 25)
    for ws in range(4, 200):
        weakness = find_continguous_set(data, ws, first_invalid)
        if weakness != -1:
            break
    print(weakness)
    print(sum(weakness))
