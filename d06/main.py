import numpy as np

# Load data
file = open("input.txt", "r")
lines = file.readlines()
file.close()
data = list(map(int, lines[0].strip().split(",")))

# Initial counts
initial_state = np.zeros(9)
initial_state[:6] = np.bincount(data)

# Transition from i -> j given by X_{i, j}
transition_matrix = np.array([
    
    [0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0]
    
]).astype(float)

# Solution given by \pi_0 X^n
day_80 = np.sum(initial_state @ np.linalg.matrix_power(transition_matrix, 80))
day_256 = np.sum(initial_state @ np.linalg.matrix_power(transition_matrix, 256))
print(day_80)
print(day_256)
