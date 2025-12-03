#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser("Day 3")
parser.add_argument("infile", help="The input file")
args = parser.parse_args()

def part1(lines: list[str]):
    print("\n\n~~ PART 1~~")
    totalJoltage = 0
    for ix, line in enumerate(lines):
        batteryBank = [int(x) for x in line]
        largest = max(batteryBank)
        largestIndex = batteryBank.index(largest)

        ## The largest digit is the second digit, and is preceded
        laterDigits = batteryBank[largestIndex + 1:]
        # print("> later:", laterDigits)
        if len(laterDigits) > 0:
            largestLater = max(laterDigits)
        else:
            largestLater = -100000
        laterJoltage = largest * 10 + largestLater

        ## The largest digit is the first digit
        previousDigits = batteryBank[:largestIndex]
        # print("> prev:", previousDigits)
        if len(previousDigits) > 0:
            largestPrevious = max(previousDigits)
        else:
            largestPrevious = -100000
        previousJoltage = largestPrevious * 10 + largest

        maxJoltage = max(laterJoltage, previousJoltage)
        # print(f"Joltage in bank {ix}: {maxJoltage}")
        totalJoltage += maxJoltage
    print("Total joltage:", totalJoltage)


def part2(lines: list[str]):
    print("\n\n~~ PART 2~~")
    totalJoltage = 0
    for ix, line in enumerate(lines):
        batteryBank = [int(x) for x in line]
        # print()
        # print(line)
        # print(batteryBank)

        while len(batteryBank) > 12:
            nextIter = False

            # If a battery is followed by one larger than it, we can get
            # more joltage by turning off the first and using the later
            # (larger) one instead.
            for i in range(0, len(batteryBank) - 2):
                if batteryBank[i] < batteryBank[i+1]:
                    batteryBank.pop(i)
                    nextIter = True
                    break
            if nextIter:
                continue

            # Trim small things from the rear
            smallest = min(batteryBank)
            batteryBank.remove(smallest)

        # print("trimmed:", batteryBank)
        joltage = int(''.join(str(x) for x in batteryBank))
        # print("- ", joltage)
        totalJoltage += joltage

    print("Total joltage:", totalJoltage)


with open(args.infile) as file:
    lines = [line.rstrip() for line in file.readlines()]
    part1(lines)

    part2(lines)
