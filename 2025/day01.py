from helper import get_input


def main():
    lines = get_input()
    res = 50
    perfect_zero = 0
    passed_zero = 0
    for line in lines:

        sign = (1 if line[0] == "R" else -1)
        remainder = int(line[1:]) % 100

        passed_zero += int(line[1:]) // 100

        acc = res + sign * remainder
        if (sign > 0 and acc > 99) or (sign < 0 < res and acc < 1):
            passed_zero += 1

        res = (acc + 100) % 100
        if res == 0:
            perfect_zero += 1

    print(f"Part 1: {perfect_zero}")
    print(f"Part 2: {passed_zero}")


if __name__ == '__main__':
    main()

