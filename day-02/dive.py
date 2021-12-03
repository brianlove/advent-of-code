#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='The input file')

args = parser.parse_args()

with open(args.filename) as file:
    instructions = file.readlines()


# Part 1

position = 0
depth = 0

for instruction in instructions:
    direction, amount = instruction.split()
    amount = int(amount)

    if direction == "forward":
        position += amount
    elif direction == "down":
        depth += amount
    elif direction == "up":
        depth -= amount

print("== Part 1 ==")
print(f"Final location: {position}, {depth}")
print(f"Question answer: {position} * {depth} = {position * depth}")


# Part 2

print()
print("--------")
print()

position = 0
depth = 0
aim = 0

for instruction in instructions:
    direction, amount = instruction.split()
    amount = int(amount)

    if direction == "forward":
        position += amount
        depth += aim * amount
    elif direction == "down":
        aim += amount
    elif direction == "up":
        aim -= amount

print("== Part 2 ==")
print(f"Final location: {position}, {depth}, {aim}")
print(f"Question answer: {position} * {depth} = {position * depth}")
