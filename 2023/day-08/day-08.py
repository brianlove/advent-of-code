#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser("Day 8")
parser.add_argument("infile", help="The input file")
args = parser.parse_args()

def part1(lines):
    print("\n\n~~ PART 1~~")

    instructions = lines[0]

    split = [x.split(' = ') for x in lines[2:]]
    mapping = {x[0]: tuple(x[1][1:-1].split(', ')) for x in split}

    location = 'AAA'
    step_count = 0

    while location != 'ZZZ':
        direction = instructions[step_count % len(instructions)]

        if direction == 'L':
            location = mapping[location][0]
        else:
            location = mapping[location][1]

        step_count += 1

    print("Step count:", step_count)



def part2(lines):
    print("\n\n~~ PART 2~~")

    instructions = lines[0]
    print(instructions)
    split = [x.split(' = ') for x in lines[2:]]
    mapping = {x[0]: tuple(x[1][1:-1].split(', ')) for x in split}

    endings = [] # debug

    locations = []
    for node in split:
        # print(node)
        if node[0].endswith("A"):
            locations.append(node[0])
        elif node[0].endswith("Z"):
            endings.append(node[0])
    print("Starts:", locations)
    print("Endings:", endings)

    step_count = 0
    num_ending_z = 0

    while num_ending_z != len(locations):
    # while num_ending_z == 0:
        direction = instructions[step_count % len(instructions)]
        dir_ix = 0 if direction == 'L' else 1
        num_ending_z = 0
        
        for ix, loc in enumerate(locations):
            # print(ix, loc)
            locations[ix] = mapping[loc][dir_ix]
            if locations[ix].endswith('Z'):
                num_ending_z += 1
        # print(direction, locations, num_ending_z)
        step_count += 1

        # if step_count > 10:
        #     break
        if step_count % 1000000 == 0 or num_ending_z > 3:
            print(step_count, locations, num_ending_z)

    print("Locations:", locations)
    print("Step count:", step_count)




    pass


with open(args.infile) as file:
    lines = [line.rstrip() for line in file.readlines()]
    # part1(lines)

    part2(lines)
