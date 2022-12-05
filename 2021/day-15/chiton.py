#! /usr/bin/env python3

import argparse
import operator
import sys
import time

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='The input file')
parser.add_argument('-D', '--debug', action='store_true')
parser.add_argument('--part-two', action='store_true', help='Should we run part 2?')

args = parser.parse_args()

INFINITY = sys.maxsize

START = (0, 0)

DIFFS = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]

REPETITIONS = 5 if args.part_two else 1

with open(args.filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

core_height = len(lines)
height = core_height * REPETITIONS
core_width = len(lines[0])
width = core_width * REPETITIONS
print(f"Total nodes: {width * height}")

DESTINATION = (width - 1, height - 1)

risk_levels = [[int(x) for x in list(line)] for line in lines]
if args.debug:
    print("Risk levels:")
    for line in risk_levels:
        print(line)
    print()


def get_risk_level(node):
    x, y = node

    # Which x/y coordinates do the coordinates that we have map to in the
    # orignal map? 
    core_x = x % core_width
    core_y = y % core_height

    raw_risk = risk_levels[core_y][core_x]

    # Each time we repeat the core grid, the risk levels change a bit.  Figure
    # out how much we need to adjust the levels.
    repetition_x = x // core_width
    repetition_y = y // core_height

    # The adjustment factor increases in both the X and Y directions
    risk_adjustment = repetition_x + repetition_y

    # Risk levels go from 1 to 9 (no zero).  So, it's really a Base-9 system,
    # with the digits shifted.
    return ((raw_risk - 1 + risk_adjustment) % 9) + 1


if args.debug:
    print("Risk levels:")
    for y in range(height):
        for x in range(width):
            print(get_risk_level((x, y)), end='')
        print()
    print()

# The input can be viewed as a graph where the distance from one node (cell) to
# another is the value of the second cell.

# The best-known cost to get to a given node from the start node
shortest_path = {}

for y in range(height):
    for x in range(width):
        shortest_path[(x, y)] = INFINITY
shortest_path[START] = 0

unvisited_nodes = set(shortest_path.keys())

nodes_we_have_looked_at = set([START])


# The best route to get to a given node
previous_nodes = {}

count = 0

start_time = time.time()

while unvisited_nodes:
    smallest_node = None

    # When we start out, only one node (START) has a distance value other than
    # the placeholder.  As we visit nodes, those other nodes (with placeholder
    # values) will begin to get real distances.  Keep track of those and add
    # them as we go to `nodes_we_have_looked_at` to keep access times more
    # reasonable.
    if count < 0.6 * width * height:
        for node in nodes_we_have_looked_at:
            if node not in unvisited_nodes:
                continue
            if smallest_node is None:
                smallest_node = node
            elif shortest_path[node] < shortest_path[smallest_node]:
                smallest_node = node
    else:
        for node in unvisited_nodes:
            if smallest_node is None:
                smallest_node = node
            elif shortest_path[node] < shortest_path[smallest_node]:
                smallest_node = node
    if args.debug:
        print("Smallest node:", smallest_node)

    current_node = smallest_node

    for diff in DIFFS:
        neighbor = tuple(map(operator.add, current_node, diff))

        if neighbor[0] < 0 or neighbor[0] >= width or neighbor[1] < 0 or neighbor[1] >= height:
            continue

        tentative_value = shortest_path[current_node] + get_risk_level(neighbor)
        if tentative_value < shortest_path[neighbor]:
            nodes_we_have_looked_at.add(neighbor)
            shortest_path[neighbor] = tentative_value
            previous_nodes[neighbor] = current_node

        if args.debug:
            print(f"  Neighbor: {neighbor}")
            print(f"    tentative: {tentative_value}")
            print(f"  Updated neighbor: {neighbor}, Shortest path: {shortest_path[neighbor]}, previous node: {previous_nodes[neighbor]}")

    unvisited_nodes.remove(current_node)

    if args.debug:
        print()

    count += 1

    if count % 2000 == 0:
        print(f"Finished node {count}: {time.time() - start_time}")
        start_time = time.time()

print(f"Finished node {count}")

print(f"Destination node: {DESTINATION}")
print(f"Shortest path to destination: {shortest_path[DESTINATION]}")
print()

# Get a list of the nodes that we took to get to DESTINATION
previous = DESTINATION
path = [previous]
while previous != START:
    previous = previous_nodes[previous]
    path.append(previous)
path.reverse()

# print("Map:")
# for y in range(height):
#     for x in range(width):
#         if (x, y) in path:
#             print('X', end='')
#         else:
#             print('-', end='')
#     print()
