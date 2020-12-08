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
    while len(record) >= 0:
        if commands[idx][0] == 'nop':
            idx += 1 
        elif commands[idx][0] == 'jmp':
            sign = commands[idx][1][0]
            ops  = int(commands[idx][1][1])
            if sign == '+':
                idx += ops
            else: 
                idx -= ops 
        elif commands[idx][0] == 'acc':
            sign = commands[idx][1][0]
            ops  = int(commands[idx][1][1])
            if sign == '+':
                accumulator += int(ops)
            else: 
                accumulator -= int(ops)
            idx += 1
        if idx in record:
            break
        record.append(idx)
    print(accumulator)
    print(record)
    
if __name__ == '__main__':
    commands = parse_input('data/2020_d08_input_test.txt')
    first_run(commands)
