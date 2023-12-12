from days.base import Basesolver
import numpy as np
from itertools import combinations

class Solver(Basesolver):
    def process_input(self, input):
        self.image = np.array(input,dtype=str)
        self.get_emptiness()
    
    def solve(self):
        galaxies = [list(g) for g in np.transpose(np.where(self.image == '#'))]
        galaxy_pairs = list(combinations(galaxies,2))
        galaxy_length = 0
        for g1,g2 in galaxy_pairs:
            galaxy_length += self.compute_distance(g1,g2)
        return galaxy_length
       
    def get_emptiness(self):
        self.empty_rows = []
        self.empty_columns = []
        for i in range(self.image.shape[0]):
            if (self.image[i,:] == '.').all():
                self.empty_rows += [i]
        for j in range(self.image.shape[1]):
            if (self.image[:,j] == '.').all():
                self.empty_columns += [j]
        self.empty_rows = set(self.empty_rows)
        self.empty_columns = set(self.empty_columns)

    def compute_distance(self,g1,g2):
        dist = abs(g1[0]-g2[0]) + abs(g1[1]-g2[1])
        if g1[0] > g2[0]:
            rows_passed = set(range(g2[0],g1[0]))
        else:
            rows_passed = set(range(g1[0],g2[0]))
        if g1[1] > g2[1]:
            columns_passed = set(range(g2[1],g1[1]))
        else:
            columns_passed = set(range(g1[1],g2[1]))
        if self.part == 1:
            dist += len(self.empty_rows.intersection(rows_passed))
            dist += len(self.empty_columns.intersection(columns_passed))
        if self.part == 2:
            dist += 999999*len(self.empty_rows.intersection(rows_passed))
            dist += 999999*len(self.empty_columns.intersection(columns_passed))
        return dist
