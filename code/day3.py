import numpy as np
import re
from itertools import chain


def try_number(c):
    try:
        int(c)
        return True
    except ValueError:
        return False

def create_symbol_mask(input):
    p_mask = []
    p_regex = r'\.'
    n_mask = []
    n_regex = r'\d'
    for line in input:
        p_mask += [list(map(lambda x: bool(re.match(p_regex, x)), line))]
        n_mask += [list(map(lambda x: bool(re.match(n_regex, x)), line))]
    symbol_mask_inv = np.logical_or(p_mask, n_mask)
    return np.where(np.invert(symbol_mask_inv))

def create_engine_mask(input):
    e_mask = []
    e_regex = r'\*'
    for line in input:
        e_mask += [list(map(lambda x: bool(re.match(e_regex, x)), line))]

    return np.where(e_mask)
    
def create_adjacent_dict(symbol_mask, size):
    adjacent_dict = {}
    symbol_coordinates = [list(pair) for pair in np.transpose(symbol_mask)]

    for position in symbol_coordinates:
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if not ((i == 0) & (j == 0)):
                    if ((position[0]+i < size) & (position[1]+j < size) & (position[0]+i >= 0) & (position[1]+j >= 0)):
                        try:
                            adjacent_dict[position[0]+i] += [position[1]+j]
                        except KeyError:
                            adjacent_dict[position[0]+i] = [position[1]+j]
    for line in adjacent_dict:
        adjacent_dict[line] = list(set(adjacent_dict[line]))
    return adjacent_dict

def extract_adjacent_numbers(adjacent_dict, engine_schematic):
    size = len(engine_schematic)
    # work per line here
    for line in adjacent_dict:
        # filter dots
        current_line = [position for position in adjacent_dict[line] if try_number(engine_schematic[line][position])]
        # don't consider empty lists
        if len(current_line) == 0:
            adjacent_dict[line] = current_line
            continue

        # get all number-chars that belong to an adjacent number
        new_found = True
        while (new_found):
            new_found = False
            for position in current_line:
                for i in [-1,1]:
                    if ((position + i) not in current_line) & (position + i >= 0) & (position + i < size):
                        if (try_number(engine_schematic[line][position+i])):
                            current_line += [position + i]
                            new_found = True
        
        # sort for further processing
        current_line.sort()

        # split the index-list for differing numbers
        number_list = []
        tmp = [current_line[0]]
        for i in range(1,len(current_line)):
            if (int(current_line[i]) - int(current_line[i-1])) > 1:
                number_list += [tmp]
                tmp = [current_line[i]]
            else:
                tmp += [current_line[i]]
        number_list += [tmp]

        # reset the number list
        adjacent_dict[line] = [[v[0],v[-1]] for v in number_list]

    return adjacent_dict

def create_engine_dict(engine_mask, adjacent_dict, size):
    engine_coordinates = [list(pair) for pair in np.transpose(engine_mask)]
    engine_dict = {}
    id = 0
    for position in engine_coordinates:
        engine_adjacents = {}
        for i in [-1,0,1]:
            if (position[0] + i >= 0) & (position[0] + i < size):
                try:
                    engine_adjacents[position[0]+i] += [n for n in adjacent_dict[position[0]+i] if (position[1] >= n[0] - 1) & (position[1] <= n[1] + 1)]
                except KeyError:
                    engine_adjacents[position[0]+i] = [n for n in adjacent_dict[position[0]+i] if (position[1] >= n[0] - 1) & (position[1] <= n[1] + 1)]
        # don't consider empty results
        engine_dict[id] = {k : v for k,v in engine_adjacents.items() if len(v) > 0}
        id += 1
    
    return engine_dict

def get_numbers(input, adjacent_dict):
    numbers_per_line = [[int(''.join(input[line][p[0]:p[1]+1])) for p in position] for line,position in adjacent_dict.items()]
    return list(chain(*numbers_per_line))

def get_gear_ratio(engine, input):
    ratio = 1
    number_adjacents = 0
    for pos_x in engine:
        for pos_y in engine[pos_x]:
            ratio *= int(''.join(input[pos_x][pos_y[0]:pos_y[1]+1]))
            number_adjacents += 1
    if number_adjacents != 2:
        ratio = 0
    return ratio

def solve(input):
    # size for the map - x = y in this case
    size = len(input)
    # part 1
    adjacent_dict = create_adjacent_dict(create_symbol_mask(input), size)
    adjacent_dict = extract_adjacent_numbers(adjacent_dict, input)
    adjacent_numbers = get_numbers(input, adjacent_dict)
    print(sum(adjacent_numbers))

    # part 2
    engine_mask = create_engine_mask(input)
    adjacent_dict = create_adjacent_dict(engine_mask, size)
    adjacent_dict = extract_adjacent_numbers(adjacent_dict, input)
    engine_dict = create_engine_dict(engine_mask, adjacent_dict, size)
    print(sum([get_gear_ratio(engine, input) for engine in engine_dict.values()]))
