import numpy as np
import pandas as pd
from itertools import product 
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

def get_explicit_rules(rules, key):
    curr_rule = rules[key]
    #chk = [r.isdigit() for r in curr_rule]
    chk = [r.isdigit() for r in curr_rule if type(r) != list]
    if any(chk):
        str_rules = []
        str_rule = [] 
        for i in range(len(curr_rule)):
            if curr_rule[i] != '|':
                exp_rule = get_explicit_rules(rules, curr_rule[i])
                if type(exp_rule) == list and len(str_rule) != 0:
                    str_rule = list(product(str_rule, exp_rule))
                    print(str_rule)
                    str_rule = ["".join(s) for s in str_rule]
                else:
                    str_rule += exp_rule
            else:
                str_rules.append(''.join(str_rule))
                str_rule = [] 
        str_rules.append(''.join(str_rule))
        rules[key] = str_rules
        return rules[key]
    else:
        return ["".join(curr_rule)]

if __name__ == '__main__':
    rules, msg = parse_input('data/2020_d19_input_test.txt')
    print(get_explicit_rules(rules, '1'))
