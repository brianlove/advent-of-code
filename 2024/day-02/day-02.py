#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser("Day 2")
parser.add_argument("infile", help="The input file")
args = parser.parse_args()

def part1(lines):
    print("\n\n~~ PART 1~~")

    num_safe = 0

    for report in lines:
        levels = [int(x) for x in report.split()]
        print(levels)

        increasing = False
        decreasing = False
        safe_change = True

        prev = levels[0]
        for entry in levels[1:]:
            if entry > prev:
                increasing = True
            elif entry < prev:
                decreasing = True
            diff = abs(entry - prev)
            if diff < 1 or 3 < diff:
                safe_change = False
            prev = entry
        
        if not safe_change:
            # print("Unsafe due to large change:", levels)
            pass
        elif (increasing and not decreasing) or (decreasing and not increasing):
            # print("SAFE")
            num_safe += 1
        else:
            # print("Unsafe")
            pass

    print("Part 1: num safe:", num_safe)


## ========
## Part 2
## ========

def increaseOrDecrease(arr):
    isIncreasing = True
    isDecreasing = True
    prev = arr[0]
    for entry in arr[1:]:
        if prev <= entry:
            isDecreasing = False
        if prev >= entry:
            isIncreasing = False
        prev = entry
    return isIncreasing ^ isDecreasing

def diffWithinBounds(arr):
    prev = arr[0]
    for entry in arr[1:]:
        d = abs(entry - prev)
        if d < 1 or d > 3:
            return False
        prev = entry
    return True

def part2(lines):
    print("\n\n~~ PART 2~~")

    num_safe = 0

    for report in lines:
        levels = [int(x) for x in report.split()]
        safeIncreaseOrDecrease = increaseOrDecrease(levels)
        safeDifference = diffWithinBounds(levels)

        if safeIncreaseOrDecrease and safeDifference:
            num_safe += 1
        else:
            for ix in range(len(levels)):
                new_levels = list(levels)
                del new_levels[ix]
                safeIncreaseOrDecrease = increaseOrDecrease(new_levels)
                safeDifference = diffWithinBounds(new_levels)
                if safeIncreaseOrDecrease and safeDifference:
                    num_safe += 1
                    break

    print("Part 2: num safe:", num_safe)


with open(args.infile) as file:
    lines = [line.rstrip() for line in file.readlines()]
    part1(lines)

    part2(lines)
