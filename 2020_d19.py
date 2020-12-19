import numpy as np
import pandas as pd
from pdb import set_trace

def parse_input(filename):
    rules = {}
    msg = []
    with open(filename) as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            if lines[i] == '\n':
                i += 1
                break
            line = lines[i].rstrip().replace("\"", "").split(": ")
            rules[line[0]] = line[1].split()
            i += 1
        while i < len(lines):
            msg.append(lines[i].rstrip())
            i += 1
    return rules, msg

def get_rule_zero(rules, key):
    curr_rule = rules[key]
    chk = [r.isdigit() for r in curr_rule]
    set_trace()
    if any(chk):
        for i in range(len(curr_rule)):
            if chk[i]:
                return get_rule_zero(rules, curr_rule[i])
    else:
        return curr_rule

if __name__ == '__main__':
    rules, msg = parse_input('data/2020_d19_input_test.txt')
    get_rule_zero(rules, '0')
