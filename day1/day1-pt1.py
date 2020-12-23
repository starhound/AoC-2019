import math

file = open('day1.txt', 'r')

fuel = []

for line in file:
    mass = int(line.strip())
    first_step = mass / 3
    second_step = math.floor(first_step)
    required_fuel = second_step - 2
    fuel.append(required_fuel)

print(sum(fuel))
