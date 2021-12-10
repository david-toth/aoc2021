from collections import deque

with open("input.txt", "r") as file:
    lines = file.readlines()
    data = [[int(i) for i in line.strip()] for line in lines]

up = (1, 0)
down = (-1, 0)
left = (0, -1)
right = (0, 1)

total = 0
nrows = len(data)
ncols = len(data[0])

for row in range(nrows):
    for col in range(ncols):
        neighbors = []
        for i, j in [up, down, left, right]:
            ii = row + i
            jj = col + j
            if (0 <= ii < nrows) and (0 <= jj < ncols):
                neighbors.append(data[ii][jj])
        point = data[row][col]
        if (point < min(neighbors)):
            total += point + 1
print(total)

basin_sizes = []
covered = set()
for row in range(nrows):
    for col in range(ncols):
        if ((row, col) not in covered) and (data[row][col] != 9):
            size = 0
            queue = deque()
            queue.append((row, col))
            while queue:
                (row, col) = queue.popleft()
                if (row, col) in covered:
                    continue
                covered.add((row, col))
                size += 1
                for i, j in [up, down, left, right]:
                    ii = row + i
                    jj = col + j
                    if ((0 <= ii < nrows) and (0 <= jj < ncols) and
                        (data[ii][jj] != 9)):
                        queue.append((ii, jj))
            basin_sizes.append(size)
basin_sizes = sorted(basin_sizes)
total = 1
for i in basin_sizes[-3:]:
    total *= i
print(total)
