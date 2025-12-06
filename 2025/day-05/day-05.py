#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser("Day 5")
parser.add_argument("infile", help="The input file")
args = parser.parse_args()

def checkIfFresh(freshRanges: list[list[int]], ingredient: int) -> bool:
    for testRange in freshRanges:
        if testRange[0] <= ingredient and ingredient <= testRange[1]:
            return True
    return False

def part1(lines: list[str]):
    print("\n\n~~ PART 1~~")
    freshRanges: list[list[int]] = []
    availableIngredients: list[int] = []
    finishedFreshRanges = False
    largestFresh = 0
    for line in lines:
        if line == "":
            finishedFreshRanges = True
            continue

        if finishedFreshRanges:
            availableIngredients.append(int(line))
        else:
            range = [int(x) for x in line.split('-')]
            freshRanges.append(range)
            if range[1] > largestFresh:
                largestFresh = range[1]

    print("Total num avail:", len(availableIngredients))

    freshRanges.sort()
    mergedRanges = [freshRanges[0].copy()]
    for nextRange in freshRanges[1:]:
        if nextRange[0] <= mergedRanges[-1][1]:
            if mergedRanges[-1][1] < nextRange[1]:
                mergedRanges[-1][1] = nextRange[1]
        else:
            mergedRanges.append(nextRange.copy())

    print("Merged ranges", len(mergedRanges))
    # for x in mergedRanges:
    #     print("> ", x)

    numFresh = 0
    for ingredient in availableIngredients:
        isFresh = checkIfFresh(mergedRanges, ingredient)
        if isFresh:
            numFresh += 1

    print("Number of fresh ingredients:", numFresh)


def part1_take2(lines: list[str]):
    print("\n\n~~ PART 1, take 2~~")
    freshRanges = []
    availableIngredients = []
    finishedFreshRanges = False
    for line in lines:
        if line == "":
            finishedFreshRanges = True
            continue

        if finishedFreshRanges:
            availableIngredients.append(int(line))
        else:
            range = [int(x) for x in line.split('-')]
            freshRanges.append(range)

    numFresh = 0
    for ingredient in availableIngredients:
        for testRange in freshRanges:
            if testRange[0] <= ingredient and ingredient <= testRange[1]:
                numFresh += 1
                break

    print("Num fresh:", numFresh)


def part2(lines: list[str]):
    print("\n\n~~ PART 2~~")
    freshRanges = []
    for line in lines:
        if line == "":
            # Finished; not needed anymore
            break
        range = [int(x) for x in line.split('-')]
        freshRanges.append(range)

    freshRanges.sort()
    mergedRanges = [freshRanges[0].copy()]
    for nextRange in freshRanges[1:]:
        if nextRange[0] <= mergedRanges[-1][1]:
            # Make sure we're actually extending the range
            if mergedRanges[-1][1] < nextRange[1]:
                mergedRanges[-1][1] = nextRange[1]
        else:
            mergedRanges.append(nextRange.copy())

    print("Merged ranges", len(mergedRanges))
    numFreshIds = 0
    for x in mergedRanges:
        numFreshIds += x[1] - x[0] + 1

    print("Num fresh ingredient IDs", numFreshIds)


with open(args.infile) as file:
    lines = [line.rstrip() for line in file.readlines()]
    part1(lines)
    part1_take2(lines)

    part2(lines)
