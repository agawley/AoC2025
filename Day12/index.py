with open("data.txt") as f:
    input = [line.strip() for line in f.readlines()]


def parse_input(input):
    shape_num = 0
    shapes = {}
    boards = []
    parsing_shape = False
    parsing_board = False
    for line in input:
        if not parsing_shape and not parsing_board:
            if line[-1] == ":":
                shape_num = int(line[0])
                parsing_shape = True
                continue
            elif "x" in line:
                boards.append(parse_board(line))
                parsing_board = True
                continue
        elif parsing_shape:
            if line == "":
                parsing_shape = False
                parsing_board = False
                continue
            else:
                shapes[shape_num] = shapes.get(shape_num, "") + line
        elif parsing_board:
            boards.append(parse_board(line))
    return shapes, boards


def parse_board(b_line):
    shape, required_shapes = b_line.split(": ")
    width, height = map(int, shape.split("x"))
    required_shapes = list(map(int, required_shapes.split(" ")))
    return (width, height, required_shapes)


def get_shape_info(shape):
    parity = 2 if shape.count("#") % 2 == 0 else 1
    size = shape.count("#")
    return parity, size


def can_fill_board(board, shapes):
    width, height, required_shapes = board
    area = width * height
    area_check = 0
    for shape_num, req in enumerate(required_shapes):
        shape = shapes[shape_num]
        _, shape_size = get_shape_info(shape)
        area_check += shape_size * req
    print(board)

    return area_check <= area


shapes, boards = parse_input(input)
count = 0

for shape in shapes.values():
    print(get_shape_info(shape))

for board in boards:
    if can_fill_board(board, shapes):
        count += 1

print(count)
