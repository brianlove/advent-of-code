#! /usr/bin/env python3

import argparse
import functools

parser = argparse.ArgumentParser("Day 3")
parser.add_argument("infile", help="The input file")
args = parser.parse_args()


def part1(lines):
    print("\n\n~~ PART 1~~")
    part_numbers = []

    grid = [[c for c in line.rstrip()] for line in lines]
    print(grid)

    ROWS = len(grid)
    COLS = len(grid[0])

    for r in range(ROWS):
        num = 0
        is_part = False
        for c in range(COLS):
            print(grid[r][c])

            if grid[r][c].isdigit():
                num = 10 * num + int(grid[r][c])
                for rr in [-1, 0, 1]:
                    for cc in [-1, 0, 1]:
                        if 0 <= r + rr < ROWS and 0 <= c + cc < COLS:
                            if grid[r + rr][c + cc] != '.' and not grid[r + rr][c + cc].isdigit():
                                is_part = True
                                print("  We have a part: ", num)

            if not grid[r][c].isdigit() or c == COLS -1:
                if is_part:
                    print("  We found a part:", num)
                    part_numbers.append(num)
                    num = 0
                    is_part = False
                elif num > 0:
                    print("    not a part:", num)
                    num = 0
                    is_part = False

    sum = functools.reduce(lambda x,y: x + y, part_numbers, 0)
    print("Sum:", sum)


def part2(lines):
    print("\n\n~~ PART 2~~")
    part_numbers = []
    gear_candidates = {}

    grid = [[c for c in line.rstrip()] for line in lines]
    print(grid)

    ROWS = len(grid)
    COLS = len(grid[0])

    for r in range(ROWS):
        num = 0
        is_part = False
        pending_gears = []
        for c in range(COLS):
            print(grid[r][c])

            if grid[r][c].isdigit():
                num = 10 * num + int(grid[r][c])
                for rr in [-1, 0, 1]:
                    for cc in [-1, 0, 1]:
                        if 0 <= r + rr < ROWS and 0 <= c + cc < COLS:
                            ch = grid[r + rr][c + cc]
                            space_id = (r+rr, c+cc)
                            if ch != '.' and not ch.isdigit():
                                is_part = True
                                print("  We have a part: ", num, ":", ch, space_id)
                                if ch == "*":
                                    print("   We have a GEAR")
                                    space_id = (r+rr, c+cc)
                                    pending_gears.append(space_id)

            if not grid[r][c].isdigit() or c == COLS -1:
                if is_part:
                    print("  We found a part:", num)
                    part_numbers.append(num)
                    for gear_id in pending_gears:
                        if gear_id in gear_candidates:
                            gear_candidates[gear_id].append(num)
                        else:
                            gear_candidates[gear_id] = [num]
                        print("gear status:", gear_id, gear_candidates[gear_id])

                    num = 0
                    is_part = False
                    pending_gears = []
                elif num > 0:
                    print("    not a part:", num)
                    num = 0
                    is_part = False
                    pending_gears = []

    sum = functools.reduce(lambda x,y: x + y, part_numbers, 0)
    print("Sum:", sum)

    print("Gear candidates:", gear_candidates)

    gear_ratio_sum = 0
    for candidate in gear_candidates:
        part_set = list(set(gear_candidates[candidate]))
        if ( len(part_set) == 2 ):
            print(candidate, part_set)
            gear_ratio = part_set[0] * part_set[1]
            print("  ratio:", gear_ratio)
            gear_ratio_sum += gear_ratio
    
    print("Gear ratio sum:", gear_ratio_sum)



with open(args.infile) as file:
    lines = file.readlines()
    # part1(lines)

    part2(lines)
