import itertools

with open("input.txt", "r") as file:
    lines = file.readlines()
    data = []
    for line in lines:
        x, y = line.strip().split(" | ")
        data.append([x.split(), y.split()])

# Part 1
count = 0
for i in data:
    for j in i[1]:
        if (len(j) in [2, 3, 4, 7]):
            count += 1
print(count)


def decode(x):
    m = {}
    v = [10] * 10
    # Find 1's, 7's, 4's, and 8's
    for i, j in enumerate(x):
        if len(j) == 2:
            v[i] = 1
            m[1] = j
        elif len(j) == 3:
            v[i] = 7
            m[7] = j
        elif len(j) == 4:
            v[i] = 4
            m[4] = j
        elif len(j) == 7:
            v[i] = 8
            m[8] = j
        else:
            continue
    # Find the rest
    for i, j in enumerate(x):
        if v[i] != 10:
            continue
        if len(j) == 5:
            if len(set(m[1]) ^ set(j)) == 3:
                v[i] = 3
                m[3] = j
            elif len(set(m[4]) ^ set(j)) == 5:
                v[i] = 2
                m[2] = j
            else:
                v[i] = 5
                m[5] = j
        else:
            if len(set(m[1]) ^ set(j)) == 6:
                v[i] = 6
                m[6] = j
            elif len(set(m[4]) ^ set(j)) == 4:
                v[i] = 0
                m[0] = j
            else:
                v[i] = 9
                m[9] = j
    return v, m


def get_numbers(x, mapping):
    d = ""
    for i in x:
        for k, v in mapping.items():
            if set(i) == set(k):
                d += str(v)
                break
    return int(d)


# Part 2
count = 0
for i in data:
    v, m = decode(i[0])
    reversed_map = {v: k for k, v in m.items()}
    count += get_numbers(i[1], reversed_map)
print(count)
