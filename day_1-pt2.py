import numpy as np

file = open('day1.txt', 'r')

fuel = 0
input = file.readlines()
for line in input:
    new_fuel = int(line)
    while True:
        new_fuel = np.floor(new_fuel / 3) - 2
        if new_fuel > 0:
            fuel += new_fuel
        else:
            break

print(fuel)
