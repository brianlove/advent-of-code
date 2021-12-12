
#filename = 'demo-12.txt'
#filename = 'demo-12c.txt'
filename = 'input-12.txt'

DEBUG = False

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip().split('-') for line in lines]

doors = {}
paths = []

for start, end in lines:
    if start in doors:
        doors[start].append(end)
    else:
        doors[start] = [end]
    if end in doors:
        doors[end].append(start)
    else:
        doors[end] = [start]


if DEBUG:
    for cave in doors:
        print(f"{cave} -> {doors[cave]}")
    print()
    print()


# return: a full path to the end, if possible, otherwise false??
def check_path(room, so_far, indent):
    this_path = so_far[:]
    this_path.append(room)
    if DEBUG:
        print(f"{'  '*indent}Checking: '{room}', This path: {this_path}")

    solutions = []
    for dest in doors[room]:
        if dest == 'end':
            solution = this_path[:]
            solution.append(dest)
            solutions.append(solution)
            if DEBUG:
                print(f"{'  '*indent}- found solution '{dest}', Path: {solution}")
        elif dest[0].islower() and dest in so_far:
            if DEBUG:
                print(f"{'  '*indent}- '{dest}' = dup")
            continue
        else:
            if DEBUG:
                print(f"{'  '*indent}- '{dest}' = new cave")
            next_solutions = check_path(dest, this_path, indent+1)
            if len(next_solutions):
                solutions += next_solutions

    if DEBUG:
        print(f"{'  '*indent} Room '{room}' :: {solutions}")
    return solutions

result = check_path('start', [], 0)

print()
print(f"Part 1 result: {len(result)} paths found")
#for entry in result:
#    print(entry)

