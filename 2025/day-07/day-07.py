#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser("Day 7")
parser.add_argument("infile", help="The input file")
args = parser.parse_args()

START    = 'S'
SPLITTER = '^'

def part1(lines: list[str]):
    print("\n\n~~ PART 1~~")
    grid = []
    for line in lines:
        grid.append(line)

    maxColumn = len(grid[0]) - 1
    beams = {grid[0].index(START)}
    numSplits = 0
    for rix, row in enumerate(grid):
        if rix == 0:
            continue
        newBeams = set()
        # print(row)
        for beam in beams:
            if row[beam] == SPLITTER:
                if beam > 0:
                    newBeams.add(beam - 1)
                if beam < maxColumn:
                    newBeams.add(beam + 1)
                numSplits += 1
            else:
                newBeams.add(beam)
        beams = newBeams
    finalBeams = list(beams)
    finalBeams.sort()
    # print("Beams:", finalBeams)
    print("Num splits:", numSplits)



def part2(lines: list[str]):
    print("\n\n~~ PART 2~~")
    grid = []
    for line in lines:
        grid.append(line)

    maxColumn = len(grid[0]) - 1
    beams = [0] * len(grid[0])
    beams[grid[0].index(START)] = 1
    for rix, row in enumerate(grid):
        # print(rix, row)
        if rix == 0:
            continue

        newBeams = beams.copy()
        for cix, col in enumerate(row):
            if col == SPLITTER:
                if cix > 0:
                    newBeams[cix - 1] += beams[cix]
                if cix < maxColumn:
                    newBeams[cix + 1] += beams[cix]
                newBeams[cix] = 0
        beams = newBeams
        # print(rix, beams)
    print("Num timelines", sum(beams))


with open(args.infile) as file:
    lines = [line.rstrip() for line in file.readlines()]
    part1(lines)

    part2(lines)
