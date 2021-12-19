with open("day1_input.txt") as f:
    data = list(map(int, f.read().strip().splitlines()))

# part 1
print(sum(1 for i in range(1, len(data)) if data[i] > data[i-1]))

# part 2
print(sum(1 for i in range(3, len(data)) if data[i] > data[i-3]))