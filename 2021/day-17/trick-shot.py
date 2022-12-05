#! /usr/bin/env python3

import argparse
import math
import re

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='The input file')
parser.add_argument('-D', '--debug', action='store_true')

args = parser.parse_args()

PART_1 = True

with open(args.filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

data = lines[0]


target_regex = re.compile(r'target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)')
match = target_regex.match(lines[0])

x_min = int(match[1])
x_max = int(match[2])
y_min = int(match[3])
y_max = int(match[4])

print(x_min, x_max, y_min, y_max)


# x_min <= n*(n+1)/2 <= x_max
# 2*x_min <= n^2 + n
# a*x^2 + b*x + c = 0
# x = (-b +/- math.sqrt(b^2 - 4*a*c)) / (2*a)

# min_speed_1 = (-1 + math.sqrt(1 + 8*x_min)) / 2
# min_speed_2 = (-1 - math.sqrt(1 + 8*x_min)) / 2
# max_speed_1 = (-1 + math.sqrt(1 + 8*x_max)) / 2
# max_speed_2 = (-1 - math.sqrt(1 + 8*x_max)) / 2


# NOTE: We don't need to have the probe *stop* in the target area, it just has
# to reach there during one of the steps.

# We can determine the minimum horizontal starting velocity, as that would be
# what it takes to reach the minimum X coordinate.  We can also determine the
# maximum horizontal velocity, which is the maximum X coordinate (since any
# faster and the probe would never end up in the target area)

# min_horizontal = (-1 + math.sqrt(1 + 8*x_min)) / 2
# min_horizontal = int(round(min_horizontal, 0))

# max_horizontal = x_max


# So, from those we know how many steps we have to work with.

# min_step = min_horizontal
# max_step = max_horizontal # Uhh.... this isn't right




# ==== Horizontal speed ====

# The greatest number of steps that we would have to deal with is if the probe
# travelled horizontally at the absolute slowest that it could, which means that
# it would reach a `v_x` of `0` at the farthest point in the target area.
# Therefore, we will first figure out what that slowest possible velocity is.

slowest_horizontal = (-1 + math.sqrt(1 + 8*x_max)) / 2
slowest_horizontal = int(round(slowest_horizontal, 0))
# max_step = slowest_horizontal

# Alternatively, as long as the probe reaches at least as far as the minimum x
# coordinate, but then reaches a zero horizontal velocity, we have any number of
# steps to get the vertical velocity correct


# Depending on the horizontal speed that we start at, some steps may or may work
# for our final answer.

# The fastest initial horizontal speed would be the one that takes us to the
# very end of the target space in one go.

# Steps that, for some initial horizontal speed, are within the target zone
valid_steps = set()

# Speeds that result in the probe reaching a horizontal speed of zero within the
# target zone.  (due to the nature of the probe slowing down, these speeds are
# also the step at which the probe reaches zero velocity)
stops_in_target_zone = set()

for x_speed_start in range(1, x_max+1):
    # print("Start speed:", x_speed_start)
    x_position = 0
    x_speed = x_speed_start
    step = 0
    while x_position <= x_max:
        step += 1
        x_position += x_speed

        if x_speed > 0:
            x_speed -= 1
        elif x_speed < 0:
            x_speed += 1
        # print(f"  Step {step}: position: {x_position}, speed: {x_speed}")

        #print(f"    {x_min} <= {x_position} <= {x_max}")
        if x_min <= x_position and x_position <= x_max:
            valid_steps.add(step)

        if x_speed == 0:
            stops_in_target_zone.add(x_speed_start)
            break

print("Valid steps:", valid_steps)
print()
print("Speeds that stop within target area:", stops_in_target_zone)
print()





# ==== Vertical speed ====

# For each possible starting y velocity, figure out which ones end up in our
# target area within the max number of steps that we found above.


# When the probe comes down, once it reaches `y=0`, it will be traveling at a
# speed of `-initial_y`.  The fastest probe would then reach `y=y_min` in the
# very next step, so we can use the difference between these to cap our initial
# velocity.

max_vertical_velocity = 0 - y_min
print("Max vertical:", max_vertical_velocity)


highest_point = 0
initial_speed = 0

candidates = []


for initial_vertical_speed in range(0, max_vertical_velocity):
    if args.debug:
        print(f"Checking speed {initial_vertical_speed}")

    step = 0
    have_solution = False
    highest_for_this_start = 0
    vertical_position = 0
    vertical_velocity = initial_vertical_speed

    while vertical_position > y_min:
        step += 1
        vertical_position += vertical_velocity
        vertical_velocity -= 1
        if args.debug:
            print(f"> Step {step}: Pos: {vertical_position}, Vel: {vertical_velocity}")

        if vertical_position > highest_for_this_start:
            highest_for_this_start = vertical_position

        # if step in valid_steps and y_min <= vertical_position and vertical_position <= y_max:
        if y_min <= vertical_position and vertical_position <= y_max:
            candidates.append({
                'initial_v_y': initial_vertical_speed,
                'highest': highest_for_this_start,
                'steps': step,
                'endpoint': vertical_position,
            })
            have_solution = True
            break

    if have_solution:
        if args.debug:
            print(f"  > SOLUTION - initial v_y: {initial_vertical_speed}, highest: {highest_for_this_start}")
        if highest_for_this_start > highest_point:
            if args.debug:
                print(f"    > Highest so far")
            highest_point = highest_for_this_start
            initial_speed = initial_vertical_speed
    if args.debug:
        print()


print("Candidates:")
for candidate in candidates:
    print(candidate)
print()
print(f"Highest: {highest_point}, initial speed: {initial_speed}")









