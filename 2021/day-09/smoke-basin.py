#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='The input file')

args = parser.parse_args()

MAP_DIAGONALS = True

with open(args.filename) as file:
    lines = file.readlines()
    lines = [[int(x) for x in list(line.rstrip())] for line in lines]

num_rows = len(lines)
num_cols = len(lines[0])

for line in lines:
    print(line)

low_points = []

diffs = [
    #(-1, -1),
    (-1, 0),
    #(-1, 1),
    (0, -1),
    #(0, 0),
    (0, 1),
    #(1, -1),
    (1, 0),
    #(1, 1)
]

risk_level_sum = 0

low_coords = []

for row,line in enumerate(lines):
    low_points.append([True] * num_cols)

    for col,cell in enumerate(line):
        for diff in diffs:
            x = col + diff[0]
            y = row + diff[1]
            if x >= 0 and x < num_cols and y >= 0 and y < num_rows:
                if lines[y][x] <= cell:
                    low_points[row][col] = False

        if low_points[row][col]:
            low_coords.append((col, row))
            risk_level = cell + 1
            print(f"risk level ({col}, {row}): {risk_level}")
            risk_level_sum += risk_level


print()
for row in low_points:
    print(row)

print(low_coords)

print()
print(f"The total risk level is {risk_level_sum}")


# Part 2

print()
print("== Part 2 ==")
basins = {}

for lowpoint in low_coords:
    print(f"low point {lowpoint}")
    basin_cells = []






