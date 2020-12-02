import numpy as np
import pandas as pd
import sys
sys.path.insert(0, "/home/gcao/Projects/retrieval/misc/")
from fileproc import loadstr
from pdb import set_trace

def parse_input(data):
    inputs = []
    for line in data:
        lower = line.split(':')[0].split()[0].split('-')[0]
        upper = line.split(':')[0].split()[0].split('-')[1]
        letter = line.split(':')[0].split()[1]
        pwd = line.split(':')[1][1:]
        inputs.append([lower, upper, letter, pwd])
    return inputs

def count_char_in_str(letter, pwd):
    cnt = 0
    for c in pwd:
        if c == letter:
            cnt += 1
    return cnt

def count_valid_pwd_pt1(inputs):
    cnt = 0
    for entry in inputs:
        lower = int(entry[0])
        upper = int(entry[1])
        letter = entry[2]
        pwd = entry[3]
        letter_cnt = count_char_in_str(letter, pwd)
        if letter_cnt >= lower and letter_cnt <= upper:
            cnt += 1
    return cnt

def count_valid_pwd_pt2(inputs):
    cnt = 0
    for entry in inputs:
        lower = int(entry[0])
        upper = int(entry[1])
        letter = entry[2]
        pwd = entry[3]
        if (pwd[lower - 1] == letter and pwd[upper - 1] != letter) or  (pwd[lower - 1] != letter and pwd[upper - 1] == letter):
            cnt += 1
    return cnt

def get_product(arr):
    print(arr[0]*arr[1]*arr[2])

if __name__ == '__main__':
    data = loadstr('data/2020_d02_input.txt')
    inputs = parse_input(data)
    cnt = count_valid_pwd_pt2(inputs)
    print(cnt)
