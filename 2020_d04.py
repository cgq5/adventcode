import numpy as np
import pandas as pd
from pdb import set_trace

def get_product(arr):
    print(arr[0]*arr[1]*arr[2])

def parse_input(filename):
    curr_dict = {} 
    all_dicts = []
    with open(filename, 'r') as f:
        for line in f:
            if line == '\n':
                all_dicts.append(curr_dict)
                curr_dict = {} 
            else:
                segments = line.split()
                for s in segments:
                    curr_dict[s.split(':')[0]] = s.split(':')[1]
    return all_dicts

def check_validity_pt1(dicts):
    cnt = 0
    for d in dicts:
        if len(d.keys()) == 8:
            cnt += 1
        elif len(d.keys()) == 7 and not 'cid' in d: 
            cnt += 1
    return cnt

def chk_byr(byr):
    byr = int(byr)
    if byr >= 1920 and byr <= 2002:
        return True
    else:
        return False

def chk_iyr(iyr):
    iyr = int(iyr)
    if iyr >= 2010 and iyr <= 2020:
        return True
    else:
        return False

def chk_eyr(eyr):
    eyr = int(eyr)
    if eyr >= 2020 and eyr <= 2030:
        return True
    else:
        return False

def chk_hgt(hgt):
    unit = hgt[-2:]
    hgt = int(hgt[:-2])
    if unit == 'cm':
        if hgt <= 193 and hgt >= 150:
            return True
    elif unit == 'in':
        if hgt <= 76 and hgt >= 59:
            return True
    return False 

def chk_hcl(hcl):
    str_set = set("".join(str(x) for x in range(10)) + 'abcdef')
    if hcl[0] == '#' and set(hcl[1:]) <= str_set:
        return True
    return False

def chk_ecl(ecl):
    ecl_set = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if ecl in ecl_set:
        return True
    return False 

def chk_pid(pid):
    pid_set = set("".join(str(x) for x in range(10)))
    if len(pid) == 9 and set(pid) <= pid_set:
        return True
    return False 

def check_validity_pt2(dicts):
    cnt = 0
    for d in dicts:
        if len(d.keys()) == 8: 
            if chk_byr(d['byr']) and chk_iyr(d['iyr']) and chk_eyr(d['eyr']) and chk_hgt(d['hgt']) and chk_hcl(d['hcl']) and chk_ecl(d['ecl']) and chk_pid(d['pid']):
                cnt += 1
        elif len(d.keys()) == 7 and not 'cid' in d:
            if chk_byr(d['byr']) and chk_iyr(d['iyr']) and chk_eyr(d['eyr']) and chk_hgt(d['hgt']) and chk_hcl(d['hcl']) and chk_ecl(d['ecl']) and chk_pid(d['pid']):
                cnt += 1
    return cnt

if __name__ == '__main__':
    all_dicts = parse_input('data/2020_d04_input.txt')
    #print(all_dicts)
    cnt = check_validity_pt2(all_dicts)
    print(cnt)
