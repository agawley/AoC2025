with open("data.txt") as f:
    instructions = [line.strip() for line in f.readlines()]

pos = 50
count_zero = 0
number_of_positions = 100

for instruction in instructions:
    print(instruction)
    dir = instruction[0]
    val = int(instruction[1:])
    
    if dir == "R":
        num_rotations = (pos + val) // number_of_positions
        count_zero += num_rotations
        pos = (pos + val) % number_of_positions
    if dir == "L":
        num_rotations = -((pos - val - 1) // number_of_positions)
        count_zero += (num_rotations - (1 if pos == 0 else 0))
        pos = (pos - val) % number_of_positions
    print(pos)
    print("-----")

print(count_zero)