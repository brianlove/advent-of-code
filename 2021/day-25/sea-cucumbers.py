#! /usr/bin/env python3

import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='The input file')
parser.add_argument('-D', '--debug', action='store_true')

args = parser.parse_args()

PART_1 = True

MOVE_HORIZ = 1
MOVE_VERT = 2

with open(args.filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

map = [[{'val': x, 'moved': False} for x in line] for line in lines]
height = len(map)
width = len(map[0])

def print_map():
    for row in map:
        for cell in row:
            print(cell['val'], end='')
        print()
    print()

step = 0
num_moved = sys.maxsize

print_map()

while num_moved > 0:
    step += 1
    num_moved = 0

    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if cell['val'] != '>' or cell['moved']:
                continue

            if x < width - 1:
                if row[x+1]['val'] == '.' and row[x]['moved'] != MOVE_HORIZ:
                    row[x]['val'] = '.'
                    row[x+1]['val'] = '>'
                    row[x]['moved'] = MOVE_HORIZ
                    row[x+1]['moved'] = MOVE_HORIZ
                    num_moved += 1
            else:
                if row[0]['val'] == '.' and row[0]['moved'] != MOVE_HORIZ:
                    row[x]['val'] = '.'
                    row[0]['val'] = '>'
                    row[x]['moved'] = MOVE_HORIZ
                    row[0]['moved'] = MOVE_HORIZ
                    num_moved += 1

    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if cell['val'] != 'v' or cell['moved'] == MOVE_VERT:
                continue

            if y < height - 1:
                if map[y+1][x]['val'] == '.' and map[y+1][x]['moved'] != MOVE_VERT:
                    map[y][x]['val'] = '.'
                    map[y+1][x]['val'] = 'v'
                    map[y][x]['moved'] = MOVE_VERT
                    map[y+1][x]['moved'] = MOVE_VERT
                    num_moved += 1
            else:
                if map[0][x]['val'] == '.' and map[0][x]['moved'] != MOVE_VERT:
                    map[y][x]['val'] = '.'
                    map[0][x]['val'] = 'v'
                    map[y][x]['moved'] = MOVE_VERT
                    map[0][x]['moved'] = MOVE_VERT
                    num_moved += 1

    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            map[y][x]['moved'] = False

    if args.debug:
        print(f"Step {step}")
        print_map()

    if num_moved == 0:
        print(f"Step {step}")
        print_map()
        print("No move movement!")
        break
