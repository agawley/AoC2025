with open("data.txt") as file:
    grid = [list(line.strip()) for line in file.readlines()]


def part1():
    rows = len(grid)
    cols = len(grid[0])
    visible_count = 0

    for y, columns in enumerate(grid):
        for x, c in enumerate(columns):
            if c == ".":
                continue
            neighbours = 0
            for dy, dx in [
                (-1, 0),
                (-1, -1),
                (-1, 1),
                (0, 1),
                (0, -1),
                (1, 0),
                (1, 1),
                (1, -1),
            ]:
                ny, nx = y + dy, x + dx
                if not (0 <= ny < rows and 0 <= nx < cols):
                    continue
                if grid[ny][nx] == "@":
                    neighbours += 1
                    if neighbours == 4:
                        break
            visible_count = visible_count + 1 if neighbours < 4 else visible_count

    return visible_count


def part2():
    rows = len(grid)
    cols = len(grid[0])
    visible_count = 0

    while True:
        removals = []
        for y, columns in enumerate(grid):
            for x, c in enumerate(columns):
                if c == ".":
                    continue
                neighbours = 0
                for dy, dx in [
                    (-1, 0),
                    (-1, -1),
                    (-1, 1),
                    (0, 1),
                    (0, -1),
                    (1, 0),
                    (1, 1),
                    (1, -1),
                ]:
                    ny, nx = y + dy, x + dx
                    if not (0 <= ny < rows and 0 <= nx < cols):
                        continue
                    if grid[ny][nx] == "@":
                        neighbours += 1
                        if neighbours == 4:
                            break
                if neighbours < 4:
                    visible_count = visible_count + 1
                    removals.append((y, x))

        if len(removals) == 0:
            break
        for y, x in removals:
            grid[y][x] = "."

    return (visible_count, grid)


print(part2())
