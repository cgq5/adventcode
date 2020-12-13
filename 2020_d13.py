import numpy as np
import pandas as pd
from math import prod
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

def get_primes_and_mod(nums):
    bus_deps = [(int(x), idx) for idx, x in enumerate(nums) if x != "x"]
    return bus_deps

def get_closest_bus_pt2(nums):
    #for nums in tests:
    bus_deps = get_primes_and_mod(nums)
    invm = lambda a, b: 0 if a==0 else 1 if b%a==0 else b - invm(b%a,a)*b//a
    N = prod([bs[0] for bs in bus_deps])
    x = sum([bs[1]*(N//bs[0])*invm(N//bs[0], bs[0]) for bs in bus_deps])
    #print(N, x)
    print(N - x % N)

def parse_input_pt2(filename):
    tests = []
    with open(filename) as f:
        for line in f:
            nums = line.rstrip().split(',')
            tests.append(nums)
    return tests

if __name__ == '__main__':
    time, buses = parse_input('data/2020_d13_input_test1.txt')
    #bus, closesd = get_closest_bus_pt1(time, buses)
    #print((closesd - time)*bus )
    get_closest_bus_pt2(buses)
