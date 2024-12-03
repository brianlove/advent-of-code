#! /usr/bin/env python3

import argparse
import collections

parser = argparse.ArgumentParser("Day 1")
parser.add_argument("infile", help="The input file")
args = parser.parse_args()

def part1(lines):
    print("\n\n~~ PART 1~~")

    left = []
    right = []
    for line in lines:
        split = line.split()
        left.append(int(split[0]))
        right.append(int(split[1]))
    left.sort()
    right.sort()

    total_dist = 0
    for i in range(len(left)):
        total_dist += abs(left[i] - right[i])

    print("Part 1: ", total_dist)


def part2(lines):
    print("\n\n~~ PART 2~~")

    right_counts = collections.defaultdict(lambda: 0)

    left = []
    right = []
    for line in lines:
        split = line.split()
        left.append(int(split[0]))
        r = int(split[1])
        right.append(r)
        right_counts[r] += 1
    left.sort()
    right.sort()

    similarity_score = 0
    for item in left:
        similarity_score += item * right_counts[item]

    print("Part 2, similarity score:", similarity_score)
    pass


with open(args.infile) as file:
    lines = [line.rstrip() for line in file.readlines()]
    part1(lines)

    part2(lines)
