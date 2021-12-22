#! /usr/bin/env python3

import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='The input file')
parser.add_argument('-D', '--debug', action='store_true')
# parser.add_argument('--demo', action='store_true')

args = parser.parse_args()

PART_1 = True

with open(args.filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

instruction_regex = re.compile(r'(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)')
instructions = []
for line in lines:
    match = instruction_regex.match(line)
    instructions.append((
        match[1], # on/off
        (int(match[2]), int(match[3])), # x
        (int(match[4]), int(match[5])), # y
        (int(match[6]), int(match[7]))  # z
    ))

OFFSET = 50
MIN_BOUND = -50
MAX_BOUND = 50


# == Part 1 ==
reactor = []
for x in range(0, 102):
    reactor.append([])
    for y in range(0, 102):
        reactor[x].append([False] * 102)

cubes_on = 0

for inst in instructions:
    new_state, x_range, y_range, z_range = inst
    print(new_state, x_range, y_range, z_range)

    for x in range(max(x_range[0], MIN_BOUND), min(x_range[1], MAX_BOUND) + 1):
        for y in range(max(y_range[0], MIN_BOUND), min(y_range[1], MAX_BOUND) + 1):
            for z in range(max(z_range[0], MIN_BOUND), min(z_range[1], MAX_BOUND) + 1):
                if new_state == 'on':
                    if not reactor[x][y][z]:
                        if args.debug:
                            print(f"    Turning {(x, y, z)} on")
                        reactor[x][y][z] = True
                        cubes_on += 1
                else:
                    if reactor[x][y][z]:
                        if args.debug:
                            print(f"    Turning {(x, y, z)} off")
                        reactor[x][y][z] = False
                        cubes_on -= 1
    print()

print(f"There are {cubes_on} cubes turned on")
