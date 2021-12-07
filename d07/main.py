import numpy as np

file = open("input.txt", "r")
lines = file.readlines()
data = np.array(list(map(int, lines[0].strip().split(","))))
file.close()


def modified_fuel_intake(x):
    return 0.5 * x * (x + 1)


# Part one solution 
median = np.median(data)
print(np.sum(np.abs(data - median)))

# Part two solution
optimal_floor, optimal_ceil = np.floor(data.mean()), np.ceil(data.mean())
dist_floor, dist_ceil = np.abs(data - optimal_floor), np.abs(data - optimal_ceil)
weighted_floor, weighted_ceil = (np.sum(modified_fuel_intake(dist_floor)),
                                 np.sum(modified_fuel_intake(dist_ceil)))
print(np.min([weighted_floor, weighted_ceil]))
