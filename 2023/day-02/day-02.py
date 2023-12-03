#! /usr/bin/env python3

import argparse
import functools
import re

parser = argparse.ArgumentParser("Day 2")
parser.add_argument("infile", help="The input file")
args = parser.parse_args()

def part1(lines):
    print("\n\n~~ PART 1~~")

    MAX_GREEN = 13
    MAX_RED = 12
    MAX_BLUE = 14

    candidate_games = []

    rounds = [[x.split("; ") for x in line.rstrip().split(": ")] for line in lines]
    
    for round in rounds:
        game_match = re.search(r'\d+', round[0][0])
        game_id = int(game_match.group(0))
        print()
        print("Game:", game_id)

        game_could_work = True

        for sample in round[1]:
            print(" ", sample)
            green_match = re.findall(r'(\d+) green', sample)
            blue_match = re.findall(r'(\d+) blue', sample)
            red_match = re.findall(r'(\d+) red', sample)

            green = 0 if not green_match else int(green_match[0])
            blue = 0 if not blue_match else int(blue_match[0])
            red = 0 if not red_match else int(red_match[0])

            print("    [green, blue, red]", [green, blue, red])

            if green > MAX_GREEN or blue > MAX_BLUE or red > MAX_RED:
                game_could_work = False

        if game_could_work:
            candidate_games.append(game_id)

    print("Candidate games:", candidate_games)
    print("  Total:", functools.reduce(lambda x,y: x+y, candidate_games, 0))


def part2(lines):
    print("\n\n~~ PART 2~~")

    MAX_GREEN = 13
    MAX_RED = 12
    MAX_BLUE = 14

    candidate_games = []
    power_sum = 0

    rounds = [[x.split("; ") for x in line.rstrip().split(": ")] for line in lines]
    
    for round in rounds:
        game_match = re.search(r'\d+', round[0][0])
        game_id = int(game_match.group(0))
        print()
        print("Game:", game_id)

        fewest_balls = {
            "green": 0,
            "red": 0,
            "blue": 0,
        }

        game_could_work = True

        for sample in round[1]:
            print(" ", sample)
            green_match = re.findall(r'(\d+) green', sample)
            blue_match = re.findall(r'(\d+) blue', sample)
            red_match = re.findall(r'(\d+) red', sample)

            green = 0 if not green_match else int(green_match[0])
            blue = 0 if not blue_match else int(blue_match[0])
            red = 0 if not red_match else int(red_match[0])

            print("    [green, blue, red]", [green, blue, red])

            if green > MAX_GREEN or blue > MAX_BLUE or red > MAX_RED:
                game_could_work = False

            if green > fewest_balls["green"]:
                fewest_balls["green"] = green
            if blue > fewest_balls["blue"]:
                fewest_balls["blue"] = blue
            if red > fewest_balls["red"]:
                fewest_balls["red"] = red

        if game_could_work:
            candidate_games.append(game_id)

        print("Fewest balls:", fewest_balls)
        print("  sum:", fewest_balls["green"])
        power_of_set = fewest_balls["green"] * fewest_balls["blue"] * fewest_balls["red"]
        print(f"Game {game_id}, power={power_of_set}")
        power_sum += power_of_set

    print("Candidate games:", candidate_games)
    print("  Total:", functools.reduce(lambda x,y: x+y, candidate_games, 0))

    print("Power sum:", power_sum)



with open(args.infile) as file:
    lines = file.readlines()
    # part1(lines)

    part2(lines)
