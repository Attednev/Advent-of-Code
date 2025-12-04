from helper import get_input


def max_joltage(batteries, flips):
    current = ""
    index = 0
    for current_len in range(flips):
        for i in range(index, len(batteries) - flips + current_len + 1):
            if batteries[i] > batteries[index]:
                index = i
        current += batteries[index]
        index += 1
    return int(current)


def main(lines, flips):
    total = 0
    for l in lines:
        total += max_joltage(l, flips)
    return total


if __name__ == '__main__':
    lines = get_input()
    print(f"Part 1: {main(lines, 2)}")
    print(f"Part 2: {main(lines, 12)}")

