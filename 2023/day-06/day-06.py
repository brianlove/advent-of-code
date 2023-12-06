#! /usr/bin/env python3

import argparse
import functools
import re

parser = argparse.ArgumentParser("Day 6")
parser.add_argument("infile", help="The input file")
args = parser.parse_args()

def part1(lines):
    print("\n\n~~ PART 1~~")

    times = [int(x) for x in re.split(r'\s+', lines[0])[1:]]
    record_dists = [int(x) for x in re.split(r'\s+', lines[1])[1:]]

    print("Times:", times)
    print("Dist:", record_dists)

    num_won = [0] * len(times)

    for race in range(len(times)):
        for time_pressed in range(times[race]):
            speed = time_pressed
            duration = times[race] - speed
            distance = speed * duration
            # print(f"  {speed} * {duration} = {distance}  (record is {record_dists[race]})")
            if distance > record_dists[race]:
                # print("    > WIN!")
                num_won[race] += 1

    print(num_won)
    print("Total:", functools.reduce(lambda x,y: x * y, num_won, 1))


def part2(lines):
    print("\n\n~~ PART 2~~")

    time = int(''.join(re.split(r'\s+', lines[0])[1:]))
    record_dist = int(''.join(re.split(r'\s+', lines[1])[1:]))

    print("Times:", time)
    print("Dist:", record_dist)

    # num_won = [0] * len(times)
    num_won = 0

    for time_pressed in range(time):
        speed = time_pressed
        duration = time - speed
        distance = speed * duration
        # print(f"  {speed} * {duration} = {distance}  (record is {record_dists[race]})")
        if distance > record_dist:
            # print("    > WIN!")
            num_won += 1

    print("Num won:", num_won)
    # print("Total:", functools.reduce(lambda x,y: x * y, num_won, 1))


with open(args.infile) as file:
    lines = [line.rstrip() for line in file.readlines()]
    # part1(lines)

    part2(lines)


