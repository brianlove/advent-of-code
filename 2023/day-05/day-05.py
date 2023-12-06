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

def build_mapping(lines) -> dict:
    mapping = {
        "seed": {},
        "soil": {},
        "fertilizer": {},
        "water": {},
        "light": {},
        "temperature": {},
        "humidity": {},
    }

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

    return mapping


def seed_to_location(seed: int, mapping: dict) -> int:
    value = seed
    for step in mapping:
        for start in mapping[step]:
            range_end = start + mapping[step][start]["range"]
            # print(f"  Checking for '{value}' from {start} to {range_end}")
            if start <= value < range_end:
                offset = value - start
                value = mapping[step][start]["dest_start"] + offset
                break
        # print(f"   {STEPS[STEPS.index(step)+1]} {value}")

    # print(f"Seed {seed} --> location {value}")
    return value



def part1b(lines):
    print("\n\n~~ PART 1~~")

    seeds = [int(x) for x in lines[0].split(": ")[1].split(" ")]

    mapping = build_mapping(lines)
    lowest_location_map = {}

    for seed in seeds:
        lowest_location_map[seed] = seed_to_location(seed, mapping)

    lowest_location = min(lowest_location_map.values())
    print()
    print()
    print("Lowest location:", lowest_location)





def part2_initial(lines):
    print("\n\n~~ PART 2~~")

    seeds_input = [int(x) for x in lines[0].split(": ")[1].split(" ")]
    seed_ranges = list(zip(seeds_input[::2], seeds_input[1::2]))
    print(seed_ranges)

    mapping = build_mapping(lines)
    lowest_location = 10**12

    for seed_range in seed_ranges:
        start_seed, range_len = seed_range
        print("Range:", start_seed, range_len)

        for i in range(range_len):
            location = seed_to_location(start_seed+i, mapping)
            if location < lowest_location:
                lowest_location = location

    print("Lowest location:", lowest_location)



def part2_new(lines):
    print("\n\n~~ PART 2~~")


    pass



with open(args.infile) as file:
    lines = [line.rstrip() for line in file.readlines()]
    # part1b(lines)

    # part2_initial(lines)
    part2_new(lines)
