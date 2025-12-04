import re
from math import ceil
from helper import get_input


def main(MAX_REP):
    line = get_input()[0]
    splits = re.split(r"[,-]", line)
    ranges = list(zip(splits[0::2], splits[1::2]))
    largest = max(splits, key=int)

    numbers = set()
    max_i = '9' * ceil(len(largest) / 2)
    for i in range(1, int(max_i)):
        for j in range(2, MAX_REP):
            current = f"{i}" * j
            if int(current) > int(largest):
                break
            for s, e in ranges:
                if int(s) <= int(current) <= int(e):
                    numbers.add(current)
                    break
    return sum(int(n) for n in numbers)


if __name__ == '__main__':
    print(f"Part 1: {main(3)}")
    print(f"Part 2: {main(100)}")
