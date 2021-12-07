import numpy as np

file = open("input.txt", "r")
lines = file.readlines()
data = np.array(list(map(int, lines[0].strip().split(","))))
file.close()


def absolute_distance(x_array, target):
    return np.sum(np.abs(x_array - target))


def modified_fuel_intake(x):
    return 0.5 * x * (x + 1)


# Part one solution 
median = np.median(data)
print(absolute_distance(data, median))

# Part two solution
min_fuel = int(1e9)
for i in range(data.max() + 1):
    distance = np.abs(data - i)
    weighted_dist = np.sum(modified_fuel_intake(distance))
    if weighted_dist < min_fuel:
        min_fuel = weighted_dist
print(min_fuel)
