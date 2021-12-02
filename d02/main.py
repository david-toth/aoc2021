def parse_input(filename):
    file = open(filename, "r")
    lines = file.readlines()
    data = [l.strip().split(" ") for l in lines]
    data = [[i[0], int(i[1])] for i in data]
    file.close()
    return data

positions = parse_input("input.txt")

#------- Part 1
horizontal = 0
depth = 0
for i in positions:
    if (i[0] == "up"):
        depth -= i[1]
    elif (i[0] == "down"):
        depth += i[1]
    else:
        horizontal += i[1]

print(horizontal * depth)

#--------- Part 2
horizontal = 0
aim = 0
depth = 0
for i in positions:
    if (i[0] == "up"):
        aim -= i[1]
    elif (i[0] == "down"):
        aim += i[1]
    else:
        horizontal += i[1]
        depth += i[1] * aim

print(horizontal * depth)
