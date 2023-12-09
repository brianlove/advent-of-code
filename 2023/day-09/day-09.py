#! /usr/bin/env python3

import argparse
import re

parser = argparse.ArgumentParser("Day 9")
parser.add_argument("infile", help="The input file")
args = parser.parse_args()

def is_all_zeros(value) -> bool:
    for x in value:
        if x != 0:
            return False
    return True


def part1(lines):
    print("\n\n~~ PART 1~~")

    extrapolated_sums = 0

    for line in lines:
        history = [int(c) for c in line.split(' ')]
        print()
        print(history)

        ## Evaluate the history
        record = [history]
        print("-", record)
        iteration = 0
        print("All zeros?", is_all_zeros(record[iteration]))
        while not is_all_zeros(record[iteration]):
            prev_history = record[iteration]
            iteration += 1
            record.append([None] * (len(record[iteration-1])-1))
            print("> ", record[iteration-1])
            for ix in range(len(record[iteration])):
                record[iteration][ix] = prev_history[ix+1] - prev_history[ix]

        print("> ", record[iteration])

        record[iteration].append(0)


        ## Build up the next values
        while iteration > 0:
            delta_iteration = iteration
            iteration -= 1
            print("> ", iteration)

            delta_seq = record[delta_iteration]
            delta_value = delta_seq[-1]
            print("delta_value:", delta_value)

            current_value = record[iteration][-1]

            record[iteration].append(delta_value + current_value)
            print("> ", record[iteration])

        new_history_value = record[0][-1]
        print(f"New history: {new_history_value}: ", history)
        extrapolated_sums += new_history_value

    print("Extrapolated sums:", extrapolated_sums)


def part2(lines):
    print("\n\n~~ PART 2~~")

    extrapolated_sums = 0

    for line in lines:
        history = [int(c) for c in line.split(' ')]
        print()
        print(history)

        ## Evaluate the history
        record = [history]
        print("-", record)
        iteration = 0
        print("All zeros?", is_all_zeros(record[iteration]))
        while not is_all_zeros(record[iteration]):
            prev_history = record[iteration]
            iteration += 1
            record.append([None] * (len(record[iteration-1])-1))
            print("> ", record[iteration-1])
            for ix in range(len(record[iteration])):
                record[iteration][ix] = prev_history[ix+1] - prev_history[ix]

        print("> ", record[iteration])

        # record[iteration].append(0)
        record[iteration].insert(0, 0)


        ## Build up the next values
        while iteration > 0:
            delta_iteration = iteration
            iteration -= 1
            print("> ", iteration)

            delta_seq = record[delta_iteration]
            delta_value = delta_seq[0]
            print("delta_value:", delta_value)

            current_value = record[iteration][0]

            record[iteration].insert(0, current_value - delta_value)
            print("> ", record[iteration])

        new_history_value = record[0][0]
        print(f"New history: {new_history_value}: ", history)
        extrapolated_sums += new_history_value
        # break;

    print("Extrapolated sums:", extrapolated_sums)


with open(args.infile) as file:
    lines = [line.rstrip() for line in file.readlines()]
    part1(lines)

    part2(lines)
