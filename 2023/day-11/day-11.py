#! /usr/bin/env python3

import argparse
import itertools

parser = argparse.ArgumentParser("Day 11")
parser.add_argument("infile", help="The input file")
args = parser.parse_args()

def empties_between_indices(empty_arr, start, stop, expansion) -> int:
    count = 0
    for ix in range(min(start, stop), max(start, stop)):
        if empty_arr[ix]:
            count += 1

    ## Subtract 1 to account for the row/col that's already there
    return count * (expansion - 1)


def calculate_galaxy_distances(lines, expansion_factor):
    galaxies = []
    empty_rows = [True] * len(lines)
    empty_cols = [True] * len(lines[0])

    for r, line in enumerate(lines):
        for c, spot in enumerate(line):
            if spot == '#':
                empty_rows[r] = False
                empty_cols[c] = False
                galaxies.append((c, r))


    print("Galaxies:", len(galaxies))
    # print("Empty rows:", empty_rows.count(True), empty_rows)
    # print("Empty cols:", empty_cols.count(True), empty_cols)

    # print("Empties:", empties_between_indices(empty_cols, 0, 6))
    # print("Empty rows:", empties_between_indices(empty_rows, 4, 9))

    distances = {}

    combinations = itertools.combinations(galaxies, 2)

    for combo_ix, combo in enumerate(combinations):
        # print()
        # print("\n\nCombo:", combo)
        a, b = combo
        pair = frozenset([a, b])

        orig_distance = abs(a[0]-b[0]) + abs(a[1]-b[1])

        ## Compensate for the expansion of the universe
        # expansion_rows = empties_between_indices(empty_rows, a[1], b[1])
        # expansion_cols = empties_between_indices(empty_cols, a[0], b[0])
        expansion = (
            empties_between_indices(empty_rows, a[1], b[1], expansion_factor) +
            empties_between_indices(empty_cols, a[0], b[0], expansion_factor)
        )

        distances[pair] = orig_distance + expansion

        # if combo_ix % 100:
        #     print(f"{combo_ix}: {galaxies.index(a)+1} -> {galaxies.index(b)+1}   distance:", distances[pair])

    print()
    print("Sum:", sum(distances.values()))


def part1(lines):
    print("\n\n~~ PART 1~~")
    calculate_galaxy_distances(lines, 2)


def part2(lines):
    print("\n\n~~ PART 2~~")
    calculate_galaxy_distances(lines, 1000000)


with open(args.infile) as file:
    lines = [line.rstrip() for line in file.readlines()]
    part1(lines)

    part2(lines)
