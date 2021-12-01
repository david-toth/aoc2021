# Load data
data = None
with open("input.txt", "r") as file:
    data = file.readlines()
data = [int(i.strip()) for i in data]

#------------ Part 1
def pairwise_diff(x):
    return [j - i for i, j in zip(x, x[1:])]

increases = sum(diff > 0 for diff in pairwise_diff(data))
print(increases)

#------------- Part 2
sums = []
for i in range(2, len(data)):
    sums.append(sum(data[i-2:i+1]))

increases = sum(diff > 0 for diff in pairwise_diff(sums))
print(increases)
