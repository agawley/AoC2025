from functools import reduce
from itertools import combinations, product

import numpy as np

with open("data.txt") as f:
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
def get_matrix_from_input_line(line):
    target_jolts = [int(val) for val in line[-1][1:-1].split(",")]
    raw_buttons = [
        [int(val) for val in button[1:-1].split(",")] for button in line[1:-1]
    ]
    buttons = []
    for button in raw_buttons:
        button_array = np.zeros(len(target_jolts), dtype=int)
        for jolt in button:
            button_array[jolt] = 1
        buttons.append(button_array)
    output_matrix = np.zeros((len(target_jolts), len(buttons) + 1), dtype=float)
    for i, button in enumerate(buttons):
        output_matrix[:, i] = button
    output_matrix[:, -1] = target_jolts
    return output_matrix


def rectangular_gaussian_elimination(M):
    rows, cols = M.shape
    num_vars = cols - 1

    pivot_cols = []
    free_cols = []

    curr_row = 0

    for curr_col in range(num_vars):
        # print(curr_row)
        if curr_row >= rows:
            # We ran out of equations! The rest are free variables.
            free_cols.append(curr_col)
            continue

        # Look at the column 'curr_col' from 'curr_row' downwards
        candidates = np.abs(M[curr_row:, curr_col])
        row_with_max_value = np.argmax(candidates) + curr_row

        # If the best pivot is 0, this variable is linearly dependent (Free)
        if (
            np.abs(M[row_with_max_value, curr_col]) < 1e-10
        ):  # Consider a small tolerance for floating point
            free_cols.append(curr_col)
            continue  # Move to next column, but stay on same row

        # Found a pivot! Mark it.
        pivot_cols.append(curr_col)

        # Swap rows to bring pivot to top
        if curr_row != row_with_max_value:
            M[[curr_row, row_with_max_value]] = M[[row_with_max_value, curr_row]]

        # Normalize the pivot row (make diagonal 1)
        M[curr_row] = M[curr_row] / M[curr_row, curr_col]

        # print("normalise")
        # print(M)

        # Zero out this column in ALL other rows by subtracting a factor of the pivot row
        for r in range(rows):
            if r != curr_row:
                factor = M[r, curr_col]
                M[r] -= factor * M[curr_row]

        curr_row += 1

        # print(M)

    # print("Row-Echelon Form:\n", M)

    return pivot_cols, free_cols


def solve_hybrid(A, b, p_cols, f_cols):
    A_sq = A[:, p_cols]
    A_free = A[:, f_cols]

    num_free = len(f_cols)
    best_cost = float("inf")
    found = False

    # Heuristic limit for free variables (usually small, e.g., 0-20)
    for free_vals in product(range(50), repeat=num_free):
        x_free = np.array(free_vals)

        # Calculate the Pivot Variables based on the Free Variables
        rhs = b - (A_free @ x_free)
        x_sq, residuals, rank, s = np.linalg.lstsq(A_sq, rhs, rcond=None)

        if residuals.size > 0 and residuals[0] > 1e-9:
            # print(f"  [Free={x_free}] -> Residual Error (No Solution)")
            continue

        x_sq_rounded = np.round(x_sq)

        if not np.allclose(x_sq, x_sq_rounded, atol=1e-9):
            # print(f"  [Free={x_free}] -> Result {np.round(x_sq, 2)} (Not Integers)")
            continue

        if np.any(x_sq_rounded < 0):
            # print(
            #    f"  [Free={x_free}] -> Result {x_sq_rounded.astype(int)} (Negative values!)"
            # )
            continue

        total_presses = np.sum(x_free) + np.sum(x_sq_rounded)
        # print(
        #    f"  [Free={x_free}] -> VALID SOLUTION! x_pivot={x_sq_rounded.astype(int)}. Total Cost: {total_presses}"
        # )
        if total_presses < best_cost:
            best_cost = total_presses
            found = True
    if not found:
        for free_vals in product(range(200), repeat=num_free):
            x_free = np.array(free_vals)

            # Calculate the Pivot Variables based on the Free Variables
            rhs = b - (A_free @ x_free)
            x_sq, residuals, rank, s = np.linalg.lstsq(A_sq, rhs, rcond=None)

            if residuals.size > 0 and residuals[0] > 1e-9:
                # print(f"  [Free={x_free}] -> Residual Error (No Solution)")
                continue

            x_sq_rounded = np.round(x_sq)

            if not np.allclose(x_sq, x_sq_rounded, atol=1e-9):
                # print(f"  [Free={x_free}] -> Result {np.round(x_sq, 2)} (Not Integers)")
                continue

            if np.any(x_sq_rounded < 0):
                # print(
                #    f"  [Free={x_free}] -> Result {x_sq_rounded.astype(int)} (Negative values!)"
                # )
                continue

            total_presses = np.sum(x_free) + np.sum(x_sq_rounded)
            # print(
            #    f"  [Free={x_free}] -> VALID SOLUTION! x_pivot={x_sq_rounded.astype(int)}. Total Cost: {total_presses}"
            # )
            if total_presses < best_cost:
                best_cost = total_presses
                found = True
    if not found:
        print(f"No solution found for any free variable combination.{A}, {b}")
    return int(best_cost) if found else 0


def part2():
    total_cost = 0
    for line in input:
        base_matrix = get_matrix_from_input_line(line)
        pivot_cols, free_cols = rectangular_gaussian_elimination(base_matrix.copy())
        result = solve_hybrid(
            base_matrix[:, :-1], base_matrix[:, -1], pivot_cols, free_cols
        )
        total_cost += result
        print("Result:", result)
    print("Total Cost:", total_cost)


part2()

""" line = "[....###] (3,4) (0,1,2) (1,4,5,6) (2,4) (0,1) (0,2,5,6) (0,1,2,3,5,6) (2,5,6) {24,36,153,9,156,35,35}".split()
base_matrix = get_matrix_from_input_line(line)
print("Base Matrix:\n", base_matrix)
pivot_cols, free_cols = rectangular_gaussian_elimination(base_matrix.copy())
print("Pivot Columns:", pivot_cols)
print("Free Columns:", free_cols)
result = solve_hybrid(base_matrix[:, :-1], base_matrix[:, -1], pivot_cols, free_cols)
print("Result:", result)
 """
