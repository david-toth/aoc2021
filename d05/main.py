import numpy as np

file = open("input.txt", "r")
lines = file.readlines()
file.close()
data = []
for line in lines:
    line = line.replace("->", "").strip().split("  ")
    x1_y1 = list(map(int, line[0].split(",")))
    x2_y2 = list(map(int, line[1].split(",")))
    data.append([x1_y1, x2_y2])

x_max = np.array(data)[:, :, 0].max()
y_max = np.array(data)[:, :, 1].max()


def find_straight_lines(input_data):
    grid = np.zeros((x_max + 1, y_max + 1))
    for pair in input_data:
        x_vals = (pair[0][0], pair[1][0])
        y_vals = (pair[0][1], pair[1][1])
        x0, x1 = min(x_vals), max(x_vals)
        y0, y1 = min(y_vals), max(y_vals)
        if x0 == x1:
            grid[y0:y1 + 1, x0] += 1
        elif y0 == y1:
            grid[y0, x0:x1 + 1] += 1
        else:
            continue
    return grid


def find_diagonal_lines(input_data):
    grid = np.zeros((x_max + 1, y_max + 1))
    for pair in input_data:
        x0, x1 = (pair[0][0], pair[1][0])
        y0, y1 = (pair[0][1], pair[1][1])
        if (x0 != x1) and (y0 != y1):
            slope = (y1 - y0) / (x1 - x0)
            intercept = y0 - slope * x0
            if x0 > x1:
                x0, x1 = x1, x0
            for i in range(x0, x1 + 1):
                y = slope * i + intercept
                grid[int(y), i] += 1
    return grid


straight = find_straight_lines(data)
print(np.sum(straight >= 2))
diagonal = find_diagonal_lines(data)
combined = straight + diagonal
print(np.sum(combined >= 2))
