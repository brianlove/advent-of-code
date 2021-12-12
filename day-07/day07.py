
#filename = 'demo-07.txt'
filename = 'input-07.txt'

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

positions = [int(x) for x in lines[0].split(',')]


# Part 1

min_fuel = None
min_loc = None

for location in range(min(positions), max(positions)):
    fuel = 0
    for crab in positions:
        fuel += abs(crab - location)
    #print(f"location {location}: {fuel} used")
    
    if min_loc is None or min_fuel > fuel:
        min_loc = location
        min_fuel = fuel

print("Part 1")
print(f"The minimum cost position is {min_loc} with a fuel cost of {min_fuel}")


# Part 2

costs = [0] * (max(positions)+1)
for ix, pos in enumerate(costs):
    costs[ix] = sum(range(1, ix+1))

def calculate_fuel(start, end):
    distance = abs(crab - location)
    return costs[distance]

min_fuel = None
min_loc = None

for location in range(min(positions), max(positions)):
    fuel = 0
    for crab in positions:
        fuel += calculate_fuel(crab, location)
    #print(f"location {location}: {fuel} used")
    
    if min_loc is None or min_fuel > fuel:
        min_loc = location
        min_fuel = fuel

print("Part 2")
print(f"The minimum cost position is {min_loc} with a fuel cost of {min_fuel}")
