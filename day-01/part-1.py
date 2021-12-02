#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='The input file')

args = parser.parse_args()

with open(args.filename) as file:
    lines = file.readlines()
    depths = [int(line.rstrip()) for line in lines]

num_increases = 0
prev_depth = depths[0]

for depth in depths[1:]:
    if depth > prev_depth:
        print(f"{depth} +")
        num_increases += 1
    else:
        print(depth)
    prev_depth = depth

print(f"There are {num_increases} increases in the depths")
