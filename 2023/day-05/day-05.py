#! /usr/bin/env python3

import argparse
import re

parser = argparse.ArgumentParser("Day 5")
parser.add_argument("infile", help="The input file")
args = parser.parse_args()


STEPS = [
    "seed",
    "soil",
    "fertilizer",
    "water",
    "light",
    "temperature",
    "humidity",
    "location",
]


def part1_wrong(lines):
    print("\n\n~~ PART 1~~")

    mapping = {
        "seed": {},
        "soil": {},
        "fertilizer": {},
        "water": {},
        "light": {},
        "temperature": {},
        "humidity": {},
        "location": {},
    }

    seeds = [int(x) for x in lines[0].split(": ")[1].split(" ")]
    print(seeds)

    current_line = 0
    # current_source = "seed"
    # current_dest = "soil"

    for line in lines[2:]:
        section_start_match = re.findall(r'(\w+)-to-(\w+) map:', line)
        if section_start_match:
            source_type = section_start_match[0][0]
            dest_type = section_start_match[0][1]
            # print("line: ", line)
            print(source_type, dest_type)
            current_line = 0
            continue

        if line == "":
            continue
            # break

        print(f"Line {current_line}")
        current_line += 1

        ## Process the mappings
        # print("> ", line)
        dest_start, source_start, range_len = [int(x) for x in line.split()]
        for i in range(range_len):
            mapping[source_type][source_start+i] = dest_start+i
        # print(mapping[source_type])

    print()
    print()

    seed_location_map = {}

    for seed in seeds:
        value = seed
        for step in STEPS:
            # Map the value if applicable
            if value in mapping[step]:
                value = mapping[step][value]
            # Otherwise, it's one-to-one so just leave as is
        seed_location_map[seed] = value
        print(f"Seed {seed} --> location {value}")

    lowest_location = min(seed_location_map.values())
    print("Lowest location:", lowest_location)

## ============





def part1b(lines):
    print("\n\n~~ PART 1~~")

    mapping = {
        "seed": {},
        "soil": {},
        "fertilizer": {},
        "water": {},
        "light": {},
        "temperature": {},
        "humidity": {},
        # "location": {},
    }

    seeds = [int(x) for x in lines[0].split(": ")[1].split(" ")]

    for line in lines[2:]:
        section_start_match = re.findall(r'(\w+)-to-(\w+) map:', line)
        if section_start_match:
            source_type = section_start_match[0][0]
            dest_type = section_start_match[0][1]
            continue

        if line == "":
            continue
            # break

        ## Process the mappings
        dest_start, source_start, range_len = [int(x) for x in line.split()]
        mapping[source_type][source_start] = {
            "dest_start": dest_start,
            "range": range_len,
        }

    # for step in mapping:
    #     print()
    #     print(step)
    #     print(mapping[step])
    # print()

    lowest_location_map = {}

    for seed in seeds:
        print()
        print(f"Checking seed {seed}")
        value = seed

        for step in mapping:
            print()
            print(f"Step: {step}")
            next_step = STEPS[STEPS.index(step) + 1]
            # print(mapping[step])
            for start in mapping[step]:
                range_end = start + mapping[step][start]["range"]
                # print(f"  Checking for '{value}' from {start} to {range_end}")
                if start <= value < range_end:
                    # print("  ", step, start, mapping[step][start])
                    offset = value - start
                    newValue = mapping[step][start]["dest_start"] + offset
                    # print(f"    offset {offset}")
                    value = newValue
                    break

            ## If we get through all mappings for this step and didn't
            ## find one that matches, we're fine, because the mapping
            ## at that point is one-to-one
            print(f"   {next_step} {value}")
            lowest_location_map[seed] = value

    lowest_location = min(lowest_location_map.values())
    print()
    print()
    print("Lowest location:", lowest_location)





def part2(lines):
    print("\n\n~~ PART 2~~")
    pass


with open(args.infile) as file:
    lines = [line.rstrip() for line in file.readlines()]
    part1b(lines)

    # part2(lines)
