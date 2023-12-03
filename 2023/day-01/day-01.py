#! /usr/bin/python3

import argparse


parser = argparse.ArgumentParser("Day 1")
parser.add_argument("infile", help="The input file")


args = parser.parse_args()


def extract_digits(line):
    digits = []
    for ch in line:
        try:
            x = int(ch)
            digits.append(x)
        except:
            continue
    return digits


def part1(lines):
    print("\n\n~~ PART 1~~")
    sum = 0
    for line in lines:
        stripped = line.rstrip()
        digits = extract_digits(stripped)
        # print("> ", stripped, "-->", digits)
        line_sum = 10 * digits[0] + digits[-1]
        # print("   >", line_sum)
        sum += line_sum
    print("Final total:", sum)

DIGITS = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

DIGITS_MAP = {
    "eight": "8",
    "two": "2",
    # "zero": "0",
    "one": "1",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "nine": "9",
}

# def part2(lines):
#     print("\n\n~~ PART 2~~")

#     sum = 0
#     for l in lines:
#         l = "7mhjsq7ninetwo3tbnkglngltwo"
#         line = l.rstrip()
#         # line = "ggdone3nbmsthreefourninefiveoneightpr"
#         # line = "7mhjsq7ninetwo3tbnkglngltwo"
#         # print("> line:", line)
#         # for digit in DIGITS_MAP:
#         #     line = line.replace(digit, DIGITS_MAP[digit])
#         #     # print("    ", line)

#         replaced_digit = False
#         ix = 0
#         while ix < len(line) and not replaced_digit:
#             try:
#                 int(line[ix])
#                 break;
#             except:
#                 pass
#             # print("ix=", ix)
#             for digit in DIGITS_MAP:
#                 # print(" digit:", digit)
#                 if line.startswith(digit, ix):
#                     line = line.replace(digit, DIGITS_MAP[digit], 1)
#                     # print("  REPLACED:", line)
#                     replaced_digit = True
#                     break
#                 # print("  line:", line)
#             ix += 1
#         # break

#         # print("Working backwards:", line)
#         replaced_digit = False
#         ix = len(line) - 1
#         # print(line, ix)
#         while ix >= 0 and not replaced_digit:
#             print("ix:", ix, line[ix:])
#             try:
#                 int(line[ix])
#                 break;
#             except:
#                 pass
#             for digit in DIGITS_MAP:
#                 if line.startswith(digit, ix):
#                     line = line.replace(digit, DIGITS_MAP[digit])
#                     print("   REPLACED!", line)
#                     replaced_digit = True
#                     break
#             ix -= 1
#             # break;

#         digits = extract_digits(line)
#         # print("  ", digits)
#         line_sum = 10 * digits[0] + digits[-1]
#         sum += line_sum

#         print(" ", l, " --> ", digits)
#         break

#     print("Final total:", sum)


def part2_alt(lines):
    print("\n\n~~ PART 2 (alt)~~")

    sum = 0
    for l in lines:
        line = l.rstrip()

        first_digit = None
        for ix in range(len(line)):
            if line[ix] in DIGITS:
                first_digit = int(line[ix])
                break
            else:
                for digit in DIGITS_MAP:
                    if line.startswith(digit, ix):
                        first_digit = int(DIGITS_MAP[digit])
                        break
            if first_digit is not None:
                break
        
        # print(">", line, "-->", first_digit)

        last_digit = None
        for ix in range(len(line)-1, -1, -1):
            if line[ix] in DIGITS:
                last_digit = int(line[ix])
                break
            else:
                for digit in DIGITS_MAP:
                    if line.startswith(digit, ix):
                        last_digit = int(DIGITS_MAP[digit])
                        break
            if last_digit is not None:
                break
        # print("  >", line, "-->", last_digit)

        # print(line, " : ", first_digit, " ", last_digit)
        line_sum = first_digit * 10 + last_digit
        sum += line_sum

    print("Final total:", sum)



with open(args.infile) as file:
    lines = file.readlines()
    part1(lines)

    # part2(lines)
    part2_alt(lines)


