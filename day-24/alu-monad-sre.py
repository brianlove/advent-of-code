#! /usr/bin/env python3

import argparse

import alu

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='The input file')
parser.add_argument('-D', '--debug', action='store_true')

args = parser.parse_args()

with open(args.filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
monad = lines

C_D = [(4, 1), (5, 2), (6, 3), (7, 4), (8, 5), (9, 6)]
G_H = [(6, 1), (7, 2), (8, 3), (9, 4)]
I_J = [(3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6), (9, 7)]
F_K = [(1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8), (7, 9)]
E_L = [(9, 1)]
B_M = [(1, 4), (2, 5), (3, 6), (4, 7), (5, 8), (6, 9)]
A_N = [(1, 7), (2, 8), (3, 9)]

valid_model_numbers = []

for cd_entry in C_D:
    c, d = cd_entry
    for gh_entry in G_H:
        g, h = gh_entry
        for ij_entry in I_J:
            i, j = ij_entry
            for fk_entry in F_K:
                f, k = fk_entry
                for el_entry in E_L:
                    e, l = el_entry
                    for bm_entry in B_M:
                        b, m = bm_entry
                        for an_entry in A_N:
                            a, n = an_entry

                            model_number = [a, b, c, d, e, f, g, h, i, j, k, l, m, n]
                            model_str = ''.join(map(str, model_number))

                            result = alu.alu(monad, model_number)

                            if result['z'] == 0:
                                valid_model_numbers.append(int(model_str))
                                # print(f"{model_str}: {result}")


valid_model_numbers.sort(reverse=True)
largest_model_number = valid_model_numbers[0]
smallest_model_number = valid_model_numbers[-1]

print(f"There are {len(valid_model_numbers)} valid model numbers")
print(f"The largest valid model number is {largest_model_number}")
print(f"The smallest valid model number is {smallest_model_number}")
