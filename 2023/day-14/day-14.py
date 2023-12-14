#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser("Day 14")
parser.add_argument("infile", help="The input file")
args = parser.parse_args()

def part1(lines):
    print("\n\n~~ PART 1~~")

    grid = [[c for c in line] for line in lines]

    NUM_COLUMNS = len(lines[0])
    MAX_LOAD = len(lines)
    print(MAX_LOAD)

    column_loads = [0] * NUM_COLUMNS

    for cix in range(NUM_COLUMNS):
        next_load = MAX_LOAD
        for rix in range(len(lines)):
            if lines[rix][cix] == 'O':
                column_loads[cix] += next_load
                next_load -= 1
            elif lines[rix][cix] == '#':
                next_load = MAX_LOAD - rix - 1

    print("Total load:", sum(column_loads))


def part2(lines):
    print("\n\n~~ PART 2~~")
    pass


with open(args.infile) as file:
    lines = [line.rstrip() for line in file.readlines()]
    part1(lines)

    # part2(lines)
