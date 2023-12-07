import numpy as np
from days.base import Basesolver

class Solver(Basesolver):

    def process_input(self, input):
        self.races = np.transpose(input)
        self.race = [''.join(input[0]),''.join(input[1])]

    def solve_1(self):
        return np.prod([self.get_win_count(race) for race in self.races])
    
    def solve_2(self):
        return self.get_win_count(self.race)

    def get_distances(self,time):
        return [i*(time-i) for i in range(time+1)]

    def get_win_count(self,race):
        return len([i for i in self.get_distances(int(race[0])) if i > int(race[1])])