with open("data.txt") as f:
    red_tiles = [[int(x) for x in item.strip().split(",")] for item in f.readlines()]


def compress_2d_space(tiles):
    x_coords = sorted(set([tile[0] for tile in tiles]))
    y_coords = sorted(set([tile[1] for tile in tiles]))
    x_mapping = {x_coords[i]: i for i in range(len(x_coords))}
    y_mapping = {y_coords[i]: i for i in range(len(y_coords))}
    compressed_tiles = [[x_mapping[tile[0]], y_mapping[tile[1]]] for tile in tiles]
    return compressed_tiles, x_coords, y_coords


def part1():
    max_rect_area = 0
    tiles, x_coords, y_coords = compress_2d_space(red_tiles)
    for tile in tiles:
        for other_tile in tiles:
            if tile == other_tile:
                continue
            area = (abs(x_coords[tile[0]] - x_coords[other_tile[0]]) + 1) * (
                abs(y_coords[tile[1]] - y_coords[other_tile[1]]) + 1
            )
            if area > max_rect_area:
                max_rect_area = area
    print(max_rect_area)


part1()


def part2():
    max_rect_area = 0
    tiles, x_coords, y_coords = compress_2d_space(red_tiles)
    boundary = get_boundary(tiles)
    for tile in tiles:
        for other_tile in tiles:
            if tile == other_tile:
                continue
            if not check_rectangle_within_boundary(tile, other_tile, boundary):
                continue
            area = (abs(x_coords[tile[0]] - x_coords[other_tile[0]]) + 1) * (
                abs(y_coords[tile[1]] - y_coords[other_tile[1]]) + 1
            )
            if area > max_rect_area:
                max_rect_area = area
    print(max_rect_area)


def get_boundary(tiles):
    boundary_lines = {"horizontal": set(), "vertical": set()}
    for i in range(len(tiles)):
        first_tile = tiles[i]
        second_tile = tiles[(i + 1) % len(tiles)]
        if first_tile[0] == second_tile[0]:  # vertical line
            y_start = min(first_tile[1], second_tile[1])
            y_end = max(first_tile[1], second_tile[1])
            for y in range(y_start, y_end + 1):
                boundary_lines["vertical"].add((first_tile[0], y))
        elif first_tile[1] == second_tile[1]:  # horizontal line
            x_start = min(first_tile[0], second_tile[0])
            x_end = max(first_tile[0], second_tile[0])
            for x in range(x_start, x_end + 1):
                boundary_lines["horizontal"].add((x, first_tile[1]))

    return boundary_lines


def check_rectangle_within_boundary(start, end, boundary):
    x_start = min(start[0], end[0])
    x_end = max(start[0], end[0])
    y_start = min(start[1], end[1])
    y_end = max(start[1], end[1])

    # horizontal lines
    for x in range(x_start + 1, x_end):
        # Check bottom edge: if boundary enters upwards
        if (x, y_start) in boundary["vertical"]:
            return False
        # Check top edge: if boundary enters downwards
        if (x, y_end) in boundary["vertical"] and (x, y_end - 1) in boundary[
            "vertical"
        ]:
            return False

    # vertical lines
    for y in range(y_start + 1, y_end):
        # Check left edge: if boundary enters rightwards
        if (x_start, y) in boundary["horizontal"] and (x_start + 1, y) in boundary[
            "horizontal"
        ]:
            return False
        # Check right edge: if boundary enters leftwards
        if (x_end, y) in boundary["horizontal"] and (x_end - 1, y) in boundary[
            "horizontal"
        ]:
            return False
    return True


part2()


# Note that part2_uncompressed doesn't work
def part2_uncompressed():
    max_rect_area = 0
    tiles = red_tiles
    boundary = get_boundary(tiles)
    for tile in tiles:
        for other_tile in tiles:
            if tile == other_tile:
                continue
            if not check_rectangle_within_boundary(tile, other_tile, boundary):
                continue
            area = (abs(tile[0] - other_tile[0]) + 1) * (
                abs(tile[1] - other_tile[1]) + 1
            )
            if area > max_rect_area:
                max_rect_area = area
    print(max_rect_area)


part2_uncompressed()
