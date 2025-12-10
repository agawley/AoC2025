with open("data.txt") as f:
    red_tiles = [[int(x) for x in item.strip().split(",")] for item in f.readlines()]


def part1():
    max_rect_area = 0
    for tile in red_tiles:
        for other_tile in red_tiles:
            if tile == other_tile:
                continue
            area = (abs(tile[0] - other_tile[0]) + 1) * (
                abs(tile[1] - other_tile[1]) + 1
            )
            if area > max_rect_area:
                max_rect_area = area
    print(max_rect_area)


part1()
