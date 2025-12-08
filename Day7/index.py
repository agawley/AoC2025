with open("data.txt") as f:
    lines = [line.strip() for line in f.readlines()]

visited_nodes = set()


def follow_path(lines, line_num, pos):
    if line_num == len(lines):
        return 0
    if lines[line_num][pos] == ".":
        return follow_path(lines, line_num + 1, pos)
    if lines[line_num][pos] == "^":
        if (line_num, pos) in visited_nodes:
            return 0
        visited_nodes.add((line_num, pos))
        return (
            1
            + follow_path(lines, line_num, pos - 1)
            + follow_path(lines, line_num, pos + 1)
        )


bottoms = 0


def follow_all_paths(lines, line_num, pos):
    global bottoms
    if line_num == len(lines):
        bottoms += 1
        print(bottoms)
        return 1
    if lines[line_num][pos] == ".":
        return follow_all_paths(lines, line_num + 1, pos)
    if lines[line_num][pos] == "^":
        return follow_all_paths(lines, line_num, pos - 1) + follow_all_paths(
            lines, line_num, pos + 1
        )


def part1():
    start_pos = lines[0].index("S")
    return follow_path(lines, 1, start_pos)


def part2():
    beams = {}
    paths = 1
    print(len(lines))
    beams[lines[0].index("S")] = 1
    for line in lines[1:]:
        for key, val in beams.copy().items():
            if line[key] == "^":
                beams[key - 1] = beams.get(key - 1, 0) + val
                beams[key + 1] = beams.get(key + 1, 0) + val
                beams[key] = 0
    return sum(beams.values())


print(part1())

print(part2())
