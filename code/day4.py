import numpy as np

def process_input(input):
    return [[set([int(n) for n in m.split(' ')]) for m in line.split('|')] for line in input]

def makeshift_pow(n):
    if n == 0:
        return 0
    else:
        return pow(2,n-1)
    
def sum_up_the_scratch(games):
    scratch_multiples = np.array([1]*len(games))
    scratch_sum = 0
    for i in range(len(games)):
        # how many consecutive cards are added
        scratch_adds = len(games[i][0].intersection(games[i][1]))
        # take into account multiplicity from earlier rounds
        scratch_multiples[i+1:i+1+scratch_adds] += scratch_multiples[i]
        scratch_sum += scratch_multiples[i]

    return scratch_sum

def solve(input):
    games = process_input(input)
    # part 1
    print(sum([makeshift_pow(len(g[0].intersection(g[1]))) for g in games]))
    #part 2
    print(sum_up_the_scratch(games))