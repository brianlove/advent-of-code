#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser("Day ??")
parser.add_argument("infile", help="The input file")
args = parser.parse_args()

def part1(lines):
    print("\n\n~~ PART 1~~")
    pass


def part2(lines):
    print("\n\n~~ PART 2~~")
    pass


with open(args.infile) as file:
    lines = [line.rstrip() for line in file.readlines()]
    part1(lines)

    # part2(lines)
