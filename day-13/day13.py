#! /usr/bin/env python3

import re

#filename = 'demo-13.txt'
#filename = 'demo-12c.txt'
filename = 'input-13.txt'

DEBUG = False
PART_1 = False

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

dots = []
grid = []
folds = []

dot_regex = re.compile(r'(\d+),(\d+)')
fold_regex = re.compile(r'fold along (x|y)=(\d+)')

largest_x = 0
largest_y = 0

for line in lines:
    match = dot_regex.match(line)
    if match:
        x = int(match[1])
        y = int(match[2])
        dots.append((x, y))
        if x > largest_x:
            largest_x = x
        if y > largest_y:
            largest_y = y
    else:
        match = fold_regex.match(line)
        if match:
            folds.append((match[1], int(match[2])))

for y in range(largest_y+1):
    grid.append(['.'] * (largest_x+1))

for x, y in dots:
    grid[y][x] = '#'

if DEBUG:
    print()
    for row in grid:
        print(row)
    print()

x_border = largest_x
y_border = largest_y

for axis, position in folds:
    print("folding", axis, position)

    if axis == 'x':
        for y in range(0, largest_y + 1):
            for index in range(largest_x + 1 - position):
                if grid[y][position - index] == '.':
                    grid[y][position - index] = grid[y][position + index]
        x_border = position -1
    else:
        # y-axis
        for index, line in enumerate(grid[position:]):
            for x in range(0, largest_x+1):
                if grid[position - index][x] == '.':
                    grid[position - index][x] = grid[position + index][x]
        y_border = position - 1

    if PART_1:
        break

count = 0
for y in range(y_border+1):
    for x in range(x_border+1):
        if grid[y][x] == '#':
            count += 1

print()
if PART_1:
    print(f"Part 1: {count}")
else:
    for row in grid[:y_border+1]:
        for cell in row[:x_border+1]:
            print(cell, end='')
        print()
