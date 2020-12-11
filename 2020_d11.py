import numpy as np
import pandas as pd
import sys
sys.path.insert(0, "/home/gcao/Projects/retrieval/misc/")
from fileproc import loadstr
from copy import deepcopy
from pdb import set_trace

def parse_input(filename):
    # convert the input to a binary array
    data = []
    with open(filename) as f:
        for line in f:
            line = line.rstrip().replace('L', '0').replace('#', '1').replace('.', '2')
            arr = [int(c) for c in line]
            data.append(np.array(arr))
    return np.array(data)

def get_neighbor_idx(cell):
    from itertools import product
    size = 3
    for c in product(*(range(n-1, n+2) for n in cell)):
        if c != cell and all(0 <= n < size for n in c):
            yield c

def refresh_once_pt1(data, cell_indices):
    new_data = deepcopy(data)
    pad_data = np.zeros((np.shape(data)[0]+2, np.shape(data)[1]+2))
    pad_data[1:np.shape(data)[0]+1, 1:np.shape(data)[1]+1] = data
    # for data not on the boundary
    for x in range(1, np.shape(pad_data)[0]-1):
        for y in range(1, np.shape(pad_data)[1]-1):
            indices = cell_indices + (x-1,y-1)
            neighbors = np.array([pad_data[tuple(idx)] for idx in indices])
            if sum(neighbors != 1) == 8 and pad_data[x,y] == 0:
                new_data[x-1,y-1] = 1
            if pad_data[x,y] == 1 and sum(neighbors == 1) >= 4:
                new_data[x-1,y-1] = 0 
    return new_data

def all_refresh(data):
    cell_indices = np.asarray(list(get_neighbor_idx((1,1))))
    curr_data = deepcopy(data)
    i = 0
    while True:
        #new_data = refresh_once_pt1(curr_data, cell_indices)
        new_data = refresh_once_pt2(curr_data, cell_indices)
        if new_data.tolist() == curr_data.tolist():
            break
        else:
            curr_data = deepcopy(new_data)
        i += 1
        print(i)
    print(sum(sum(new_data == 1)))

if __name__ == '__main__':
    data = parse_input('data/2020_d11_input_test.txt')
    all_refresh(data)
