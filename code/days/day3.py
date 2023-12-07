import numpy as np
import re
from itertools import chain

class Solver:
    def __init__(self,input):
        self.input = input
        self.size = len(input)

    # check if position has a number and is not out of index range
    def try_number(self,x,y):
        try:
            int(self.input[x][y])
            return True
        except ValueError:
            return False
        except IndexError:
            return False

    # 
    def get_coordinates(self,regex):
        mask = []
        for line in self.input:
            mask += [list(map(lambda x: bool(re.match(regex, x)), line))]
        return [list(coord) for coord in np.transpose(np.where(mask))]
    
    def remove_duplicates(self,in_list):
        return [list(d) for d in list(dict.fromkeys([tuple(e) for e in in_list]))]
    
    def get_adjacent_number_coordinates(self, position):
        adjacent_number_coordinates = []
        x,y = position
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if i | j:
                    if self.try_number(x+i,y+j):
                        adjacent_number_coordinates += [[x+i,y+j]]
        return adjacent_number_coordinates
    
    def get_number_and_coordinates(self, position):
        x = position[0]
        y_start = position[1]
        y_end = position[1]
        while(True):
            if self.try_number(x,y_start-1):
                y_start -= 1
            elif self.try_number(x,y_end+1):
                y_end += 1
            else:
                break
        number = int(''.join(self.input[x][y_start:y_end+1]))
        return [x,y_start,y_end,number]
    
    def solve(self, regex, part):
        engine_coordinates = self.get_coordinates(regex)
        if (part == 1):
            numbers_with_coordinates = []
            for position in engine_coordinates:
                for adjacent_number_coordinate in self.get_adjacent_number_coordinates(position):
                    numbers_with_coordinates += [self.get_number_and_coordinates(adjacent_number_coordinate)]

            print(sum([n_w_c[3] for n_w_c in self.remove_duplicates(numbers_with_coordinates)]))

        if (part == 2):
            engine_power = 1
            for position in engine_coordinates:
                numbers_with_coordinates = [self.get_number_and_coordinates(p) for p in  self.get_adjacent_number_coordinates(position)]
                distinct_numbers = [n_w_c[3] for n_w_c in self.remove_duplicates(numbers_with_coordinates)]
                if len(distinct_numbers) == 2:
                    engine_power += distinct_numbers[0]*distinct_numbers[1]
            print(engine_power)

def solve(input):

    solver = Solver(input)
    solver.solve('[^\d\.]',1)
    solver.solve('\*',2)