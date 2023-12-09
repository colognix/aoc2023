from days.base import Basesolver
from math import lcm

class Solver(Basesolver):
    
    def process_input(self, input):
        self.instructions = [i for i in input[0]]
        self.num_instructions = len(self.instructions)
        self.neighbourdict = {}
        for pos_and_neighbours in input[2:]:
            pos, neighbour_string = pos_and_neighbours.split('=')
            neighbour_list = neighbour_string.strip('()').split(',')
            self.neighbourdict[pos] = {'L':neighbour_list[0],'R':neighbour_list[1]}

    def solve_1(self):
        pos = 'AAA'
        steps = 0
        i = 0
        while pos != 'ZZZ':
            pos = self.neighbourdict[pos][self.instructions[i]]
            i += 1
            steps += 1
            if i == self.num_instructions:
                i = 0
        return steps
        

    def solve_2(self):
        steps = [self.get_steps(pos) for pos in self.neighbourdict if pos[-1] == 'A']
        return lcm(*steps)
    

    def get_steps(self,pos):
        steps = 0
        i = 0
        while pos[-1] != 'Z':
            pos = self.neighbourdict[pos][self.instructions[i]]
            i += 1
            steps += 1
            if i == self.num_instructions:
                i = 0
        return steps