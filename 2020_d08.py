import numpy as np
import pandas as pd
from copy import deepcopy
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
            idx += 1
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
            return 0 
    print(accumulator)
    #print(record)
    return 1 

def debugging(commands):
    record = []
    idx = 0 # current command line idx
    accumulator = 0
    while idx < len(commands):
        record.append(idx)
        ops  = commands[idx][0]
        sign = commands[idx][1][0]
        step = int(commands[idx][1][1:])
        print(record)
        if ops == 'nop':
            idx += 1
        elif ops == 'jmp':
            new_commands = deepcopy(commands)
            new_commands[idx][0] = 'nop'
            if first_run(new_commands) == 1:
                print("The line to change is " + str(idx))
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

if __name__ == '__main__':
    commands = parse_input('data/2020_d08_input_test1.txt')
    debugging(commands)
    #print(first_run(commands))
