from collections import Counter, defaultdict

with open("input.txt", "r") as f:
    lines = list(map(str.strip, f.readlines()))
    template = lines[0]
    rules = {}
    for line in lines:
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
    counts0 = defaultdict(int)
    counts1 = defaultdict(int)
    for k, v in pairs.items():
        counts0[k[0]] += v
        counts1[k[1]] += v
    final = {i: max(counts0[i], counts1[i]) for i in set(counts0).union(set(counts1))}
    return max(final.values()) - min(final.values())


print(count_elements(template, rules, 10))
print(count_elements(template, rules, 40))
    
