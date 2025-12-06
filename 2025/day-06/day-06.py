#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser("Day 6")
parser.add_argument("infile", help="The input file")
args = parser.parse_args()

ADD = '+'
MUL = '*'
OPERATIONS = [ADD, MUL]

def part1(lines: list[str]):
    print("\n\n~~ PART 1~~")
    arguments = []
    operations = ''
    for line in lines:
        splitLine = line.split()
        if splitLine[0] in OPERATIONS:
            operations = splitLine
        else:
            arguments.append([int(x) for x in splitLine])
    for args in arguments:
        print(args)
    print(operations)

    grandTotal = 0
    for ix, operator in enumerate(operations):
        if operator == ADD:
            total = 0
            for arg in arguments:
                total += arg[ix]
        elif operator == MUL:
            total = 1
            for arg in arguments:
                total *= arg[ix]
        grandTotal += total
    print("Grand total:", grandTotal)



def part2(lines: list[str]):
    print("\n\n~~ PART 2~~")
    arguments = []
    operations = ''
    for line in lines:
        print(f"> '{line}'")
        if line[0] in OPERATIONS:
            operations = line
        else:
            arguments.append(line)
    print()

    grandTotal = 0
    currentOperation = None
    numbers = []
    for ix in range(len(operations)-1, -1, -1):
        buffer = ''
        for argument in arguments:
            buffer += argument[ix]

        if buffer.strip() == '':
            continue # no-op
        else:
            numbers.append(int(buffer))

        if operations[ix] in OPERATIONS:
            currentOperation = operations[ix]
            print(f"op {currentOperation}, {numbers}")
            if currentOperation == ADD:
                total = 0
                for num in numbers:
                    total += num
            elif currentOperation == MUL:
                total = 1
                for num in numbers:
                    total *= num
            print(" - total:", total)
            grandTotal += total
            numbers = []
    print("Grand total:", grandTotal)



with open(args.infile) as file:
    lines = [line.rstrip("\n\r") for line in file.readlines()]
    part1(lines)

    part2(lines)
