from timeit import default_timer as timer

class Basesolver:

    def __init__(self,input):
        self.process_input(input)
        self.set_constants()
        self.set_part(1)

    # process input, override if neccessary
    def process_input(self,input):
        self.input = input

    # declare constant stuff for both parts
    def set_constants(self):
        return

    # set part for checks and also load part dependent stuff, override if neccessary
    def set_part(self,part):
        self.part = part

    def solve_1(self):
        return input
    
    def solve_2(self):
        return input

    # solve, needs to be overwritten
    def solve(self):
        if self.part == 1:
            start = timer()
            solution = self.solve_1()
            print('Part 1 took ' + str(timer()-start) + ' seconds.')
            return solution
        if self.part == 2:
            start = timer()
            solution = self.solve_2()
            print('Part 2 took ' + str(timer()-start) + ' seconds.')
            return solution
