#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='The input file')
parser.add_argument('-d', '--double-back', action='store_true', help='Can we double back?')

args = parser.parse_args()

#filename = 'demo-12.txt'
#filename = 'demo-12c.txt'
#filename = 'input-12.txt'

DEBUG = False

with open(args.filename) as file:
    lines = file.readlines()
    lines = [line.rstrip().split('-') for line in lines]

doors = {}
paths = []

for start, end in lines:
    if start in doors:
        doors[start].append(end)
    else:
        doors[start] = [end]
    if end in doors:
        doors[end].append(start)
    else:
        doors[end] = [start]


for cave in doors:
    doors[cave].sort()
    if DEBUG:
        print(f"{cave} -> {doors[cave]}")
print()
print()


# return: a full path to the end, if possible, otherwise false??
def check_path(room, so_far, indent, has_doubled_back):
    this_path = so_far[:]
    this_path.append(room)
    if DEBUG:
        print(f"{'  '*indent}Checking: '{room}', This path: {this_path}")

    solutions = []
    for dest in doors[room]:
        repeat_small_cave = dest[0].islower() and dest in so_far


        if dest == 'end':
            # Found the path out; record the solution
            solution = this_path[:]
            solution.append(dest)
            solutions.append(solution)
            if DEBUG:
                print(f"{'  '*indent}- found solution '{dest}', Path: {solution}")
        elif repeat_small_cave and (not args.double_back or has_doubled_back or dest == 'start'):
            # Part 1:
            #   repeat small cave
            # Part 2:
            #   repeat small cave, and we have either already doubled back or it is 'start'

            # We've already met the max number of times that we can visit this cave
            if DEBUG:
                print(f"{'  '*indent}- '{dest}' = dup")
            continue
        else:
            # Keep searching
            if DEBUG:
                print(f"{'  '*indent}- '{dest}' = new cave")

            double_back_eligible = repeat_small_cave and dest != 'start'
            will_double_back = has_doubled_back or (double_back_eligible and args.double_back)

            next_solutions = check_path(dest, this_path, indent+1, will_double_back)
            if len(next_solutions):
                solutions += next_solutions

    if DEBUG:
        print(f"{'  '*indent} Room '{room}' :: {solutions}")
    return solutions

result = check_path('start', [], 0, False)

print()
print(f"Part 1 result: {len(result)} paths found")
#for entry in result:
#    print(entry)
