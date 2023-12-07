
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
        return
    
    def solve_2(self):
        return

    # solve, needs to be overwritten
    def solve(self):
        if self.part == 1:
            return self.solve_1()
        if self.part == 2:
            return self.solve_2()
