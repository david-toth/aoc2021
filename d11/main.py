def load_data():
    with open("input.txt", "r") as file:
        lines = file.readlines()
        x = [[int(i) for i in line.strip()] for line in lines]
    return x

neighbors = [
    (1, 0), (-1, 0),
    (0, 1), (0, -1),
    (1, 1), (1, -1),
    (-1, 1), (-1, -1)
]


def increment(x):
    for i in range(len(x)):
        for j in range(len(x[i])):
            x[i][j] += 1
    return


def check_flashes(x):
    flashes = 0
    for i in range(len(x)):
        for j in range(len(x[i])):
            if (x[i][j] == 0):
                flashes += 1
    return flashes


def increment_neighbors(x):
    for i in range(len(x)):
        for j in range(len(x[i])):
            if (x[i][j] > 9):
                for ii, jj in neighbors:
                    iii = i + ii
                    jjj = j + jj
                    if (0 <= iii < len(x) and 0 <= jjj < len(x[i])):
                        if (0 < x[iii][jjj] <= 9):
                            x[iii][jjj] += 1
                x[i][j] = 0
    return


# Part 1
data = load_data()
total = 0
for i in range(100):
    increment(data)
    while True:
        increment_neighbors(data)
        if not any(v > 9 for r in data for v in r):
            break
    total += check_flashes(data)
print(total)
# Part 2
data = load_data()
it = 1
while True:
    increment(data)
    while True:
        increment_neighbors(data)
        if not any(v > 9 for r in data for v in r):
            break
    if all(v == 0 for r in data for v in r):
        print(it)
        break
    it += 1
