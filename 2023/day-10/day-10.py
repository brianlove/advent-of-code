#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser("Day 10")
parser.add_argument("infile", help="The input file")
args = parser.parse_args()

import collections

class Queue:
    def __init__(self):
        self.elements = collections.deque()
    
    def empty(self) -> bool:
        return not self.elements
    
    def put(self, x):
        self.elements.append(x)
    
    def get(self):
        return self.elements.popleft()



PIPES = {
    "|": [(0, -1), (0, 1)],
    "-": [(-1, 0), (1, 0)],
    "L": [(0, -1), (1, 0)],
    "J": [(0, -1), (-1, 0)],
    "7": [(-1, 0), (0, 1)],
    "F": [(1, 0), (0, 1)],
    "S": [],
}

ADJ = [
    (0, -1), (-1, 0), (1, 0), (0, 1)
    # (-1, -1), (0, -1), (1, -1),
    # (-1,  0),          (1,  0),
    # (-1,  1), (0,  1), (1,  1),
]


def part1(lines):
    print("\n\n~~ PART 1~~")

    puzzle = [[c for c in list(line)] for line in lines]

    start_coords = None

    for r, row in enumerate(puzzle):
        # print(row)
        for c, col in enumerate(row):
            if puzzle[r][c] == 'S':
                start_coords = (c, r)

    print()
    print("Start coords:", start_coords)

    ## Search
    frontier = Queue()
    frontier.put(start_coords)
    record = dict()
    record[start_coords] = { "came_from": None, "distance": 0 }

    while not frontier.empty():
        current = frontier.get()
        curr_c, curr_r = current
        cell = puzzle[curr_r][curr_c]
        # print("Current:", current, cell)

        if cell == 'S':
            for adj in ADJ:
                adj_coords = (curr_c + adj[0], curr_r + adj[1])
                other = puzzle[adj_coords[1]][adj_coords[0]]
                # print(adj_coords, other)
                if other in PIPES:
                    for connection in PIPES[other]:
                        connection_difference = tuple(sum(x) for x in zip(adj, connection))
                        # print("  -", connection, "=>", connection_difference)
                        if connection_difference == (0, 0):
                            PIPES["S"].append(adj)
                            # pass
        # print("PIPES:", PIPES)
        # print()

        # for next in puzzle[curr_r][curr_c]
        if cell in PIPES:
            connections = PIPES[cell]
            for connection in connections:
                # print(current, "->", connection)
                next_coord = tuple(sum(x) for x in zip(current, connection))
                # print("  checking:", next_coord)

                # if next_coord 
                if next_coord in record:
                    pass
                else:
                    frontier.put(next_coord)
                    record[next_coord] = {
                        "came_from": current,
                        "distance": record[current]["distance"] + 1
                    }

    longest_distance = 0
    print()
    print("Record:")
    for entry in record:
        # print(entry, record[entry]["distance"])
        if record[entry]["distance"] > longest_distance:
            longest_distance = record[entry]["distance"]

    print()
    print("Longest distatnce:", longest_distance)


def part2(lines):
    print("\n\n~~ PART 2~~")
    pass


with open(args.infile) as file:
    lines = [line.rstrip() for line in file.readlines()]
    part1(lines)

    # part2(lines)
