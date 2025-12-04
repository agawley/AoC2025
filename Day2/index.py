import re

with open("data.txt") as f:
    input = f.read()


def part1():
    total = 0
    matcher = re.compile(r"^(\d+)\1$")

    for item in input.split(","):
        ends = [int(val) for val in item.split("-")]
        for i in range(ends[0], ends[1] + 1):
            if matcher.match(str(i)):
                total += i
    print(total)


def part2():
    total = 0
    matcher = re.compile(r"^(\d+)\1+$")

    for item in input.split(","):
        ends = [int(val) for val in item.split("-")]
        for i in range(ends[0], ends[1] + 1):
            if matcher.match(str(i)):
                total += i
    print(total)


part1()
part2()
