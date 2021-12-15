from collections import Counter, defaultdict

with open("input.txt", "r") as f:
    lines = list(map(str.strip, f.readlines()))
    template = lines[0]
    rules = {}
    for line in lines[2:]:
        i, j = line.split(" -> ")
        rules[i] = j


def count_elements(template, rules, it):
    pairs = defaultdict(int)
    for i, j in zip(template, template[1:]):
        pairs[i + j] += 1
    for i in range(it):
        new_pairs = defaultdict(int)
        for p in pairs:
            insertion = rules[p]
            new_pairs[p[0] + insertion] += pairs[p]
            new_pairs[insertion + p[1]] += pairs[p]
        pairs = new_pairs
    c0 = defaultdict(int)
    c1 = defaultdict(int)
    for k, v in pairs.items():
        c0[k[0]] += v
        c1[k[1]] += v
    final = {i: max(c0[i], c1[i]) for i in set(c0) | set(c1)}
    return max(final.values()) - min(final.values())


print(count_elements(template, rules, 10))
print(count_elements(template, rules, 40))
