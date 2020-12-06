import numpy as np
import pandas as pd
from pdb import set_trace

def get_product(arr):
    print(arr[0]*arr[1]*arr[2])

def parse_input(filename, pt):
    ans = set()
    grps = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        if pt == 2:
            ans = set(lines[0][:-1])
        for i in range(len(lines)):
            line = lines[i]
            if line == '\n':
                grps.append(ans)
                if pt == 1:
                    ans = set() 
                else:
                    ans = set(lines[i+1][:-1]) 
            else:
                if pt == 1:
                    ans = ans.union(set(line[:-1]))
                else:
                    ans = ans.intersection(set(line[:-1]))
        grps.append(ans) # add last group 
    return grps 

def count_questions(grps):
    cnt = 0
    for g in grps:
        cnt += len(g)
    return cnt

if __name__ == '__main__':
    grps = parse_input('data/2020_d06_input.txt', 2)
    #print(grps)
    cnt = count_questions(grps)
    print(cnt)
