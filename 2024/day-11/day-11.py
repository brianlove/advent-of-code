#! /usr/bin/env python3

import argparse
import collections
import math

parser = argparse.ArgumentParser("Day 11")
parser.add_argument("infile", help="The input file")
args = parser.parse_args()


def splitNumber(number):
    magnitude = math.floor(math.log(number, 10))
    numDigits = magnitude + 1
    leftBase = 10**(numDigits // 2)
    left = number // leftBase
    right = number - left * leftBase
    return [left, right]

def transformStones(stones):
    newStones = []
    for stone in stones:
        # strStone = str(stone)
        # lenStone = len(strStone)
        if stone == 0:
            # print("  > 1")
            newStones.append(1)
        # elif len(strStone) % 2 == 0:
            # print("  >- ", strStone, strStone[:lenStone // 2])
            # newStones.append(int(strStone[:lenStone // 2]))
            # newStones.append(int(strStone[lenStone // 2:]))
        elif (math.floor(math.log(stone, 10)) + 1) % 2 == 0:
            left, right = splitNumber(stone)
            newStones.append(left)
            newStones.append(right)
        else:
            # print("  > multiply")
            newStones.append(stone * 2024)
    return newStones


def part1(lines):
    print("\n\n~~ PART 1~~")

    numbers = [int(x) for x in lines[0].split()]
    print(numbers)
    stones = list(numbers)
    print("[init]", stones)

    for blink in range(25):
        stones = transformStones(stones)
        # print(f"[{blink+1}] ({len(stones)} stones)", stones)
        # print(f"[{blink+1}]", "numStones =", len(stones))

    print("Num stones:", len(stones))


def part2(lines):
    print("\n\n~~ PART 2~~")
    numbers = [int(x) for x in lines[0].split()]
    numbers.sort()
    print(numbers)
    stones = list(numbers)

    stoneCounts = collections.defaultdict(lambda: 0)
    for stone in stones:
        stoneCounts[stone] += 1

    print("stone counts:", stoneCounts)

    for blink in range(75):
        newCounts = collections.defaultdict(lambda: 0)
        for stone in stoneCounts:
            number = stoneCounts[stone]
            if stone == 0:
                newCounts[1] += number
            elif (math.floor(math.log(stone, 10)) + 1) % 2 == 0:
                left, right = splitNumber(stone)
                newCounts[left] += number
                newCounts[right] += number
            else:
                newCounts[stone * 2024] += number
        stoneCounts = newCounts
        # print(f"\n[{blink+1}]", stoneCounts)

    sum = 0
    for stone in stoneCounts:
        sum += stoneCounts[stone]
    print("num stones:", sum)


with open(args.infile) as file:
    lines = [line.rstrip() for line in file.readlines()]
    part1(lines)

    part2(lines)
