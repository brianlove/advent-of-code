#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='The input file')
parser.add_argument('-d', '--diagonals', action='store_true', help='Map diagonals?')

args = parser.parse_args()

MAP_DIAGONALS = True

with open(args.filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

largest_index = 0
vents = []

# Parse the vents and find the size of the board
for line in lines:
    a, b = [[int(x) for x in p.split(',')] for p in line.split(' -> ')]

    local_max = max(a[0], a[1], b[0], b[1])
    if local_max > largest_index:
        largest_index = local_max

    vents.append((a, b))


# Prepare the board
grid_size = largest_index + 1
grid = []
for x in range(grid_size):
    grid.append([0] * grid_size)


def print_grid():
    for row in grid:
        for cell in row:
            value = "." if cell == 0 else cell
            print(value, end='')
        print()


# Mapping the vents
for vent in vents:
    a, b = vent

    if a[0] == b[0] and a[1] == b[1]:
        # Single point
        grid[a[1]][a[0]] += 1

    elif a[0] == b[0]:
        # Vertical
        if a[1] < b[1]:
            for y in range(a[1], b[1] + 1):
                grid[y][a[0]] += 1
        elif a[1] > b[1]:
            for y in range(a[1], b[1] - 1, -1):
                grid[y][a[0]] += 1

    elif a[1] == b[1]:
        # Horizontal
        if a[0] < b[0]:
            for x in range(a[0], b[0] + 1):
                grid[a[1]][x] += 1
        elif a[0] > b[0]:
            for x in range(a[0], b[0] - 1, -1):
                grid[a[1]][x] += 1

    elif MAP_DIAGONALS and args.diagonals:
        x_step = 1 if a[0] < b[0] else -1
        y_step = 1 if a[1] < b[1] else -1

        x_points = range(a[0], b[0] + x_step, x_step)
        y_points = range(a[1], b[1] + y_step, y_step)

        points = zip(x_points, y_points)


        for p in points:
            grid[p[1]][p[0]] += 1

    # print_grid()
    # print()


# Count the number of cells greater than 2
count = 0
for row in grid:
    for cell in row:
        if cell >= 2:
            count += 1

print(f"Cells with overlapping vents: {count}")
