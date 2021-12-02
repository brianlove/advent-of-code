#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='The input file')

args = parser.parse_args()

with open(args.filename) as file:
    lines = file.readlines()
    depths = [int(line.rstrip()) for line in lines]

window_size = 3

slices = [depths[i:i+window_size] for i in range(len(depths)-window_size+1)]
sums = [sum(slice) for slice in slices]

num_increases = 0
prev_sum = sums[0]

for sum in sums[1:]:
    if sum > prev_sum:
        print(f"{sum} +")
        num_increases += 1
    else:
        print(sum)
    prev_sum = sum

print(f"There are {num_increases} increases in the sums of the depths")
