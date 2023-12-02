import day1
import aoc_utils

def solve (day, input_format, example=False):
    if (example):
        input = aoc_utils.read_input('./input/example_day' + str(day) + '.txt', input_format)
    else:
        input = aoc_utils.read_input('./input/in_day' + str(day) + '.txt', input_format)
    if day == 1:
        day1.solve(input)



solve(1, 'plain_lines')