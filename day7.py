with open("day7_input.txt") as f:
    data = [int(s) for s in f.read().strip().split(',')]

# part 1
print(min(sum(abs(x - y) for y in data) for x in range(min(data), max(data) + 1)))

# part 2
print(min(sum(int(abs(x - y)*(abs(x - y) + 1)/2) for y in data) for x in range(min(data), max(data) + 1)))