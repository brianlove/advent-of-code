#! /usr/bin/env python3

import argparse
import collections
import functools

parser = argparse.ArgumentParser("Day 5")
parser.add_argument("infile", help="The input file")
args = parser.parse_args()

def parseUpdates(lines):
    rules = []
    updates = []
    afterMap = collections.defaultdict(lambda: [])

    haveFinishedRules = False
    for line in lines:
        if line == "":
            haveFinishedRules = True
        elif not haveFinishedRules:
            rule = [int(x) for x in line.split('|')]
            rules.append(rule)
            first, second = rule
            afterMap[first].append(second)
        elif haveFinishedRules:
            updates.append([int(x) for x in line.split(',')])

    goodUpdates = []
    badUpdates = []

    for update in updates:
        isUpdateOkay = True
        for ix, entry in enumerate(update):
            previousEntries = update[:ix]
            intersections = list(set(previousEntries) & set(afterMap[entry]))

            if len(intersections) > 0:
                isUpdateOkay = False
                break

        if isUpdateOkay:
            goodUpdates.append(update)
        else:
            badUpdates.append(update)

    return afterMap, goodUpdates, badUpdates


def part1(lines):
    print("\n\n~~ PART 1~~")

    afterMap, goodUpdates, badUpdates = parseUpdates(lines)

    print("Good updates:", goodUpdates)

    middlePages = [(update[len(update) // 2]) for update in goodUpdates]

    print("middle pages:", middlePages)
    print("  Sum:", sum(middlePages))


def part2(lines):
    print("\n\n~~ PART 2~~")

    afterMap, goodUpdates, badUpdates = parseUpdates(lines)

    def sortComparator(a, b):
        if b in afterMap[a]:
            return -1
        elif a in afterMap[b]:
            return 1
        else:
            return 0

    sortedUpdates = [
        sorted(update, key=functools.cmp_to_key(sortComparator))
        for update in badUpdates
    ]
    middlePages = [(update[len(update) // 2]) for update in sortedUpdates]

    print("middle pages:", middlePages)
    print("  Sum:", sum(middlePages))


with open(args.infile) as file:
    lines = [line.rstrip() for line in file.readlines()]
    part1(lines)

    part2(lines)
