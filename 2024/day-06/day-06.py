#! /usr/bin/env python3

import argparse
import collections

parser = argparse.ArgumentParser("Day 6")
parser.add_argument("infile", help="The input file")
args = parser.parse_args()

NORTH = ( 0, -1)
EAST  = ( 1,  0)
SOUTH = ( 0,  1)
WEST  = (-1,  0)

TURN_RIGHT = {
    NORTH: EAST,
    EAST:  SOUTH,
    SOUTH: WEST,
    WEST:  NORTH,
}

def addCoords(a, b):
    return tuple(sum(t) for t in zip(a, b))

def part1(lines):
    print("\n\n~~ PART 1~~")

    MAX_J = len(lines) - 1
    MAX_I = len(lines[0]) - 1
    obstacles = []
    start = (None, None)
    facing = NORTH

    for jx, line in enumerate(lines):
        row = list(line)
        for ix, ch in enumerate(row):
            if ch == "#":
                obstacles.append((ix, jx))
            elif ch == "^":
                start = (ix, jx)
    print("Starting position:", start)

    path = [start]
    position = start

    while True:
        test = addCoords(position, facing)
        # print("new pos?", test)
        if test in obstacles:
            facing = TURN_RIGHT[facing]
        elif test[0] < 0 or test[0] > MAX_I or test[1] < 0 or test[1] > MAX_J:
            print("Out of bounds", test)
            break
        else:
            path.append(test)
            position = test

    print("Path", path)
    uniquePositions = set(path)
    print("Unique positions in path:", len(uniquePositions))
    return obstacles, start, path


def part2(obstacles, start, path):
    print("\n\n~~ PART 2~~")

    pathWithoutFirst = path[1:]



    pass


with open(args.infile) as file:
    lines = [line.rstrip() for line in file.readlines()]
    obstacles, start, path = part1(lines)

    # part2(lines)
    part2(obstacles, start, path)
