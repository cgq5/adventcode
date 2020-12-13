import numpy as np
import pandas as pd
from pdb import set_trace

def parse_input(filename):
    with open(filename) as f:
        lines = f.readlines()
        time = int(lines[0])
        buses = lines[1].rstrip().split(',')
    return time, buses

def chk_divisible(num, primes):
    for p in primes:
        if num % p == 0:
            return p
    return 0

def get_closest_bus_pt1(time, buses):
    # It is a multiple of a prime number
    primes = [int(p) for p in buses if p != 'x']
    while True:
        mod = chk_divisible(time, primes)
        if mod:
            return mod, time 
        time += 1

def get_closest_bus_pt1(time, buses):
    # It is a multiple of a prime number
    primes = [int(p) for p in buses if p != 'x']
    while True:
        mod = chk_divisible(time, primes)
        if mod:
            return mod, time 
        time += 1

if __name__ == '__main__':
    time, buses = parse_input('data/2020_d13_input.txt')
    bus, closesd = get_closest_bus_pt2(time, buses)
    print((closesd - time)*bus )
