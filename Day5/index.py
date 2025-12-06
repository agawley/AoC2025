with open("data.txt") as f:
    input = [line.strip() for line in f.readlines()]


def part1():
    ranges = True
    fresh_IDs = []
    count = 0
    for line in input:
        if line == "":
            ranges = False
            continue
        if ranges:
            range_ends = [int(num) for num in line.split("-")]
            fresh_IDs.append(range_ends)
        else:
            for ID_range in fresh_IDs:
                if int(line) >= ID_range[0] and int(line) <= ID_range[1]:
                    count += 1
                    break
    print(count)


# part1()


def part2():
    ranges = []
    for line in input:
        if line == "":
            break
        range_ends = [int(num) for num in line.split("-")]
        ranges.append(range_ends)
    print(ranges)
    # Sort ranges by their starting point
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    # Merge overlapping ranges
    merged_ranges = []
    for r in sorted_ranges:
        # Just append the first range
        if not merged_ranges:
            merged_ranges.append(r)
        else:
            # Get largest previous (merged) range. It is guaranteed to have starting point lower than r
            last = merged_ranges[-1]
            if r[0] <= last[1]:  # Overlap
                last[1] = max(last[1], r[1])  # Merge
            else:
                merged_ranges.append(r)
    print("Merged Ranges:", merged_ranges)
    count = 0
    for r in merged_ranges:
        count += r[1] - r[0] + 1
    print(count)


part2()
