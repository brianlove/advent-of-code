#! /usr/bin/env python3

import argparse
from functools import reduce
from operator import add

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='The input file')

args = parser.parse_args()

def bits_to_dec(bits):
    return int(''.join([str(x) for x in bits]), 2)

with open(args.filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

bit_array = [[int(x) for x in list(line)] for line in lines]
num_entries = len(bit_array)

data_width = len(bit_array[0])

# Count how many bits are in each position
initial = [0] * data_width
sums = reduce((lambda acc, val: list(map(add, acc, val))), bit_array, initial)

# Gamma is the most common bits in each position
gamma_bits = list(map((lambda x: round(x / num_entries)), sums))
gamma = bits_to_dec(gamma_bits)

# Epsilon is the least common bit, therefore is the inverse of gamma
epsilon_bits = [0 if x == 1 else 1 for x in gamma_bits]
epsilon = bits_to_dec(epsilon_bits)


print("== Part 1 ==")
print(f"gamma rate:   {gamma}")
print(f"epsilon rate: {epsilon}")
print(f"Power:        {gamma * epsilon}")

print()
print('--------')


def most_common(index, data):
    count = 0
    for entry in data:
        count += entry[index]

    if count / len(data) >= 0.5:
        return 1
    else:
        return 0


def least_common(index, data):
    count = 0
    for entry in data:
        count += entry[index]

    if count / len(data) >= 0.5:
        return 0
    else:
        return 1



print()
print("== Part 2 ==")

# Oxygen - most common value in current bit position
oxygen_data = bit_array
for ix in range(data_width):
    target_val = most_common(ix, oxygen_data)
    oxygen_data = [entry for entry in oxygen_data if entry[ix] == target_val]

    if len(oxygen_data) == 1:
        break

oxygen = bits_to_dec(oxygen_data[0])

print(f"oxygen:       {oxygen}")

# Carbon dioxide - least common value in current bit position
co2_data = bit_array
for ix in range(data_width):
    target_val = least_common(ix, co2_data)
    co2_data = [entry for entry in co2_data if entry[ix] == target_val]

    if len(co2_data) == 1:
        break

co2 = bits_to_dec(co2_data[0])

print(f"co2:          {co2}")
print(f"Life support: {oxygen * co2}")

