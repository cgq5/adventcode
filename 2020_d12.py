import numpy as np
import pandas as pd
import sys
sys.path.insert(0, "/home/gcao/Projects/retrieval/misc/")
from fileproc import loadstr
from pdb import set_trace

def get_dir(curr_dir):
    return curr_dir % 4 

def get_postition_pt1(data):
    curr_dir = 0 
    curr_units = {'0':0, '1':0} # to east and south
    for move in data:
        if move[0] == 'F':
            if get_dir(curr_dir) == 0:
                curr_units['0'] += int(move[1:])
            elif get_dir(curr_dir) == 2:
                curr_units['0'] -= int(move[1:])
            elif get_dir(curr_dir) == 1:
                curr_units['1'] += int(move[1:])
            elif get_dir(curr_dir) == 3:
                curr_units['1'] -= int(move[1:])
        elif move[0] == 'R':
            if int(move[1:]) == 90:
                curr_dir = curr_dir + 1
            elif int(move[1:]) == 180:
                curr_dir = curr_dir + 2
            elif int(move[1:]) == 270:
                curr_dir = curr_dir + 3
        elif move[0] == 'L':
            if int(move[1:]) == 90:
                curr_dir = curr_dir + 3 
            elif int(move[1:]) == 180:
                curr_dir = curr_dir + 2
            elif int(move[1:]) == 270:
                curr_dir = curr_dir + 1 
        elif move[0] == 'E':
            curr_units['0'] += int(move[1:])
        elif move[0] == 'W':
            curr_units['0'] -= int(move[1:])
        elif move[0] == 'S':
            curr_units['1'] += int(move[1:])
        elif move[0] == 'N':
            curr_units['1'] -= int(move[1:])
    return abs(curr_units['0']) + abs(curr_units['1'])

if __name__ == '__main__':
    data = loadstr('data/2020_d12_input_test.txt')
    dist = get_postition(data)
    print(dist)
