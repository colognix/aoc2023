import math
import numpy as np

def process(input):
    seeds = [int(s) for s in input[0].split(': ')[1].split(' ')]
    conversions = []
    tmp = []
    for line in input[3:]:
        if len(line) == 0:
            continue
        if ':' in line:
            conversions += [tmp]
            tmp = []
        else:
            tmp += [[int(v) for v in line.split(' ')]]
    conversions += [tmp]
    return seeds, conversions

def convert_single(s, conversion_path):
    for conversions in conversion_path:
        converted = False
        for conversion in conversions:
            if (not converted) & (s >= conversion[1]) & (s < conversion[1]+conversion[2]):
                s += conversion[0]-conversion[1]
                converted = True
    return s

def convert_bulk(s_start, s_end, conversion_path):
    # care for int overflow..
    seeds = np.arange(s_start, s_end, dtype=float)
    for conversions in conversion_path:
        converted = np.array([False]*len(seeds))
        for conversion in conversions:
            cond = np.where((converted == False) & (seeds >= conversion[1]) & (seeds < conversion[1]+conversion[2]))
            seeds[cond] += conversion[0]-conversion[1]
            converted[cond] = True
    print(np.min(seeds))
    return np.min(seeds)

def get_minimum_location(seeds, conversion_path, part):
    min_loc = math.inf
    if part == 1:
        for i in range(len(seeds)):
            min_loc = min(min_loc,convert_single(seeds[i], conversion_path))
    if part == 2:
        for i in range(0,len(seeds),2):
            min_loc = min(min_loc, convert_bulk(seeds[i], seeds[i]+seeds[i+1], conversion_path))
    return min_loc



def solve(input):
    seeds, conversion_path = process(input)
    # part 1
    print(get_minimum_location(seeds, conversion_path,1))
    # part 2
    print(get_minimum_location(seeds, conversion_path,2))