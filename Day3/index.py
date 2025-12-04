with open("test.txt") as file:
    batteries = [line.strip() for line in file.readlines()]


def part1():
    total = 0
    for battery in batteries:
        print(battery)
        max_num = max(battery[: len(battery) - 1])
        print(max_num)
        max_num_pos = battery.index(max_num)
        print(max_num_pos)
        next_max_num = max(battery[max_num_pos + 1 :])
        print(next_max_num)
        total += int(max_num) * 10 + int(next_max_num)
    return total


# print(part1())


def part2():
    total = 0
    for battery in batteries:
        max_digits = []
        last_pos = 0
        for n in range(12):
            max_digit = max(battery[last_pos : len(battery) - (11 - n)])
            last_pos = battery.index(max_digit) + 1
            max_digits.append(max_digit)
            total += int(max_digit) * (10 ** (11 - n))
    return total


print(part2())
