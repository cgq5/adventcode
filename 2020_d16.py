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
        for i in range(np.shape(data['valid_n_tkt'])[1]):
            c = data['valid_n_tkt'][:,i]
            idx = np.invert((c < lower1) | ((c > upper1) & (c < lower2)) | (c > upper2))
            idx[c==0] = True
            indices.append(all(idx))
        return np.array(indices)
    else:
        idx = (tkt < lower1) | ((tkt > upper1) & (tkt < lower2)) | (tkt > upper2)
        return idx 

def get_err_rate(data, tkt_field):
    idx = data[tkt_field] > 0
    for k in data:
        if k not in ['y_tkt', 'n_tkt', 'valid_y_tkt', 'valid_n_tkt']:
            idx = idx & chk_class_range(data, k, tkt_field)
    return idx 

def get_field_order(data):
    order = [[] for i in range(len(data['valid_n_tkt']))]
    keys = []
    mat = []
    for k in data:
        if k not in ['y_tkt', 'n_tkt', 'valid_y_tkt', 'valid_n_tkt']:
            keys.append(k)
            mat.append(chk_class_range(data, k, 'valid_n_tkt').astype(int))
    return keys, np.array(mat)

def get_uniq_field(mat):
    if sum(sum(mat)) == np.shape(mat)[0]:
        return mat
    rows = np.where(np.sum(mat, axis=1) == 1)[0]
    cols = np.nonzero(mat[rows, :])[1]
    mat[:,cols] = 0
    mat[rows,cols] = 1
    return get_uniq_field(mat)

def get_valid_nearby(data, unit):
    n_tkt = [data['n_tkt'][x:x+unit] for x in range(0, len(data['n_tkt']), unit)]
    indices = get_err_rate(data, 'n_tkt')
    indices = [indices[x:x+unit] for x in range(0, len(indices), unit)]
    valid_n_tkt = []
    for i, line in enumerate(n_tkt):
        line[indices[i]] = 0
        valid_n_tkt.append(line)
    return np.array(valid_n_tkt)

def get_dept_multiply(data, mat):
    cols = np.where(mat == 1)[1]
    print(np.prod(data['valid_y_tkt'][cols[:6]]))

if __name__ == '__main__':
    data = parse_input('data/2020_d16_input.txt')
    unit = 20 
    #print(get_err_rate(data, 'n_tkt'))
    data['valid_y_tkt'] = data['y_tkt'][np.invert(get_err_rate(data, 'y_tkt'))] # get valid tickets
    data['valid_n_tkt'] = get_valid_nearby(data, unit)
    keys, mat = get_field_order(data)
    mat = get_uniq_field(mat)
    get_dept_multiply(data, mat)
