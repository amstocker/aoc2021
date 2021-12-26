with open("day7_input.txt") as f:
    data = [int(s) for s in f.read().strip().split(',')]

d1 = lambda x, y: abs(x - y)
d2 = lambda x, y: abs(x - y) * (abs(x - y) + 1) * (1/2)

# part 1
print(min(sum(d1(x, y) for y in data) for x in range(min(data), max(data) + 1)))

# part 2
print(min(sum(d2(x, y) for y in data) for x in range(min(data), max(data) + 1)))