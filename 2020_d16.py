import numpy as np
import pandas as pd
from pdb import set_trace

def parse_input(filename):
    data = {}
    with open(filename) as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            line = lines[i].rstrip()
            if len(line.split(': ')) > 1:
                field = line.split(': ')[0]
                data[field] = line.split(': ')[1].split(' or ')
            if line == 'your ticket:':
                j = i + 1
                data['y_tkt']  = [] 
                while lines[j] != '\n':
                    line = lines[j].rstrip()
                    data['y_tkt'].extend(line.split(','))
                    j += 1
                i = j + 1
                continue
            if line == 'nearby tickets:':
                j = i + 1
                data['n_tkt']  = [] 
                while j < len(lines):
                    line = lines[j].rstrip()
                    data['n_tkt'].extend(line.split(','))
                    j += 1
            i += 1
    data['n_tkt'] = np.asarray([int(d) for d in data['n_tkt']])
    data['y_tkt'] = np.asarray([int(d) for d in data['y_tkt']])
    return data

def chk_class_range(data, field, tkt_field):
    tkt = data[tkt_field]
    lower1 = int(data[field][0].split('-')[0])
    upper1 = int(data[field][0].split('-')[1])
    lower2 = int(data[field][1].split('-')[0])
    upper2 = int(data[field][1].split('-')[1])
    if tkt_field == 'valid_n_tkt':
        indices = []
        for d in data['valid_n_tkt']:
            indices.append(np.invert((d < lower1) | ((d > upper1) & (d < lower2)) | (d > upper2)))
        return indices
    else:
        idx = (tkt < lower1) | ((tkt > upper1) & (tkt < lower2)) | (tkt > upper2)
        return idx 

def get_err_rate(data, tkt_field):
    idx = data[tkt_field] > 0
    for k in data:
        if k not in ['y_tkt', 'n_tkt', 'valid_y_tkt', 'valid_n_tkt']:
            idx = idx & chk_class_range(data, k, tkt_field)
    #print(sum(data['n_tkt'][idx]))
    return idx 

def get_field_order(data):
    order = ['' for i in range(len(data['valid_n_tkt']))]
    for k in data:
        if k not in ['y_tkt', 'n_tkt', 'valid_y_tkt', 'valid_n_tkt']:
            indices = chk_class_range(data, k, 'valid_n_tkt')
            set_trace()
            for i in range(len(indices)):
                if sum(indices[i]==False)==0:
                    order[i] = k
                    break
    print(order)

def get_valid_nearby(data, unit):
    invalid = set(data['n_tkt'][get_err_rate(data, 'n_tkt')])
    valid_n_tkt = []
    for idx in range(len(data['n_tkt']))[::unit]:
        valid_n_tkt.append(np.array(list(set(data['n_tkt'][idx:(idx+unit)]) - invalid)))
    return valid_n_tkt

if __name__ == '__main__':
    data = parse_input('data/2020_d16_input_test.txt')
    #print(get_err_rate(data, 'n_tkt'))
    data['valid_y_tkt'] = data['y_tkt'][np.invert(get_err_rate(data, 'y_tkt'))] # get valid tickets
    data['valid_n_tkt'] = get_valid_nearby(data, 3)
    get_field_order(data)
