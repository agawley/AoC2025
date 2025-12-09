import math

with open("data.txt") as f:
    boxes = [
        tuple(int(val) for val in line.strip().split(",")) for line in f.readlines()
    ]


def distance(point1, point2):
    return math.sqrt(
        (point1[0] - point2[0]) ** 2
        + (point1[1] - point2[1]) ** 2
        + (point1[2] - point2[2]) ** 2
    )


def part1():
    box_distance = []
    circuits = []
    for box in boxes:
        circuits.append(set([box]))
        for other_box in boxes:
            if box != other_box:
                box_distance.append((box, other_box, distance(box, other_box)))
    boxes_by_distance = sorted(box_distance, key=lambda x: x[2])[1::2]
    for box1, box2, _ in boxes_by_distance[:1000]:
        circuit_one = 0
        circuit_two = 0
        for i in range(len(circuits)):
            if box1 in circuits[i]:
                circuit_one = i
            if box2 in circuits[i]:
                circuit_two = i
        if circuit_one == circuit_two:
            continue
        else:
            circuits[circuit_one] = circuits[circuit_one].union(circuits[circuit_two])
            circuits.pop(circuit_two)
    largest_circuits = sorted(circuits, key=lambda circuit: len(circuit), reverse=True)[
        :3
    ]
    total = 1
    for circuit in largest_circuits:
        total *= len(circuit)
    print(total)


# part1()


def part2():
    box_distance = []
    circuits = []
    for box in boxes:
        circuits.append(set([box]))
        for other_box in boxes:
            if box != other_box:
                box_distance.append((box, other_box, distance(box, other_box)))
    boxes_by_distance = sorted(box_distance, key=lambda x: x[2])[1::2]
    for box1, box2, _ in boxes_by_distance:
        circuit_one = 0
        circuit_two = 0
        for i in range(len(circuits)):
            if box1 in circuits[i]:
                circuit_one = i
            if box2 in circuits[i]:
                circuit_two = i
        if circuit_one == circuit_two:
            continue
        else:
            circuits[circuit_one] = circuits[circuit_one].union(circuits[circuit_two])
            circuits.pop(circuit_two)
        if len(circuits) == 1:
            print(box1[0] * box2[0])


part2()
