import day1,day2
import aoc_utils

def solve (day, example=False):
    if (example):
        input = aoc_utils.read_input('./input/example_day', day)
    else:
        input = aoc_utils.read_input('./input/in_day', day)
    if day == 1:
        day1.solve(input)
    if day == 2:
        day2.solve(input)


#solve(1)
solve(2)