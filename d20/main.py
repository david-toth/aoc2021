import numpy as np
from scipy import ndimage

with open("input.txt", "r") as file:
    data = file.readlines()

data = [i.strip() for i in data]
algo = [i == "#" for i in data[0]]
chars = np.array([[j == "#" for j in i] for i in data[2:]])

def decode(x):
    s = "".join("1" if i else "0" for i in x)
    return algo[int(s, 2)]

def solve(n_times):
    x = np.pad(chars, 1, constant_values=False)
    for i in range(n_times):
        x = ndimage.generic_filter(np.pad(x, 1, mode="edge"),
                                    decode,
                                    size=(3, 3),
                                    mode="nearest")
    return x.sum()

print(solve(2))
print(solve(50))
