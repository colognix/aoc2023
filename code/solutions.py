import day1,day2,day3,day4
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
    if day == 3:
        day3.solve(input)
    if day == 4:
        day4.solve(input)

#solve(1)
#solve(2)
#solve(3)
solve(4)