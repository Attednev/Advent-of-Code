from helper import get_input


def part1(ranges, ingredients):
    ingredient_idx = 0
    ranges_idx = 0
    fresh = 0
    while ingredient_idx < len(ingredients) and ranges_idx < len(ranges):
        if ingredients[ingredient_idx] < ranges[ranges_idx][0]:
            ingredient_idx += 1
        elif ingredients[ingredient_idx] > ranges[ranges_idx][1]:
            ranges_idx += 1
        else:
            fresh += 1
            ingredient_idx += 1
    print(f"Part 1 {fresh}")


def part2(ranges):
    for i in range(1, len(ranges)):
        start, end = ranges[i]
        prev_start, prev_end = ranges[i - 1]
        if start == prev_end + 1:
            ranges[i] = (prev_start, end)
            ranges[i - 1] = (0, 0)
        if prev_start <= start <= prev_end:
            ranges[i] = (prev_start, max(end, prev_end))
            ranges[i - 1] = (0, 0)
    max_fresh = 0
    for start, end in ranges:
        if start == end:
            continue
        max_fresh += end - start + 1
    print(f"Part 2 {max_fresh}")


def main(lines):
    ranges = []
    ingredients = []
    for l in lines:
        splits = l.split("-")
        if len(splits) == 1:
            if splits[0] == "":
                continue
            ingredients.append(int(splits[0]))
        else:
            ranges.append((int(splits[0]), int(splits[1])))
    ingredients.sort()
    ranges.sort()
    part1(ranges, ingredients)
    part2(ranges)


if __name__ == '__main__':
    lines = get_input()
    main(lines)
