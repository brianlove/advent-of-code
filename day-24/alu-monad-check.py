#! /usr/bin/env python3

import math
import time

import alu

monad = [
    [
        'inp w',
        'mul x 0',
        'add x z',
        'mod x 26',
        'div z 1',
        'add x 11',
        'eql x w',
        'eql x 0',
        'mul y 0',
        'add y 25',
        'mul y x',
        'add y 1',
        'mul z y',
        'mul y 0',
        'add y w',
        'add y 6',
        'mul y x',
        'add z y',
    ], [
        'inp w',
        'mul x 0',
        'add x z',
        'mod x 26',
        'div z 1',
        'add x 11',
        'eql x w',
        'eql x 0',
        'mul y 0',
        'add y 25',
        'mul y x',
        'add y 1',
        'mul z y',
        'mul y 0',
        'add y w',
        'add y 12',
        'mul y x',
        'add z y',
    ], [
        'inp w',
        'mul x 0',
        'add x z',
        'mod x 26',
        'div z 1',
        'add x 15',
        'eql x w',
        'eql x 0',
        'mul y 0',
        'add y 25',
        'mul y x',
        'add y 1',
        'mul z y',
        'mul y 0',
        'add y w',
        'add y 8',
        'mul y x',
        'add z y',
    ], [
        'inp w',
        'mul x 0',
        'add x z',
        'mod x 26',
        'div z 26',
        'add x -11',
        'eql x w',
        'eql x 0',
        'mul y 0',
        'add y 25',
        'mul y x',
        'add y 1',
        'mul z y',
        'mul y 0',
        'add y w',
        'add y 7',
        'mul y x',
        'add z y',
    ], [
        'inp w',
        'mul x 0',
        'add x z',
        'mod x 26',
        'div z 1',
        'add x 15',
        'eql x w',
        'eql x 0',
        'mul y 0',
        'add y 25',
        'mul y x',
        'add y 1',
        'mul z y',
        'mul y 0',
        'add y w',
        'add y 7',
        'mul y x',
        'add z y',
    ], [
        'inp w',
        'mul x 0',
        'add x z',
        'mod x 26',
        'div z 1',
        'add x 15',
        'eql x w',
        'eql x 0',
        'mul y 0',
        'add y 25',
        'mul y x',
        'add y 1',
        'mul z y',
        'mul y 0',
        'add y w',
        'add y 12',
        'mul y x',
        'add z y',
    ], [
        'inp w',
        'mul x 0',
        'add x z',
        'mod x 26',
        'div z 1',
        'add x 14',
        'eql x w',
        'eql x 0',
        'mul y 0',
        'add y 25',
        'mul y x',
        'add y 1',
        'mul z y',
        'mul y 0',
        'add y w',
        'add y 2',
        'mul y x',
        'add z y',
    ], [
        'inp w',
        'mul x 0',
        'add x z',
        'mod x 26',
        'div z 26',
        'add x -7',
        'eql x w',
        'eql x 0',
        'mul y 0',
        'add y 25',
        'mul y x',
        'add y 1',
        'mul z y',
        'mul y 0',
        'add y w',
        'add y 15',
        'mul y x',
        'add z y',
    ], [
        'inp w',
        'mul x 0',
        'add x z',
        'mod x 26',
        'div z 1',
        'add x 12',
        'eql x w',
        'eql x 0',
        'mul y 0',
        'add y 25',
        'mul y x',
        'add y 1',
        'mul z y',
        'mul y 0',
        'add y w',
        'add y 4',
        'mul y x',
        'add z y',
    ], [
        'inp w',
        'mul x 0',
        'add x z',
        'mod x 26',
        'div z 26',
        'add x -6',
        'eql x w',
        'eql x 0',
        'mul y 0',
        'add y 25',
        'mul y x',
        'add y 1',
        'mul z y',
        'mul y 0',
        'add y w',
        'add y 5',
        'mul y x',
        'add z y',
    ], [
        'inp w',
        'mul x 0',
        'add x z',
        'mod x 26',
        'div z 26',
        'add x -10',
        'eql x w',
        'eql x 0',
        'mul y 0',
        'add y 25',
        'mul y x',
        'add y 1',
        'mul z y',
        'mul y 0',
        'add y w',
        'add y 12',
        'mul y x',
        'add z y',
    ], [
        'inp w',
        'mul x 0',
        'add x z',
        'mod x 26',
        'div z 26',
        'add x -15',
        'eql x w',
        'eql x 0',
        'mul y 0',
        'add y 25',
        'mul y x',
        'add y 1',
        'mul z y',
        'mul y 0',
        'add y w',
        'add y 11',
        'mul y x',
        'add z y',
    ], [
        'inp w',
        'mul x 0',
        'add x z',
        'mod x 26',
        'div z 26',
        'add x -9',
        'eql x w',
        'eql x 0',
        'mul y 0',
        'add y 25',
        'mul y x',
        'add y 1',
        'mul z y',
        'mul y 0',
        'add y w',
        'add y 13',
        'mul y x',
        'add z y',
    ], [
        'inp w',
        'mul x 0',
        'add x z',
        'mod x 26',
        'div z 26',
        'add x 0',
        'eql x w',
        'eql x 0',
        'mul y 0',
        'add y 25',
        'mul y x',
        'add y 1',
        'mul z y',
        'mul y 0',
        'add y w',
        'add y 7',
        'mul y x',
        'add z y',
    ]
]

MODE_B = True

# model_number = 99999985841897
model_number = 99999893325755
model_number = 99999891830005
# 99999555600005
# 99999446000005
# 99999228950005
model_number = 99999166700005
model_number = 99998536200005
model_number = 99998535350005
model_number = 99998479000005
model_number = 99998464400005
model_number = 99997632950005

cache = []
for ix in range(14):
    cache.append({
        'input': '9',
        'vars': { 'w': 0, 'x': 0, 'y': 0, 'z': 0 },
    })


def calculate_mode_b(w, z, AA, BB, CC):
    x = (z % 26) + AA
    z = math.trunc(z / BB)
    # x = 0 if x == w else 1
    # z = z * (25 * x + 1)
    # y = (w + CC) * x
    # return z + y

    if x != w:
        z = 26 * z + w + CC
    return z

prev_time = time.time()

MODE_B_SETTINGS = [
    [11, 1, 6], # I had CC as 8 for a while...
    [11, 1, 12],
    [15, 1, 8],
    [-11, 26, 7],
    [15, 1, 7], # I had BB as 26 for a while
    [15, 1, 12],
    [14, 1, 2],
    [-7, 26, 15],
    [12, 1, 4],
    [-6, 26, 5],
    [-10, 26, 12],
    [-15, 26, 11],
    [-9, 26, 13],
    [0, 26, 7],
]

while model_number > 0:
    if model_number % 50000 == 5:
        print(f"Finished {model_number}: {time.time() - prev_time}")
        prev_time = time.time()

    model_str = str(model_number)
    if '0' in model_str:
        model_number -= 1
        continue

    vars = {
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
    }

    for ix in range(13):
        # print(f">>{' '*ix}{model_str[ix]}")
        if model_str[ix] == cache[ix]['input']:
            vars = cache[ix]['vars']
        else:
            if MODE_B:
                # if ix == 0:
                #     vals = [11, 1, 6] # I had CC as 8 for a while...
                # elif ix == 1:
                #     vals = [11, 1, 12]
                # elif ix == 2:
                #     vals = [15, 1, 8]
                # elif ix == 3:
                #     vals = [-11, 26, 7]
                # elif ix == 4:
                #     vals = [15, 26, 7]
                # elif ix == 5:
                #     vals = [15, 1, 12]
                # elif ix == 6:
                #     vals = [14, 1, 2]
                # elif ix == 7:
                #     vals = [-7, 26, 15]
                # elif ix == 8:
                #     vals = [12, 1, 4]
                # elif ix == 9:
                #     vals = [-6, 26, 5]
                # elif ix == 10:
                #     vals = [-10, 26, 12]
                # elif ix == 11:
                #     vals = [-15, 26, 11]
                # elif ix == 12:
                #     vals = [-9, 26, 13]
                # elif ix == 13:
                #     vals = [0, 26, 7]

                vars['z'] = calculate_mode_b(
                    int(model_str[ix]),
                    vars['z'],
                    *MODE_B_SETTINGS[ix]
                )
            else:
                vars = alu.alu(monad[ix], model_str[ix], vars)

            # Save this state for future runs
            cache[ix]['input'] = model_str[ix]
            cache[ix]['vars'] = vars

    result = alu.alu(monad[13], model_str[13], vars)

    if result['z'] == 0:
        print(f"Model number validated: {model_number}")
        break

    model_number -= 1
