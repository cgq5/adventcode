import numpy as np
import pandas as pd
#import compiler
import parser
from pdb import set_trace

def parse_input(filename):
    eqs = []
    with open(filename) as f:
        for line in f:
            #eq = compiler.parse(line.rstrip()) 
            eq = parser.expr(line)
            #eq = parser.expr(line).compile()
            set_trace()

if __name__ == '__main__':
    data = parse_input('data/2020_d18_input_test.txt')
    parse_input(filename)
