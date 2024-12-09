#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser("Day 9")
parser.add_argument("infile", help="The input file")
args = parser.parse_args()

def part1(lines):
    print("\n\n~~ PART 1~~")
    rawInput = list(int(x) for x in lines[0])

    fileIdsToSizes = {}
    filesystem = []
    for ix, digit in enumerate(rawInput):
        if ix % 2 == 0: ## looking at a file
            fileId = ix // 2
            fileIdsToSizes[fileId] = digit
            filesystem.extend([fileId] * digit)
        else:
            filesystem.extend([None] * digit)

    # print("fileIdsTOSizes:", fileIdsToSizes)
    # print("filesystem:", filesystem)

    fillingIndex = 0
    compactedFilesystem = list(filesystem)
    while None in compactedFilesystem:
        lastEntry = compactedFilesystem.pop()
        if lastEntry == None:
            continue
        while compactedFilesystem[fillingIndex] is not None:
            fillingIndex += 1
        compactedFilesystem[fillingIndex] = lastEntry
    # print("compacted>", compactedFilesystem)

    checksum = sum(ix * digit for ix, digit in enumerate(compactedFilesystem))
    print("checksum:", checksum)


def part2(lines):
    print("\n\n~~ PART 2~~")
    pass


with open(args.infile) as file:
    lines = [line.rstrip() for line in file.readlines()]
    part1(lines)

    # part2(lines)
