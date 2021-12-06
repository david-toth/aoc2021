from collections import Counter, defaultdict

file = open("input.txt", "r")
lines = file.readlines()
file.close()
data = list(map(int, lines[0].strip().split(",")))


def count_fish(initial_state, days):
    copy_state = Counter(initial_state)
    for day in range(days):
        tmp_count = defaultdict(int)
        for i, j in copy_state.items():
            if (i == 0):
                tmp_count[6] += j
                tmp_count[8] += j
            else:
                tmp_count[i - 1] += j
        copy_state = tmp_count
    return sum(copy_state.values())


print(count_fish(data, 80))
print(count_fish(data, 256))
