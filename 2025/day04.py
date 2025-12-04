from helper import get_input


ROLLS_SYMBOL = "@"


def get_neighbours(grid, x, y):
    neighbours = []
    for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        if 0 <= x + dx < len(grid[0]) and 0 <= y + dy < len(grid) and grid[y + dy][x + dx] == ROLLS_SYMBOL:
            neighbours.append((x + dx, y + dy))
    return neighbours


def main(lines):
    is_removable_roll = lambda x, y: lines[y][x] == ROLLS_SYMBOL and len(get_neighbours(lines, x, y)) < 4
    to_remove = set([ (x, y) for y in range(len(lines)) for x in range(len(lines[y])) if is_removable_roll(x, y) ])

    print(f"Part 1: {len(to_remove)}")

    removed_count = 0
    while len(to_remove) > 0:
        removed_count += len(to_remove)
        for dx, dy in to_remove:
             lines[dy] = lines[dy][:dx] + "." + lines[dy][dx + 1:]
        to_remove = set([ (nx, ny) for dx, dy in to_remove for nx, ny in get_neighbours(lines, dx, dy) if is_removable_roll(nx, ny) ])

    print(f"Part 2: {removed_count}")


if __name__ == '__main__':
    lines = get_input()
    main(lines)
