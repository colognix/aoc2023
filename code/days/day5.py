import math
import numpy as np
from days.base import Basesolver

class Solver(Basesolver):
    def process_input(self, input):
        self.seeds = [int(s) for s in input[0].split(': ')[1].split(' ')]
        self.conversions = []
        tmp = []
        for line in input[3:]:
            if len(line) == 0:
                continue
            if ':' in line:
                conversions += [tmp]
                tmp = []
            else:
                tmp += [[int(v) for v in line.split(' ')]]
        self.conversions += [tmp]

    def solve_1(self):
        min_loc = math.inf
        for i in range(len(self.seeds)):
            min_loc = min(min_loc,self.convert_single(self.seeds[i], self.conversion_path))
        return min_loc
    
    def solve_2(self):
        min_loc = math.inf
        for i in range(0,len(self.seeds),2):
            min_loc = min(min_loc, self.convert_bulk(self.seeds[i], self.seeds[i]+self.seeds[i+1], self.conversion_path))
        return min_loc

    def convert_single(self, s, conversion_path):
        for conversions in conversion_path:
            converted = False
            for conversion in conversions:
                if (not converted) & (s >= conversion[1]) & (s < conversion[1]+conversion[2]):
                    s += conversion[0]-conversion[1]
                    converted = True
        return s

    def convert_bulk(self, s_start, s_end, conversion_path):
        seeds = np.arange(s_start, s_end, dtype=float)
        for conversions in conversion_path:
            converted = np.array([False]*len(seeds))
            for conversion in conversions:
                cond = np.where((converted == False) & (seeds >= conversion[1]) & (seeds < conversion[1]+conversion[2]))
                seeds[cond] += conversion[0]-conversion[1]
                converted[cond] = True
        return np.min(seeds)