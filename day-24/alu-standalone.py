#! /usr/bin/env python3

import argparse
import math
import re
import sys

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='The input file')
parser.add_argument('-D', '--debug', action='store_true')

args = parser.parse_args()

PART_1 = True

with open(args.filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


INSTRUCTION_REGEX = re.compile(r'(\w{3}) (\w)(?: (\w|-?\d+))?')
NUMBER_REGEX = re.compile(r'(-?\d+)')

def alu(instructions, input_str, in_vars):
    input = (x for x in input_str)
    vars = {
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
    }
    if in_vars:
        vars.update(in_vars)

    for ix, line in enumerate(instructions):
        # if ix % 100 == 0:
        #     print(f"  instruction {ix}")

        match = INSTRUCTION_REGEX.match(line)
        inst = match[1]
        argA = match[2]
        argB = match[3]

        if argB:
            if NUMBER_REGEX.match(argB):
                var_b = int(argB)
            else:
                var_b = vars[argB]
        else:
            var_b = None

        # print(f"  Instruction:", inst, argA, argB, type(argB))

        if inst == 'inp':
            vars[argA] = int(next(input))
        elif inst == 'add':
            vars[argA] += var_b
        elif inst == 'mul':
            vars[argA] *= var_b
        elif inst == 'div':
            if var_b == 0:
                print('Fatal error: you destroyed the magic smoke')
                print(line, vars)
                sys.exit(10)
            temp = vars[argA] / var_b
            vars[argA] = math.trunc(temp)
        elif inst == 'mod':
            if vars[argA] < 0 or var_b < 0:
                print('Fatal error: you destroyed the magic smoke')
                print(line, vars)
                sys.exit(10)
            vars[argA] %= var_b
        elif inst == 'eql':
            vars[argA] = 1 if vars[argA] == var_b else 0

    return vars


# model_number = 99999999999999
# model_number = 99999994775989
# model_number = 99999985841897
model_number = 99999893325755

while model_number > 0:
    model_str = str(model_number)
    if '0' in model_str:
        model_number -= 1
        continue
    result = alu(lines, model_str)
    if model_number % 50 == 5:
        print(f"{model_number}: {result}")
    if result['z'] == 0:
        print(f"Model number validated: {model_number}")
        break
    model_number -= 1
