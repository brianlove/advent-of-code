#! /usr/bin/env python3

import argparse
import functools
import re

parser = argparse.ArgumentParser("Day 4")
parser.add_argument("infile", help="The input file")
args = parser.parse_args()

def part1(lines):
    print("\n\n~~ PART 1~~")

    total_value = 0

    for line in lines:
        card, nums = line.split(": ")
        winning, my_nums = [[int(c) for c in x.split()] for x in nums.split(" | ")]
        # print(line)
        # print("  win: ", winning)
        # print("  mine:", my_nums)

        value = 0
        for num in my_nums:
            if num in winning:
                value = 1 if value == 0 else value * 2
                # print(f"    - {num}: match - {value}")

        print(f"{card} value: {value}")
        total_value += value

    print()
    print("Total value:", total_value)


def part2(lines):
    print("\n\n~~ PART 2~~")

    card_copies = [1] * len(lines)

    for line in lines:
        card_temp, nums = line.split(": ")
        card_match = re.search(r'\d+', card_temp)
        card_num = int(card_match.group(0)) if card_match else None

        winning, my_nums = [[int(c) for c in x.split()] for x in nums.split(" | ")]
        num_matches = 0
        for num in my_nums:
            if num in winning:
                num_matches += 1

        print(f"{card_num}: {num_matches} matches")

        for i in range(num_matches):
            # print(i)
            card_copies[card_num + i] += card_copies[card_num - 1]
            # print(f"   Card {card_num}")
            # print((card_num, i), card_copies)
            pass
        print(f"  After card {card_num}", card_copies)

        # break

    total_cards = functools.reduce(lambda x,y: x + y, card_copies, 0)
    print("Total cards:", total_cards)


with open(args.infile) as file:
    lines = [line.rstrip() for line in file.readlines()]
    part1(lines)

    part2(lines)
