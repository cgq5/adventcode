import numpy as np
import pandas as pd
import re
from copy import deepcopy
from pdb import set_trace

def parse_input(filename):
    masks = []
    memories = []
    memory = {}
    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            if line[:3] == 'mas':
                masks.append(line[7:])
                if any(memory):
                    memories.append(memory)
                memory = {}
            else:
                memory[re.findall("\[(.*?)\]", line)[0]] = int(line.split(' = ')[1])
        memories.append(memory)
    return masks, memories

def mask_memories_pt1(masks, memories):
    for i in range(len(masks)):
        for key in memories[i]:
            mem = bin(memories[i][key])[2:].zfill(36)
            new_mem = ''.join([masks[i][j] if masks[i][j]!='X' else mem[j] for j in range(36)])
            memories[i][key] = int(new_mem, 2)
    new_memory = {}
    for i in range(len(masks)):
        for key in memories[i]:
            new_memory[key] = memories[i][key]
    all_sum = 0
    for key in new_memory:
        all_sum += new_memory[key]
    print(all_sum)

def gen_binaries(patt, bins):
    if "X" not in patt:
        bins.append(int(patt, 2))
    else:
        gen_binaries(patt.replace("X", "0", 1), bins)
        gen_binaries(patt.replace("X", "1", 1), bins)
    return bins

def mask_memories_pt2(masks, memories):
    new_memory = {}
    for i in range(len(masks)):
        for key in memories[i]:
            mem = bin(int(key))[2:].zfill(36)
            # decoding
            new_mem = ''.join([mem[j] if masks[i][j]=='0' else masks[i][j] for j in range(36)])
            bins = []
            new_keys = gen_binaries(new_mem, bins)
            for k in new_keys:
                new_memory[k] = memories[i][key]
    all_sum = 0
    for key in new_memory:
        if isinstance(new_memory[key], list):
            all_sum += sum(new_memory[key])
        else:
            all_sum += new_memory[key]
    print(all_sum)

if __name__ == '__main__':
    masks, memories = parse_input('data/2020_d14_input.txt')
    #mask_memories_pt1(masks, memories)
    mask_memories_pt2(masks, memories)
