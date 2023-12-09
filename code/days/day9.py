from days.base import Basesolver

class Solver(Basesolver):



    def solve_1(self):
        sum_extrapolates = 0
        for history in self.input:
            sum_extrapolates += self.get_extrapolation_f(history)
        return sum_extrapolates
    
    def solve_2(self):
        sum_extrapolates = 0
        for history in self.input:
            sum_extrapolates += self.get_extrapolation_h(history)
        return sum_extrapolates

    # future
    def get_extrapolation_f(self,seq):
        diff = self.get_differences(seq)
        if self.is_zeros(diff):
            return seq[-1]+diff[-1]
        else:
            return seq[-1]+self.get_extrapolation_f(diff)
        
    # history
    def get_extrapolation_h(self,seq):
        diff = self.get_differences(seq)
        if self.is_zeros(diff):
            return seq[0]-diff[0]
        else:
            return seq[0]-self.get_extrapolation_h(diff)

    def get_differences(self,seq):
        return [j-i for i, j in zip(seq[:-1], seq[1:])]
    
    def is_zeros(self,seq):
        return sum([abs(s) for s in seq]) == 0