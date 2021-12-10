file_name = "input.txt"
with open(file_name, "r") as file:
    lines = file.readlines()

char_map = {"(": ")", "[": "]", "{": "}", "<": ">"}
error_table = {")": 3, "]": 57, "}": 1197, ">": 25137}

points = 0
for line in lines:
    line = line.strip()
    matches = []
    for i in line:
        if (i in char_map):
            matches.append(char_map[i])
        elif (i == matches[-1]):
            matches.pop()
        else:
            points += error_table[i]
            break
print(points)

point_table = {")": 1, "]": 2, "}": 3, ">": 4}
total = []

for line in lines:
    line = line.strip()
    matches = []
    corrupt = False
    for i in line:
        if (i in char_map):
            matches.append(char_map[i])
        elif (i == matches[-1]):
            matches.pop()
        else:
            corrupt = True
            break
    if (not corrupt):
        points = 0
        for i in matches[::-1]:
            points *= 5
            points += point_table[i]
        total.append(points)
total = sorted(total)
print(total[len(total) // 2])
