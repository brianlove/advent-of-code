#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='The input file')
parser.add_argument('-d', '--days', type=int, default=80, help='The number of days')
parser.add_argument('--insane-mode', action='store_true', help='The insane, slow mode')

args = parser.parse_args()
print(args)

print(f"Calculating lantern fish after {args.days} days")
print(f"-- Using {'INSANE mode' if args.insane_mode else 'rational mode'}")
print()


with open(args.filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

initial_states = [int(x) for x in lines[0].split(',')]


if args.insane_mode:
    # Part 1
    # Naive / insane mode, keeping track of each fish individually like the
    # demo input.  NOT a great idea for 256 days!
    state = initial_states.copy()
    for day in range(args.days):
        num_spawn = 0
        for ix, fish in enumerate(state):
            if fish == 0:
                num_spawn += 1
                state[ix] = 6
            else:
                state[ix] -= 1
        state += [8] * num_spawn
        # print(f"Day {day+1}: {state}")

    print("== Insane mode ==")
    print(f"After {args.days} days, there are {len(state)} fish")
    print()


if not args.insane_mode:
    # Sane mode - developed for Part 2
    # Instead of keeping track of the ages of each fish individually,
    # keep track of how many fish are of each age.  That's a more
    # manageable size of array, which will help with performance.

    # Fish are 0-8 days old
    ages = [0] * 9
    for fish in initial_states:
        ages[fish] += 1
    # print(f"Initial ages: {ages}")

    for day in range(args.days):
        to_spawn = ages[0]
        ages = ages[1:] + [to_spawn]
        ages[6] += to_spawn
        # print(f"Day {day+1}: {ages}")

    print("== Rational mode ==")
    print(f"After {args.days} days, there are {sum(ages)} fish")
