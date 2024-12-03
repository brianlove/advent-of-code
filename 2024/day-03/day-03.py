#! /usr/bin/env python3

import argparse
import re

parser = argparse.ArgumentParser("Day 3")
parser.add_argument("infile", help="The input file")
args = parser.parse_args()

def part1(lines):
    print("\n\n~~ PART 1~~")

    total = 0
    for line in lines:
        matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)', line)
        print(matches)

        for match in matches:
            raw_nums = re.findall(r'\d{1,3}', match)
            nums = [int(x) for x in raw_nums]
            product = nums[0] * nums[1]
            print(match, "--> ", nums, "-->", product)
            total += product

    print("Part 1:", total)


def part2(lines):
    print("\n\n~~ PART 2~~")

    is_multiplication_enabled = True
    total = 0
    for line in lines:
        matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', line)
        print(matches)

        for match in matches:
            if match == "do()":
                is_multiplication_enabled = True
            elif match == "don't()":
                is_multiplication_enabled = False
            elif is_multiplication_enabled:
                raw_nums = re.findall(r'\d{1,3}', match)
                nums = [int(x) for x in raw_nums]
                product = nums[0] * nums[1]
                print(match, "--> ", nums, "-->", product)
                total += product

    print("Part 1:", total)


with open(args.infile) as file:
    lines = [line.rstrip() for line in file.readlines()]
    part1(lines)

    part2(lines)
