#! /usr/bin/env python3

import argparse
import collections
import itertools

parser = argparse.ArgumentParser("Day 7")
parser.add_argument("infile", help="The input file")
args = parser.parse_args()

def ADD(a, b):
    return a + b

def MUL(a, b):
    return a * b

OPERATORS = [ ADD, MUL ]

def calculateCalibrationResult(lines, operators):
    totalCalibrationResult = 0

    for line in lines:
        split = line.split(": ")
        testVal = int(split[0])
        inputVals = [int(x) for x in split[1].split()]

        numOperators = len(inputVals) - 1
        operatorSeqs = itertools.product(operators, repeat=numOperators)
        for seq in operatorSeqs:
            res = inputVals[0]
            for val, op in zip(inputVals[1:], seq):
                res = op(res, val)

            if res == testVal:
                totalCalibrationResult += res
                break

    return totalCalibrationResult


def part1(lines):
    print("\n\n~~ PART 1~~")

    totalCalibrationResult = calculateCalibrationResult(lines, OPERATORS)
    print("Total calibration result:", totalCalibrationResult)


def CONCAT(a, b):
    return int(f"{a}{b}")

OPERATORS_PT2 = [ ADD, MUL, CONCAT ]

def part2(lines):
    print("\n\n~~ PART 2~~")

    totalCalibrationResult = calculateCalibrationResult(lines, OPERATORS_PT2)
    print("Total calibration result:", totalCalibrationResult)


with open(args.infile) as file:
    lines = [line.rstrip() for line in file.readlines()]
    part1(lines)

    part2(lines)
