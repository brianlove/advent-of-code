#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser("Day 2")
parser.add_argument("infile", help="The input file")
args = parser.parse_args()

def hasRepeatingDigits(id: int):
    s = str(id)
    a = s[:len(s) // 2]
    b = s[len(s) // 2:]
    return a == b

def part1(lines: list[str]):
    print("\n\n~~ PART 1~~")
    invalidIdSum = 0
    for line in lines:
        first, last = [int(x) for x in line.split('-')]
        for id in range(first, last + 1):
            if hasRepeatingDigits(id):
                # print("invalid id:", id)
                invalidIdSum += id
    print("Total of invalid IDs:", invalidIdSum)


def divideId(id: int):
    s = str(id)
    for l in range(2, len(s)+1):
        candidate = s[:len(s)//l]
        if s == candidate * l:
            return True
    return False

def part2(lines: list[str]):
    print("\n\n~~ PART 2~~")
    invalidIdSum = 0
    for line in lines:
        first, last = [int(x) for x in line.split('-')]
        for id in range(first, last + 1):
            if divideId(id):
                invalidIdSum += id
    print("Total of invalid IDs:", invalidIdSum)


with open(args.infile) as file:
    lines = [line.rstrip() for line in file.readlines()]
    idRanges = lines[0].split(',')
    part1(idRanges)

    part2(idRanges)
