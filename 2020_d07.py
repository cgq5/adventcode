import numpy as np
import pandas as pd
from pdb import set_trace
import re

def parse_input(filename):
    bags = {} 
    with open(filename, 'r') as f:
        for line in f:
            line = line.replace('bags', '').replace('bag', '')
            line = line.replace('.', '').replace(',', '')
            outer_key = ' '.join(line.split(' contain ')[0].split()[:2])
            bags[outer_key] = []
            items = line.split(' contain ')[1].split()
            for i in range(int(len(items)/3)):
                key = ' '.join(items[i*3+1:i*3+3] )
                val = int(items[i*3])
                d = {}
                d[key] = val 
                bags[outer_key].append(d)
    return bags

if __name__ == '__main__':
    data = parse_input('data/2020_d07_input_test.txt') 
    print(data)
