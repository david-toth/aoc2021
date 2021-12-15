import numpy as np
import heapq


def load_data(file):
    with open(file, "r") as f:
        data = []
        for line in f:
            line = list(line.strip())
            data.append(list(map(int, line)))
    return data


def extend_grid(data):
    data = np.array(data)
    dc = data.copy()
    for i in range(4):
        x = np.mod(dc, 9) + 1
        data = np.hstack((data, x))
        dc = x

    dc = data.copy()
    for i in range(4):
        x = np.mod(dc, 9) + 1
        data = np.vstack((data, x))
        dc = x
    return data.tolist()


def solve(data):
    paths = [(0, 0, 0)] # risk, x, y
    visited = set()
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while True:
        r, x, y = heapq.heappop(paths)
        if (x, y) in visited:
            continue
        if (x == len(data) - 1) and (y == len(data[x]) - 1):
            return r
        visited.add((x, y))
        for i, j in directions:
            xi = x + i
            yj = y + j
            if not (0 <= xi < len(data) and 0 <= yj < len(data[0])):
                continue
            if (xi, yj) in visited:
                continue
            heapq.heappush(paths, (r + data[xi][yj], xi, yj))
            

in1 = load_data("input.txt")
in2 = extend_grid(in1)
print(solve(in1))
print(solve(in2))
