#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser("Day 1")
parser.add_argument("infile", help="The input file")
args = parser.parse_args()

def part1(lines):
    print("\n\n~~ PART 1~~")
    countAtZero = 0
    currentPosition = 50

    for line in lines:
        dir = -1 if "L" in line else 1
        steps = int(line[1:])
        currentPosition = (currentPosition + dir * steps) % 100
        if currentPosition == 0:
            countAtZero += 1
    print("lock at position:", currentPosition)
    print(f"Lock was at zero {countAtZero} times")


def part2(lines):
    print("\n\n~~ PART 2~~")
    countAtZero = 0
    currentPosition = 50

    for line in lines:
        dir = -1 if "L" in line else 1
        steps = int(line[1:])

        # Account for rotations that turn the dial all the way, which are
        # guaranteed to pass by zero one or more times
        countAtZero += steps // 100

        movement = (dir * (steps % 100))
        newPosition = currentPosition + movement
        if currentPosition != 0 and (newPosition >= 100 or newPosition <= 0):
            countAtZero += 1
        # print(dir, movement, "-->", newPosition, newPosition % 100, "::", countAtZero)
        currentPosition = newPosition % 100
    print("lock at position:", currentPosition)
    print(f"Lock was at zero {countAtZero} times")


with open(args.infile) as file:
    lines = [line.rstrip() for line in file.readlines()]
    part1(lines)

    part2(lines)
