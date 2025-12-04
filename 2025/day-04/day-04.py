#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser("Day 4")
parser.add_argument("infile", help="The input file")
args = parser.parse_args()

DIRECTIONS = [
    (0, 0)
]

def part1(lines: list[str]):
    print("\n\n~~ PART 1~~")
    grid = [[c for c in line.rstrip()] for line in lines]
    ROWS = len(grid)
    COLS = len(grid[0])

    countGrid = [[0 for c in range(COLS)] for r in range(ROWS)]
    cellsFewerThanFour = 0

    for r in range(ROWS):
        for c in range(COLS):
            # Skip cells that don't contain a roll of paper
            if grid[r][c] == '.':
                continue

            countAdjacent = 0
            for rr in [-1, 0, 1]:
                for cc in [-1, 0, 1]:
                    if rr == 0 and cc == 0:
                        continue
                    if 0 <= r + rr < ROWS and 0 <= c + cc < COLS:
                        if grid[r + rr][c + cc] == '@':
                            countAdjacent += 1
            countGrid[r][c] = countAdjacent
            if countAdjacent < 4:
                cellsFewerThanFour += 1

    # for row in countGrid:
    #     print(row)
    print("Cells fewer than four adjacent rolls:", cellsFewerThanFour)


def countAdjacentRolls(grid: list[list[chr]], r: int, c: int) -> int:
    count = 0
    ROWS = len(grid)
    COLS = len(grid[0])
    for rr in [-1, 0, 1]:
        for cc in [-1, 0, 1]:
            if rr == 0 and cc == 0:
                continue
            if 0 <= r + rr < ROWS and 0 <= c + cc < COLS:
                if grid[r + rr][c + cc] == '@':
                    count += 1
    return count

def part2(lines: list[str]):
    print("\n\n~~ PART 2~~")
    grid = [[c for c in line.rstrip()] for line in lines]
    ROWS = len(grid)
    COLS = len(grid[0])
    # for row in grid:
    #     print(row)

    totalRollsRemoved = 0
    numRemoved = 9999999999999999
    while numRemoved > 0:
        rollsToRemove = []
        for r in range(ROWS):
            for c in range(COLS):
                # Skip cells that don't contain a roll of paper
                if grid[r][c] == '.':
                    continue

                countAdjacent = countAdjacentRolls(grid, r, c)
                if countAdjacent < 4:
                    rollsToRemove.append((r, c))
        numRemoved = len(rollsToRemove)
        totalRollsRemoved += numRemoved
        for r, c in rollsToRemove:
            grid[r][c] = '.'
        # for row in grid:
        #     print(row)
    print("Total rolls removed:", totalRollsRemoved)


with open(args.infile) as file:
    lines = [line.rstrip() for line in file.readlines()]
    part1(lines)

    part2(lines)
