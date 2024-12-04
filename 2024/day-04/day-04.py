#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser("Day 4")
parser.add_argument("infile", help="The input file")
args = parser.parse_args()

DIRECTIONS = [
    (-1, -1),
    ( 0, -1),
    ( 1, -1),
    (-1,  0),
    # skip origin
    ( 1,  0),
    (-1,  1),
    ( 0,  1),
    ( 1,  1),
]

TESTS = [
    # ("X", 0),
    ("M", 1),
    ("A", 2),
    ("S", 3),
]

def testDirection(grid, x, y, direction, MAX_X, MAX_Y):
    for letter, dist in TESTS:
        newX = x + direction[0] * dist
        newY = y + direction[1] * dist
        if newX < 0 or newX > MAX_X or newY < 0 or newY > MAX_Y:
            return False
        if grid[newY][newX] != letter:
            return False
    return True

def part1(lines):
    print("\n\n~~ PART 1~~")
    grid = [list(x) for x in lines]
    MAX_X = len(grid[0]) - 1
    MAX_Y = len(grid) - 1
    count = 0

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != "X":
                continue
            for direction in DIRECTIONS:
                if testDirection(grid, x, y, direction, MAX_X, MAX_Y):
                    count += 1

    print("Part 1: ", count)



def part2(lines):
    print("\n\n~~ PART 2~~")
    grid = [list(x) for x in lines]
    MAX_X = len(grid[0]) - 2
    MAX_Y = len(grid) - 2
    count = 0

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != "A":
                continue
            if y < 1 or x < 1 or y > MAX_Y or x > MAX_X:
                continue
            nw_se = set([grid[y-1][x-1], grid[y+1][x+1]])
            ne_sw = set([grid[y-1][x+1], grid[y+1][x-1]])

            if (
                ("M" in nw_se and "S" in nw_se) and 
                ("M" in ne_sw and "S" in ne_sw)
            ):
                count += 1

    print("Part 2: ", count)


with open(args.infile) as file:
    lines = [line.rstrip() for line in file.readlines()]
    part1(lines)

    part2(lines)
