#! /usr/bin/env python3

#import argparse

#parser = argparse.ArgumentParser()
#parser.add_argument('filename', help='The input file')

#args = parser.parse_args()

#filename = 'demo-09.txt'
filename = 'input-09.txt'

with open(filename) as file:
    lines = file.readlines()
    lines = [[int(x) for x in list(line.rstrip())] for line in lines]

num_rows = len(lines)
num_cols = len(lines[0])

for line in lines:
    print(line)

low_points = []

diffs = [
    #(-1, -1),
    (-1, 0),
    #(-1, 1),
    (0, -1),
    #(0, 0),
    (0, 1),
    #(1, -1),
    (1, 0),
    #(1, 1)
]

risk_level_sum = 0

low_coords = []

for row,line in enumerate(lines):
    low_points.append([True] * num_cols)

    for col,cell in enumerate(line):
        for diff in diffs:
            x = col + diff[0]
            y = row + diff[1]
            if x >= 0 and x < num_cols and y >= 0 and y < num_rows:
                if lines[y][x] <= cell:
                    low_points[row][col] = False

        if low_points[row][col]:
            low_coords.append((col, row))
            risk_level = cell + 1
            print(f"risk level ({col}, {row}): {risk_level}")
            risk_level_sum += risk_level


print(low_coords)

print()
print(f"The total risk level is {risk_level_sum}")


# Part 2

print()
print("== Part 2 ==")
basins = {}
counts = []

basin_map = []
for x in range(num_rows):
    basin_map.append(['-'] * num_cols)

def check_basin(point, name):
    x, y = point
    # out of bounds
    if x < 0 or x >= num_cols or y < 0 or y >= num_rows:
        return 0, []
    # mountain ridges
    if lines[y][x] == 9:
        return 0, []
    # already in another basin
    if basin_map[y][x] != '-':
        return 0, []
    # add to this basin
    basin_map[y][x] = name
    count = 1
    cells = [point]
    for diff in diffs:
        new_count, new_cells = check_basin((x+diff[0], y+diff[1]), name)
        count += new_count
        cells += new_cells
    return count, cells

for ix, lowpoint in enumerate(low_coords):
    name = chr(65+ix)    
    basin_count, basin_cells = check_basin(lowpoint, name)
    
    basins[lowpoint] = {
        'center': lowpoint,
        'count': basin_count,
        'cells': basin_cells
    }
    counts.append(basin_count)

counts.sort(reverse=True)
a, b, c, *rest = counts

print(f"Multiplication of basin sizes: {a * b * c}")
