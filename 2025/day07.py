from helper import get_input


def main(starting_pos, splitters, max_x, max_y):
    splits = 0
    positions = { starting_pos: 1 }
    while next(iter(positions))[1] < max_y:
        splitters_hit = { (x, y): n for (x, y), n in positions.items() if (x, y) in splitters }
        positions = { (x, y + 1): n for (x, y), n in positions.items() if (x, y) not in splitters_hit }
        for (x, y), n in splitters_hit.items():
            if x > 0:
                positions[(x - 1, y + 1)] = positions.get((x - 1, y + 1), 0) + n
            if x < max_x:
                positions[(x + 1, y + 1)] = positions.get((x + 1, y + 1), 0) + n
        splits += len(splitters_hit)
    print(f"Part 1 {splits}")
    print(f"Part 1 {sum(positions.values())}")


def get_data(lines):
    max_x =  len(lines[0])
    max_y = len(lines)
    raw = ''.join(lines)
    starting_index = raw.find('S')
    starting_pos = (starting_index % max_x, starting_index // max_x)
    splitters = set((index % max_x, index // max_x) for index, character in enumerate(raw) if character == '^')
    return starting_pos, splitters, max_x - 1, max_y - 1


if __name__ == '__main__':
    lines = get_input()
    starting_pos, splitters, max_x, max_y = get_data(lines)
    main(starting_pos, splitters, max_x, max_y)
