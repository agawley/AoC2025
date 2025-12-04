with open("data.txt") as f:
    instructions = [line.strip() for line in f.readlines()]

pos = 50
count_zero = 0
number_of_positions = 100

for instruction in instructions:
    #print(instruction)
    dir = instruction[0]
    val = int(instruction[1:])
    if dir == "L":
        pos = (pos -val) % number_of_positions
    elif dir == "R":
        pos = (pos + val) % number_of_positions
    if pos == 0:
        count_zero += 1
    #print(pos)
    #print("-----")

print(count_zero)