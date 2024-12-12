#! /usr/bin/env python3

import argparse
import collections

parser = argparse.ArgumentParser("Day 12")
parser.add_argument("infile", help="The input file")
args = parser.parse_args()

NORTH = ( 0, -1)
EAST  = ( 1,  0)
SOUTH = ( 0,  1)
WEST  = (-1,  0)

DIRECTIONS = [ NORTH, SOUTH, EAST, WEST ]

def addCoords(a, b):
    return tuple(sum(t) for t in zip(a, b))

def inBounds(coords, MAX_X, MAX_Y):
    x, y = coords
    return x >= 0 and y >= 0 and x < MAX_X and y < MAX_Y

def part1(lines):
    print("\n\n~~ PART 1~~")
    MAX_Y = len(lines)
    MAX_X = len(lines[0])

    grid = collections.defaultdict(lambda: {
        "crop": None,
        "examined": False,
    })
    for jx, line in enumerate(lines):
        for ix, crop in enumerate(line):
            cell = (ix, jx)
            grid[cell]["crop"] = crop

    regions = []
    for cell in grid:
        if grid[cell]["examined"]:
            continue
        desiredCrop = grid[cell]["crop"]
        newRegion = {
            "cells": set([cell]),
            "crop": desiredCrop,
            "perimeter": 0,
        }
        grid[cell]["examined"] = True
        frontier = [cell]
        
        while len(frontier) > 0:
            currentCell = frontier.pop(0)
            for dir in DIRECTIONS:
                candidate = addCoords(currentCell, dir)
                if not inBounds(candidate, MAX_X, MAX_Y):
                    newRegion["perimeter"] += 1
                    continue
                if grid[candidate]["examined"] and grid[candidate]["crop"] == desiredCrop:
                    continue
                if grid[candidate]["crop"] != desiredCrop:
                    newRegion["perimeter"] += 1
                else:
                    newRegion["cells"].add(candidate)
                    grid[candidate]["examined"] = True
                    frontier.append(candidate)
        print("Done looking at region", newRegion)
        regions.append(newRegion)

    totalCost = sum(len(region["cells"]) * region["perimeter"] for region in regions)
    print("Total cost:", totalCost)


def part2(lines):
    print("\n\n~~ PART 2~~")
    pass


with open(args.infile) as file:
    lines = [line.rstrip() for line in file.readlines()]
    part1(lines)

    # part2(lines)
