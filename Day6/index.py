with open("data.txt") as f:
    input = f.readlines()


def part1():
    raw_problems = [line.strip().split() for line in input]
    print(raw_problems)
    problems = list(zip(*raw_problems))
    print(problems)
    total = 0

    for problem in problems:
        nums = []
        for val in problem:
            try:
                nums.append(int(val))
            except ValueError:
                if val == "+":
                    total += sum(nums)
                if val == "*":
                    product = 1
                    for n in nums:
                        product *= n
                    total += product
    return total


# print(part1())


def part2():
    problems = list(zip(*[line.replace("\n", "") for line in input]))
    operator = ""
    values = []
    total = 0
    for column in problems:
        print(column)
        if column == (" ", " ", " ", " ", " "):
            if operator == "+":
                print("SUM:", sum(values))
                total += sum(values)
            elif operator == "*":
                product = 1
                for n in values:
                    product *= n
                print("PRODUCT:", product)
                total += product
            operator = ""
            values = []
            continue
        value = ""
        for val in column:
            if val in ("+", "*"):
                operator = val
            elif val == "":
                continue
            else:
                value += val
        if value:
            values.append(int(value))
    print(total)


part2()
