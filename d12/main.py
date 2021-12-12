from collections import defaultdict, deque

graph = defaultdict(list)
for line in open("input.txt"):
    a, b = line.strip().split("-")
    graph[a].append(b)
    graph[b].append(a)

def find_paths1():
    total = 0
    state0 = ("start", set(["start"]))
    queue = deque([state0])
    while queue:
        current, small_caves = queue.popleft()
        if current == "end":
            total += 1
            continue
        for i in graph[current]:
            if (i not in small_caves):
                new_small_caves = set(small_caves)
                if (i.islower()):
                    new_small_caves.add(i)
                queue.append((i, new_small_caves))
            else:
                continue
    return total


print(find_paths1())


def find_paths2():
    total = 0
    state0 = ("start", set(["start"]), None)
    queue = deque([state0])
    while queue:
        current, small_caves, visit_twice = queue.popleft()
        if current == "end":
            total += 1
            continue
        for i in graph[current]:
            if (i not in small_caves):
                new_small_caves = set(small_caves)
                if (i.islower()):
                    new_small_caves.add(i)
                queue.append((i, new_small_caves, visit_twice))
            elif ((i in small_caves) and (visit_twice is None)
                    and (i not in ["start", "end"])):
                queue.append((i, small_caves, i))
            else:
                continue
    return total


print(find_paths2())
