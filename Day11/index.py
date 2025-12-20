from functools import cache

with open("data.txt") as f:
    nodes = [
        {line_list[0][:-1]: line_list[1:]}
        for line_list in [line.split() for line in f.readlines()]
    ]


def get_path_count(start, end):
    if start == end:
        return 1
    total_paths = 0
    for node in nodes:
        if start in node:
            for next_node in node[start]:
                total_paths += get_path_count(next_node, end)
    return total_paths


@cache
def get_path_count_with_stops(start, end, has_fft, has_dac):
    if start == end:
        if has_fft and has_dac:
            return 1
        else:
            return 0
    total_paths = 0
    for node in nodes:
        if start in node:
            for next_node in node[start]:
                total_paths += get_path_count_with_stops(
                    next_node,
                    end,
                    has_fft or next_node == "fft",
                    has_dac or next_node == "dac",
                )
    return total_paths


def part1():
    print(get_path_count("you", "out"))
    return


def part2():
    print(get_path_count_with_stops("svr", "out", False, False))
    return


part1()
part2()
