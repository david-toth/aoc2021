#  Load data 
file = open("input.txt", "r")
lines = file.readlines()
binary_digits = [line.strip() for line in lines]
file.close()

#--------- Part 1
n = len(binary_digits[0]) # all have same length 
counts = {i: {"0": 0, "1": 0} for i in range(n)}
for i in binary_digits:
    for pos, j in enumerate(i):
        counts[pos][j] += 1

gamma, epsilon = "", ""
for key, value in counts.items():
    if (value["0"] > value["1"]):
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"
        
gamma_decimal = int(gamma, 2)
epsilon_decimal = int(epsilon, 2)
print(gamma_decimal * epsilon_decimal)

#---------- Part 2
def bit_filter(digits, index, rating_type):
    counts = {"0": 0, "1": 0}
    for digit in digits:
        counts[digit[index]] += 1
    if (counts["0"] == counts["1"]):
        if (rating_type == "o2"):
            return "1"
        else:
            return "0"
    if (rating_type == "o2"):
        return max(counts, key=counts.get)
    else:
        return min(counts, key=counts.get)
        
# Find oxygen rating 
idx = 0
o2_list = binary_digits
while (len(o2_list) > 1):
    bit_o2 = bit_filter(o2_list, idx, "o2")
    o2_list = list(filter(lambda x: x[idx] == bit_o2, o2_list))
    idx += 1
    
# Find co2 rating 
idx = 0
co2_list = binary_digits
while(len(co2_list) > 1):
    bit_co2 = bit_filter(co2_list, idx, "co2")
    co2_list = list(filter(lambda x: x[idx] == bit_co2, co2_list))
    idx += 1
    
print(int(o2_list[0], 2) * int(co2_list[0], 2))