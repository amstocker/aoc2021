with open("day3_input.txt") as f:
    lines = f.read().strip().splitlines()
    nums = [int(s, 2) for s in lines]

# part 1
gamma = 0
epsilon = 0
for i in range(len(lines[0])):
    if sum(1 for x in nums if (x % 2**(i+1)) >= 2**i) > (len(lines) / 2):
        gamma += 2**i
    else:
        epsilon += 2**i
print(gamma * epsilon)

# part 2
oxygen = 0
co2 = 0
for i in range(len(lines[0])):
    if sum(1 for x in nums if (x % 2**(i+1)) >= 2**i) > (len(lines) / 2):
        gamma += 2**i
    else:
        epsilon += 2**i
print(gamma * epsilon)

