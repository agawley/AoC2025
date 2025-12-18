from functools import reduce
from itertools import combinations

with open("test.txt") as f:
    input = [line.split() for line in f.read().splitlines()]


def get_bit_values(input):
    machines = ()
    for line in input:
        target_string = line[0][1:-1][::-1]
        target_string_length = len(target_string)
        target = 0
        for i, char in enumerate(target_string):
            if char == "#":
                target += 2**i
        buttons = []
        for button in line[1:-1]:
            button_val = 0
            bits = [int(val) for val in button[1:-1].split(",")]
            for bit in bits:
                button_val += 2 ** (target_string_length - bit - 1)
            buttons.append(button_val)
        machines += ((target, buttons),)
    return machines


def part1():
    machines = get_bit_values(input)
    total = 0
    for machine in machines:
        total += check_machine(machine)
    print("Total:", total)


def check_machine(machine):
    target, buttons = machine
    for i in range(1, len(buttons) + 1):
        for combo in combinations(buttons, i):
            if reduce(lambda x, y: x ^ y, combo, 0) == target:
                print("Found combo:", combo)
                return len(combo)
    return 0


# part1()


def part2():
    for I, L in enumerate(input, 1):
        _, *coeffs, goal = L
        goal = tuple(int(i) for i in goal[1:-1].split(","))
        coeffs = [[int(i) for i in r[1:-1].split(",")] for r in coeffs]
        coeffs = [tuple(int(i in r) for i in range(len(goal))) for r in coeffs]
        print(coeffs)

def get 

part2()
