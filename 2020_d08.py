import numpy as np
import pandas as pd
from pdb import set_trace

def parse_input(filename):
    commands = []
    with open(filename) as f:
        for line in f:
            commands.append(line.split())
    return commands 

def first_run(commands):
    record = []
    idx = 0 # current command line idx
    accumulator = 0
    while idx < len(commands):
        record.append(idx)
        ops  = commands[idx][0]
        sign = commands[idx][1][0]
        step = int(commands[idx][1][1:])
        if ops == 'nop':
            chk = idx
            idx += 1
            if sign == '+':
                chk += step 
            else: 
                chk -= step
            if chk == 638:
                set_trace() 
        elif ops == 'jmp':
            if sign == '+':
                idx += step 
            else: 
                idx -= step 
        elif ops == 'acc':
            if sign == '+':
                accumulator += int(step)
            else: 
                accumulator -= int(step)
            #print(accumulator)
            idx += 1
        if idx in record:
            break
    print(accumulator)
    print(record)
    
if __name__ == '__main__':
    commands = parse_input('data/2020_d08_input.txt')
    first_run(commands)
