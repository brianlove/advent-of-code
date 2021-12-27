#! /usr/bin/env python3

import math
import re
import sys

INSTRUCTION_REGEX = re.compile(r'(\w{3}) (\w)(?: (\w|-?\d+))?')
NUMBER_REGEX = re.compile(r'(-?\d+)')

def alu(instructions, input, vars={'w': 0, 'x': 0, 'y': 0, 'z': 0}):
    input_generator = (x for x in input)
    _vars = {
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
    }
    if vars:
        _vars.update(vars)

    for ix, line in enumerate(instructions):
        split = line.split()
        inst = split[0]
        argA = split[1]
        if len(split) == 3:
            argB = split[2]
        else:
            argB = None

        if argB:
            if NUMBER_REGEX.match(argB):
                var_b = int(argB)
            else:
                var_b = _vars[argB]
        else:
            var_b = None

        if inst == 'inp':
            _vars[argA] = int(next(input_generator))
        elif inst == 'add':
            _vars[argA] += var_b
        elif inst == 'mul':
            _vars[argA] *= var_b
        elif inst == 'div':
            if var_b == 0:
                print('Fatal error: you destroyed the magic smoke')
                print(line, _vars)
                sys.exit(10)
            temp = _vars[argA] / var_b
            _vars[argA] = math.trunc(temp)
        elif inst == 'mod':
            if _vars[argA] < 0 or var_b < 0:
                print('Fatal error: you destroyed the magic smoke')
                print(line, _vars)
                sys.exit(10)
            _vars[argA] %= var_b
        elif inst == 'eql':
            _vars[argA] = 1 if _vars[argA] == var_b else 0

    return _vars
