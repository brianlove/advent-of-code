#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='The input file')

args = parser.parse_args()

MAP_DIAGONALS = True

with open(args.filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

octopodes = [[{ 'energy': int(x), 'flashed': False } for x in line] for line in lines]

NUM_ROUNDS = 100

num_rows = len(octopodes)
num_cols = len(octopodes[0])
num_octopodes = num_rows * num_cols

diffs = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]

def try_flash(x, y):
    print(f"  try_flash({x}, {y}")
    if x >= 0 and x < num_cols and y >= 0 and y < num_rows:
        if octopodes[y][x]['energy'] > 9:
            octopodes[y][x]['flashed'] = True
            for diff in diffs:
                try_flash(x + diff[0], y + diff[1])
    else:
        return


def increment_neighbors(x0, y0):
    incremented = False
    for diff in diffs:
        x = x0 + diff[0]
        y = y0 + diff[1]

        if x < 0 or x >= num_cols or y < 0 or y >= num_rows:
            continue
        else:
            octopodes[y][x]['energy'] += 1
            incremented = True
    return incremented


flashes_this_round = 0
total_flashes = 0
round = 0

## Part 1 loop vs Part 2 loop:
# for round in range(1, NUM_ROUNDS + 1):
while flashes_this_round != num_octopodes and round < 600:
    round += 1
    print()
    print(f"Round {round}")

    flashes_this_round = 0

    # Increase energy levels
    for row in octopodes:
        for octopus in row:
            octopus['energy'] += 1


    # Flash octopodes
    incremented_neighbor = True
    while incremented_neighbor:
        incremented_neighbor = False
        for y, row in enumerate(octopodes):
            for x, octopus in enumerate(row):
                if not octopus['flashed'] and octopus['energy'] > 9:
                    octopus['flashed'] = True
                    flashes_this_round += 1
                    total_flashes += 1
                    if increment_neighbors(x, y):
                        incremented_neighbor = True


    if flashes_this_round == num_octopodes:
        print("  == Part 2 ==")
        print(f"  Round {round}: All {num_octopodes} flashed this round!")

    # Reset energy to zero if it flashed
    for row in octopodes:
        for octopus in row:
            if octopus['flashed']:
                octopus['flashed'] = False
                octopus['energy'] = 0

    for row in octopodes:
        print([x['energy'] for x in row])


print()
print(f"After {round} rounds, there have been {total_flashes} flashes")
