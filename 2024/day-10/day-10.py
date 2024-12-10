#! /usr/bin/env python3

import argparse
import collections

parser = argparse.ArgumentParser("Day 10")
parser.add_argument("infile", help="The input file")
args = parser.parse_args()

def addCoords(a, b):
    return tuple(sum(t) for t in zip(a, b))

ADJACENT = [ (-1, 0), (0, -1), (1, 0), (0, 1) ]

def part1(lines):
    print("\n\n~~ PART 1~~")
    grid = []
    gridMap = collections.defaultdict(lambda: -99)
    trailheads = []
    for jx, line in enumerate(lines):
        row = [int(x) for x in line]
        grid.append(row)
        for ix, value in enumerate(row):
            cell = (ix, jx)
            gridMap[cell] = value
            if value == 0:
                trailheads.append(cell)

    print("\nMap:")
    for row in grid:
        print(row)

    print("\nTrailheads:", trailheads)

    distinctTrailEndings = collections.defaultdict(lambda: [])
    trailheadScores = collections.defaultdict(lambda: 0)

    trails = []
    for trailhead in trailheads:
        frontier = [ [trailhead] ]
        reached = {}
        reached[trailhead] = True

        while len(frontier) > 0:
            currentPath = frontier.pop(0)
            currentNode = currentPath[-1]
            print(">", currentNode, currentPath) ## DEBUG
            for direction in ADJACENT:
                candidate = addCoords(currentNode, direction)
                if gridMap[candidate] == gridMap[currentNode] + 1:
                    newPath = list(currentPath)
                    newPath.append(candidate)
                    if gridMap[candidate] == 9:
                        trails.append(newPath)
                        if candidate not in distinctTrailEndings[newPath[0]]:
                            distinctTrailEndings[newPath[0]].append(candidate)
                    else:
                        frontier.append(newPath)

    print("\nMap:")
    for row in grid:
        print(row)

    print("\nTrails:")
    for trail in trails:
        print(trail)

    print("\nDistinct trail start/end:", distinctTrailEndings)
    trailheadScores = [len(distinctTrailEndings[x]) for x in distinctTrailEndings]

    print("Total score =", sum(trailheadScores))

    print("\n\nPart 2:")
    print("len(trails):", len(trails))


## See part 1
# def part2(lines):
#     print("\n\n~~ PART 2~~")
#     pass


with open(args.infile) as file:
    lines = [line.rstrip() for line in file.readlines()]
    part1(lines)

    # part2(lines)
