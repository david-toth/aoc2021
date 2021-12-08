import itertools

with open("input.txt", "r") as file:
    lines = file.readlines()

# Part 1 - EZ
count = 0
for line in lines:
    start, end = line.split(" | ")
    for s in end.split():
        if (len(s) in [2, 3, 4, 7]):
            count += 1
print(count)

# Part 2 - RIP
count = 0
orig_signals = [
    "abcefg", "cf", "acdeg", "acdfg",
    "bcdf", "abdfg", "abdefg",
    "acf", "abcdefg", "abcdfg"
]
orig_set = set(orig_signals)
for line in lines:
    start, end = line.split(" | ")
    for p in itertools.permutations("abcdefg"):
        x = {i: j for i, j in zip(p, "abcdefg")}
        y = set("".join(sorted(map(x.get, s))) for s in start.split())
        if y == orig_set:
            output = ["".join(sorted(map(x.get, s))) for s in end.split()]
            output = "".join(str(orig_signals.index(s)) for s in output)
            count += int(output)
print(count)
