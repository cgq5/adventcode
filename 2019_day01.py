import numpy as np
import pandas as pd
from pdb import set_trace

LINK='https://adventofcode.com/2019/day/1/input'
LINK2='https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt'

def get_mass(data):
    sum_fuels = 0
    for e in data:
        sum_fuels += get_fuel(e)
    return sum_fuels

def get_fuel(element):
    all_fuels = 0
    fuel = np.floor(element/ 3) - 2
    if fuel > 0:
        all_fuels += fuel 
        fuel = get_fuel(fuel)
        all_fuels += fuel 
    else:
        return 0
    return all_fuels

if __name__ == '__main__':
    data = pd.read_csv('inputs.txt', header=None).iloc[:, 0].to_numpy()
    mass = get_mass(data)
    print(mass)
