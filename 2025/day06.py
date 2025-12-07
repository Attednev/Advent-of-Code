import re

from helper import get_input
import math

def part2(lines):
    number_lengths = [ len(whitespace) for whitespace in re.split(r'([+*])', lines[-1])[1:][1::2] ]
    # Counting whitespaces only works because the whitespace used to separate columns can be used as compensation
    # for the actual operator symbol, but since the last column has no next column, there is also no additional space
    # to compensate for the symbol, which is why we need to manually compensate for it
    number_lengths[-1] += 1

    results = []
    calculations = []
    for line in lines:
        current_calculation = 0
        index = 0
        while index < len(line):
            if len(calculations) < current_calculation + 1:
                calculations.append([ '' for _ in range(number_lengths[current_calculation]) ])
            for i in range(number_lengths[current_calculation]):
                if line[index] == '+':
                    results.append(sum([ int(n) for n in calculations[current_calculation] ]))
                elif line[index] == '*':
                    results.append(math.prod([ int(n) for n in calculations[current_calculation] ]))
                elif line[index] != ' ':
                    calculations[current_calculation][i] += line[index]
                index += 1
            current_calculation += 1
            index += 1 # To skip the whitespace between columns
    print(sum(results))


def part1(lines):
    results = []
    calculations = []
    for line in lines:
        numbers = list(filter(None, line.split(" ")))
        if len(calculations) == 0:
            calculations = [ [] for _ in range(len(numbers)) ]
        for i in range(len(numbers)):
            if not numbers[i].isdigit():
                results.append(sum(calculations[i]) if numbers[i] == "+" else math.prod(calculations[i]))
            else:
                calculations[i].append(int(numbers[i]))
    print(sum(results))


if __name__ == '__main__':
    lines = get_input()
    part1(lines)
    part2(lines)
