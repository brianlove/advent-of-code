#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='The input file')
parser.add_argument('-D', '--debug', action='store_true')

args = parser.parse_args()

PART_1 = True

with open(args.filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

algorithm = lines[0]
map_from_zeros = '1' if algorithm[0] == '#' else '0'
map_from_ones = '1' if algorithm[-1] == '#' else '0'

DIFFS = [
    (-1, -1),
    ( 0, -1),
    ( 1, -1),
    (-1,  0),
    ( 0,  0),
    ( 1,  0),
    (-1,  1),
    ( 0,  1),
    ( 1,  1),
]

DISPLAY = {
    0:   '.',
    '0': '.',
    1:   '#',
    '1': '#'
}


def print_image(image):
    for row in image:
        for cell in row:
            print(DISPLAY[cell[-1]], end='')
        print()


# After each round of enhancement, one more pixel (in each direction) has the
# potential to have a non-zero value, so we need to give enough space for those
# new values.
ENHANCEMENTS = 50
orig_width = len(lines[2])
new_width = orig_width + 2 * ENHANCEMENTS

# The individual cells of the image array contain a list of the values of the
# cell over time, so that we can both add the next step's enhancements while
# still being able to reference the previous step's values.
image = []
for row in range(ENHANCEMENTS):
    new_row = []
    for x in range(new_width):
        new_row.append(['0'])
    image.append(new_row)
for line in lines[2:]:
    row = [['0'] if ch == '.' else ['1'] for ch in list(line)]
    new_row = []
    for x in range(ENHANCEMENTS):
        new_row.append(['0'])
    new_row.extend(row)
    for x in range(ENHANCEMENTS):
        new_row.append(['0'])
    image.append(new_row)
for row in range(ENHANCEMENTS):
    new_row = []
    for x in range(new_width):
        new_row.append(['0'])
    image.append(new_row)

print("Step 0")
print_image(image)
print()

null_space_value = '0'

for step in range(1, ENHANCEMENTS+1):
    print(f"Step {step}")

    lit_pixels = 0

    for row_ix, row in enumerate(image):
        for cell_ix, cell in enumerate(row):
            if args.debug:
                print(f"Cell {(cell_ix, row_ix)}:")
            val = ''
            for diff in DIFFS:
                if args.debug:
                    print(f"  diff: {diff}  ", end='')
                x = cell_ix + diff[0]
                y = row_ix + diff[1]
                if args.debug:
                    print(f"x={x}, y={y}")
                    print(f"    len(row): {len(row)}, {row}")
                if y < 0 or y >= len(image) or x < 0 or x >= len(row):
                    val += null_space_value
                else:
                    if args.debug:
                        print(f"    y={y}, x={x}, step={step-1}")
                    val += image[y][x][step-1]
            if args.debug:
                print(f"  Cell {(cell_ix, row_ix)}: val={val}")
            index = int(val, 2)
            new_val = '1' if algorithm[index] == '#' else '0'
            if new_val == '1':
                lit_pixels += 1
            image[row_ix][cell_ix].append(new_val)
    
    if null_space_value == '0':
        null_space_value = map_from_zeros
    else:
        null_space_value = map_from_ones

    if step % 10 == 0:
        print_image(image)
        print()
        print(f"  There are {lit_pixels} lit pixels")
        print()
        print()


print_image(image)
print()
print(f"  There are {lit_pixels} lit pixels")







