#! /usr/bin/env python3

import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='The input file')
parser.add_argument('-D', '--debug', action='store_true')

args = parser.parse_args()

PART_1 = True

with open(args.filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

target_regex = re.compile(r'target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)')
match = target_regex.match(lines[0])

x_min = int(match[1])
x_max = int(match[2])
y_min = int(match[3])
y_max = int(match[4])

# The fastest possible horizontal speed is `x_max`, as otherwise the probe would
# overshoot the target area right away.
max_horizontal_speed = x_max

# The fastest possible vertical speed is `y_min`, as otherwise the probe would
# go deeper than the target area right away.
max_positive_vertical_speed = abs(y_min)
max_negative_vertical_speed = y_min


def probe_trajectory(initial_x, initial_y):
    step = 0
    x_speed = initial_x
    x_pos = 0
    y_speed = initial_y
    y_pos = 0

    while x_pos <= x_max and y_pos >= y_min:
        step += 1

        x_pos += x_speed
        if x_speed > 0:
            x_speed -= 1
        elif x_speed < 0:
            x_speed += 1

        y_pos += y_speed
        y_speed -= 1

        if x_min <= x_pos and x_pos <= x_max and y_min <= y_pos and y_pos <= y_max:
            # This probe is within the target area
            return True

    # Once we go past the target area, there's no hope
    return False

valid_speeds = []

for horiz_speed in range(1, max_horizontal_speed + 1):
    for vert_speed in range(max_negative_vertical_speed, max_positive_vertical_speed + 1):
        velocity = (horiz_speed, vert_speed)
        result = probe_trajectory(horiz_speed, vert_speed)
        if result:
            if args.debug:
                print(f"  Success: {velocity}")
            valid_speeds.append(velocity)

print(f"There are {len(valid_speeds)} trajectories that reach the target zone")
