import aoc_utils
from importlib import import_module

def solve (day, example=False):
    if (example):
        input = aoc_utils.read_input('./input/example_day', day)
    else:
        input = aoc_utils.read_input('./input/in_day', day)

    solver = import_module('days.day'+str(day))
    solver.solve(input)

solve(7)