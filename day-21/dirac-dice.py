#! /usr/bin/env python3

import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='The input file')
parser.add_argument('-D', '--debug', action='store_true')
parser.add_argument('--demo', action='store_true')

args = parser.parse_args()

PART_1 = True

with open(args.filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

player_start_regex = re.compile(r'Player \d starting position: (\d+)')
player_1_start = int(player_start_regex.match(lines[0])[1])
player_2_start = int(player_start_regex.match(lines[1])[1])

if args.debug:
    print("Starting positions:", player_1_start, player_2_start)


def generate_dice(max):
    dice = [x for x in range(1, max+1)]
    index = 0
    while True:
        yield dice[index]
        index += 1
        if index >= len(dice):
            index = 0

dice = generate_dice(100)

players = [
    {
        'name': 'Player 1',
        'start': player_1_start,
        'score': 0,
        'position': player_1_start
    },
    {
        'name': 'Player 2',
        'start': player_2_start,
        'score': 0,
        'position': player_2_start
    }
]

winner = False
game_running = True
have_losing_score = False

losing_score = 0
die_rolls = 0

while True:
    for player in players:
        if args.debug:
            print(game_running, player)

        if not game_running:
            losing_score = player['score']
            have_losing_score = True
            break

        a = next(dice)
        b = next(dice)
        c = next(dice)
        rolled = a + b + c
        die_rolls += 3

        # The `+ 1` and `- 1` are to deal with the use of 1-up numbers on the
        # board, while still having 0-up numbers internally
        player['position'] = ((player['position'] + rolled - 1) % 10) + 1

        player['score'] += player['position']
        if args.debug:
            print(f"  {player['name']} rolls {(a, b, c)}, score is {player['score']}")

        if player['score'] >= 1000:
            winner = player
            game_running = False
    if winner and have_losing_score:
        break

print("Score limit reached:", winner)
print("Loser score:", losing_score)
print("Die rolls:", die_rolls)
print()

print(f"Part 1 result: {losing_score * die_rolls}")



