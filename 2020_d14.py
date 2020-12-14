import numpy as np
import pandas as pd
import re
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

if __name__ == '__main__':
    masks, memories = parse_input('data/2020_d14_input.txt')
    mask_memories_pt1(masks, memories)
