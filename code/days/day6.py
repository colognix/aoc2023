import numpy as np

def process(input):
    return np.transpose(input)

def get_distances(time):
    return [i*(time-i) for i in range(time+1)]

def get_win_count(race):
    return len([i for i in get_distances(int(race[0])) if i > int(race[1])])

def solve(input):
    
    # part 1
    races = process(input)
    print(np.prod([get_win_count(race) for race in races]))
    # part 2
    race = [''.join(input[0]),''.join(input[1])]
    print(get_win_count(race))