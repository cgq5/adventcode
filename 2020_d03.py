import numpy as np
import pandas as pd
import sys
sys.path.insert(0, "/home/gcao/Projects/retrieval/misc/")
from fileproc import loadstr
from pdb import set_trace

def count_trees_brute_force(data, toright, tobelow):
    idx = 0 
    cnt = 0
    for entry in data[::tobelow]:
        if idx >= len(entry):
            idx = idx - len(entry)
        if entry[idx] == '#':
            cnt += 1
        idx += toright 
    return cnt

if __name__ == '__main__':
    data = loadstr('data/2020_d03_input.txt')
    data = loadstr('data/2020_d03_input_test.txt')
    nums = [1,3,5,7]
    cnt = 1
    for n in nums:
        cnt *= count_trees_brute_force(data, n, 1)
    cnt *= count_trees_brute_force(data, 1, 2)
    print(cnt)
