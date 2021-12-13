import numpy as np

data = []
folds = []
filename = "input.txt"
for line in open(filename, "r"):
    line = line.strip()
    if line.startswith("fold"):
        axis, value = line[11:].split("=")
        folds.append((axis, int(value)))
    elif line != "":
        data.append(tuple(map(int, line.split(","))))
    else:
        continue

nrows = max(i[1] for i in data) + 1
ncols = max(i[0] for i in data) + 1
grid = np.zeros((nrows, ncols))
for i, j in data:
    grid[j, i] += 1


def fold(x, axis, pos):
    if (axis == "x"):
        left, right = x[:, :pos], x[:, pos+1:]
        right = np.flip(right, 1)
        if left.shape[1] == right.shape[1]:
            return left + right
        elif left.shape[1] > right.shape[1]:
            diff = left.shape[1] - right.shape[1]
            right = np.concatenate((right, np.zeros((left.shape[0], diff))))
            return left + right
        else:
            diff = right.shape[1] - left.shape[1]
            return left  + right[:, diff:]
    else:
        top, bottom = x[:pos, :], x[pos+1:, :]
        bottom = np.flip(bottom, 0)
        if top.shape[0] == bottom.shape[0]:
            return top + bottom
        elif top.shape[0] > bottom.shape[0]:
            diff = top.shape[0] - bottom.shape[0]
            bottom = np.concatenate((bottom, np.zeros((diff, top.shape[1]))))
            return top + bottom
        else:
            diff = bottom.shape[0] - top.shape[0]
            return top + bottom[diff:, :]


# Part one
print(np.sum(fold(grid, folds[0][0], folds[0][1]).flatten() != 0))

# Part two
for i in folds:
    grid = fold(grid, i[0], i[1])

letters = [["."] * grid.shape[1] for i in range(grid.shape[0])]
for i in range(len(grid)):
    for j in range(len(grid[i])):
        letters[i][j] = "#" if grid[i, j] != 0 else "."
print(*(' '.join(row) for row in letters), sep='\n')
