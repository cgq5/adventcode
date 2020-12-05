import numpy as np
import pandas as pd
import sys
sys.path.insert(0, "/home/gcao/Projects/retrieval/misc/")
from fileproc import loadstr
from pdb import set_trace

def get_loc(letters, i, j):
    if set(letters) <= {'F', 'B'}:
        chk = 'F'
    else:
        chk = 'L'
    while i < j:
        m = int((i + j) / 2)
        if letters[0] == chk:
            j = m
        else:
            i = m + 1
        letters = letters[1:]
    return i

def get_seat_id(data):
    all_ids = set(list(range(0, 127*8+7)))
    ids = []
    cnt = 0
    for l in data:
        row = get_loc(l[:7], 0, 127)
        col = get_loc(l[7:], 0, 7)
        ids.append(row * 8 + col)
    my_id = all_ids - set(ids) - set(list(range(38))) - set(list(range(999, 1023)))
    print(my_id)

if __name__ == '__main__':
    data = loadstr('data/2020_d05_input.txt')
    #data = ['BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']
    get_seat_id(data)
